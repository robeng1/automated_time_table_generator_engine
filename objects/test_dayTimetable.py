from unittest import TestCase, main
# import factory
from .classroom import Classroom
from .timeslot import TimeSlot
from .daytimetable import DayTimetable
from .timetableslot import TimetableSlot
from .lecturer import Lecturer
from .course import Course
from .section import Section
from .data import CurriculumItem
from .lecture import Lecture


# TODO
# test for lecturer clashes
# test for section clashes
class TestDayTimetable(TestCase):
    def setUp(self) -> None:
        # self.classrooms = factory.generate_batch(ClassRoomFactory, size=20, strategy="build")
        # self.slots = slots
        # self.day_tt = DayTimetable(classrooms=self.classrooms, time_slots=self.slots)

        classrooms = [
            Classroom('LT ', 45, 'PBOO2'),
            Classroom('PB001', 100, 'Petroleum building'),
            Classroom('PBOO2 ', 45, 'Petroleum building'),
            # Classroom('Pb103', 67, 'Petroleum Building'),
            # Classroom('PB119', 150, 'Petroluem'),
            # Classroom(' A110', 300, 'Libary'),
            # Classroom('Computer lab', 67, 'vodafone'),
            # Classroom('LAB-12', 40, 'vodafone'),
            # Classroom('Room A', 100, 'tyeh'),
            # Classroom('Room B ', 45, 'PBOO2'),
            # Classroom('Main Library ', 60, 'Admiss'),
            Classroom('Room C', 67, 'N1')]

        timeslots = [
            TimeSlot('8:00', '9:00'),
            TimeSlot('9:00', '10:00'),
            TimeSlot('10:00', '11:00'),
            TimeSlot('11:00', '12:00'),
            TimeSlot('12:00', '13:00'),
            TimeSlot('13:00', '14:00'),
            TimeSlot('14:00', '15:00'),
            TimeSlot('15:00', '16:00'),
            TimeSlot('16:00', '17:00')
        ]

        self.timetable = DayTimetable(classrooms, timeslots, 'Mon')

    # def test_validate_time_slots(self):
    #    self.assertTrue(self.timetable.validate_time_slots())

    def test_day(self):
        self.timetable.day = 'Tues'
        self.assertEqual(self.timetable.day, 'Tues')

        slots = self.timetable.all_slots()

        for slot in slots:
            self.assertEqual(slot.day, 'Tues')

    def test_has_left_neighbour(self):
        # TODO
        # Test for timetableslots that are occupied with lectures
        # Test for edge cases

        # test for extreme left condition
        # left most slot should lack left neigbour
        self.assertFalse(self.timetable.has_left_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00'))))

        # test for slot with left neighbour
        self.assertTrue(self.timetable.has_left_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('9:00', '10:00'))))

        # test for extreme right
        # testing for index out of bounds
        self.assertTrue(self.timetable.has_left_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))))

        # test for slot not in timetable
        self.assertFalse(self.timetable.has_left_neighbour(
            TimetableSlot('Tues', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('9:00', '10:00'))))

        # test for slot not in timetable
        self.assertFalse(self.timetable.has_left_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 50, 'Petroleum building'), TimeSlot('16:00', '17:00'))))

    def test_has_right_neighbour(self):
        # TODO
        # Test for timetableslots that are occupied with lectures

        # test for edge cases

        # test for extreme left condition
        # test for left index out of bounds
        self.assertTrue(self.timetable.has_right_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00'))))

        # test for slot with right neighbour
        self.assertTrue(self.timetable.has_right_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('9:00', '10:00'))))

        # test for extreme right
        # should lack right neighbour
        self.assertFalse(self.timetable.has_right_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))))

        # test for slot not in timetable
        self.assertFalse(self.timetable.has_right_neighbour(
            TimetableSlot('Tues', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('9:00', '10:00'))))

        # test for slot not in timetable
        self.assertFalse(self.timetable.has_right_neighbour(
            TimetableSlot('Mon', Classroom('PB001', 50, 'Petroleum building'), TimeSlot('16:00', '17:00'))))

    def test_left_neighbour(self):
        # test for edge cases

        # test extreme right slot with left neighbour
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('15:00', '16:00'))
        self.assertEqual(self.timetable.left_neighbour(ttslot1), ttslot2)

        # test a normal midlle slot with a left neighour
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('10:00', '11:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('9:00', '10:00'))
        self.assertEqual(self.timetable.left_neighbour(ttslot1), ttslot2)

        # test an extreme left slot with no left neighbour
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00'))
        self.assertEqual(self.timetable.left_neighbour(ttslot1), None)

        # test for slot not in timetable
        ttslot1 = TimetableSlot('Tues', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))
        self.assertEqual(self.timetable.left_neighbour(ttslot1), None)

    def test_right_neighbour(self):
        # test for extreme cases

        # test for leftmost slot with right neighbour
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('9:00', '10:00'))
        self.assertEqual(self.timetable.right_neighbour(ttslot1), ttslot2)

        # test for normal middle slot with right neighbour
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('10:00', '11:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('11:00', '12:00'))
        self.assertEqual(self.timetable.right_neighbour(ttslot1), ttslot2)

        # test for rightmost with no right neigbour
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))
        self.assertEqual(self.timetable.right_neighbour(ttslot1), None)

        # test for slot not in timtetable
        ttslot1 = TimetableSlot('Wed', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))
        self.assertEqual(self.timetable.right_neighbour(ttslot1), None)

    def test_left_neighbours(self):
        # TODO
        # test for cases with lectures assigned to timetableslots

        # test for edge cases
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('10:00', '11:00'))
        neighbours = [TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00')),
                      TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('9:00', '10:00'))]
        self.assertEqual(self.timetable.left_neighbours(ttslot1), neighbours)

        # leftmmost slot with no left neighours
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00'))
        self.assertEqual(self.timetable.left_neighbours(ttslot1), [])

        # slot not in timetable has no neighbours
        ttslot1 = TimetableSlot('Fri', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00'))
        self.assertEqual(self.timetable.left_neighbours(ttslot1), [])

        # extreme right slot with left neighbours

    def test_right_neighbours(self):
        # TODO
        # test for cases with lectures assigned to timetableslots

        # test for edge cases
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('14:00', '15:00'))
        neighbours = [TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('15:00', '16:00')),
                      TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))]
        self.assertEqual(self.timetable.right_neighbours(ttslot1), neighbours)

        # leftmmost slot with no right neighours
        ttslot1 = TimetableSlot('Mon', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('16:00', '17:00'))
        self.assertEqual(self.timetable.right_neighbours(ttslot1), [])

        # slot not in timetable has no neighbours
        ttslot1 = TimetableSlot('Fri', Classroom('PB001', 100, 'Petroleum building'), TimeSlot('8:00', '9:00'))
        self.assertEqual(self.timetable.right_neighbours(ttslot1), [])

    def test_insert_time_table_slot(self):
