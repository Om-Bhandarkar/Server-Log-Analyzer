# 🧾 Server Log Analyzer

A Python-based CLI tool that parses server logs, counts log levels, finds the most recent log by severity, and filters logs by date range. Includes `pytest` unit tests for validation.

---

## 📁 Project Structure

```
server_log_analyzer/
├── log_analyzer.py       # Main script
├── logs.txt              # Raw log file
├── filtered_logs.txt     # Auto-generated filtered logs
├── test_log_analyzer.py  # Unit tests
└── README.md             # Documentation
```

---

## ▶️ How to Run the Program

### 1️⃣ Ensure You Have Python 3 Installed
Make sure Python 3 is installed on your system. You can check your version by running:
```sh
python --version
```

### 2️⃣ Prepare Your Log File
Create a file named `logs.txt` in the same directory. Example log contents:
```
2025-01-10 09:23:45 INFO Application started
2025-01-10 09:25:00 WARNING Disk space low
2025-01-10 09:26:30 ERROR Unable to connect to database
2025-01-10 09:30:15 INFO User logged in
2025-01-10 09:35:20 ERROR Timeout occurred
2025-01-10 09:40:05 WARNING CPU usage high
2025-01-11 10:15:45 DEBUG Debugging started
```

### 3️⃣ Run the Log Analyzer
To execute the script, run:
```sh
python log_analyzer.py
```

### 4️⃣ Follow the Prompts
- Enter a log level (e.g., `ERROR`) to get the most recent entry.
- Enter a start and end date (e.g., `2025-01-10`) to filter logs.
- Filtered logs (if any) will be saved to `filtered_logs.txt`.

---

## 🧪 Running Unit Tests with Pytest

### 1️⃣ Install pytest (if not installed)
```sh
pip install pytest
```

### 2️⃣ Run Tests
```sh
pytest test_log_analyzer.py
```

### Expected Output
```
test_log_analyzer.py .....                         [100%]
5 passed in 0.10s
```

---

## ✅ Features Implemented

- ✅ Parse and validate logs
- ✅ Handle malformed lines gracefully
- ✅ Count log entries per level
- ✅ Show most recent entry for a chosen level
- ✅ Filter logs within a date range
- ✅ Save filtered results to a new file
- ✅ Unit tests using pytest

