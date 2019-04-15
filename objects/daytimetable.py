#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 15:27

from data import CurriculumItem
from classroom import Classroom
from timetableslot import Timetableslot

#TODO:
#resolve import, already imported from timetableslot

from timeslot import Timeslot

##################################TODO######################################
# 1. Validation for all function paramers                                  #
# 2. Exceptions and exception handlers                                     #
# 3. Doc strings                                                           #
# 4. Unit tests                                                            #
############################################################################

class Daytimetable:
#class to hold the timetable for a particular day
#knows nothing about collisions
#only checks to make sure that a lecture can fit into a particular slot
#based on the room size and the section size 
#and on if the duration of the lecture can fit into the slot

    rooms = [] #rooms sorted in reverse order of their size
    timeslots =[] 
    table = {}

    def __init__(self,classrooms=[],timeslots=[]):
        #classrooms is the list of all classrooms in the school
        #timeslots can vary for each day
        #validate to check instances of particular class

        #ensures each classroom only appears once on the list
        classrooms = list(set(classrooms))
    
        classrooms.sort(key = lambda classroom: classroom.capacity,reverse =True)
        self.rooms = classrooms

        #ensures each timeslot only occurs once in the least
        timeslots = list(set(timeslots))

        #sort the timeslots according to starting time
        timeslots.sort(key = lambda timeslot: timeslot.start)

        #ensure there are no overlapping times in the timeslots
        for i in range(len(timeslots)-1):
            if timeslots[i].end > timeslots[i+1].start: #proove correctness
                #raise exception
                pass
        self.timeslots = timeslots

        for room in self.rooms:
            slots = []
            for timeslot in self.timeslots:
                timetableslot = Timetableslot(0,room,timeslot) #convert 0 to enums use enum for days
                slots.append(timetableslot)
            self.table[room] = slots

        ############################################Test stub###############################
        #for room in self.rooms:
        #    for slot in self.table[room]:
        #        print(str(slot.day)+ '\n'+ str(slot.timeslot)+ '\n'+ str(slot.room) )
        ####################################################################################

    def __str__(self):
        #print the entire timetable for that particular day
        pass

    #assigns lecture without checking if slot is free
    def add_lecture(self,lecture,timetableslot,free=True):
        #validate the lecture
        #validate the tableslot
        #check if timetableslot has a lecture in it
        #free enables assignment only if the timetableslot is free
            #day is not checked, assumed checked by timetable module
            
            #check if class room is on the list of  class rooms
            #check if the timeslot is in the table
        try:
            self.rooms.index(timetableslot.room)
            timeslot_index = self.timeslots.index(timetableslot.timeslot)
        except ValueError:
            #handle exception
            pass

        #check if lecture can fit into classroom based on size
        #check if the duration of the lecture can fit into the slot
        if free:#assign slot only if the lecture is free
            if timetableslot.isfree:
                if lecture.duration <= timetableslot.timeslot.duration:
                    if lecture.curriculum_item.section.size <= timetableslot.room.capacity:
                        timetableslot.lecture = lecture
                        self.table[timetableslot.room][timeslot_index]  = timetableslot
                        return True
        elif not free: #assign lecture wether slot is free or not
            if lecture.duration <= timetableslot.timeslot.duration:
                if lecture.curriculum_item.section.size <= timetableslot.room.capacity:
                    timetableslot.lecture = lecture
                    self.table[timetableslot.room][timeslot_index]  = timetableslot
                    return True
        #assign the lecture to the timetable slot
        #return true if successful
        return False

    #convert to decorator function        
    def move_lecture(self,sourceslot,destslot,free=True):
        #validate the source and the destination slots
        #check if the sourceslot is occupied

        #move the lecture from the sourceslot to the destlot
        timetableslot = self.timetableslot(sourceslot.room,sourceslot.timeslot)
        if  self.add_lecture(sourceslot.lecture,destslot,free):
            if self.remove_lecture(timetableslot):
                return True
        return False
        #mark the source slot as free
        #mark destination as occupied
        #return true if successful
    def swap_lectures(self,slot1,slot2):
        #validate slot1
        #validate slot2
        #slot1 and slot2 are timetable slots

        #check if both lectures can be swapped
        #slots can only be swapped if they have equal durations
        #slots can only be swapped if the at each slot can accomodate the different slots
        #only swap if both slots are occupied
        #swap both lectures in slot
        if (slot1 != slot2) and (slot1.isoccupied and slot2.isoccupied):
            if slot1.timeslot.duration == slot2.timeslot.duration:
                if slot1.room.can_accomodate(slot2.lecture.curriculum_item.section.size)\
                    and slot2.room.can_accomodate(slot1.lecture.curriculum_item.section.size): 
                    index_1 = self.table[slot1.room].index(slot1)
                    index_2 = self.table[slot2.room].index(slot2)
                    self.table[slot1.room][index_1],self.table[slot2.room][index_2] =\
                         slot2,slot1
                    return True
        return False

    def remove_lecture(self,timetableslot):
        #validate tableslot
        #make sure the slot is occupied
        #remove the lecture at table slot
        #mark the slot as free
        #return true if sucessful

        if timetableslot.isoccupied:
            index = self.table[timetableslot.room].index(timetableslot)
            self.table[timetableslot.room][index].remove_lecture()
            return True
        
        return False

    def occupied_slots(self):
        #returns a list containing all the occupied timetable slots in the table
        occupied = []
        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isoccupied:
                    occupied.append(slot)
        return occupied

    def free_slots(self):
        free = []#returns a list containing all the free slots in the table
        pass
        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isfree:
                    free.append(slot)
        return free

    def lecturer_free(self,lecturer,timeslot):
        #validate the lecturer and the timeslot
        #check all classes within that time if the lecturer is free
        #checks if a room is free at a particular day and at a particular time
        #return true if empty 
        index = self.timeslots.index(timeslot)
        for room in self.rooms:
            slot = self.table[room][index]
            if slot.isoccupied:
                for lect in slot.lecture.curriculum_item.lecturers:
                    if lect == lecturer:
                        return False
        
        return True

    def room_free(self,room,timeslot):
        #validate room and timeslot 

        #check if the room is free within that time 
        #return true if the room is empty
        for slot in self.table[room]:
            if slot.timeslot == timeslot and slot.isfree:
                return True
        
        return False

    def timetableslot(self,room,timeslot):
        #validate the room and the timeslot
        #return the timetableslot at the time and the room
        for slot in self.table[room]:
            if slot.timeslot == timeslot:
                return slot
    
    def best_fit(self,lecture,allowance = 0):
        #returns the free timetable slot with smallest room size big big enough to hold 
        #the lecture
        #******take care of if none is found
        class_size = lecture.curriculum_item.section.size
        max = -1 #the first class that picks will be best and then ...
        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isfree:
                    if (slot.room.capacity +allowance - class_size)> max: #check
                        if lecture.duration <= slot.timeslot.duration: #check after construction
                            best = slot
                            max = slot.room.capacity - class_size

        #*take care of if none is found
        return best

    def first_fit(self,lecture):
        #returns the index of the first position in the timetable that is can contain the given
        #lecture based on all the given constraints
        #********take care of if none is found
        class_size = lecture.curriculum_item.section.size

        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isfree:
                    if slot.room.capacity >= class_size :
                        if lecture.duration <= slot.timeslot.duration: #check after construction
                            return slot


if __name__ == '__main__':
    timeslots = [Timeslot('11:15','12:15'),Timeslot('8:15','11:15'),Timeslot('13:15','14:15')]
    for slot in timeslots:
        print(str(slot))
    timeslots.sort(key = lambda timeslot: timeslot.start)
    for slot in timeslots:
        print(str(slot))

    for i in range(len(timeslots)-1):
        if timeslots[i].end > timeslots[i+1].start:
            print("Overlap exits")

    
    classrooms = [Classroom('PB001',100),Classroom('PB001',120),Classroom('PB002',110),\
        Classroom('PB003',120),Classroom('PB003',111),Classroom('PB004',120),\
            Classroom('PB005',120),Classroom('PB006',120),Classroom('PB007',120)]
    
    timetable = Daytimetable(classrooms,timeslots)