# TrimCal

A Python script to filter out past events from an `.ics` (iCalendar) file, keeping only those that occur on or after a specified threshold date.

---

## Features

- Parses `.ics` files line by line (no third-party dependencies)
- Keeps events with `DTSTART` or `DTEND` on or after a threshold date
- Writes filtered events to a new `.ics` file (`filtered.ics`)

---

## Requirements

- Python 3.x
- No external libraries required

---

## Usage

### 1. Clone or download this repository

```bash
git clone https://github.com/yourusername/filter-ics-events.git
cd filter-ics-events
```

### 2. Run the script

```bash
python3 filter_ics_events.py
```

### 3. Provide inputs when prompted:

- **Path to the .ics file** — for example: `~/Downloads/calendar.ics`
- **Threshold date** — in format `YYYY-MM-DD` (e.g., `2025-04-01`)

The script will:
- Load the `.ics` file
- Filter out any events that end *before* the given date
- Save the remaining events to a file named `filtered.ics`

---

## Output

- Output file: `filtered.ics`
- Only events with `DTSTART` or `DTEND` dates on or after the threshold will be retained.

---

## Example

**Input:**
```text
Path to the .ics file: /home/user/calendar.ics
Threshold date (YYYY-MM-DD): 2025-04-01
```

**Output:**
```text
Filtered file written to: filtered.ics
```

---

## Notes

- This script uses raw text parsing and does not rely on `ics` or `icalendar` libraries.
- It assumes standard `.ics` formatting with lines like `DTSTART:YYYYMMDD` or `DTEND:YYYYMMDD`.

---

## License

GPL 3
