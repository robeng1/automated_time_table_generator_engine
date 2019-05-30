from .datagenerator import DataGenerator
from .timetablegenerator import TimeTableGenerator
from objects.timetable import Timetable


class Generate:
    def __init__(self):
        self.data = DataGenerator()
        self.empty_table = Timetable()
        self.gen = TimeTableGenerator(
            timetable=self.empty_table, lectures=self.data.lectures
        )

    def generate(self):
        return self.gen.timetable
