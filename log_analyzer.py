import os
from datetime import datetime
from collections import defaultdict

# Define log file paths
LOG_FILE = 'logs.txt'  # Path to the log file
FILTERED_FILE = 'filtered_logs.txt'  # Path to save filtered logs

# Valid log levels
VALID_LOG_LEVELS = {'INFO', 'WARNING', 'ERROR', 'DEBUG'}

def parse_log_line(line):
    """Parses a single line of the log file into its components."""


    try:
        # Split the log line into three parts: timestamp, log level, and message
        parts = line.strip().split(' ', 2)

        # Convert the timestamp string into a datetime object
        timestamp = datetime.strptime(parts[0], "%Y-%m-%d")  

        log_level = parts[1].strip()  # Extract log level
        
        message = parts[2].strip() if len(parts) > 2 else ""  # Extract message 

        

        # Validate log level
        if log_level not in VALID_LOG_LEVELS:
            raise ValueError("Invalid log level")

        return {
            "timestamp": timestamp,
            "log_level": log_level,
            "message": message,
            "raw": line.strip()
        }
    except Exception:
        print(f"Warning: Skipping malformed log line: {line.strip()}")
        return None

def load_logs(file_path):
    """Loads log entries from the specified file and returns a list of parsed logs."""
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("Log file is empty or does not exist.")
        return []

    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                logs.append(parsed)
    return logs

def count_log_levels(logs):
    """Counts occurrences of each log level in the log file."""
    counter = defaultdict(int)
    for log in logs:
        counter[log['log_level']] += 1
    return counter

def most_recent_log(logs, level):
    """Finds the most recent log entry of a specific log level."""
    if level not in VALID_LOG_LEVELS:
        print("Invalid log level.")
        return None
    
    # Filter logs by the specified level
    filtered = [log for log in logs if log['log_level'] == level]
    
    if not filtered:
        print(f"No logs found for level: {level}")
        return None
    
    # Return the most recent log based on timestamp
    return max(filtered, key=lambda x: x['timestamp'])

def filter_logs_by_date(logs, start_date, end_date):
    """Filters logs within a given date range and saves them to a file."""
    filtered = [
        log for log in logs
        if start_date <= log['timestamp'].date() <= end_date
    ]
    
    # Save the filtered logs to a file
    with open(FILTERED_FILE, 'w') as f:
        for log in filtered:
            f.write(log['raw'] + '\n')
    
    return filtered

def main():
    # """Main function to execute log analysis."""
    logs = load_logs(LOG_FILE)
    # Display log level counts
    print("\n\t1. Log Level Counts: ")
    counts = count_log_levels(logs)
    for level in VALID_LOG_LEVELS:
        print(f"{level}: {counts.get(level, 0)}")
    
    # Get the most recent log entry for a given log level
    level = input("\n2. Most Recent ERROR Entry: ").strip().upper()
    recent_log = most_recent_log(logs, level)
    if recent_log:
        print(f"\nMost recent {level} log:")
        print(recent_log['raw'])
    
    try:
        # Get start and end date inputs for filtering logs
        start = input("\nEnter start date (YYYY-MM-DD): ").strip()
        end = input("Enter end date (YYYY-MM-DD): ").strip()
        
        # Convert input strings to date objects
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()

        # Filter logs based on date range
        filtered = filter_logs_by_date(logs, start_date, end_date)
        if filtered:
            print(f"\nFiltered logs saved to '{FILTERED_FILE}' ({len(filtered)} entries).")
        else:
            print("\nNo logs found in the specified date range.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Entry point of the script
if __name__ == '__main__':
    main()
