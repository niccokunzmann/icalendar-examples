from icalendar import Calendar, Event
from datetime import datetime
from pathlib import Path
import uuid
from zoneinfo import ZoneInfo

calendar = Calendar()
calendar.add("VERSION", "2.0")
calendar.add("PRODID", "my calendar program")

event = Event()
event.add("UID", uuid.uuid4())
event.start = datetime(2026, 3, 19, 12, 30, tzinfo=ZoneInfo("Europe/London"))
event.DTSTAMP = datetime.now(ZoneInfo("UTC"))

event.add("SUMMARY", "This is my first event!")

calendar.add_component(event)

calendar.add_missing_timezones()
Path("export.ics").write_bytes(calendar.to_ical())
