#  Copyright (c) 2019.  Hex Inc.
#  Author: Romeo Obeng
#  Date: 13/04/2019
#  Time: 01:27

class Section(object):
    """
    A class used to represent a class
    we are calling it section here
    for eg. ``computer engineering 3``

    ...

    Attributes
    ----------
    name : str
        the name of class
    faculty : str
        the name of the faculty this class belongs to
    department : str
        the name of the department this class belongs to
    size : int
        the number of students in the class
    year : int
        the year group of the class

    """

    # TODO: add validations to attributes

    def __init__(self, name, faculty, department, size, year):
        self._name = name
        self._faculty = faculty
        self._department = department
        self._size = size
        self._year = year

    def __str__(self):
        return '{name} {year}'.format(
            name=self._name,
            year=self._year,
        )

    def set_name(self, name):
        self._name = name

    def set_faculty(self, faculty):
        self._faculty = faculty

    def set_department(self, department):
        self._department = department

    def set_size(self, size):
        self._size = size

    def set_year(self, year):
        self._year = year

    def get_name(self) -> str:
        return self._name

    def get_faculty(self) -> str:
        return self._faculty

    def get_department(self) -> str:
        return self._department

    def get_size(self) -> int:
        return self._size

    def get_year(self) -> int:
        return self._year
