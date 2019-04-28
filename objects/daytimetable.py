#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 15:27

#  modifications  


from data import CurriculumItem
from classroom import Classroom
from timetableslot import Timetableslot
from lecturer import Lecturer
from course import Course
from section import Section
from lecture import Lecture
from timeslot import Timeslot
import copy


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


class DayTimetable:
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

    rooms = []  # all classrooms that are available for that day
    table = {}  # maps each classroom to the different times it is available for lectures

    def __init__(self, classrooms, timeslots=[], day=None):
        """
        Parameters
        ----------
        classrooms : list
            All classrooms available for the day 
        timeslots : list
            If specified represents all the possible time intervals allowed for scheduling on that day
        """

        # TODO
        # validate to check instances of particular class

        self._day = day

        # remove duplicates from the list of classrooms
        # problems may arise if classrooms is mutated
        classrooms = list(set(classrooms))

        # sort classrooms according to capacity
        classrooms.sort(key=lambda classroom: classroom.capacity, reverse=True)
        self.rooms = classrooms

        timeslots = self.validate_timeslots(timeslots)

        for room in self.rooms:
            self.set_timeslots(room, timeslots)

    def __str__(self):
        # print the entire timetable for that particular day
        mystr = ''
        for room in self.rooms:
            for timetableslot in self.table[room]:
                mystr += str(room) + '    ' + str(timetableslot.timeslot) + '\n'

                if (timetableslot.isoccupied):
                    mystr += str(timetableslot.lecture.curriculum_item.course) + ' \n'
        return mystr

    def set_timeslots(self, room, timeslots):
        self.validate_timeslots(timeslots)
        slots = []
        for timeslot in timeslots:
            timetableslot = Timetableslot(self.day, room, timeslot)
            slots.append(timetableslot)
        self.table[room] = slots

    @staticmethod
    def validate_timeslots(timeslots):
        # if timeslots are not specified then they can be added specifically for each room
        # through the set_timeslots(self,room,timeslots) function
        if timeslots:

            # remove duplicates from timeslot
            # problems may arise if timeslots is mutated
            timeslots = list(set(timeslots))

            # sort the timeslots according to starting time
            timeslots.sort(key=lambda timeslot: timeslot.start)

            # ensures there are no overlapping times in the timeslots
            #############################################################################
            for i in range(len(timeslots) - 2):
                if timeslots[i].end > timeslots[i + 1].start:  # proove correctness
                    # raise overlap exception
                    pass
            #############################################################################
        return timeslots

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value
        for room in self.rooms:
            for slot in self.table[room]:
                slot.day = value

    def has_left_neighbour(self, timetableslot):
        try:
            index = (self.table[timetableslot.room]).index(timetableslot)
        except Exception:
            return False
        else:
            return 0 < index < len(self.table[timetableslot.room])

    def has_right_neighbour(self, timetableslot):
        try:
            index = self.table[timetableslot.room].index(timetableslot)
        except Exception:
            return False
        else:
            return 0 <= index < len(self.table[timetableslot.room]) - 1

    def left_neighbour(self, timetableslot):
        if self.has_left_neighbour(timetableslot):
            neighbour_index = self.table[timetableslot.room].index(timetableslot) - 1
            return self.table[timetableslot.room][neighbour_index]

    def right_neighbour(self, timetableslot):
        if self.has_right_neighbour(timetableslot):
            neighbour_index = self.table[timetableslot.room].index(timetableslot) + 1
            return self.table[timetableslot.room][neighbour_index]

    def left_neighbours(self, timetableslot):
        index = self.table[timetableslot.room].index(timetableslot)

        neighbours = []

        if index < len(self.table[timetableslot.room]):
            for i in range(index - 1, -1, -1):
                # if self.table[timetableslot.room][i].timeslot.end \
                #   == self.table[timetableslot.room][i+1].timeslot.start:
                neighbours.append(self.table[timetableslot.room][i])
            neighbours.sort(key=lambda ttslot: ttslot.timeslot.start)
        return neighbours

    def right_neighbours(self, timetableslot):
        index = self.table[timetableslot.room].index(timetableslot)

        neighbours = []

        if index > 0:
            for i in range(index + 1, len(self.table[timetableslot.room])):
                # if self.table[timetableslot.room][i].timeslot.start \
                #   == self.table[timetableslot.room][i-1].timeslot.end:
                neighbours.append(self.table[timetableslot.room][i])
            neighbours.sort(key=lambda ttslot: ttslot.timeslot.start)
        return neighbours

    def insert_timetableslot(self, room, timetableslot):
        if not timetableslot in self.table[room]:
            self.table[room].append(timetableslot)
            self.table[room].sort(key=lambda ttslot: ttslot.timeslot.start)

    def assign_lecture(self, lecture, timetableslot):
        # TODO : change for function to have single exit point
        timeslot_index = self.table[timetableslot.room].index(timetableslot)

        timetableslot = self.timetableslot(timetableslot.room, timetableslot.timeslot)

        if timetableslot.room.can_accomodate(lecture.curriculum_item.section.size):
            timetableslot.lecture = lecture

            if lecture.duration == timetableslot.timeslot.duration:
                self.table[timetableslot.room][timeslot_index] = timetableslot
                return True

            elif timetableslot.timeslot.duration > lecture.duration:
                index = self.table[timetableslot.room].index(timetableslot)
                time_diff = timetableslot.timeslot.duration - lecture.duration

                if self.has_right_neighbour(timetableslot) and \
                        self.right_neighbour(timetableslot).isfree:
                    timetableslot.timeslot.start
                    self.left_neighbour(timetableslot).timeslot.end
                    if timetableslot.timeslot.end == self.right_neighbour(timetableslot).timeslot.start:
                        timetableslot.timeslot.shift_end(-time_diff)
                        self.table[timetableslot.room][index + 1].timeslot.shift_start(-time_diff)
                        self.table[timetableslot.room][index] = timetableslot

                        return True

                if self.has_left_neighbour(timetableslot) and \
                        self.left_neighbour(timetableslot).isfree:
                    if timetableslot.timeslot.start == self.left_neighbour(timetableslot).timeslot.end:
                        timetableslot.timeslot.shift_start(time_diff)
                        self.table[timetableslot.room][index - 1].timeslot.shift_end(time_diff)
                        self.table[timetableslot.room][index] = timetableslot
                        return True

            new_slot = copy.deepcopy(timetableslot)
            new_slot.remove_lecture()
            new_slot.timeslot.shift_start(time_diff)
            timetableslot.timeslot.shift_end(-time_diff)
            print(new_slot.timeslot.start)
            print(new_slot.timeslot.end)
            print(timetableslot.timeslot.start)
            print(timetableslot.timeslot.end)
            self.table[timetableslot.room][index] = timetableslot
            self.insert_timetableslot(new_slot.room, new_slot)
            return True

    def add_lecture(self, lecture, timetableslot, free=True):
        # timetable slot could be the actual timetableslot or just a wrapper that contains the room
        # and the timeslot

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
        # TODO
        # validate lecture
        # validate timetableslot
        # update docstring
        # lecture_added = False

        try:
            timetableslot = self.timetableslot(timetableslot.room, timetableslot.timeslot)

            lecture_added = False

            if free:  # assign slot only if the lecture is free
                if timetableslot.isfree:
                    lecture_added = self.assign_lecture(lecture, timetableslot)

            elif not free:  # assign lecture wether slot is free or not
                lecture_added = self.assign_lecture(lecture, timetableslot)
        except Exception as e:
            print(e)
            return False
        else:
            return lecture_added

    def move_lecture(self, sourceslot, destslot, free=True):
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
        # TODO
        # validate the sourceslot and destslot

        # move the lecture from the sourceslot to the destlot

        # *****Only move if the source slot is occupied

        timetableslot = self.timetableslot(sourceslot.room, sourceslot.timeslot)

        if timetableslot.isoccupied:
            if self.add_lecture(timetableslot.lecture, destslot, free):  # if lecture is added but
                if self.remove_lecture(timetableslot):  # fails to be removed what happens?
                    return True
        return False

    def swap_lectures(self, slot1, slot2):
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
        # TODO
        # validate slot1
        # validate slot2
        # edit docstring

        # slot1 and slot2 may just be wrappers containing timeslot and rooms
        # get actual timetable slot from those positions

        slot1 = self.timetableslot(slot1.room, slot1.timeslot)
        slot2 = self.timetableslot(slot2.room, slot2.timeslot)

        if slot1 == slot2:
            return True

        if (slot1.isoccupied and slot2.isoccupied):
            if slot1.timeslot.duration == slot2.timeslot.duration:  # proove
                if slot1.room.can_accomodate(slot2.lecture.curriculum_item.section.size) \
                        and slot2.room.can_accomodate(slot1.lecture.curriculum_item.section.size):
                    index_1 = self.table[slot1.room].index(slot1)
                    index_2 = self.table[slot2.room].index(slot2)
                    self.table[slot1.room][index_1], self.table[slot2.room][index_2] = \
                        self.table[slot2.room][index_2], self.table[slot1.room][index_1]  # verify
                    return True
        return False

    def remove_lecture(self, timetableslot):
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
        # TODO
        # validate timetableslot
        # false should only returned for in valid timetable slot

        removed = False

        # review effects of changes
        timetableslot = self.timetableslot(timetableslot.room, timetableslot.timeslot)

        if timetableslot.isfree:
            removed = True
        if timetableslot.isoccupied:
            index = self.table[timetableslot.room].index(timetableslot)
            self.table[timetableslot.room][index].remove_lecture()
            removed = True

        return removed

    # Needs review and testing
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
                removed = self.remove_lecture(slot)  # check if lecture was removed

                if not removed:  # if any lecture at all failed to be removed
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

    def lecturers_are_free(self, lecturers, timeslot):
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
        # TODO
        # validate the lecturer and the timeslot
        for room in self.rooms:
            for timetableslot in self.table[room]:
                if timetableslot.isoccupied and \
                        set(lecturers) == set(timetableslot.lecture.curriculum_item.lecturers):
                    if self.timeslots_overlap(timeslot, timetableslot.timeslot):
                        return False
        return True

    def lecturer_is_free(self, lecturer, timeslot):
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
        # TODO
        # validate the lecturer and the timeslot
        for room in self.rooms:
            for timetableslot in self.table[room]:
                if timetableslot.isoccupied and \
                        lecturer in timetableslot.lecture.curriculum_item.lecturers:
                    if self.timeslots_overlap(timeslot, timetableslot.timeslot):
                        return False
        return True

    def section_is_free(self, section, timeslot):
        for room in self.rooms:
            for timetableslot in self.table[room]:
                sec = timetableslot.lecture.curriculum_item.section
                if timetableslot.isoccupied and sec == section:
                    if self.timeslots_overlap(timeslot, timetableslot.timeslot):
                        return False
        return True

    @staticmethod
    def timeslots_overlap(timeslot1, timeslot2):
        if (timeslot1.start <= timeslot2.end and timeslot1.end >= timeslot2.start) or \
                (timeslot2.start <= timeslot1.end and timeslot2.end >= timeslot1.start):
            return True
        return False

    def room_is_free(self, room, timeslot):
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
        # TODO
        # validate room and timeslot

        for slot in self.table[room]:
            if slot.timeslot == timeslot and slot.isfree:
                return True

        return False

    def timetableslot(self, room, timeslot):
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

        # TODO
        # validate the room and the timeslot

        for slot in self.table[room]:
            if slot.timeslot == timeslot:
                return slot

    def best_fit(self, lecture, allowance=0, free=True):
        # true indicates if the best fit is being found only among free slots
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

        # TODO:
        # Validate lecture and allowance
        # take care of if none is found

        # changed logic to use free and occupied slots
        # verify slots
        class_size = lecture.curriculum_item.section.size

        best = self.first_fit(lecture, free)

        if best != None:
            min_cur = best.room.capacity + allowance - class_size

        if free:
            slots = self.free_slots()
        else:
            slots = self.occupied_slots()

        for slot in slots:
            if 0 <= (slot.room.capacity + allowance - class_size) < min_cur:  # check
                if lecture.duration <= slot.timeslot.duration:  # check after construction
                    best = slot
                    min_cur = slot.room.capacity - class_size

        # *take care of if none is found
        return best

    def first_fit(self, lecture, free=True):
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

        # TODO
        # Validate lecture
        # Add allowance
        # take care of if none is found
        class_size = lecture.curriculum_item.section.size

        # change logic to use free slots function and occupied slots

        if free:
            slots = self.free_slots()
        else:
            slots = self.occupied_slots()

        for slot in slots:
            if slot.room.capacity >= class_size:
                if lecture.duration <= slot.timeslot.duration:  # check after construction
                    return slot

    # dummy test stub
    # remove after developing unit tests
    def testprint(self):
        for room in self.rooms:
            for slot in self.table[room]:
                if slot.isoccupied:
                    print(str(slot.day) + '\n' + str(slot.timeslot) + '\n' + str(slot.room))
                    print(str(slot.lecture))

# check for or not check for clashes?
