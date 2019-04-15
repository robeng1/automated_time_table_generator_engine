#  Copyright (c) 2019.  Hex Inc.
#  Author: Romeo Obeng
#  Date: 13/04/2019
#  Time: 06:27

from data import CurriculumItem


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

    def __init__(self,c_item,duration):
        self.curriculum_item = c_item
        self.duration = duration

    def __str__(self):
        return ''
    @property
    def section(self):
        return self.section

    @property
    def curriculum_item(self):
        return self.curriculum_item

    @curriculum_item.setter
    def curriculum_item(self,value):
        self.curriculum_item = value

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self,duration):
        self.duration = duration
    
    @property
    def section_size(self):
        return self.section.size
