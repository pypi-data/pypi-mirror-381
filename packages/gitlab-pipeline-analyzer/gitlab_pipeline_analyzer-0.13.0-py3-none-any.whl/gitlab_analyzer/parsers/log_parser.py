"""
Generic log parser implementing SOLID principles.

This parser provides utilities for extracting errors and warnings from CI/CD logs
and serves as a fallback when no specific framework parser is available.

Following SOLID principles:
- Single Responsibility: Log parsing utilities and generic error extraction
- Open/Closed: Extensible through framework-specific parsers
- Liskov Substitution: Can be used as BaseFrameworkParser fallback
- Interface Segregation: Focused on log parsing concerns
- Dependency Inversion: Uses abstract BaseParser utilities

Copyright (c) 2025 Siarhei Skuratovich
Licensed under the MIT License - see LICENSE file for details
"""

import re
from typing import Any

from ..models import LogEntry
from .base_parser import (
    BaseFrameworkDetector,
    BaseFrameworkParser,
    BaseParser,
    TestFramework,
)


class GenericLogDetector(BaseFrameworkDetector):
    """Fallback detector for generic logs when no specific framework detected"""

    @property
    def framework(self) -> TestFramework:
        return TestFramework.GENERIC

    @property
    def priority(self) -> int:
        return 1  # Lowest priority - only as fallback

    def detect(self, job_name: str, job_stage: str, trace_content: str) -> bool:
        """Always returns True as fallback - but will be last due to low priority"""
        return True


class GenericLogParser(BaseFrameworkParser):
    """Generic log parser implementing BaseFrameworkParser interface"""

    @property
    def framework(self) -> TestFramework:
        return TestFramework.GENERIC

    def parse(self, trace_content: str, **kwargs) -> dict[str, Any]:
        """Parse logs using generic LogParser and convert to standard format"""
        entries = LogParser.extract_log_entries(trace_content)

        # Convert LogEntry objects to standardized format
        errors = []
        warnings = []

        for entry in entries:
            error_data = {
                "message": entry.message,
                "line_number": entry.line_number,
                "exception_type": (
                    "Generic Error" if entry.level == "error" else "Generic Warning"
                ),
                "test_file": "unknown",
                "test_function": "unknown",
                "has_traceback": False,
            }

            if entry.level == "error":
                errors.append(error_data)
            else:
                warnings.append(error_data)

        return self.validate_output(
            {
                "parser_type": "generic",
                "framework": self.framework.value,
                "errors": errors,
                "error_count": len(errors),
                "warnings": warnings,
                "warning_count": len(warnings),
                "summary": {
                    "total_tests": len(errors),
                    "failed": len(errors),
                    "passed": 0,
                    "skipped": 0,
                },
            }
        )

    def _extract_source_file_and_line(
        self, error_message: str, full_log_text: str = "", error_type: str = ""
    ) -> tuple[str | None, int | None]:
        """
        Extract source file path and line number from generic error messages.

        This method handles various generic error message formats including:
        - Python tracebacks: "File \"/path/to/file.py\", line 42, in function"
        - Generic file:line patterns: "filename.py:42: error message"
        - Make errors: "filename.py:42: error description"
        """
        import re

        # Pattern 1: Python traceback format
        traceback_match = re.search(r'File "([^"]+)", line (\d+)', error_message)
        if traceback_match:
            return traceback_match.group(1), int(traceback_match.group(2))

        # Pattern 2: Generic file:line format
        file_line_match = re.search(r"([a-zA-Z0-9_/.-]+\.py):(\d+):", error_message)
        if file_line_match:
            return file_line_match.group(1), int(file_line_match.group(2))

        # Pattern 3: Look in full log text for more context
        if full_log_text:
            # Search for traceback in full text
            traceback_match = re.search(r'File "([^"]+)", line (\d+)', full_log_text)
            if traceback_match:
                return traceback_match.group(1), int(traceback_match.group(2))

        return None, None


