from unittest import TestCase
import factory
from objects.classroom import Classroom
from objects.timeslot import TimeSlot
from objects.daytimetable import DayTimetable
from objects.timetableslot import TimetableSlot


class TestDayTimetable(TestCase):
    def setUp(self) -> None:
        # self.classrooms = factory.generate_batch(ClassRoomFactory, size=20, strategy="build")
        # self.slots = slots
        # self.day_tt = DayTimetable(classrooms=self.classrooms, time_slots=self.slots)

        classrooms = [
            Classroom('PB001', 100, 'Petroleum building'),
            Classroom('PBOO2 ', 45, 'Petroleum building'),
            Classroom('LT ', 300, 'Near building'),
            Classroom('Pb103', 67, 'Petroleum Building'),
            Classroom('PB119', 150, 'Petroluem'),
            Classroom('PB001', 100, 'Petroluem'),
            Classroom('LT ', 45, 'PBOO2'),
            Classroom(' A110', 300, 'Libary'),
            Classroom('Computer lab', 67, 'vodafone'),
            Classroom('LAB-12', 40, 'vodafone'),
            Classroom('Room A', 100, 'tyeh'),
            Classroom('Room B ', 45, 'PBOO2'),
            Classroom('Main Library ', 60, 'Admiss'),
            Classroom('Room C', 67, 'N1')]

        timeslots = [
            TimeSlot('8:00','9:00'),
            TimeSlot('9:00','10:00'),
            TimeSlot('10:00', '11:00'),
            TimeSlot('11:00', '12:00'),
            TimeSlot('12:00', '13:00'),
            TimeSlot('13:00', '14:00'),
            TimeSlot('14:00', '15:00'),
            TimeSlot('15:00', '16:00'),
            TimeSlot('16:00', '17:00')
        ]

        self.day = 'Mon'
        self.timetable = DayTimetable(classrooms, timeslots)
        print(self.timetable)

    def test_validate_time_slots(self):
       self.assertTrue(self.timetable.validate_time_slots())

    def test_day(self):
        self.fail()

    def test_has_left_neighbour(self):
        self.assertFalse(self.timetable.has_left_neighbour(TimetableSlot('Mon',TimeSlot('8:00','9:00'),Classroom('PB001', 100, 'Petroleum building'))))
        self.assertTrue(self.timetable.has_left_neighbour(
            TimetableSlot('Mon', TimeSlot('9:00', '9:00'), Classroom('PB001', 100, 'Petroleum building'))))
        self.assertTrue(self.timetable.has_left_neighbour(
            TimetableSlot('Mon', TimeSlot('16:00', '17:00'), Classroom('PB001', 100, 'Petroleum building'))))
    def test_has_right_neighbour(self):
        self.fail()

    def test_left_neighbour(self):
        self.fail()

    def test_right_neighbour(self):
        self.fail()

    def test_left_neighbours(self):
        self.fail()

    def test_right_neighbours(self):
        self.fail()

    def test_insert_time_table_slot(self):
        self.fail()

    def test_assign_lecture(self):
        self.fail()

    def test_add_lecture(self):
        self.fail()

    def test_move_lecture(self):
        self.fail()

    def test_swap_lectures(self):
        self.fail()

    def test_remove_lecture(self):
        self.fail()

    def test_remove_all(self):
        self.fail()

    def test_occupied_slots(self):
        self.fail()

    def test_free_slots(self):
        self.fail()

    def test_all_slots(self):
        self.fail()

    def test_lecturers_are_free(self):
        self.fail()

    def test_lecturer_is_free(self):
        self.fail()

    def test_section_is_free(self):
        self.fail()

    def test_time_slots_overlap(self):
        self.fail()

    def test_room_is_free(self):
        self.fail()

    def test_timetableslot(self):
        self.fail()

    def test_best_fit(self):
        self.fail()

    def test_first_fit(self):
        self.fail()

    def test_lecturer_clashes(self):
        self.fail()

    def test_section_clashes(self):
        self.fail()


class ClassRoomFactory(factory.Factory):
    class Meta:
        model = Classroom

    name = factory.Faker('name')
    capacity = factory.sequence(lambda n: n in range(120, 180))
    location = factory.Faker('name')


# class TimeSlotFactory(factory.Factory):
#     class Meta:
#         model = TimeSlot
#
#     start = factory.Faker('time')
#     end = factory.Faker('time')


time1 = TimeSlot('8:00', '10:00')
time2 = TimeSlot('1:00', '13:00')
time3 = TimeSlot('15:00', '17:00')
time4 = TimeSlot('9:00', '11:00')
time5 = TimeSlot('12:00', '14:00')
time6 = TimeSlot('17:00', '18:00')
time5 = TimeSlot('12:00', '14:00')
time6 = TimeSlot('17:00', '18:00')

time7 = TimeSlot('12:00', '14:00')
time8 = TimeSlot('17:00', '18:00')

time9 = TimeSlot('12:00', '14:00')
time10 = TimeSlot('17:00', '18:00')

time11 = TimeSlot('12:00', '14:00')
time12 = TimeSlot('17:00', '18:00')

time13 = TimeSlot('12:30', '14:30')
time14 = TimeSlot('17:00', '18:00')

slots = [time1, time2, time3, time4, time5, time7, time8, time9, time10]
