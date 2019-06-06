from unittest import TestCase,main
#import factory
from .classroom import Classroom
from .timeslot import TimeSlot
from .timetableslot import TimetableSlot


class TestTimetableSlot(TestCase):
    def setUp(self) -> None:
        self.ttslot1 = TimetableSlot('mon',Classroom('PB001',120),TimeSlot('8:00','9:00'))
        self.ttslot2 = TimetableSlot('mon',Classroom('PB001',120),TimeSlot('9:00','10:00'))

    def test__eq__(self):
        self.assertTrue(self.ttslot1==self.ttslot1)
        self.assertTrue(self.ttslot1!=self.ttslot2)

if __name__ == '__main__':
    main()