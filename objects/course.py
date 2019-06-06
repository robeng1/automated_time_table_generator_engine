#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 01:27


class Course(object):
    # TODO add validation to setter methods
    # remove redundant attributes     
    """
      A class for representing Courses

      ...

      Attributes
      ----------

        _name : str
      		Full name of the course

        _code : str
      		unique identification for the course

        _lecturers : []
      		list of all lecturers teaching the course
            list is ordered by importance of lecturers
        
        _assistants : []
            list of teaching assistants 

        _department: department 
      		Department offering the course
            
        _teaching_mins: int
            minutes for tutorial munutes
        
        _practical_mins:  int
            minutes for practical sessions
            
        _tutorial_mins: int
            minutes fpr tutorial sessions

        _sections: []
            list of all sections taking the course

        _preferred_room: classroom
            The preferred room for scheduling the course

    """

    def __init__(self, name, dept_code,course_code, t, p,c,tutorial):
        self._name = name
        self._dept_code = dept_code
        self._course_code = course_code
        if t:
            self._teaching = int(t)
        else:
            self._teaching = 0

        if p:
            self._practical = int(p)
        else:
            self._practical = 0 
        if c:
            self._credits = int(c)
        else:
            self._credits = 0

        if tutorial:
            self._tutorial = int(tutorial)
        else:
            self._tutorial = 0

    def __str__(self):
        coursestr = self._dept_code +' '+self._course_code + ' ' + self._name + ' '
        return coursestr

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dept_code(self):
        return self._dept_code

    @property
    def course_code(self):
        return self._course_code

    @dept_code.setter
    def dept_code(self,code):
        self._course_code = code

    @course_code.setter
    def course_code(self, code):
        self._course_code = code

    @property
    def teaching(self):
        return self._teaching

    @teaching.setter
    def teaching(self, t):
        if t:
            self._teaching = int(t)
        else:
            self._teaching = 0

    @property
    def practical(self):
        return self._practical

    @practical.setter
    def practical(self, p):
        if p:
            self._practical = int(p)
        else:
            self._practical = 0

    @property
    def credits(self):
        return self._credits
        
    @credits.setter
    def credits(self, c):
        if c:
            self._credits = int(c)
        else:
            self._credits = 0

    @property
    def tutorial(self):
        return self._tutorial

    @tutorial.setter
    def tutorial(self, tutorial):
        if tutorial:
            self._tutorial = int(tutorial)
        else:
            self._tutorial = 0
    