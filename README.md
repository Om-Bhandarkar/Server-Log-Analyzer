# 🧾 Server Log Analyzer

A Python-based CLI tool that parses server logs, counts log levels, finds the most recent log by severity, and filters logs by date range. Includes `pytest` unit tests for validation.

---

<h2>📁 Project Structure</h2>

<pre>
server_log_analyzer/
├── <b>log_analyzer.py</b>       - Main script
├── <b>logs.txt</b>              - Raw log file
├── <b>filtered_logs.txt</b>     - Auto-generated filtered logs
├── <b>test_log_analyzer.py</b>  - Unit tests
└── <b>README.md</b>            - Documentation
</pre>
---

## ▶️ How to Run the Program

1. **Ensure you have Python 3 installed**
2. **Prepare your log file** named `logs.txt` in the same folder.  
   Example contents:

2025-01-10 09:23:45 INFO Application started
2025-01-10 09:25:00 WARNING Disk space low
2025-01-10 09:26:30 ERROR Unable to connect to database
2025-01-10 09:30:15 INFO User logged in
2025-01-10 09:35:20 ERROR Timeout occurred
2025-01-10 09:40:05 WARNING CPU usage high
2025-01-11 10:15:45 DEBUG Debugging started

3. **Run the analyzer:**

python log_analyzer.py

	4.	Follow the prompts:
	•	Enter a log level to get the most recent entry (e.g., ERROR)
	•	Enter a start and end date (e.g., 2025-01-10)
	5.	Filtered logs (if any) will be saved to filtered_logs.txt.

⸻

🧪 Running Unit Tests with Pytest

Step 1: Install pytest if not installed

pip install pytest

Step 2: Run tests

pytest test_log_analyzer.py

You should see something like:

test_log_analyzer.py .....                         [100%]
5 passed in 0.10s



⸻

<table border="1" cellspacing="0" cellpadding="10">
    <thead>
        <tr>
            <th>✅ Features Implemented</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>✅ Parse and validate logs</td>
        </tr>
        <tr>
            <td>✅ Handle malformed lines gracefully</td>
        </tr>
        <tr>
            <td>✅ Count log entries per level</td>
        </tr>
        <tr>
            <td>✅ Show most recent entry for a chosen level</td>
        </tr>
        <tr>
            <td>✅ Filter logs within a date range</td>
        </tr>
        <tr>
            <td>✅ Save filtered results to a new file</td>
        </tr>
        <tr>
            <td>✅ Unit tests using pytest</td>
        </tr>
    </tbody>
</table>