<<<<<<< HEAD
        # TODO
        # do tests for slots  containing lectures
        # insert to the right
        room = Classroom('LT ', 45, 'PBOO2')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('17:00', '18:00'))
        self.timetable.insert_time_table_slot(room, ttslot)
        self.assertEqual(self.timetable.right_neighbour(
            TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('16:00', '17:00'))), ttslot)

        # test for inserting to the left
        room = Classroom('LT ', 45, 'PBOO2')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('7:00', '8:00'))
        self.timetable.insert_time_table_slot(room, ttslot)
        self.assertEqual(self.timetable.left_neighbour(
            TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))), ttslot)

        # test for inserting slot that already exists
        room = Classroom('LT ', 45, 'PBOO2')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        self.assertFalse(self.timetable.insert_time_table_slot(room, ttslot), ttslot)
=======
        #TODO
        #do tests for slots  containing lectures
        #insert to the right
        room =  Classroom('LT ', 45, 'PBOO2')
        ttslot =  TimetableSlot('Mon', room,TimeSlot('17:00', '18:00'))
        self.timetable.insert_time_table_slot(ttslot)
        self.assertEqual(self.timetable.right_neighbour(TimetableSlot('Mon',room,TimeSlot('16:00', '17:00'))),ttslot)
        
        #test for inserting to the left
        room =  Classroom('LT ', 45, 'PBOO2')
        ttslot =  TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'),TimeSlot('7:00', '8:00'))
        self.timetable.insert_time_table_slot(ttslot)
        self.assertEqual(self.timetable.left_neighbour(TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))),ttslot)

        #test for inserting slot that already exists 
        room =  Classroom('LT ', 45, 'PBOO2')
        ttslot =  TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        self.assertFalse(self.timetable.insert_time_table_slot(ttslot),ttslot)
