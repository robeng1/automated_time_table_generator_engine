#  Copyright (c) 2019.  Hex Inc.
#  Author: Romeo Obeng
#  Date: 13/04/2019
#  Time: 06:27

from . section import Section
from . course import Course
from . lecturer import Lecturer


class CurriculumItem:
    """
        This class repr an item on the curriculum
        we combine a class, a lecturer and a course
        to create a unique tuple

        for instance (MATH151, Computer Eng1, Dr.Barnes)
        this tuple uniquely identifies a ``lecture``

        for instances of shared courses
        the section will be a list of all the sections
        taking that class
        eg. Economics
        ...

        Attributes
        ----------
        section: Section
            this is effectively a class eg. comp eng 3
        course : Course
            this is course
        lecturer : Lecturer
            a list of lecturers thus the first and second examiner
        _allocated : int
            the mins of the total teaching mins that have been
            allocated

    """

    def __init__(self, section, course, lecturer):
        self._section = section
        self._course = course
        self._lecturer = lecturer
        self._allocated = 0

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        self._section = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if not isinstance(value, Course):
            raise TypeError("Value must be of type CourseModel")
        self._course = value

    @property
    def lecturer(self):
        return self._lecturer

    @lecturer.setter
    def lecturer(self, value):
        if not isinstance(value, Lecturer):
            raise TypeError("Value must be of type Lecturer")
        self._lecturer = value

    @property
    def teaching_mins(self):
        return self._course.teaching_mins
    
    def __str__(self) -> str:
        return self.section.name + ' ' + self.course


class Curriculum:
    """
        This will be fed into the generator to generate the timetable
            ...

            Attributes
            ----------
            items: list
                this is a list of curriculum items

        """
    def __init__(self, items):
        self.items = items
        self._index = 0
        self._length = len(items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self._length == 0 or self._index == self._length - 1:
            raise StopIteration
        item = self.items[self._index]
        self._index = self._index + 1
        return item

    def add(self, item: CurriculumItem):
        if not isinstance(item, CurriculumItem):
            raise TypeError("Value must be of type CurriculumItem")
        self.items.append(item)
