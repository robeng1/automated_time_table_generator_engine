#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 04:08

from datetime import datetime, timedelta


# TODO: Validations
# end time cannot be greater than start time

class TimeSlot(object):
    """
      A class for representing TimeSlot

      ...

      Attributes
      ----------
        _start : datetime
      	    Holds the starting time of the time_slot
            The date part of the datetime is irrelevant

        fmt : str
      		Holds format string for creating date time objects
            default value is '%H:%M'

        _end: datetime
      		Holds the ending time for the timeslot
            The date part of the datetime is irrelevant

        duration : int
            Holds the duration of the time_slot in minutes

    """

    # format string for the date
    fmt = '%H:%M'

    def __init__(self, start, end):

        # used datetime for start and end instead of time
        # to allow for arithmetic on the start and end times
        # only time portion of datetime is of interest
     
    
        self._start = datetime.strptime(start, self.fmt)
        self._end = datetime.strptime(end, self.fmt)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.start == other.start and self.end == other.end
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.start != other.start or self.end != other.end
        else:
            return NotImplemented

    def __hash__(self):
        # should not be hashable, only used in methods for removing duplicates via set
        return hash((self.start, self.end))

    def __str__(self):
        return self._start.strftime(self.fmt) + ' - ' + self._end.strftime(self.fmt)

    def shift_start(self, duration):
        self._start += timedelta(minutes=duration)

    def shift_end(self, duration):
        self._end += timedelta(minutes=duration)

    @property 
    def startstr(self):
        return self.start.strftime(self.fmt)
    
    @property
    def endstr(self):
        return self.end.strftime(self.fmt)

    @property
    def duration(self):
        time_delta = self._end - self._start  # returns a timedelta object not a datetime object
        return int(time_delta.total_seconds() // 60)

    @duration.setter
    def duration(self, duration):
        # duration is the time of the slot in minutes
        # duration must be non negative
        self._end = self._start + timedelta(minutes=duration)

    @property
    def start(self):
        return self._start.time()

    @start.setter
    def start(self, start):
        self._start = datetime.strptime(start, self.fmt)

    @property
    def end(self):
        return self._end.time()

    @end.setter
    def end(self, end):
        # end time must be greater than start time
        self._end = datetime.strptime(end, self.fmt)
