#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 14/04/2019
#  Time: 00:48

from timeslot import Timeslot
from data import CurriculumItem

#TODO:  dealing with lectures within the timetableslot
class Timetableslot():

    def __init__(self,day,room,timeslot):
        self._day = day
        self._timeslot = timeslot
        self._room = room
        self._occupied = False

    def _str__(self):
        return str(self.day) + str(self.room.name) + str(self.timeslot)#edit

    def remove_lecture(self):
        #only remove lecture from an occupied slot
        if self._occupied:
            self._occupied = False
        #delete the lecture

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self,d):
        self._day = d

    @property
    def lecture(self):
        if self._occupied:
            return self._lecture

    @property
    def timeslot(self):
        return self._timeslot

    @timeslot.setter
    def timeslot(self,tslot):
        self._timeslot = tslot

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self,room):
        self._room = room

    @lecture.setter
    def lecture(self,lect):
        self._lecture = lect
        self._occupied = True

    @property
    def isfree(self):
        return ~self._occupied
    
    @property
    def isoccupied(self):
        return self._occupied
  
