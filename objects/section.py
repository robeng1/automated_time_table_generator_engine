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

    def __init__(self,department,year, code, size):
        self._department = department
        self._code = code
        self._size = size
        self._year = year

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.department == other.department and self.code == self.code \
                   and self.year == self.year and self.size == other.size
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.department != other.department or self.code != self.code \
                   or self.year != self.year or self.size != other.size
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.year, self.department, self.code,self.size))

    def __str__(self):
        return str(self._code) +' '+ str(self._department) + ' ' + str(self._year)
        

    @property
    def department(self) -> str:
        return self._department

    @property
    def size(self) :
        return self._size

    @property
    def year(self):
        return self._year

    @property
    def code(self) -> str:
        return self._code


    @code.setter
    def code(self, code):
        self._code = code

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
            code=self.code,
            size=self.size,
            year=self.year,
            department=self.department,
        )
