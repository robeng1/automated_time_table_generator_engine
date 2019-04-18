#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 16/04/2019
#  Time: 15:27

from daytimetable import Daytimetable
from random import choice
##################################TODO######################################
# 0. Complete logic for best_fit(self,lecture)
# 1. Validation for all function paramers                                  #
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
    #class for holding the timetable structure of the institution
    # does not handle the creation of day timetables or the days
    # does not handle business logic
    # assumes days,timeslots etc make sense passed in make sense*

    days = [] #the days for which lectures can be scheduled
                #format for days decided by business logic
                #format must 
    timetable = {} #holds the timetable for teach day
                #keys are the days and the values are day timetables

    def __init__(self,days=[], daytables = []):
        #days is the list of all days open for scheduling
        #decide on business rule for validity of days
        #daytables is a list of Daytimetables representing the timetable
        #days must be the same as the day tables
        #decide on application rules to validate day tables
        #create timetable from days and daytables

        self.days = days

        for day in self.days:
            self.timetable[day] = daytables[self.days.index(day)]
            self.timetable[day].day = day #makes sure daytiemtable has a day
            #verify

        #set the day for each timetable slot

    def add_lecture(self,day,lecture,timetableslot,free=True):
        # validate the day //day should belong to days[]
        # lecture and timetableslot assumed valid

        if self.day_is_valid(day): #change to duck typing... catch exception
            return self.timetable[day].add_lecture(lecture,timetableslot,free)

        return False

    def move_lecture(self,sourceday,sourceslot,destday,destslot,free=True):
        # moves lecture from sourceslot to destslot
        # validate all day parameters and free
        # sourceday is compulsory
        # destday should be optional if user does not specify then move to first possible
        # sourceslot and destslot are validated by timetableslot module
        # returns false if parameters are invalid
        # true only returned from the daytimetable.move_lecture

        if sourceday == destday:
            return self.timetable[sourceday].move_lecture(sourceslot,destslot)
        else:
            timetableslot = self.timetable[sourceday].timetableslot(sourceslot.room,sourceslot.timeslot)
            
            if timetableslot.isoccupied:
                if self.add_lecture(destday,timetableslot.lecture,destslot,free):
                    if self.remove_lecture(sourceday,timetableslot):
                        return True
        return False

    def swap_lectures(self,day1,slot1,day2,slot2):
        # swaps the lectures in slots specified by parameters
        # validate day1 and day2 a
        # allow validation of slots to daytimetable
        # return true or false if lectures are swapped
        # validate slots and day
        # slot1 and slot2 may just be wrappers and not actually contain lectures

        swapped = False
        
        slot1 = self.timetable[day1].timetableslot(slot1.room,slot1.timeslot)
        slot2 = self.timetable[day2].timetableslot(slot2.room,slot2.timeslot)

        if day1 == day2 and slot1 == slot2:
            swapped = True

        elif day1 == day2  and slot1 != slot2:
            swapped = self.timetable[day1].swap_lectures(slot1,slot2)

        else:
             if (slot1.isoccupied and slot2.isoccupied):
                if slot1.timeslot.duration == slot2.timeslot.duration: #proove
                    if slot1.room.can_accomodate(slot2.lecture.curriculum_item.section.size)\
                        and slot2.room.can_accomodate(slot1.lecture.curriculum_item.section.size): 
                        
                        #overwrite the values in the slots by setting free = False
                        #verify
                        if self.timetable[day1].add_lecture(slot2.lecture,slot1,False):
                            if self.timetable[day2].add_lecture(slot1.lecture,slot2,False):
                                swapped = True
        return swapped
    
    def remove_lecture(self,day,timetableslot):
        # removes the lecture at day and timetable slot
        # leave timetableslot validation to daytimetable

        if self.day_is_valid(day):
            return self.timetable[day].remove_lecture(timetableslot)

        return False

    def remove_all(self):
        # removes all the lectures in the entire table
        
        for day in self.days:
            removed = self.timetable[day].remove_all()

            if not removed:
                return False

        return True

    def occupied_slots(self,day=None):
        # returns a list of all occupied slots on day
        # validate day
        # can return none
        occupied = []

        if day == None:
            for d in self.days:
                occupied += self.timetable[d].occupied_slots()
        else:
            if self.day_is_valid(day):
                occupied  = self.timetable[day].occupied_slots()

        return occupied

    def free_slots(self,day=None):
        # returns a list of all free slots on day
        # validate day 
        free =  []

        if day == None:
            for d in self.days:
                free+= self.timetable[d].free_slots()
        else:
            if self.day_is_valid(day):
                free = self.timetable[day].free_slots()

        return free

    def all_slots(self,day = None):
        # returns a list of all the slots in day
        # validate day
        #calls all_slots(unverified function) from daytimetable
        slots = []

        if day == None:
            slots = self.occupied_slots() + self.free_slots()
        else:
            if self.day_is_valid(day):
                slots = self.occupied_slots(day) + self.free_slots(day)
        
        return slots

    def lecturer_is_free(self,day,lecturer,timeslot):
        # returns true if lecturer is free on day at timeslot, false otherwise
        # validate day and lecturer
        # leave validation of timeslo to daytimetable
        # calls unverified function
        return self.timetable[day].lecturer_is_free()

    def room_is_free(self,day,room,timeslot):
        # returns true if room is free on day at timeslot, false otherwise
        # validate day
        # validate room** 
        # leave validation of timeslot for daytimetable
        # calss unverified function
        return self.timetable[day].room_is_free()

    def timetableslot(self,day,room,timeslot):
        # returns the timetableslot on day at room and at timeslot
        # validate day and * room
        # day should be an optional parameter 
        # if day not specified returns a list with timetable slots on all  those days
        # timeslot verified by daytimetable
        return self.timetable[day].timetableslot(room,timeslot)
    
    def best_fit(self,lecture):
        #  returns the best fit slot on day
        #  daytimetable may not return a timetable slot
        best_fits = []
        
        for day in self.days:
            best_fits.append(self.timetable[day].best_fit)

        #assuming all slots in best_fits are valid
        # deal with case where some of the slots are invalid
        
        return choice(best_fits)

    def first_fit(self,day,lecture):
        # returns the first fit for lecture on day
        # some days may not have any slot that can fit the lecture
        # that is some items in first may be None
        # may also return none 

        first_fits = []

        for slot in first_fits:
            if slot != None:
                return slot

    def day_is_valid(self,day): #returns true if the day is part of the initial days
        for d in self.days:
            if d == day:
                return True
        
        return False
