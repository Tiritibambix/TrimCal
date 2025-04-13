# file: trimcal.py

from datetime import datetime

input_path = input("Path to the .ics file: ").strip()
date_str = input("Threshold date (YYYY-MM-DD): ").strip()

try:
    threshold_date = datetime.strptime(date_str, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Use YYYY-MM-DD.")
    exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
event_lines = []
in_event = False
keep_event = False

for line in lines:
    if line.startswith("BEGIN:VEVENT"):
        in_event = True
        event_lines = [line]
        keep_event = False
    elif line.startswith("END:VEVENT"):
        event_lines.append(line)
        if keep_event:
            output_lines.extend(event_lines)
        in_event = False
    elif in_event:
        event_lines.append(line)
        if line.startswith("DTEND") or line.startswith("DTSTART"):
            date_part = line.split(":", 1)[1].strip()
            try:
                event_date = datetime.strptime(date_part[:8], "%Y%m%d")
                if event_date >= threshold_date:
                    keep_event = True
            except ValueError:
                pass
    else:
        output_lines.append(line)

output_path = "filtered.ics"
with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(output_lines)

print(f"Filtered file written to: {output_path}")
