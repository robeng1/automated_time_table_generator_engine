#  Copyright (c) 2019.  Hex Inc.
#  Author: Romeo Obeng
#  Date: 13/04/2019
#  Time: 06:27

# from .data import CurriculumItem


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
        course : CourseModel
            this is course
        lecturers : Lecturer
            a list of lecturers thus the first and second examiner
        allocated : int
            the mins of the total teaching mins that have been
            allocated

    """

    def __init__(self, c_item, duration):
        self._curriculum_item = c_item
        self.duration = duration

    def __str__(self):
        return str(self.curriculum_item.course) + '\n' + \
               str(self.curriculum_item.section.department) + ' '+str(self.curriculum_item.section.year) + '\n' + \
               str(self.curriculum_item.lecturer) + '\n' + \
               str(self.duration) + '\n' + '-----------------------------------------'

    @property
    def curriculum_item(self):
        return self._curriculum_item

    @curriculum_item.setter
    def curriculum_item(self, value):
        self._curriculum_item = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if duration > 0:
            self._duration = duration
        else:
            raise ValueError("Invalid Duration: Duration less than or equal to 0")
