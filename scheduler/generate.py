from .datagenerator import DataGenerator
from .timetablegenerator import TimeTableGenerator
from objects.timetable import Timetable


class Generate:
    def __init__(self, data=None):
        if data is None:
            self.data = DataGenerator()
        else:
            self.data = data
        self.empty_table = Timetable()
        self.gen = TimeTableGenerator(
            timetable=self.empty_table, lectures=self.data
        )

    @property
    def generate(self):
        return self.gen.generate_timetable()
