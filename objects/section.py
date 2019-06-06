#  Copyright (c) 2019.  Hex Inc.
#  Author: Romeo Obeng
#  Date: 13/04/2019
#  Time: 01:27


class Section(object):
    """
    Used to represent a class
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

    def __init__(self, name, size, year, department='', faculty=''):
        self._name = name
        self._faculty = faculty
        self._department = department
        self._size = size
        self._year = year

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name and self.department == self.department \
                   and self.year == self.year
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name and self.department == self.department \
                   and self.year == self.year
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.year, self.department, self.year))

    def __str__(self):
        return '{name} {year} {size}'.format(
            name=self._name,
            year=self._year,
            size=self._size
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def faculty(self) -> str:
        return self._faculty

    @property
    def department(self) -> str:
        return self._department

    @property
    def size(self) -> int:
        return self._size

    @property
    def year(self) -> int:
        return self._year

    @name.setter
    def name(self, name):
        self._name = name

    @faculty.setter
    def faculty(self, faculty):
        self._faculty = faculty

    @department.setter
    def department(self, department):
        self._department = department

    @size.setter
    def size(self, size):
        self._size = size

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def to_json(self):
        return dict(
            name=self.name,
            size=self.size,
            year=self.year,
            department=self.department,
            faculty=self.faculty
        )
