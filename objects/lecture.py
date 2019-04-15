#  Copyright (c) 2019.  Hex Inc.
#  Author: Romeo Obeng
#  Date: 13/04/2019
#  Time: 06:27

from section import Section
from course import Course
from lecturer import Lecturer


class Lecture:
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
        lecturers : Lecturer
            a list of lecturers thus the first and second examiner
        allocated : int
            the mins of the total teaching mins that have been
            allocated

    """

    def __init__(self, section, course, lecturers,duration):
        self.section = section
        self.course = course
        self.lecturers = lecturers
        self.duration = duration

    def __str__(self):
        return ''
    @property
    def section(self):
        return self.section

    @section.setter
    def section(self, value):
        self.section = value

    @property
    def course(self):
        return self.course

    @course.setter
    def course(self, value):
        if not isinstance(value, Course):
            raise TypeError("Value must be of type Course")
        self.course = value

    @property
    def lecturers(self):
        return self.lecturers

    @lecturers.setter
    def lecturers(self, value):
        if not isinstance(value, Lecturer):
            raise TypeError("Value must be of type Lecturer")
        self.lecturers = value

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self,duration):
        self.duration = duration
