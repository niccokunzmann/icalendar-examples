import icalendar
import recurring_ical_events
import requests
import datetime

url = "https://download.hebcal.com/v4/CAEQARgBIAEoATABQAFQAVj-_KEBagFzeBKAAQGIAQGYAQGgAQE/hebcal_cardiff.ics"
calendar_text = requests.get(url).text

cal = icalendar.Calendar.from_ical(calendar_text)

now = datetime.datetime.now()

for i, event in enumerate(recurring_ical_events.of(cal).after(now)):
    print(f"{i} start: {event.start} {event.get('SUMMARY')}")
    if i > 5:
        break
