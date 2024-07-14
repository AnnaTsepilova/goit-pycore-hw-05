import sys
import re
from pathlib import Path

##message_stats = {}

def parse_log_line(line: str) -> dict:
    '''
    Parse log line in format: DATE LEVEL MESSAGE
    '''
    parsed = re.split(r"^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s(\w+)\s(.*)$", line)
    return {'date': parsed[1], 'level': parsed[2], 'message': parsed[3]}

def load_logs(file_path: str) -> list:
    p = Path(file_path)
    if not p.exists():
        print(f"Error: file `{file_path}` not found")
        return False

    with open(file_path, "r", encoding="utf-8") as fh:
        lines = [el.strip() for el in fh.readlines()]
        ## Parse file line by line
        # for line in fh.readlines():
        #     parse_log_line(line.strip())

    ## Handle empty file
    if len(lines) == 0:
        print(f"Error: records not found. File `{file_path}`")
        return False

    return lines


def filter_logs_by_level(logs: list, level: str) -> list:
    '''
    Function filter and return logs by level
    '''
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    message_stats = {}
    for log in logs:
        if not message_stats.get(log['level']):
            message_stats[log['level']] = 1
        else:
            message_stats[log['level']] += 1

    return message_stats

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print('-' * 17 + '|' + '-' * 10)
    for log_type, amount in counts.items():
        print(f"{log_type}\t\t |{amount}")

def main():
    if len(sys.argv) > 1:
        raw_lines = load_logs(sys.argv[1])

        parsed_lines = []
        for line in raw_lines:
            parsed_lines.append(parse_log_line(line))

        message_stats = count_logs_by_level(parsed_lines)
        display_log_counts(message_stats)

        filtered = filter_logs_by_level(parsed_lines, "INFO")
        [print(f"{f['date']} {f['level']} {f['message']}") for f in filtered]
    else:
        print(f"  Usage: main.py LOG_FILE [MESSAGE_TYPE]")

if __name__ == "__main__":
    main()
