#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 16/04/2019
#  Time: 15:27

from .daytimetable import DayTimetable
from random import choice
from copy import deepcopy

##################################TODO######################################
# 0. Complete logic for best_fit(self,lecture)
# 1. Validation for all function params                                  #
# 2. Exceptions and exception handlers                                     #
# 3. Doc strings                                                           #
# 4. Unit tests                                                            #
# 5. Adjust logic for lecturer components. courses etc have a list of      #
# of lecturers not a single lecturer                                       #  
# 6. Add partitioning to timetable if the added lecture is less than slot
# duration           
# 7. Type hinting
# 8. Add spliting of timeslots after addition of lecture with smaller duration
############################################################################


class Timetable:
    # class for holding the timetable structure of the institution
    # does not handle the creation of day timetables or the _days
    # does not handle business logic
    # assumes _days,timeslots etc make sense passed in make sense*

    #_days = []  # the _days for which lectures can be scheduled
    # format for _days decided by business logic
    # format must
   # timetable = {}  # holds the timetable for teach day

    # keys are the _days and the values are day timetables

    def __init__(self, days=[], daytables=[]):
        # _days is the list of all _days open for scheduling
        # decide on business rule for validity of _days
        # daytables is a list of Daytimetables representing the timetable
        # _days must be the same as the day tables
        # decide on application rules to validate day tables
        # create timetable from _days and daytables
        self._days = []
        self.timetable = {}
        self._days = deepcopy(days)

        i= 0
        for day in self._days:
            std= deepcopy(daytables[i])
            self.timetable[day] = deepcopy(DayTimetable(std.rooms, std.time_slots, std.day))
            self.timetable[day].day = deepcopy(day)  # makes sure daytiemtable has a day
            i = i+1
            # verify

        # set the day for each timetable slot

    def __str__(self):
        temp_str = ''

        for day in self._days:

            temp_str = temp_str + str(self.timetable[day])
        
        return temp_str


    @property
    def day_table(self):
        return self.timetable

    @property
    def days(self):
        return self._days

    def add_lecture(self, day, lecture, timetableslot, free=True):
        # validate the day //day should belong to _days[]
        # lecture and timetableslot assumed valid

        if self.day_is_valid(day):  # change to duck typing... catch exception
            timetableslot.day = day
            return self.timetable[day].add_lecture(lecture, timetableslot, free)

        return False

    def move_lecture(self, sourceday, sourceslot, destday, destslot, free=True):
        # moves lecture from sourceslot to destslot
        # validate all day parameters and free
        # sourceday is compulsory
        # destday should be optional if user does not specify then move to first possible
        # sourceslot and destslot are validated by timetableslot module
        # returns false if parameters are invalid
        # true only returned from the daytimetable.move_lecture

        try:
            if sourceday == destday:
                return self.timetable[sourceday].move_lecture(sourceslot, destslot)
            else:
                timetableslot = self.timetable[sourceday].timetableslot(sourceslot.room, sourceslot.time_slot)

                if timetableslot.is_occupied:
                    if self.add_lecture(destday, timetableslot.lecture, destslot, free):
                        if self.remove_lecture(sourceday, timetableslot):
                            return True
        except Exception:
            print(Exception)
        return False

    def swap_lectures(self, day1, slot1, day2, slot2):
        # swaps the lectures in slots specified by parameters
        # validate day1 and day2 a
        # allow validation of slots to daytimetable
        # return true or false if lectures are swapped
        # validate slots and day
        # slot1 and slot2 may just be wrappers and not actually contain lectures

        swapped = False

        slot1 = self.timetable[day1].timetableslot(slot1.room, slot1.time_slot)
        slot2 = self.timetable[day2].timetableslot(slot2.room, slot2.time_slot)

        if day1 == day2 and slot1 == slot2:
            swapped = True

        elif day1 == day2 and slot1 != slot2:
            swapped = self.timetable[day1].swap_lectures(slot1, slot2)

        else:
            if slot1.is_occupied and slot2.is_occupied:
                if slot1.time_slot.duration == slot2.time_slot.duration:  # proove
                    if slot1.room.can_accommodate(slot2.lecture.curriculum_item.section.size) \
                            and slot2.room.can_accommodate(slot1.lecture.curriculum_item.section.size):

                        # overwrite the values in the slots by setting free = False
                        # verify
                        if self.timetable[day1].add_lecture(slot2.lecture, slot1, False):
                            if self.timetable[day2].add_lecture(slot1.lecture, slot2, False):
                                swapped = True
        return swapped

    def remove_lecture(self, day, timetableslot):
        # removes the lecture at day and timetable slot
        # leave timetableslot validation to daytimetable

        try:
            if self.day_is_valid(day):
                return self.timetable[day].remove_lecture(timetableslot)
        except Exception:
            print(Exception)
            
        return False

    def remove_all(self):
        # removes all the lectures in the entire table

        for day in self._days:
            removed = self.timetable[day].remove_all()

            if not removed:
                return False

        return True

    def occupied_slots(self, day=None):
        # returns a list of all occupied slots on day
        # validate day
        # can return none
        occupied = []

        if day == None:
            for d in self._days:
                occupied += self.timetable[d].occupied_slots()
        else:
            if self.day_is_valid(day):
                occupied = self.timetable[day].occupied_slots()

        return occupied

    def free_slots(self, day=None):
        # returns a list of all free slots on day
        # validate day 
        free = []

        if day == None:
            for d in self._days:
                free += self.timetable[d].free_slots()
        else:
            if self.day_is_valid(day):
                free = self.timetable[day].free_slots()

        return free

    def all_slots(self, day=None):
        # returns a list of all the slots in day
        # validate day
        # calls all_slots(unverified function) from daytimetable
        slots = []

        if day == None:
            slots = self.occupied_slots() + self.free_slots()
        else:
            if self.day_is_valid(day):
                slots = self.occupied_slots(day) + self.free_slots(day)

        return slots

    #############################################################################################
    def lecturer_is_free(self, day, lecturer, timeslot):
        # returns true if lecturer is free on day at timeslot, false otherwise
        # validate day and lecturer
        # leave validation of timeslo to daytimetable
        # calls unverified function
        return self.timetable[day].lecturer_is_free(lecturer, timeslot)
    
    def section_is_free(self,day,section,timeslot):
        return self.timetable[day].section_is_free(section,timeslot)


    def left_neighbours(self,ttslot):
        return self.timetable[ttslot.day].left_neighbours(ttslot)

    def right_neighbours(self,ttslot):
        return self.timetable[ttslot.day].right_neighbours(ttslot)

    def left_free_cont_neighbours(self,ttslot):
        return self.timetable[ttslot.day].left_free_cont_neighbours(ttslot)

    def right_free_cont_neighbours(self,ttslot):
        return self.timetable[ttslot.day].right_free_cont_neighbours(ttslot)

    def room_is_free(self, day, room, timeslot):
        # returns true if room is free on day at timeslot, false otherwise
        # validate day
        # validate room** 
        # leave validation of timeslot for daytimetable
        # calss unverified function
        return self.timetable[day].room_is_free(room, timeslot)

    def timetableslot(self, day, room, timeslot):
        # returns the timetableslot on day at room and at timeslot
        # validate day and * room
        # day should be an optional parameter 
        # if day not specified returns a list with timetable slots on all  those _days
        # timeslot verified by daytimetable
        return self.timetable[day].timetableslot(room, timeslot)

    def best_fit(self, lecture):
        #  returns the best fit slot on day
        #  daytimetable may not return a timetable slot
        best_fits = []

        for day in self._days:
            best_fits.append(self.timetable[day].best_fit(lecture))

        # assuming all slots in best_fits are valid
        # deal with case where some of the slots are invalid

        return choice(best_fits)

    def first_fit(self, day, lecture):
        # returns the first fit for lecture on day
        # some _days may not have any slot that can fit the lecture
        # that is some items in first may be None
        # may also return none 

        first_fits = []

        for slot in first_fits:
            if slot != None:
                return slot

    def remove_slot(self,day,room,timeslot):
        self.timetable[day].remove_time_table_slot(room,timeslot)

    def insert_slot(self,day,ttslot):
        self.timetable[day].insert_time_table_slot(ttslot)

    def day_is_valid(self, day):  # returns true if the day is part of the initial _days
        for d in self._days:
            if d == day:
                return True

        return False

    def periods(self,day,room):
        #returns all the slots on the given day and the room
        return self.timetable[day].table[room]

    def section_lectures(self,section,day):
        #returns the number of lectures that the section has had on that day
        count = 0 
        for room in self.timetable[day].table:
            for slot in self.timetable[day].table[room]:
                if slot.is_occupied and slot.lecture.curriculum_item.section == section:
                    count+=1

        return count

    def lecturer_lectures(self,lecturer,day):
        #returns the number of lectures that the lecturer has already had on the day
        count = 0 
        for room in self.timetable[day].table:
            for slot in self.timetable[day].table[room]:
                if slot.is_occupied and slot.lecture.curriculum_item.lecturer == lecturer:
                    count+=1

        return count

    def room_lectures(self,room,day):
        #returns the number of lectures that have been scheduled in that room already on that day
        count =0 

        for slot in self.timetable[day].table[room]:
            if slot.is_occupied:
                count+=1

        return count

    def day_lectures(self,day):
        #returns the number of lectures that have been scheduled already on that day

        count =0

        for room in self.timetable[day].table:
            for slot in self.timetable[day].table[room]:
                if slot.is_occupied:
                    count+=1

        return count

    def c_item_on_day(self,day,c_item):
        return self.timetable[day].c_item_on_day(c_item)

    def lecturer_clashes(self):
        clashes = []
        for day in self._days:
            clashes.append(self.timetable[day].lecturer_clashes())

        return clashes

    def section_clashes(self):
        clashes = []

        for day in self._days:
            clashes.append(self.timetable[day].lecturer_clashes())

        return clashes

    
