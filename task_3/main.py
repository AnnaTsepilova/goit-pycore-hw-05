import sys
import re
import collections
from pathlib import Path

def parse_log_line(line: str) -> dict:
    '''
    Parse log line in format: DATE LEVEL MESSAGE
    '''
    parsed = re.split(r"^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s(\w+)\s(.*)$", line)
    return {'date': parsed[1], 'level': parsed[2].upper(), 'message': parsed[3]}

def load_logs(file_path: str) -> list | bool:
    p = Path(file_path)
    if not p.exists():
        print(f"Error: file `{file_path}` not found")
        return False

    with open(file_path, "r", encoding="utf-8") as fh:
        lines = [el.strip() for el in fh.readlines()]

    ## Handle empty file
    if len(lines) == 0:
        print(f"Error: records not found. File `{file_path}`")
        return False

    parsed_lines = []
    for num, line in enumerate(lines):
        try:
            parsed_log = parse_log_line(line)
        except Exception as e:
            print(f"Unable to parse line {num}. Reason: {e}. Skipping")
            continue

        parsed_lines.append(parsed_log)

    return parsed_lines


def filter_logs_by_level(logs: list, level: str) -> list:
    '''
    Function filter and return logs by level
    '''
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    '''
    Function calculate each log level
    '''
    message_stats = dict(collections.Counter(map(lambda log: log['level'], logs)))
    return message_stats

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print('-' * 17 + '|' + '-' * 10)
    for log_type, amount in counts.items():
        print(f"{log_type}\t\t |{amount}")

def main():
    if len(sys.argv) > 1:
        log_path = sys.argv[1]
        log_level = sys.argv[2]

        parsed_lines = load_logs(log_path)

        if not parsed_lines:
            return False

        message_stats = count_logs_by_level(parsed_lines)
        display_log_counts(message_stats)

        if log_level:
            log_level = log_level.upper().strip()
            for f in filter_logs_by_level(parsed_lines, log_level):
                print(f"{f['date']} {f['level']} {f['message']}")
    else:
        print("  Usage: main.py LOG_FILE [LOG_LEVEL]")

if __name__ == "__main__":
    main()
