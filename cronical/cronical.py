import crontab
import datetime
import icalendar
import tzlocal
from crontabs import CronTabs

prodid = "cronical"
version = "0.0"

class Cronical(object):
    """
    We currently don't use ical's recurrence, but a configurable PERIOD. The  resultant ical will
    contain much unique events as needed to reach PERIOD days.
    """

    crontabs = CronTabs()
    calendar = icalendar.Calendar()

    def __init__(
            self,
            filelist=None,
            period=None,
            duration=None
        ):

        if period > 366:
            # This is completely arbitrary
            raise ValueError("Periods longer than an year are currently not supported")

        uid=0
       
        for ctab in self.crontabs:


            for job in ctab:

                if job.is_valid() and job.is_enabled():
                    
                    # Creates an event in ical for every valid job occurence in PERIOD
                    current_period = 0
                    schedule = job.schedule()
                    
                    while (current_period < period):

                        # Calculates the next occurency period from now
                        next_oc = schedule.get_next().replace(tzinfo=tzlocal.get_localzone())
                        current_period = (next_oc - datetime.datetime.now(tzlocal.get_localzone())).days

                        event = icalendar.Event()
                        event.add("uid", uid)

                        # We prefer comments over commands, if possible
                        if job.comment:
                            event.add("summary", job.comment)
                        else:
                            event.add("summary", job.command)

                        event.add("description" , job.command)

                        # For readability, all "events" have 10 minutes(see default_settings.py:
                        event.add("dtstart", next_oc)
                        event.add("dtend", next_oc + datetime.timedelta(minutes=duration))
                        event.add("dtstamp", datetime.datetime.now(tzlocal.get_localzone()))

                        self.calendar.add_component(event)
                        uid += 1

    def ical(self):
        return self.calendar.to_ical()
