from data import CurriculumItem
from classroom import Classroom
from timetableslot import Timetableslot

#TODO : convert arguments to timetable slot objects

class Timetable:

    table = []
    hashtable = {}
    POS_DAY = 0
    POS_ROOM = 1
    POS_SLOT = 2

    def __init__(self,days=[],rooms=[],timeslots=[]):
        count = 0
        for day in days:
            for room in rooms:
                for tslot in timeslots:
                    key  = hash(day,room,tslot)
                    self.hashtable[key] = count
                    timetableslot = Timetableslot(day,room,tslot)
                    self.table.append(timetableslot)
                    count+=1
    
    def __str__(self):
        pass

    def hash(self,timetableslot):
        return str(timetableslot.day) + timetableslot.room.name + str(timetableslot.timeslot)

    #checks if a lecturer is free at a particular day and a particular time interval
    #traverse all classes 
    def lecturerfree(self,day,lecturer,timeslot):
        for slot in table:
            if slot.isoccupied and slot.lecture.lecturer == lecturer:
                return True
            return False


    #checks if a room is free at a particular day and at a particular time
    def roomfree(self,day,room,timeslot):
        pass

    #checks if lecture can be held in particular room
    def roomfitslect(self,room,lect):
        pass

    #assigns a lectuer to a particular position on timetable    
    def addlect(self,day,room,slot,lecture):
        key = self.hash(day,room,slot)
        index = self._hashtable[key]

        if self._table[index][POS_SLOT].isfree:
            self._table[index][POS_SLOT].lecture = lecture

    #moves the lecture to a particular position on the time table does not check if
    #the position on the timetable is free
    #returns true if the lecture was moved
    def mov_lect(self,f_day,f_room,f_tslot,t_day,t_room,t_tslot):
        origin_key = self.hash(f_day,f_room,f_tslot)
        dest_key = self.hash(t_day,t_room,t_tslot)
        
        origin_index = self._hashtable[origin_key]
        dest_index = self._hashtable[dest_key]

        self._table[dest_index][POS_SLOT] = self._table[origin_index][POS_SLOT]

    #moves the lecture from a particular position to another
    #first checks if the destination is true
    #returns true if the lecture was moved
    #lecture does not change position if destination isfull
    def mov_lect_if_free(self,f_day,f_room,f_tslot,t_day,t_room,t_tslot):
        pass
    def remlect(self,day,room,tslot):
        key  = self.hash(day,room,tslot)
        index = self._hashtable[key]
        self._table[index][POS_SLOT].remlect()

    def lect_info(self):
        pass

    def free_slots(self):
        pass
    def free_slots(self):
        pass
    def best_fit(self):
        pass
    def first_fit(self):
        #returns the index of the first position in the timetable that is can contain the given
        #lecture based on all the given constraints
        pass
    def isfree(self,ttableslot):
        #returns true if there is no course assigend to that slot
        #returns false otherwise
        pass
    def assignlecture(self,ttableslot,lecture):
        #assigns the lecture to the timetable slot
        pass
    def freeslots(self):
        #returns a list with all the indices of free positions available in the timetable
        freeslots = []
        for position in self._table:
            if position[POS_SLOT].isfree:
                key = self.hash(position[POS_DAY],position[POS_ROOM],position[POS_SLOT])
                index = self._hashtable[key]
                freeslots.append(index)
        return freeslots  