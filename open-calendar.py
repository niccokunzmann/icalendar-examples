import icalendar
import pathlib

file = pathlib.Path("2025-05-07 1400 WoT Profile.ics")
content = file.read_text()

ical = icalendar.Calendar.from_ical(content)

for event in ical.events:
    print(event.get("SUMMARY"))
    print(event.start)
