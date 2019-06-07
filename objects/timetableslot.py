#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 14/04/2019
#  Time: 00:48

# from .timeslot import TimeSlot
# from .data import CurriculumItem
# from .classroom import Classroom


# TODO:  dealing with lectures within the timetableslot
class TimetableSlot:

    def __init__(self, day, room, time_slot):
        self._day = day
        self._time_slot = time_slot
        self._room = room
        self._occupied = False

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.day == other.day and self.time_slot == other.time_slot \
                   and self.room == other.room
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.day != other.day or self.time_slot != other.time_slot \
                   or self.room != other.room
        else:
            return NotImplemented

    # def __hash__(self):#should not be hashable
    #    return ((self.day,self.timeslot,self.room))

    def __str__(self):
        temp = str(self.day)+ "       " + str(self.room.name) + "  Capacity   :   " + str(self.room.capacity)\
        +"     "+ str(self.time_slot)

        if self.is_occupied:
            temp+=self.lecture.__str__()

        return temp

    def remove_lecture(self):
        # only remove lecture from an occupied slot
        if self._occupied:
            self._occupied = False
        # delete the lecture

    def can_hold(self, lecture):
        return self.room.can_accommodate(lecture.curriculum_item.section.size) and \
               self.time_slot.duration >= lecture.duration

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, d):
        self._day = d

    @property
    def lecture(self):
        if self._occupied:
            return self._lecture

    @property
    def time_slot(self):
        return self._time_slot

    @time_slot.setter
    def time_slot(self, tslot):
        self._time_slot = tslot

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room

    @lecture.setter
    def lecture(self, lect):
        self._lecture = lect
        self._occupied = True

    @property
    def is_free(self):
        return not self._occupied

    @property
    def is_occupied(self):
        return self._occupied

    @is_occupied.setter
    def is_occupied(self,val):
        self._occupied = val

