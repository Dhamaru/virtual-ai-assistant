# datetime_utils.py - Date and time, read from the computer's clock.
from datetime import datetime


def get_current_time():
    """Return the time, e.g. "It's currently 03:45 PM." (%I hour, %M minutes, %p AM/PM)."""
    return "It's currently " + datetime.now().strftime("%I:%M %p") + "."


def get_current_date():
    """Return the date, e.g. "Today is Wednesday, 21 October 2026." (%A day, %d, %B month, %Y)."""
    return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
