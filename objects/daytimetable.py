#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 06:27

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
    def add_lecture(self,lecture,timetableslot):
        #validate the lecture
        #validate the tableslot
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
        if lecture.duration <= timetableslot.timeslot.duration:
            if lecture.section.size <= timetableslot.room.capacity:
                timetableslot.lecture = lecture
                self.table[timetableslot.room][timeslot_index]  = timetableslot

                return True
        #assign the lecture to the timetable slot
        #return true if successful
        return False

        #assigns lecture only if slot is free
    def add_lecture_if_free(self,lecture,timetableslot):
        pass

    def move_lecture(self,sourceslot,destslot):
        #validate the source and the destination slots
        #check if the destslot is unoccupied
        #move the lecture from the sourceslot to the destlot
        #markt the source slot as free
        #mark destination as occupied
        #return true if successful
        pass

    def remove_lecture(self,tableslot):
        #validate tableslot
        #remove the lecture at table slot
        #mark the slot as free
        #return true if sucessful
        pass

    def occupied_slots(self):
        #returns a set containing all the occupied timetable slots in the table
        pass

    def free_slots(self):
        #returns a set containing all the free slots in the table
        pass

    def lecturer_free(self,lecturer,timeslot):
        #validate the lecturer and the timeslot
        #check all classes within that time if the lecturer is free
        #checks if a room is free at a particular day and at a particular time
        #return true if empty 
        pass

    def room_free(self,room,timeslot):
        #validate room and timeslot 
        #check if the room is free within that time 
        #return true if the room is empty
        pass

    def room_fits_lect(self,room,lecture,allowance=0):
        #validate the room and the lecture
        #check if the room is size is enough for the lecture with allowance given
        #return true if it does and false otherwise
        pass

    def lecture(self,room,timeslot):
        #validate the room and the timeslot
        #return an empty lecture if there is the slot is unoccupied
        #return the lecture at the time and the room
        pass
    def info(self,room,timeslot):
        #validate the room and the timeslot
        #return the timetableslot at the room and the time
    
    #def best_fit_room_size(self,lecture,allowance = 0):
        #returns the timetable with smalles room size big big enough to hold 
        #the lecture
        #take care of if none is found
        pass

    def first_fit(self):
        #returns the index of the first position in the timetable that is can contain the given
        #lecture based on all the given constraints
        #take care of if none is found
        pass

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