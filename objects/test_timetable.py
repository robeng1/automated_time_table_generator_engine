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
from .timetable import Timetable


class TestTimetable(TestCase):
    def setUp(self):
        # create an empty timetable of 5 days
        classrooms = [
            Classroom('LT ', 45, 'PBOO2'),
            Classroom('PB001', 100, 'Petroleum building'),
            Classroom('PBOO2 ', 45, 'Petroleum building'),
            Classroom('Pb103', 67, 'Petroleum Building'),
            Classroom('PB119', 150, 'Petroluem'),
            Classroom(' A110', 300, 'Libary'),
            Classroom('Computer lab', 67, 'vodafone'),
            Classroom('LAB-12', 40, 'vodafone'),
            Classroom('Room A', 100, 'tyeh'),
            Classroom('Room B ', 45, 'PBOO2'),
            Classroom('Main Library ', 60, 'Admiss'),
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

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        day_tables = []

        for day in days:
            day_tables.append(DayTimetable(classrooms, timeslots, day))

        self.timetable = Timetable(days, day_tables)
        # print(self.timetable)

    @property
    def test_day_table(self):
        pass

    def test_add_lecture(self):
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'), TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'), TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture('Monday', lecture, ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday', lecture, ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday', lecture, ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday', lecture, ttslot3))
        print(self.timetable)

    def test_move_lecture(self):
        pass

    def test_swap_lectures(self):
        pass

    def test_remove_lecture(self):
        pass

    def test_remove_all(self):
        pass

    def test_occupied_slots(self):
        pass

    def test_free_slots(self):
        pass

    def test_all_slots(self):
        pass

    def test_lecturer_is_free(self):
        pass

    def test_timetableslot(self):
        pass

    def test_best_fit(self):
        pass

    def test_first_fit(self):
        pass

    def test_day_is_valid(self):
        pass

    def test_lecturer_clashes(self):
        pass

    def test_section_clashes(self):
        pass


if __name__ == '__main__':
    main()
