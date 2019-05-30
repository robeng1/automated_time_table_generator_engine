from unittest import TestCase
from .test_dataGenerator import ModuleFactory, SectionFactory
from .datagenerator import DataGenerator
import factory
from .timetablegenerator import TimeTableGenerator
from objects.timetable import Timetable


class TestTimeTableGenerator(TestCase):
    def setUp(self) -> None:
        self.modules = factory.generate_batch(ModuleFactory, size=20, strategy='create')
        self.data_gen = DataGenerator(data=self.modules)
        self.time_gen = TimeTableGenerator(timetable=Timetable(), lectures=self.data_gen.lectures)


    def test_scheduled(self):
        self.time_gen.generate_timetable()
        table = self.time_gen.timetable
        self.assertNotEqual(table, None)
        self.assertIsInstance(table, Timetable)
        print(table)


    def test_unscheduled(self):
        self.fail()

    def test_generate_timetable(self):
        self.fail()
