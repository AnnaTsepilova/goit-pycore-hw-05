import sys
import re
from pathlib import Path

message_stats = {}

def parse_log_line(line: str) -> dict:
    parsed = re.split(r"^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s(\w+)\s(.*)$", line.strip())

    print(parsed)

    log_type = parsed[2]
    count_logs_by_level(log_type)

def load_logs(file_path: str) -> list:
    p = Path(file_path)
    if not p.exists():
        print(f"Error: file `{file_path}` not found")
        return False

    with open(file_path, "r", encoding="utf-8") as fh:
        for line in fh.readlines():
            parse_log_line(line)
        ##lines = [el.strip() for el in fh.readlines()]

    ## Handle empty file
    # if len(lines) == 0:
    #     print(f"Error: records not found. File `{file_path}`")
    #     return False

    return True


def filter_logs_by_level(logs: list, level: str) -> list:
    pass

def count_logs_by_level(type: str):
    if not message_stats.get(type):
        message_stats[type] = 1
    else:
        message_stats[type] += 1

def display_log_counts(counts: dict):
    print(message_stats)

def main():
    if len(sys.argv) > 1:
        load_logs(sys.argv[1])
        display_log_counts(None)
    else:
        print(f"  Usage: main.py LOG_FILE [MESSAGE_TYPE]")

if __name__ == "__main__":
    main()
