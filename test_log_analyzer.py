import pytest
from datetime import datetime
from log_analyzer import parse_log_line, count_log_levels, most_recent_log, filter_logs_by_date

# Unit test for parsing a log line
def test_parse_log_line():
    assert parse_log_line("2025-03-30 INFO Test log message") == {
        "timestamp": datetime(2025, 3, 30),
        "log_level": "INFO",
        "message": "Test log message",
        "raw": "2025-03-30 INFO Test log message"
    }
    assert parse_log_line("Invalid log line") is None

# Unit test for counting log levels
def test_count_log_levels():
    logs = [
        {"log_level": "INFO"},
        {"log_level": "ERROR"},
        {"log_level": "INFO"}
    ]
    assert count_log_levels(logs) == {"INFO": 2, "ERROR": 1}

# Unit test for retrieving the most recent log entry
def test_most_recent_log():
    logs = [
        {"timestamp": datetime(2025, 3, 29), "log_level": "ERROR"},
        {"timestamp": datetime(2025, 3, 30), "log_level": "ERROR"}
    ]
    assert most_recent_log(logs, "ERROR") == logs[1]
    assert most_recent_log(logs, "INFO") is None

# Unit test for filtering logs by date
def test_filter_logs_by_date():
    logs = [
        {"timestamp": datetime(2025, 3, 29), "log_level": "ERROR", "raw": "log1"},
        {"timestamp": datetime(2025, 3, 30), "log_level": "ERROR", "raw": "log2"}
    ]
    start_date = datetime(2025, 3, 29).date()
    end_date = datetime(2025, 3, 30).date()
    assert len(filter_logs_by_date(logs, start_date, end_date)) == 2
    