from .datagenerator import DataGenerator
from objects.lecture import Lecture
from objects.data import CurriculumItem
import factory
from app.models import CourseModel, SectionModel
from unittest import TestCase


class TestDataGenerator(TestCase):
    def setUp(self) -> None:
        self.modules = factory.generate_batch(ModuleFactory, size=20, strategy='create')
        self.data_gen = DataGenerator(data=self.modules)

    def test_lectures(self):
        for i in self.data_gen.lectures:
            print(i)
        self.assertNotEqual(self.data_gen.lectures, None)


class SectionFactory(factory.Factory):
    class Meta:
        model = SectionModel

    klass = 'COMP ENG 3'
    code = 'MATH 151'
    shared = False


class ModuleFactory(factory.Factory):
    class Meta:
        model = CourseModel

    title = 'Mathematics'
    code = 'MATH 151'
    teaching = 3
    practicals = 4
    credit = 5
    first_examiner = 'P. Y . Okyere'
    second_examiner = 'Dr. Barnes'
    department = 'Mathematics'
    year = '2015'
    sections = factory.List([factory.SubFactory(SectionFactory) for _ in range(6)])