class LogParser(BaseParser):
    """Parser for extracting errors and warnings from CI/CD logs"""

    # Enhanced error patterns - focus on actual failures including infrastructure issues
    ERROR_PATTERNS = [
        # CRITICAL: Job-ending failures that should ALWAYS be captured
        (r"SyntaxError: (.+)", "error"),  # Python syntax errors
        (r"ImportError: (.+)", "error"),  # Import failures
        (r"ModuleNotFoundError: (.+)", "error"),  # Missing modules
        (r"IndentationError: (.+)", "error"),  # Python indentation errors
        (r"NameError: (.+)", "error"),  # Undefined variables
        (r"TypeError: (.+)", "error"),  # Type errors
        (r"ValueError: (.+)", "error"),  # Value errors
        (r"KeyError: (.+)", "error"),  # Key errors
        (r"AttributeError: (.+)", "error"),  # Attribute errors
        (r"FileNotFoundError: (.+)", "error"),  # Missing files
        # Docker/build infrastructure failures that cause job failures
        (r"Error response from daemon: (.+)", "error"),  # Docker errors
        (r"docker: (.+)", "error"),  # Docker command failures
        (r"Failed to pull image (.+)", "error"),  # Image pull failures
        (r"exec user process caused (.+)", "error"),  # Container exec failures
        # Shell script errors that affect job execution
        (r"(.*)not a valid identifier", "error"),
        (r"(.*)command not found", "error"),
        (r"(.*)No such file or directory", "error"),
        (r"(.*)Permission denied", "error"),
        # Test execution failures
        (r"^(.+\.py):(\d+):\s+in\s+(\w+)", "error"),  # pytest detailed format
        (r"(.*)AssertionError: (.+)", "error"),
        (r"(.*)assert (.+)", "error"),
        (r"(.*)>.*assert (.+)", "error"),  # pytest assertion with > marker
        (r"(.*)E\s+(.+Error: .+)", "error"),  # pytest error format with E prefix
        (r"(.*)FAILED (.+test.*)", "error"),  # Test failures
        (r"(.*)Test failed: (.+)", "error"),
        # Build/compilation failures
        (r"(.*)compilation error", "error"),
        (r"(.*)build failed", "error"),
        (r"(.*)fatal error: (.+)", "error"),
        # Package/dependency errors that prevent job completion
        (r"(.*)could not find", "error"),
        (r"(.*)missing", "error"),
        (r"ERROR: (.+)", "error"),  # Generic ERROR lines
        # Linting tool failures
        (r"(.*)would reformat", "error"),  # black formatting issues
        (r"(.*)Lint check failed", "error"),
        (r"(.*)formatting.*issues", "error"),
        (r"(.*)files would be reformatted", "error"),
        # Ruff linting errors - specific pattern for Ruff output
        (
            r"(.+\.py):(\d+):(\d+):\s+([A-Z]\d+)\s+\[?\*?\]?\s*(.+)",
            "error",
        ),  # Ruff format: file.py:line:col: CODE [*] message
        # Note: Removed "Found (\d+) error" pattern to avoid duplicate error extraction
        # The summary line should not be treated as a separate error
        (r"(.+) error.* fixable with", "error"),  # Ruff fixable errors summary
        # Import linting failures
        (r"No matches for ignored import (.+)", "error"),  # import-linter failures
        (r"(.*)import.*not allowed", "error"),  # import policy violations
        # Import-linter domain boundary violations (actual violations only)
        (
            r"^\s*-\s+(.+)\s+->\s+(.+)\s+\(l\.(\d+)\)",
            "error",
        ),  # Specific import violation: "- file.py -> module (l.12)"
        (
            r"^(.+\.(py|serializers|views|models|services))\s+->\s+(.+)\s+\(l\.(\d+)\)",
            "error",
        ),  # Import violation without dash: "file.serializers -> users (l.12)"
        # NOTE: Removed summary patterns - these are context, not separate errors:
        # - "Contracts: .* broken." → this is just a summary line
        # - "(.+domain.+BROKEN)" → this is just status information
        # - "make: *** [.*py/lint/imports.*" → this is just tool failure message
        # The actual error is the specific import violation line above
        # Critical linting failures that cause job failures (main error indicators)
        # NOTE: Removed make lint patterns - they are just tool status, not separate errors
        # (r"make: \*\*\* \[.*py/lint/imports\] Error (\d+)", "error"),  # import-linter failures
        # (r"make: \*\*\* \[.*lint.*\] Error (\d+)", "error"),  # general linting failures
        # Make/build tool errors - exclude only test-related make failures (not linting)
        (
            r"make: \*\*\* \[(?!.*(?:test|check|format|lint))(.+)\] Error (\d+)",
            "error",
        ),  # make command failures (but not for testing/formatting/linting - those are tool status)
        (r"(.*)make.*failed", "error"),  # general make failures
        # Security/vulnerability errors
        (r"(.*)vulnerability", "error"),
        (r"(.*)security issue", "error"),
        # Traceback start - often indicates real errors
        (r"(.*)Traceback \(most recent call last\):", "error"),
    ]

    WARNING_PATTERNS = [
        # Code quality warnings
        (r"(.*)DeprecationWarning: (.+)", "warning"),
        (r"(.*)UserWarning: (.+)", "warning"),
        (r"(.*)FutureWarning: (.+)", "warning"),
        (r"(.*)WARNING: (.+)", "warning"),  # Will be filtered by excludes
        (r"(.*)WARN: (.+)", "warning"),  # Will be filtered by excludes
        # Linter warnings
        (r"(.*)warning: (.+)", "warning"),
    ]

    @classmethod
    def _is_duplicate_test_error(cls, message: str, existing_entries: list) -> bool:
        """Check if this error message represents a duplicate test failure"""
        # Extract test function name from different message formats
        test_function = None

        # Format 1: "test/test_failures.py:10: in test_intentional_failure"
        detailed_match = re.match(r"^(.+\.py):(\d+):\s+in\s+(\w+)", message)
        if detailed_match:
            test_function = detailed_match.group(3)

        # Format 2: "FAILED test/test_failures.py::test_intentional_failure"
        failed_match = re.search(r"FAILED\s+.+::(\w+)", message)
        if failed_match:
            test_function = failed_match.group(1)

        # Format 3: AssertionError from specific test
        if "AssertionError:" in message and not test_function:
            # Look for test function in context if available
            return False  # Let the deduplication handle this

        # Enhanced: Check for duplicate AttributeError messages in FAILED lines
        if "FAILED" in message and "AttributeError:" in message:
            # Extract the AttributeError message from the FAILED line
            attr_error_match = re.search(r"AttributeError:\s*(.+)", message)
            if attr_error_match:
                attr_error_text = attr_error_match.group(1).strip()
                # Check if we already have this exact AttributeError
                for entry in existing_entries:
                    if (
                        hasattr(entry, "message")
                        and "AttributeError:" in entry.message
                        and attr_error_text in entry.message
                    ):
                        return True

        # Enhanced: Check for raw AttributeError that might be duplicated in FAILED lines
        if (
            message.startswith("AttributeError:")
            or message.startswith("'")
            and "object has no attribute" in message
        ):
            # This might be a raw error that will be duplicated in a FAILED line
            error_content = message.replace("AttributeError:", "").strip()
            for entry in existing_entries:
                if (
                    hasattr(entry, "message")
                    and "FAILED" in entry.message
                    and "AttributeError:" in entry.message
                    and error_content in entry.message
                ):
                    return True

        if test_function:
            # Check if we already have an error for this test function
            for entry in existing_entries:
                if (
                    hasattr(entry, "message")
                    and test_function in entry.message
                    and (
                        f"::{test_function}" in entry.message
                        or f"in {test_function}" in entry.message
                    )
                ):
                    return True

        return False

    @classmethod
    def _is_in_pytest_failure_section(
        cls, lines: list[str], current_line_num: int
    ) -> bool:
        """
        Intelligently detect if we're currently inside a pytest FAILURES section
        by looking for pytest section markers and structure, not fixed line counts.
        """
        # Look backwards from current line to find pytest section boundaries
        failures_section_start = None
        failures_section_end = None

        # Search backwards for the start of a FAILURES section
        for i in range(current_line_num - 1, -1, -1):
            line = lines[i].strip()

            # Found the start of FAILURES section
            if re.match(r"=+\s*FAILURES\s*=+", line):
                failures_section_start = i
                break

            # If we hit another pytest section, we're not in FAILURES
            if re.match(r"=+\s*(SHORT TEST SUMMARY|ERRORS|PASSED|FAILED)\s*=+", line):
                break

            # If we hit a clear job section boundary, stop looking
            if any(
                marker in line
                for marker in [
                    "section_start:",
                    "section_end:",
                    "Job succeeded",
                    "Job failed",
                    "Running with gitlab-runner",
                    "Preparing the",
                ]
            ):
                break

        # If no FAILURES section found, we're not in one
        if failures_section_start is None:
            return False

        # Search forwards from FAILURES start to see if there's an end before our line
        for i in range(
            failures_section_start + 1, min(len(lines), current_line_num + 50)
        ):
            line = lines[i].strip()

            # Found end of FAILURES section (start of another section or summary)
            if re.match(r"=+\s*(SHORT TEST SUMMARY|ERRORS|PASSED|FAILED)\s*=+", line):
                failures_section_end = i
                break

            # Job section boundary also ends pytest output
            if any(
                marker in line
                for marker in [
                    "section_start:",
                    "section_end:",
                    "Job succeeded",
                    "Job failed",
                ]
            ):
                failures_section_end = i
                break

        # We're in FAILURES section if:
        # 1. We found a FAILURES start before our line
        # 2. Either no end was found (still in section) OR the end is after our line
        return failures_section_start is not None and (
            failures_section_end is None or failures_section_end > current_line_num
        )

    @classmethod
    def extract_log_entries(cls, log_text: str) -> list[LogEntry]:
        """Extract error and warning entries from log text"""
        # First, clean the log text from ANSI escape sequences
        cleaned_log_text = cls.clean_ansi_sequences(log_text)

        entries: list[LogEntry] = []
        lines = cleaned_log_text.split("\n")

        # Track processed pytest detailed lines to avoid duplicates
        processed_pytest_details = set()

        for line_num, log_line in enumerate(lines, 1):
            log_line = log_line.strip()
            if not log_line:
                continue

            # Skip GitLab CI infrastructure messages
            if any(
                re.search(pattern, log_line, re.IGNORECASE)
                for pattern in cls.EXCLUDE_PATTERNS
            ):
                continue

            # Skip pytest error details (E   lines) and standalone exception messages
            # if we're inside a FAILURES section - these will be captured as context
            # BUT preserve meaningful entries like file:line:function and FAILED summaries
            if (
                line_num > 1
                and (
                    re.match(r"^E\s+", log_line)
                    or (
                        re.match(r"^(AssertionError|Exception|.*Error):\s", log_line)
                        and not re.match(r"^(.+\.py):(\d+):\s+in\s+(\w+)", log_line)
                        and "FAILED" not in log_line
                    )
                )
                and cls._is_in_pytest_failure_section(lines, line_num)
            ):
                # Skip this line as it's part of test failure details
                continue

            # Check for errors
            for pattern, level in cls.ERROR_PATTERNS:
                match = re.search(pattern, log_line, re.IGNORECASE)
                if match:
                    # Check for duplicate test errors
                    if cls._is_duplicate_test_error(log_line, entries):
                        break  # Skip this duplicate

                    # Special handling for pytest detailed format to avoid duplicates
                    pytest_detail_match = re.match(
                        r"^(.+\.py):(\d+):\s+in\s+(\w+)", log_line
                    )
                    if pytest_detail_match:
                        test_key = f"{pytest_detail_match.group(1)}:{pytest_detail_match.group(3)}"
                        if test_key in processed_pytest_details:
                            break  # Skip duplicate
                        processed_pytest_details.add(test_key)

                    # Extract actual Python file line number if available
                    actual_line_number = line_num  # Default to trace line number

                    # Look for Python file:line patterns in the current line or context
                    file_line_patterns = [
                        r'^\s*File\s+"([^"]+)",\s+line\s+(\d+)',  # Python traceback format
                        r"^\s*([^:\s]+):(\d+):\s*in\s+",  # Ruby/pytest format
                        r"^\s*([^:\s]+):(\d+):\s*",  # Generic file:line format
                        r"^\s*([^:\s]+):\s*line\s+(\d+)",  # Alternative format
                    ]

                    for pattern in file_line_patterns:
                        file_match = re.search(pattern, log_line)
                        if file_match and len(file_match.groups()) >= 2:
                            # Prefer user code over system files
                            file_path = file_match.group(1)
                            if not any(
                                sys_path in file_path
                                for sys_path in [
                                    "/root/.local/share/uv/python/",
                                    "site-packages",
                                    "/usr/lib",
                                ]
                            ):
                                try:
                                    actual_line_number = int(file_match.group(2))
                                    break
                                except (ValueError, IndexError):
                                    pass

                    # If no line number found in current line, check context for user code
                    if actual_line_number == line_num:
                        context_lines = cls._get_context(lines, line_num)
                        for ctx_line in context_lines.split("\n"):
                            for pattern in file_line_patterns:
                                file_match = re.search(pattern, ctx_line)
                                if file_match and len(file_match.groups()) >= 2:
                                    file_path = file_match.group(1)
                                    # Prefer user code over system files
                                    if not any(
                                        sys_path in file_path
                                        for sys_path in [
                                            "/root/.local/share/uv/python/",
                                            "site-packages",
                                            "/usr/lib",
                                        ]
                                    ):
                                        try:
                                            actual_line_number = int(
                                                file_match.group(2)
                                            )
                                            break
                                        except (ValueError, IndexError):
                                            pass
                            if actual_line_number != line_num:
                                break

                    entry = LogEntry(
                        level=level,
                        message=log_line,
                        line_number=actual_line_number,
                        context=cls._get_context(lines, line_num),
                        error_type=cls.classify_error_type(log_line),
                    )
                    entries.append(entry)
                    break

            # Check for warnings
            for pattern, level in cls.WARNING_PATTERNS:
                match = re.search(pattern, log_line, re.IGNORECASE)
                if match:
                    # Extract actual Python file line number if available (same logic as errors)
                    actual_line_number = line_num  # Default to trace line number

                    # Look for Python file:line patterns
                    file_line_patterns = [
                        r'^\s*File\s+"([^"]+)",\s+line\s+(\d+)',  # Python traceback format
                        r"^\s*([^:\s]+):(\d+):\s*in\s+",  # Ruby/pytest format
                        r"^\s*([^:\s]+):(\d+):\s*",  # Generic file:line format
                        r"^\s*([^:\s]+):\s*line\s+(\d+)",  # Alternative format
                    ]

                    for pattern_inner in file_line_patterns:
                        file_match = re.search(pattern_inner, log_line)
                        if file_match and len(file_match.groups()) >= 2:
                            try:
                                actual_line_number = int(file_match.group(2))
                                break
                            except (ValueError, IndexError):
                                pass

                    entry = LogEntry(
                        level=level,
                        message=log_line,
                        line_number=actual_line_number,
                        context=cls._get_context(lines, line_num),
                        error_type=cls.classify_error_type(log_line),
                    )
                    entries.append(entry)
                    break

        return entries

    @classmethod
    def _get_context(
        cls,
        lines: list[str],
        current_line: int,
        context_size: int = 5,  # Increased from 2 to 5 for better context
    ) -> str:
        """Get surrounding context for a log entry, filtered of infrastructure noise"""
        start = max(0, current_line - context_size - 1)
        end = min(len(lines), current_line + context_size)
        context_lines = lines[start:end]

        # For pytest detailed failures, we want to preserve more context
        is_pytest_failure = any(
            "test" in line.lower()
            and any(
                keyword in line.lower()
                for keyword in ["fail", "error", "assert", "traceback"]
            )
            for line in context_lines[:3]  # Check first few lines
        )

        # Filter out infrastructure noise from context, but be more permissive for pytest
        filtered_lines = []
        for line in context_lines:
            line = line.strip()
            if not line:
                continue

            # Skip infrastructure messages in context, but preserve pytest test details
            should_skip = False
            if (
                not is_pytest_failure
            ):  # Only apply strict filtering for non-pytest content
                if any(
                    re.search(pattern, line, re.IGNORECASE)
                    for pattern in cls.EXCLUDE_PATTERNS
                ):
                    should_skip = True
            else:
                # For pytest failures, only exclude the most obvious infrastructure noise
                infrastructure_patterns = [
                    r"Running with gitlab-runner",
                    r"Preparing the.*executor",
                    r"Using Kubernetes",
                    r"section_start:",
                    r"section_end:",
                ]
                if any(
                    re.search(pattern, line, re.IGNORECASE)
                    for pattern in infrastructure_patterns
                ):
                    should_skip = True

            if not should_skip:
                filtered_lines.append(line)

        return "\n".join(filtered_lines)

    @classmethod
    def _categorize_formatting_error(cls, message: str) -> dict[str, str]:
        """Categorize code formatting errors (Black formatter)"""
        if (
            "files would be reformatted" in message
            or "file would be left unchanged" in message
        ):
            # Summary message with multiple files
            numbers = re.findall(r"(\d+) files? would be reformatted", message)
            unchanged = re.findall(r"(\d+) files? would be left unchanged", message)

            reformatted_count = numbers[0] if numbers else "Multiple"
            unchanged_count = unchanged[0] if unchanged else "0"

            return {
                "category": "Code Formatting Summary",
                "severity": "medium",
                "description": "Multiple files need code formatting with Black formatter",
                "details": f"Black formatter detected {reformatted_count} files requiring reformatting, {unchanged_count} files already properly formatted",
                "solution": "Run 'black .' to auto-format all files",
                "impact": "Code style consistency issues",
            }
        else:
            # Individual file message
            file_match = re.search(r"would reformat (.+)", message)
            file_path = file_match.group(1) if file_match else "unknown file"

            return {
                "category": "Code Formatting",
                "severity": "medium",
                "description": "File needs formatting with Black formatter",
                "details": f"Black formatter detected formatting issues in: {file_path}",
                "solution": f"Run 'black {file_path}' to auto-format this file",
                "impact": "Code style inconsistency",
            }

    @classmethod
    def _categorize_syntax_error(cls, message: str) -> dict[str, str]:
        """Categorize Python syntax errors"""
        error_match = re.search(r"SyntaxError:\s*(.+)", message, re.IGNORECASE)
        file_match = re.search(r'File "([^"]+)"', message) or re.search(
            r"\(([^,]+),", message
        )
        line_match = re.search(r"line (\d+)", message)

        error_detail = error_match.group(1) if error_match else "syntax error"
        file_path = file_match.group(1) if file_match else "unknown file"
        line_num = line_match.group(1) if line_match else "unknown line"

        return {
            "category": "Python Syntax Error",
            "severity": "high",
            "description": "Invalid Python syntax that prevents code execution",
            "details": f"Syntax error in {file_path} at line {line_num}: {error_detail}",
            "solution": f"Fix the syntax error in {file_path} at line {line_num}",
            "impact": "Code cannot be executed or imported",
        }

    @classmethod
    def _categorize_import_error(cls, message: str) -> dict[str, str]:
        """Categorize Python import errors"""
        module_match = (
            re.search(r"No module named '([^']+)'", message)
            or re.search(r"cannot import name '([^']+)'", message)
            or re.search(r"ImportError:\s*(.+)", message, re.IGNORECASE)
            or re.search(r"ModuleNotFoundError:\s*(.+)", message, re.IGNORECASE)
        )

        module_detail = module_match.group(1) if module_match else "unknown module"

        return {
            "category": "Python Import Error",
            "severity": "high",
            "description": "Missing module or package dependency",
            "details": f"Failed to import: {module_detail}",
            "solution": f"Install the missing package: pip install {module_detail.split('.')[0]}",
            "impact": "Code cannot access required dependencies",
        }

    @classmethod
    def _categorize_test_failure(
        cls, message: str, context: str = ""
    ) -> dict[str, str]:
        """Categorize test failures with detailed parsing"""
        # Priority 1: pytest detailed format (file.py:line: in test_function)
        detailed_format_match = re.match(r"^(.+\.py):(\d+):\s+in\s+(\w+)", message)
        if detailed_format_match:
            source_file = detailed_format_match.group(1)
            source_line = int(detailed_format_match.group(2))
            test_function = detailed_format_match.group(3)

            # Extract error details from context
            error_context = ""
            if context:
                error_match = re.search(
                    r"(AssertionError|Exception|.*Error):\s*(.+)", context
                )
                if error_match:
                    error_context = f" - {error_match.group(1)}: {error_match.group(2)}"

            details = f"Test case '{test_function}' in '{source_file}' failed execution{error_context}"

            return {
                "category": "Test Failure",
                "severity": "high",
                "description": "Unit test or integration test failed",
                "details": details,
                "solution": "Review test output and fix the failing test or code",
                "impact": "Code quality issues, potential bugs",
                "source_file": source_file,
                "source_line": str(source_line),
                "test_function": test_function,
            }

        # Priority 2: pytest summary format (FAILED test/file.py::test_function)
        test_match = re.search(r"FAILED\s+(.+)", message)
        if test_match:
            test_detail = test_match.group(1)

            if "::" in test_detail:
                parts = test_detail.split("::")
                test_file = parts[0] if parts else "unknown file"
                remaining = parts[1] if len(parts) > 1 else ""

                if " - " in remaining:
                    test_function = remaining.split(" - ")[0].strip()
                    failure_reason = remaining.split(" - ", 1)[1]
                else:
                    test_function = (
                        remaining.split()[0] if remaining else "unknown test"
                    )
                    failure_reason = "Test failed"

                details = f"Test case '{test_function}' in '{test_file}' failed execution - Reason: {failure_reason}"

                return {
                    "category": "Test Failure",
                    "severity": "high",
                    "description": "Unit test or integration test failed",
                    "details": details,
                    "solution": "Review test output and fix the failing test or code",
                    "impact": "Code quality issues, potential bugs",
                    "source_file": (
                        test_file.split("/")[-1] if "/" in test_file else test_file
                    ),
                    "test_function": test_function,
                }

        # Priority 3: Generic test failure
        if "assertion" in message.lower() or "test" in message.lower():
            error_match = re.search(
                r"(AssertionError|Exception|.*Error):\s*(.+)", message
            )
            if error_match:
                details = f"Job execution error: {error_match.group(2)}"
            else:
                details = (
                    "Test failure detected but specific details could not be extracted"
                )
        else:
            details = (
                "Test failure detected but specific details could not be extracted"
            )

        return {
            "category": "Test Failure",
            "severity": "high",
            "description": "Unit test or integration test failed",
            "details": details,
            "solution": "Review test output and fix the failing test or code",
            "impact": "Code quality issues, potential bugs",
        }

    @classmethod
    def _categorize_build_error(cls, message: str) -> dict[str, str]:
        """Categorize build and compilation errors"""
        error_match = (
            re.search(r"compilation error:\s*(.+)", message, re.IGNORECASE)
            or re.search(r"build failed:\s*(.+)", message, re.IGNORECASE)
            or re.search(r"fatal error:\s*(.+)", message, re.IGNORECASE)
        )

        error_detail = error_match.group(1) if error_match else "build process failed"

        return {
            "category": "Build Error",
            "severity": "high",
            "description": "Code compilation or build process failed",
            "details": f"Build failure: {error_detail}",
            "solution": "Check build logs for specific compilation issues",
            "impact": "Cannot create executable or deployable artifacts",
        }

    @classmethod
    def _categorize_filesystem_error(cls, message: str) -> dict[str, str]:
        """Categorize file system and permission errors"""
        file_match = (
            re.search(r"Permission denied:\s*(.+)", message, re.IGNORECASE)
            or re.search(r"No such file or directory:\s*(.+)", message, re.IGNORECASE)
            or re.search(r"'([^']+)'", message)
        )

        file_detail = file_match.group(1) if file_match else "file system resource"

        return {
            "category": "File System Error",
            "severity": "medium",
            "description": "File access or permission issue",
            "details": f"Cannot access: {file_detail}",
            "solution": f"Check file permissions and paths for: {file_detail}",
            "impact": "Cannot access required files or directories",
        }

    @classmethod
    def _categorize_linting_error(cls, message: str) -> dict[str, str]:
        """Categorize linting and code quality errors"""
        tool_match = re.search(r"(\w+)\s+.*lint.*failed", message, re.IGNORECASE)
        error_match = re.search(r"Lint check failed:\s*(.+)", message, re.IGNORECASE)

        tool_name = tool_match.group(1) if tool_match else "linter"
        error_detail = (
            error_match.group(1) if error_match else "code quality issues found"
        )

        return {
            "category": "Code Quality Error",
            "severity": "medium",
            "description": "Code quality checks failed",
            "details": f"{tool_name} found: {error_detail}",
            "solution": f"Fix linting issues reported by {tool_name}",
            "impact": "Code quality and maintainability concerns",
        }

    @classmethod
    def _categorize_generic_error(cls, message: str) -> dict[str, str]:
        """Categorize generic errors"""
        error_match = re.search(r"ERROR:\s*(.+)", message, re.IGNORECASE)
        error_detail = error_match.group(1) if error_match else message.strip()

        # Provide context-specific details
        if "no files to upload" in error_detail.lower():
            details = "GitLab CI attempted to upload artifacts but no matching files were found"
        elif "compilation" in error_detail.lower():
            details = f"Build compilation process failed: {error_detail}"
        elif "permission" in error_detail.lower():
            details = f"File system permission error encountered: {error_detail}"
        elif "connection" in error_detail.lower() or "network" in error_detail.lower():
            details = f"Network or connection error occurred: {error_detail}"
        elif "timeout" in error_detail.lower():
            details = f"Operation timed out: {error_detail}"
        else:
            details = f"Job execution error: {error_detail}"

        return {
            "category": "General Error",
            "severity": "medium",
            "description": "An error occurred during job execution",
            "details": details,
            "solution": "Review the error message and relevant logs for specific resolution steps",
            "impact": "Job execution interrupted",
        }

    @classmethod
    def _categorize_unknown_error(cls, message: str) -> dict[str, str]:
        """Fallback for unrecognized error patterns"""
        return {
            "category": "Unknown Error",
            "severity": "medium",
            "description": "Unrecognized error pattern",
            "details": f"Original message: {message}",
            "solution": "Review the full error message and context",
            "impact": "Potential job execution issue",
        }

    @classmethod
    def categorize_error(cls, message: str, context: str = "") -> dict[str, str]:
        """Categorize an error and provide detailed information using focused functions"""
        message_lower = message.lower()

        # Route to specific categorization functions based on error type
        if (
            "would reformat" in message_lower
            or "files would be reformatted" in message_lower
        ):
            return cls._categorize_formatting_error(message)

        elif "syntaxerror" in message_lower:
            return cls._categorize_syntax_error(message)

        elif "importerror" in message_lower or "modulenotfounderror" in message_lower:
            return cls._categorize_import_error(message)

        elif (
            "failed" in message_lower
            and ("test" in message_lower or "assertion" in message_lower)
        ) or re.match(r".+\.py:\d+: in test_.+", message):
            return cls._categorize_test_failure(message, context)

        elif "compilation error" in message_lower or "build failed" in message_lower:
            return cls._categorize_build_error(message)

        elif "permission denied" in message_lower or "no such file" in message_lower:
            return cls._categorize_filesystem_error(message)

        elif "lint" in message_lower and "failed" in message_lower:
            return cls._categorize_linting_error(message)

        elif "error:" in message_lower:
            return cls._categorize_generic_error(message)

        else:
            return cls._categorize_unknown_error(message)
