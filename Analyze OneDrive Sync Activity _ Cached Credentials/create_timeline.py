#!/usr/bin/env python3
import re
from datetime import datetime

def parse_log_file(filename):
    events = []
    with open(filename, 'r') as f:
        for line in f:
            # Extract timestamp and event
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)', line.strip())
            if match:
                timestamp, level, event = match.groups()
                events.append((timestamp, level, event))
    return events

def create_timeline(events):
    print("OneDrive Activity Timeline")
    print("=" * 50)
    for timestamp, level, event in sorted(events):
        print(f"{timestamp} [{level}] {event}")

# Parse the log file
events = parse_log_file('onedrive_artifacts/OneDrive/logs/Personal.log')
create_timeline(events)