>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389

    def test_remove_time_table_slot(self):
        self.timetable.remove_time_table_slot(Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        self.timetable.remove_time_table_slot(Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        self.timetable.remove_time_table_slot(Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
        self.timetable.remove_time_table_slot(Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        print('-------------------------Remove time table slot ------------------')
        print(self.timetable)

    def test_assign_lecture(self):

        # TODO
        # check for the cases where the lecture is occupied and the classroom is
        # not free
        pass

    def test_add_lecture(self):

        # test for the case of adding a lecture to a slot that is free with free parameter
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        print(self.timetable)
        print('---------------------------After Adding Lecture-----------------')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        print(self.timetable)

        # test for the case of adding a lecture to a slot that is not free with free parameter
        lecturer = Lecturer('Selasi Agbemenu', 4564541, 'Mr')
        course = Course('Linear Electronics', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        print('---------------------------After Adding Lecture to Occupied---------')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        self.assertFalse(self.timetable.add_lecture(lecture, ttslot))
        print(self.timetable)

        # test for adding a lecture to slot that is not in the timetable
        print('---------------------------After Adding Lecture to Occupied---------')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('6:00', '7:00'))
        self.assertFalse(self.timetable.add_lecture(lecture, ttslot))
        print(self.timetable)

    def test_move_lecture(self):
        # test for moving lecture from a slot that is occupied

        # first create a new lecture and then add it to a slot
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        print(self.timetable)
        print('---------------------------After Adding Lecture-----------------')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        print(self.timetable)

        # test for moving lecture from a slot that is not occupied

        self.assertFalse(
            self.timetable.move_lecture(TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00')),
                                        TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'),
                                                      TimeSlot('14:00', '15:00'))))
        print('---------------------After attempting wrong move-------------------')
        print(self.timetable)

        # test for moving lecture to a slot that is not occupied
        self.assertTrue(
            self.timetable.move_lecture(TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00')),
                                        TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
                                        ))
        print('------------------------------After moving lecture (unoccupied)-------------------------')
        print(self.timetable)
        # test for moving lecture to a slot that is occupied with free as True
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        self.assertFalse(
            self.timetable.move_lecture(TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00')),
                                        TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
                                        ))
        print(self.timetable)

        # test for moving lecture to a slot that is not occupied with free as False

        # test for moving a lecture back to itself

        # test for moving from a slot that does not exits
        self.assertFalse(
            self.timetable.move_lecture(TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '10:00')),
                                        TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
                                        ))

        # test for moving to a slot that does not exits
        self.assertFalse(
            self.timetable.move_lecture(TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00')),
                                        TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '12:00'))
                                        ))

    # def test_swap_lectures(self):
    #     self.fail()

    def test_remove_lecture(self):
        # test for removing a lecture from a slot that exists and is occupied

        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        print(self.timetable)
        print('--------TEST - REMOVE-------------------After Adding Lecture-----------------')
        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        print(self.timetable)
        self.assertTrue(self.timetable.remove_lecture(ttslot))
        print('-----TEST REMOVE-----------------------After removing Lecture---------------')
        print(self.timetable)

        # test for removing a lecture from a slot that is empty
        self.assertFalse(self.timetable.remove_lecture(ttslot))

        # test for removing a lecture from a slot that does not exists
        self.assertFalse(self.timetable.remove_lecture(
            TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('7:00', '8:00'))))

    def test_remove_all(self):
        # test for the case of adding a lecture to a slot that is free with free parameter
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot1))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot2))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot3))
        print('---------------------------After Adding Lectures-----------------')
        print(self.timetable)
        self.assertTrue(self.timetable.remove_all())
        print('---------------------------After Removing Lectures-----------------')
        print(self.timetable)

    def test_occupied_slots(self):
        # if all slots are empty return an empty lists
        self.assertEqual([], self.timetable.occupied_slots())
        print(self.timetable.occupied_slots())

        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot1))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot2))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot3))

        self.assertEqual([ttslot, ttslot1, ttslot2, ttslot3], self.timetable.occupied_slots())

        # test when slots are added to timetable

    def test_free_slots(self):
        free = self.timetable.free_slots()

        print('---------Here are the free slots -------------')
        for slot in free:
            print(slot)

    # def test_all_slots(self):
    #     self.fail()

    def test_lecturer_is_free(self):
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot1))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot2))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot3))

        self.assertFalse(self.timetable.lecturer_is_free(lecturer, ttslot.time_slot))
        self.assertFalse(self.timetable.lecturer_is_free(lecturer, ttslot1.time_slot))
        self.assertFalse(self.timetable.lecturer_is_free(lecturer, ttslot2.time_slot))
        self.assertFalse(self.timetable.lecturer_is_free(lecturer, ttslot3.time_slot))

        self.assertTrue(self.timetable.lecturer_is_free(lecturer, TimeSlot('15:00', '16:00')))
        self.assertTrue(self.timetable.lecturer_is_free(lecturer, TimeSlot('12:00', '13:00')))
        self.assertTrue(self.timetable.lecturer_is_free(lecturer, TimeSlot('16:00', '17:00')))
        self.assertTrue(self.timetable.lecturer_is_free(lecturer, TimeSlot('7:00', '8:00')))

    # def test_lecturer_is_free(self):
    #     self.fail()

    def test_section_is_free(self):
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot1))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot2))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot3))

        self.assertFalse(self.timetable.section_is_free(section, ttslot.time_slot))
        self.assertFalse(self.timetable.section_is_free(section, ttslot1.time_slot))
        self.assertFalse(self.timetable.section_is_free(section, ttslot2.time_slot))
        self.assertFalse(self.timetable.section_is_free(section, ttslot3.time_slot))

        self.assertTrue(self.timetable.section_is_free(section, TimeSlot('15:00', '16:00')))
        self.assertTrue(self.timetable.section_is_free(section, TimeSlot('12:00', '13:00')))
        self.assertTrue(self.timetable.section_is_free(section, TimeSlot('16:00', '17:00')))
        self.assertTrue(self.timetable.section_is_free(section, TimeSlot('7:00', '8:00')))

    def test_time_slots_overlap(self):
        self.assertTrue(self.timetable.time_slots_overlap(TimeSlot('12:00', '16:00'), TimeSlot('13:00', '15:00')))
        self.assertTrue(self.timetable.time_slots_overlap(TimeSlot('15:00', '16:00'), TimeSlot('15:00', '16:00')))
        self.assertTrue(self.timetable.time_slots_overlap(TimeSlot('14:00', '16:00'), TimeSlot('15:00', '16:00')))
        self.assertFalse(self.timetable.time_slots_overlap(TimeSlot('14:00', '15:00'), TimeSlot('15:00', '16:00')))
        self.assertFalse(self.timetable.time_slots_overlap(TimeSlot('15:00', '16:00'), TimeSlot('16:00', '16:00')))

    def test_room_is_free(self):
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot1))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot2))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot3))

        self.assertFalse(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('7:00', '8:00')))
        self.assertFalse(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00')))
        self.assertFalse(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00')))
        self.assertFalse(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('10:00', '11:00')))

        self.assertTrue(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('12:00', '13:00')))
        self.assertTrue(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('13:00', '14:00')))
        self.assertTrue(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('14:00', '15:00')))
        self.assertTrue(self.timetable.room_is_free(Classroom('LT ', 45, 'PBOO2'), TimeSlot('15:00', '16:00')))

    def test_timetableslot(self):
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        self.assertTrue(self.timetable.add_lecture(lecture, ttslot))
        self.assertEqual(self.timetable.timetableslot(ttslot.room, ttslot.time_slot), ttslot)
        ttslot1 = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('9:00', '10:00'))
        self.assertEqual(self.timetable.timetableslot(ttslot1.room, ttslot1.time_slot), ttslot1)

    def test_best_fit(self):
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))

        print('----------------Best Fit-----------------------------')
        print(self.timetable.best_fit(lecture))

    def test_first_fit(self):
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Mon', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))

        print('----------------First Fit-----------------------------')
        print(self.timetable.first_fit(lecture))

    # def test_lecturer_clashes(self):
    #     self.fail()

    # def test_section_clashes(self):
    #     self.fail()


# class ClassRoomFactory(factory.Factory):
#     class Meta:
#         model = Classroom

#     name = factory.Faker('name')
#     capacity = factory.sequence(lambda n: n in range(120, 180))
#     location = factory.Faker('name')


# class TimeSlotFactory(factory.Factory):
#     class Meta:
#         model = TimeSlot
#
#     start = factory.Faker('time')
#     end = factory.Faker('time')


if __name__ == "__main__":
    main()
