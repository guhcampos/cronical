# cronical
A self-contained tool to export and serve a system's crontabs as an iCalendar feed, with the purpose of easily sharing job information

Uses Flask running on Gunicorn to serve the feed.  Relies on ```python-crontab``` for parsing cronfiles and ```icalendar``` to write proper ical.

This is currently just a stub and not suited for production. Consider it ```alpha(alpha())```
