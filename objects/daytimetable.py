#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 15:27


from data import CurriculumItem
from classroom import Classroom
from timetableslot import Timetableslot
from lecturer import Lecturer
from course import Course
from section import Section
from lecture import Lecture

from timeslot import Timeslot

##################################TODO######################################
# 0. Allow segmentation in time in timetable
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

class Daytimetable:
    """
        Represents a timetable for a particular day
        ...

        Attributes
        ----------

        rooms : list
                Holds all the rooms available for the particular day
                rooms sorted in reverse order of their size
                duplicates not allowed
        
        timeslots: list 
                Holds timeslots representing all the possible time intervals
                allowed for scheduling for that particular day
                No overlaps and duplicates allowed, Sorted in increasing order of start times

        table: dictionary
                Structure for holding the day's timetable
                All rooms available for the day serve as keys for the table
                Each room has a list of time table slots as values
        
        Methods
        -------
        add_lecture(self,lecture,timetableslot,free=True)
                Assigns lecture to timetableslot

        move_lecture(self,sourceslot,destslot,free=True)
                Moves lecture in sourceslot to destslot

        swap_lectures(self,slot1,slot2)
                Moves the lecture in slot2 to slot1 and vice versa

        remove_lecture(self,timetableslot)
                Removes the lecture assigned to timetableslot

        occupied_slots(self)
                Returns a list of all occupied timetable slots
        
        free_slots(self)
                Returns a list of all free timetable slots

        lecturer_is_free(self,lecturer,timeslot)
                Checks if lecturer is free at time specified by timeslot

        room_is_free(self,room,timeslot)
                Checks if room is free at time specified by timeslot

        timetableslot(self,room,timeslot)
                Returns tiemstableslot at room and timeslot

        best_fit(self,lecture,allowance = 0)
                Returns timetableslot with smallest room size large enough to fit lecture

        first_fit(self,lecture)
                Returns the first timetableslot large enough to fit lecture

    """

