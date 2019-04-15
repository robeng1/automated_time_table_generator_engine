#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 04:08

from datetime import datetime,timedelta 

#TODO: Validations
#end time cannot be greater than start time

class Timeslot(object):
    """
      A class for representing Timeslot

      ...

      Attributes
      ----------

        _start : datetime
      		Holds the starting time of the timeslot
            The date part of the datetime is irrelevant

        fmt : str
      		Holds format string for creating date time objects
            default value is '%H:%M'

        _end: datetime
      		Holds the ending time for the timeslot
            The date part of the datetime is irrelevant
        
        duration : int
            Holds the duration of the timeslot in minutes

    """

    #format string for the date 
    fmt ='%H:%M'

    def __init__(self,start,end):

        #used datetime for start and end instead of time 
        #to allow for arithmetic on the start and end times
        self._start = datetime.strptime(start,self.fmt)
        self._end  = datetime.strptime(end,self.fmt)

    def __str__(self):
        return self._start.strftime(self.fmt) + ' - ' + self._end.strftime(self.fmt)

    @property
    def duration(self):
        tdelta = self._end - self._start #returns a timedelta object not a datetime object
        return int(tdelta.total_seconds()//60)

    @duration.setter
    def duration(self,duration):
        #duration is the time of the slot in minutes
        self._end = self._start + timedelta(minutes = duration)

    @property
    def start(self):
        return self._start.time()

    @start.setter
    def start(self,start):
        self._start = datetime.strptime(start,self.fmt)

    @property
    def end(self):
        return self._end.time()

    @end.setter
    def end(self,end):
        self._end = datetime.strptime(end,self.fmt)
    
if __name__ == '__main__':
    t1 = Timeslot('11:15','12:15')
    print(t1)
    print(t1.duration)
    print(t1.start)
    print(t1.end)
    t1.duration = 40
    print(t1)
    print(t1.duration)
    print(t1.start)
    print(t1.end)    
    t1.start = '08:15'
    print(t1.start)
