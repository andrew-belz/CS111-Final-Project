import datetime
import sys

README = "README.md"
LOG_MARKER = "#### end work log."

def main():

    if len(sys.argv) < 5:
        print("Error: Missing arguments.")
        print("Usage: python update_log.py <date|'today'> <start> <duration> \"<description>\"")
        print("Example: python update_log.py \"2025-11-02\" \"09:00\" \"2h\" \"Wrote the script.\"")
        sys.exit(1)

    log_date = sys.argv[1]
    if log_date.lower() == 'today':
        log_date = datetime.date.today().isoformat()

    start_time = sys.argv[2]
    duration = sys.argv[3]

    if start_time == 'now':
        start_time = datetime.datetime.now().strftime("%H:%M")

    description = ' '.join(sys.argv[4:])

    new_log_row = f"| {log_date} | {start_time} | {duration} | {description} |"

    try:
        with open(README, 'r') as file:
            lines = file.readlines()
        
        marker_index = -1
        for i, line in enumerate(lines):
            if LOG_MARKER in line:
                marker_index = i
                break

        if marker_index == -1:
            print(f"Error: Log marker '{LOG_MARKER}' not found in {README}")
            return
        
        lines.insert(marker_index, new_log_row + "\n")

        with open(README, 'w') as file:
            file.writelines(lines)

        print(f"Successfully added new log entry to {README}.")


    except FileNotFoundError:
        print(f"Error: {README} not found. Make sure to run the script in repo directory.")

    except Exception as e:
        print(f"An error occured: {e}")

    

if __name__ == "__main__":
    main()