#knows nothing about collisions
#only checks to make sure that a lecture can fit into a particular slot
#based on the room size and the section size 
#and on if the duration of the lecture can fit into the slot

    rooms = [] 
    timeslots =[] 
    table = {}

    def __init__(self,classrooms=[],timeslots=[],day = None):
        """
        Parameters
        ----------
        classrooms : list
            All classrooms available for the day 
        timeslots : str
            Represents all the possible time intervals allowed for scheduling on that day
        """
        
        #TODO
        #validate to check instances of particular class
        
        self._day = day

        #ensures each classroom only appears once on the list
        classrooms = list(set(classrooms))
    
        classrooms.sort(key = lambda classroom: classroom.capacity,reverse =True)
        self.rooms = classrooms

        #ensures each timeslot only occurs once in the least
        timeslots = list(set(timeslots))

        #sort the timeslots according to starting time
        timeslots.sort(key = lambda timeslot: timeslot.start)

        #ensures there are no overlapping times in the timeslots
        for i in range(len(timeslots)-1):
            if timeslots[i].end > timeslots[i+1].start: #proove correctness
                #raise exception
                pass
        self.timeslots = timeslots

        for room in self.rooms:
            slots = []
            for timeslot in self.timeslots:
                timetableslot = Timetableslot(self.day,room,timeslot) 
                slots.append(timetableslot)
            self.table[room] = slots


    def __str__(self):
        #print the entire timetable for that particular day
        pass

    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self,value):
        self._day = value

    def add_lecture(self,lecture,timetableslot,free=True):
        #timetable slot could be the actual timetableslot or just a wrapper that contains the room
        #and the timeslot 

        """Assigns lecture to timetableslot.

        Parameters
        ----------
        lecture :  Lecture
            The lecture to be added to the timetable

        timetableslot : Timetableslot
            holds location in timetable where lecture should be added
        
        free : bool, optional
            If true timetableslot if first checked if it is unoccupied
            Defaults to True

        Returns
        -------
        bool
            True if lecture was successfully assigned to timetableslot false otherwise

        Raises
        ------
     
        """
        #TODO
        #validate lecture
        #validate timetableslot
        #update docstring
                
        #Edit blocks till end#################################################
        if timetableslot == None:#remove and catch exceptions rather 
            return False

        try:
            self.rooms.index(timetableslot.room)
            timeslot_index = self.timeslots.index(timetableslot.timeslot)
        except ValueError:
            #handle exception
            return
        except AttributeError:
            #handle exception
            return
        #end##################################################################

    
        timetableslot = self.timetableslot(timetableslot.room,timetableslot.timeslot)

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
    
        return False
        
    def move_lecture(self,sourceslot,destslot,free=True):#convert to decorator
        """MOves the lecture in soourceslot to destslot.

        Parameters
        ----------
        sourceslot :  Timetableslot
            timetableslot  to move the lecture from

        destslot : Timetableslot
            timetableslot to move lecture to
        
        free : bool, optional
            If true destslot if first checked if it is unoccupied
            Defaults to True

        Returns
        -------
        bool
            True if lecture was successfully moved to destslot false otherwise

        Raises
        ------
     
        """
        #TODO
        #validate the sourceslot and destslot

        #move the lecture from the sourceslot to the destlot

        #*****Only move if the source slot is occupied

        timetableslot = self.timetableslot(sourceslot.room,sourceslot.timeslot)

        #**********check when debuggin *****************************#
        if timetableslot.isoccupied:
            if  self.add_lecture(sourceslot.lecture,destslot,free):#if lecture is added but
                if self.remove_lecture(timetableslot): #fails to be removed what happens?
                    return True
        return False

    def swap_lectures(self,slot1,slot2):
        """Swaps the lectures in slot1 and slot2

        Parameters
        ----------
        slot1 :  Timetableslot
            First timetableslot with lecture to be swapped

        slot2 : Timetableslot
            Second timetableslot with lecture to be swapped
        
        Returns
        -------
        bool
            True if lectures in slot1 and slot2 were successfully swaped, false otherwise

        Raises
        ------
     
        """
        #TODO
        #validate slot1
        #validate slot2
        #edit docstring

        #slot1 and slot2 may just be wrappers containing timeslot and rooms
        #get actual timetable slot from those positions

        slot1 = self.timetableslot(slot1.room,slot1.timeslot)
        slot2 = self.timetableslot(slot2.room,slot2.timeslot)

        if slot1 == slot2:
            return True

        if (slot1.isoccupied and slot2.isoccupied):
            if slot1.timeslot.duration == slot2.timeslot.duration: #proove
                if slot1.room.can_accomodate(slot2.lecture.curriculum_item.section.size)\
                    and slot2.room.can_accomodate(slot1.lecture.curriculum_item.section.size): 
                    index_1 = self.table[slot1.room].index(slot1)
                    index_2 = self.table[slot2.room].index(slot2)
                    self.table[slot1.room][index_1],self.table[slot2.room][index_2] =\
                         self.table[slot2.room][index_2],self.table[slot1.room][index_1]#verify
                    return True
        return False

    def remove_lecture(self,timetableslot):
        """Removes the lecture at timetable slot

        Parameters
        ----------
        timetableslot:  Timetableslot
            timetableslot with lecture to be removed
        
        Returns
        -------
        bool
            True if lecture is removed

        Raises
        ------
     
        """
        #TODO
        #validate timetableslot
        #false should only returned for in valid timetable slot

        removed = False


        #review effects of changes 
        timetableslot = self.timetableslot(timetableslot.room,timetableslot.timeslot)

        if timetableslot.isfree:
            removed = True
        if timetableslot.isoccupied:
            index = self.table[timetableslot.room].index(timetableslot)
            self.table[timetableslot.room][index].remove_lecture()
            removed = True
        
        return removed

    #Needs review and testing
    def remove_all(self):
        """Empties the daytimetable 

        Returns
        -------
        bool 
            True if all lectures are removed
        
        Raises
        ------
        """


        for room in self.rooms:
            for slot in self.table[room]:
                removed = self.remove_lecture(slot) #check if lecture was removed
                
                if not removed: #if any lecture at all failed to be removed
                    return False


    def occupied_slots(self):
        """Returns all the occupied timetable slots in the table
        
        Returns
        -------
        list
            List of all occupied timetableslots in table

        Raises
        ------
     
        """
        occupied = []
        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isoccupied:
                    occupied.append(slot)
        return occupied

    def free_slots(self):
        """Returns all the free slots in table
        
        Returns
        -------
        list
            List of all free timetableslots in table
        Raises
        ------
     
        """
        free = []

        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isfree:
                    free.append(slot)
        return free

    def all_slots(self):
        """Returns all the slots in table
        
        Returns
        -------
        list
            List of all timetableslots in table
        Raises
        ------
     
        """
        slots = []

        for room in self.rooms:
            for slot in self.table[room]:
                slots.append(slot)
        return slots

    def lecturer_is_free(self,lecturer,timeslot):
        """Checks if lecturer is free at time specified by timeslot

        Parameters
        ----------
        lecturer :  Lecturer
            lecturer to check if is free

        timeslot : Timeslot
            Time to check if lecturer is free
        
        Returns
        -------
        bool
            True if lecturer is free at time specified by timeslot, false otherwise

        Raises
        ------
     
        """
        #TODO
        #validate the lecturer and the timeslot
        #change logic. slot.lecture.curriculum_item.lecturers is a list not a single value

        index = self.timeslots.index(timeslot)
        for room in self.rooms:
            slot = self.table[room][index]
            if slot.isoccupied:
                for lect in slot.lecture.curriculum_item.lecturers:
                    if lect == lecturer:
                        return False
        
        return True


    def room_is_free(self,room,timeslot):
        """Checks if room is free at time specified by timeslot

        Parameters
        ----------
        room :  Classroom
            classroom to check if is free

        timeslot : Timeslot
            time to check if room is free
        
        Returns
        -------
        bool
            True if room is free at time specified by timeslot, false otherwise

        Raises
        ------
        """
        #TODO
        #validate room and timeslot 

        for slot in self.table[room]:
            if slot.timeslot == timeslot and slot.isfree:
                return True
        
        return False

    def timetableslot(self,room,timeslot):
        """Returns timetableslot with classroom == room and timeslot == timeslot

        Parameters
        ----------
        room :  Classroom
            room to return slot from

        timeslot : Timeslot
            timeslot of timetableslot
        
        Returns
        -------
        Timetaleslot
            Timetableslot with classroom as room and timeslot as timetslot

        Raises
        ------
        """

        #TODO
        #validate the room and the timeslot

        for slot in self.table[room]:
            if slot.timeslot == timeslot:
                return slot
    
    def best_fit(self,lecture,allowance = 0, free= True):
        #true indicates if the best fit is being found only among free slots
        """returns the free timetable slot with smallest room size big big enough to hold lecture

        Parameters
        ----------
        lecture :  Lecture
            lecture to find best fit timetable slot for

        allowance : int
            allowance applicable to room size
            Defaults to 0

        Returns
        -------
        Timetableslot
            timetable slot with smallest room size big big enough to hold lecture

        Raises
        ------
        """
        
        #TODO:
        #Validate lecture and allowance
        #take care of if none is found

        #changed logic to use free and occupied slots
        #verify slots 
        class_size = lecture.curriculum_item.section.size
        
        best = self.first_fit(lecture,free)

        if best != None:
            min_cur = best.room.capacity + allowance - class_size 

        if free:
            slots = self.free_slots()
        else:
            slots = self.occupied_slots()

        for slot in slots:
            if 0 <= (slot.room.capacity +allowance - class_size) < min_cur: #check
                if lecture.duration <= slot.timeslot.duration: #check after construction
                    best = slot
                    min_cur = slot.room.capacity - class_size

        #*take care of if none is found 
        return best

    def first_fit(self,lecture,free =True):
        """returns the first position in the timetable that is can hold lecture

        Parameters
        ----------
        lecture :  Lecture
            lecture to find first fit timetable slot for

        Returns
        -------
        Timetableslot
            first timetable slot big enough to hold lecture

        Raises
        ------
        """
        
        #TODO
        #Validate lecture
        #Add allowance
        #take care of if none is found
        class_size = lecture.curriculum_item.section.size

        #change logic to use free slots function and occupied slots

        if free:
            slots = self.free_slots()
        else:
            slots = self.occupied_slots()

        for slot in slots:
            if slot.room.capacity >= class_size :
                if lecture.duration <= slot.timeslot.duration: #check after construction
                    return slot

    #dummy test stub
    #remove after developing unit tests
    def testprint(self):
        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isoccupied:
                    print(str(slot.day)+ '\n'+ str(slot.timeslot)+ '\n'+ str(slot.room))
                    print(str(slot.lecture))


#check for or not check for clashes?