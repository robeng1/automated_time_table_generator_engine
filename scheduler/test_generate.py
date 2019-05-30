from unittest import TestCase
import factory
from .test_dataGenerator import ModuleFactory
from .datagenerator import DataGenerator
from .generate import Generate
from objects.timetable import Timetable


class TestGenerate(TestCase):
    def setUp(self) -> None:
        self.modules = factory.generate_batch(ModuleFactory, size=20, strategy='create')
        self.data_gen = DataGenerator(data=self.modules)
        self.lectures = self.data_gen.lectures

        self.gen = Generate(data=self.lectures)



    def test_generate(self):
        timetable = self.gen.generate
        self.assertNotEqual(timetable, None)
        self.assertIsInstance(timetable, Timetable)
        print(timetable.timetable)



