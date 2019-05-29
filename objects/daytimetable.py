#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 15:27

#  modifications  


from .classroom import Classroom
from .timetableslot import TimetableSlot
from .lecturer import Lecturer
from .lecture import Lecture
from .timeslot import TimeSlot
import copy


# ========================== TODO =========================================
# 0. Allow segmentation in time in timetable
# 1. Validation for all function params                                  #
# 2. Exceptions and exception handlers                                     #
# 3. Doc strings                                                           #
# 4. Unit tests                                                            #
# 5. Adjust logic for lecturer components. courses etc have a list of      #
# of lecturers not a single lecturer                                       #  
# 6. Add partitioning to timetable if the added lecture is less than slot
# duration           
# 7. Type hinting
# 8. Add splitting of time_slots after addition of lecture with smaller duration
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
        
        time_slots: list
                Holds time_slots representing all the possible time intervals
                allowed for scheduling for that particular day
                No overlaps and duplicates allowed, Sorted in increasing order of start times

        table: dictionary
                Structure for holding the day's timetable
                All rooms available for the day serve as keys for the table
                Each room has a list of time table slots as values
        
        Methods
        -------
        add_lecture(self,lecture,time_table_slot,free=True)
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

    def __init__(self, classrooms, time_slots=[], day=None):
        """
        Parameters
        ----------
        classrooms : list
            All classrooms available for the day 
        time_slots : list
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

        time_slots = self.validate_time_slots(time_slots)

        for room in self.rooms:
            self.set_time_slots(room, time_slots)

    def __str__(self):
        # print the entire timetable for that particular day
        my_str = ''
        for room in self.rooms:
            for time_table_slot in self.table[room]:
                my_str += str(room) + '    ' + str(time_table_slot.time_slot) + '\n'

                if time_table_slot.is_occupied:
                    my_str += str(time_table_slot.lecture.curriculum_item.course) + ' \n'
        return my_str

    def set_time_slots(self, room, time_slots):
        self.validate_time_slots(time_slots)
        slots = []
        for time_slot in time_slots:
            time_table_slot = TimetableSlot(self.day, room, time_slot)
            slots.append(time_table_slot)
        self.table[room] = slots

    @staticmethod
    def validate_time_slots(time_slots):
        # if time_slots are not specified then they can be added specifically for each room
        # through the set_time_slots(self,room,time_slots) function
        if time_slots:

            # remove duplicates from timeslot
            # problems may arise if time_slots is mutated
            time_slots = list(set(time_slots))

            # sort the time_slots according to starting time
            time_slots.sort(key=lambda timeslot: timeslot.start)

            # ensures there are no overlapping times in the time_slots
            #############################################################################
            for i in range(len(time_slots) - 2):
                if time_slots[i].end > time_slots[i + 1].start:  # proove correctness
                    # raise overlap exception
                    pass
            #############################################################################
        return time_slots

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value
        for room in self.rooms:
            for slot in self.table[room]:
                slot.day = value

    def has_left_neighbour(self, time_table_slot):
        try:
            index = (self.table[time_table_slot.room]).index(time_table_slot)
        except Exception:
            return False
        else:
            return 0 < index < len(self.table[time_table_slot.room])

    def has_right_neighbour(self, time_table_slot):
        try:
            index = self.table[time_table_slot.room].index(time_table_slot)
        except Exception:
            return False
        else:
            return 0 <= index < len(self.table[time_table_slot.room]) - 1

    def left_neighbour(self, time_table_slot):
        if self.has_left_neighbour(time_table_slot):
            neighbour_index = self.table[time_table_slot.room].index(time_table_slot) - 1
            return self.table[time_table_slot.room][neighbour_index]

    def right_neighbour(self, time_table_slot):
        if self.has_right_neighbour(time_table_slot):
            neighbour_index = self.table[time_table_slot.room].index(time_table_slot) + 1
            return self.table[time_table_slot.room][neighbour_index]

    def left_neighbours(self, time_table_slot):
        index = self.table[time_table_slot.room].index(time_table_slot)

        neighbours = []

        if index < len(self.table[time_table_slot.room]):
            for i in range(index - 1, -1, -1):
                # if self.table[time_table_slot.room][i].timeslot.end \
                #   == self.table[time_table_slot.room][i+1].timeslot.start:
                neighbours.append(self.table[time_table_slot.room][i])
            neighbours.sort(key=lambda ttslot: ttslot.time_slot.start)
        return neighbours

    def right_neighbours(self, time_table_slot):
        index = self.table[time_table_slot.room].index(time_table_slot)

        neighbours = []

        if index > 0:
            for i in range(index + 1, len(self.table[time_table_slot.room])):
                # if self.table[time_table_slot.room][i].timeslot.start \
                #   == self.table[time_table_slot.room][i-1].timeslot.end:
                neighbours.append(self.table[time_table_slot.room][i])
            neighbours.sort(key=lambda ttslot: ttslot.time_slot.start)
        return neighbours

    def insert_time_table_slot(self, room, time_table_slot):
        if time_table_slot not in self.table[room]:
            self.table[room].append(time_table_slot)
            self.table[room].sort(key=lambda ttslot: ttslot.time_slot.start)

    def assign_lecture(self, lecture, time_table_slot):
        # TODO : change for function to have single exit point
        time_slot_index = self.table[time_table_slot.room].index(time_table_slot)

        time_table_slot = self.timetableslot(time_table_slot.room, time_table_slot.time_slot)

        if time_table_slot.room.can_accommodate(lecture.curriculum_item.section.size):
            time_table_slot.lecture = lecture

            if lecture.duration == time_table_slot.time_slot.duration:
                self.table[time_table_slot.room][time_slot_index] = time_table_slot
                return True

            elif time_table_slot.time_slot.duration > lecture.duration:
                index = self.table[time_table_slot.room].index(time_table_slot)
                time_diff = time_table_slot.time_slot.duration - lecture.duration

                if self.has_right_neighbour(time_table_slot) and \
                        self.right_neighbour(time_table_slot).is_free:
                    time_table_slot.time_slot.start
                    self.left_neighbour(time_table_slot).time_slot.end
                    if time_table_slot.time_slot.end == self.right_neighbour(time_table_slot).time_slot.start:
                        time_table_slot.time_slot.shift_end(-time_diff)
                        self.table[time_table_slot.room][index + 1].time_slot.shift_start(-time_diff)
                        self.table[time_table_slot.room][index] = time_table_slot

                        return True

                if self.has_left_neighbour(time_table_slot) and \
                        self.left_neighbour(time_table_slot).is_free:
                    if time_table_slot.time_slot.start == self.left_neighbour(time_table_slot).time_slot.end:
                        time_table_slot.time_slot.shift_start(time_diff)
                        self.table[time_table_slot.room][index - 1].time_slot.shift_end(time_diff)
                        self.table[time_table_slot.room][index] = time_table_slot
                        return True

            new_slot = copy.deepcopy(time_table_slot)
            new_slot.remove_lecture()
            new_slot.time_slot.shift_start(time_diff)
            time_table_slot.time_slot.shift_end(-time_diff)
            print(new_slot.time_slot.start)
            print(new_slot.time_slot.end)
            print(time_table_slot.time_slot.start)
            print(time_table_slot.time_slot.end)
            self.table[time_table_slot.room][index] = time_table_slot
            self.insert_time_table_slot(new_slot.room, new_slot)
            return True

    def add_lecture(self, lecture, time_table_slot, free=True):
        # timetable slot could be the actual time_table_slot or just a wrapper that contains the room
        # and the time_slot

        """Assigns lecture to time_tables_lot.

        Parameters
        ----------
        lecture :  Lecture
            The lecture to be added to the timetable

        time_table_slot : TimetableSlot
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
        # validate time_table_slot
        # update docstring
        # lecture_added = False

        try:
            time_table_slot = self.timetableslot(time_table_slot.room, time_table_slot.time_slot)

            lecture_added = False

            if free:  # assign slot only if the lecture is free
                if time_table_slot.is_free:
                    lecture_added = self.assign_lecture(lecture, time_table_slot)

            elif not free:  # assign lecture wether slot is free or not
                lecture_added = self.assign_lecture(lecture, time_table_slot)
        except Exception as e:
            print(e)
            return False
        else:
            return lecture_added

    def move_lecture(self, source_slot, dest_slot, free=True):
        """Moves the lecture in sources_lot to dest_slot.

        Parameters
        ----------
        source_slot :  TimetableSlot
            timetableslot  to move the lecture from

        dest_slot : TimetableSlot
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
        # validate the source_slot and dest_slot

        # move the lecture from the source_slot to the destlot

        # *****Only move if the source slot is occupied

        timetableslot = self.timetableslot(source_slot.room, source_slot.time_slot)

        if timetableslot.is_occupied:
            if self.add_lecture(timetableslot.lecture, dest_slot, free):  # if lecture is added but
                if self.remove_lecture(timetableslot):  # fails to be removed what happens?
                    return True
        return False

    def swap_lectures(self, slot1, slot2):
        """Swaps the lectures in slot1 and slot2

        Parameters
        ----------
        slot1 :  TimetableSlot
            First timetableslot with lecture to be swapped

        slot2 : TimetableSlot
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

        slot1 = self.timetableslot(slot1.room, slot1.time_slot)
        slot2 = self.timetableslot(slot2.room, slot2.time_slot)

        if slot1 == slot2:
            return True
        # TODO
        # add check for lecturers free and for section free
        if (slot1.is_occupied and slot2.is_occupied):
            if slot1.time_slot.duration == slot2.time_slot.duration:  # proove
                if slot1.room.can_accommodate(slot2.lecture.curriculum_item.section.size) \
                        and slot2.room.can_accommodate(slot1.lecture.curriculum_item.section.size):
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
        timetableslot:  TimetableSlot
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
        timetableslot = self.timetableslot(timetableslot.room, timetableslot.time_slot)

        if timetableslot.is_free:
            removed = True
        if timetableslot.is_occupied:
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
                if slot.is_occupied:
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
                if slot.is_free:
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

        timeslot : TimeSlot
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
                if timetableslot.is_occupied and \
                        set(lecturers) == set(timetableslot.lecture.curriculum_item.lecturers):
                    if self.time_slots_overlap(timeslot, timetableslot.time_slot):
                        return False
        return True

    def lecturer_is_free(self, lecturer, timeslot):
        """Checks if lecturer is free at time specified by timeslot

        Parameters
        ----------
        lecturer :  Lecturer
            lecturer to check if is free

        timeslot : TimeSlot
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
                if timetableslot.is_occupied and \
                        lecturer in timetableslot.lecture.curriculum_item.lecturers:
                    if self.time_slots_overlap(timeslot, timetableslot.time_slot):
                        return False
        return True

    def section_is_free(self, section, timeslot):
        for room in self.rooms:
            for timetableslot in self.table[room]:
                sec = timetableslot.lecture.curriculum_item.section
                if timetableslot.is_occupied and sec == section:
                    if self.time_slots_overlap(timeslot, timetableslot.time_slot):
                        return False
        return True

    @staticmethod
    def time_slots_overlap(timeslot1, timeslot2):
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

        timeslot : TimeSlot
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
            if slot.time_slot == timeslot and slot.is_free:
                return True

        return False

    def timetableslot(self, room, timeslot):
        """Returns timetableslot with classroom == room and timeslot == timeslot

        Parameters
        ----------
        room :  Classroom
            room to return slot from

        timeslot : TimeSlot
            timeslot of timetableslot
        
        Returns
        -------
        Timetaleslot
            TimetableSlot with classroom as room and timeslot as timetslot

        Raises
        ------
        """

        # TODO
        # validate the room and the timeslot

        for slot in self.table[room]:
            if slot.time_slot == timeslot:
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
        Time_Table_Slot
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

        if best is not None:
            min_cur = best.room.capacity + allowance - class_size

        if free:
            slots = self.free_slots()
        else:
            slots = self.occupied_slots()

        for slot in slots:
            if 0 <= (slot.room.capacity + allowance - class_size) < min_cur:  # check
                if lecture.duration <= slot.time_slot.duration:  # check after construction
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
        Time_Table_Slot
            first timetable slot big enough to hold lecture

        Raises
        ------
        :param lecture:
        :param free:
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
                if lecture.duration <= slot.time_slot.duration:  # check after construction
                    return slot

    # dummy test stub
    # remove after developing unit tests
    def test_print(self):
        for room in self.rooms:
            for slot in self.table[room]:
                if slot.is_occupied:
                    print(str(slot.day) + '\n' + str(slot.time_slot) + '\n' + str(slot.room))
                    print(str(slot.lecture))

    # check for or not check for clashes?

    def lecturer_clashes(self):
        # returns a list of tuples
        all_clashes = []
        # list of tuples
        # each tuple contains time table slots  where the lecturer is scheduled
        # at overlapping times
        for room in self.rooms:
            for slot in self.table[room]:
                l_clashes = ()
                for other_room in self.rooms:
                    if other_room != room:
                        for other_slot in self.table[other_room]:
                            if slot.lecture.curriculum_item.lecturers == \
                                    other_slot.lecture.curriculum_item.lecturers:
                                if self.time_slots_overlap(slot, other_slot):
                                    l_clashes = l_clashes + (slot, other_slot)
                if l_clashes:
                    all_clashes.append(l_clashes)

        return list(set(all_clashes))

    def section_clashes(self):
        # returns a list of tuples
        all_clashes = []
        # list of tuples
        # each tuple contains time table slots  where the lecturer is scheduled
        # at overlapping times
        for room in self.rooms:
            for slot in self.table[room]:
                l_clashes = ()
                for other_room in self.rooms:
                    if other_room != room:
                        for other_slot in self.table[other_room]:
                            if slot.lecture.curriculum_item.section == \
                                    other_slot.lecture.curriculum_item.section:
                                if self.time_slots_overlap(slot, other_slot):
                                    l_clashes = l_clashes + (slot, other_slot)
                if l_clashes:
                    all_clashes.append(l_clashes)

        # filter duplicates
        return list(set(all_clashes))
