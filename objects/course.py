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

    def __init__(self, name, code, lecturers=[], assistants=[], t_mins=120, p_mins=0, \
                 tut_mins=0, department='', sections=[], room=''):
        self._name = name
        self._code = code
        self._lecturers = lecturers
        self._assistants = assistants
        self._teaching_mins = t_mins
        self._practical_mins = p_mins
        self._tutorial_mins = tut_mins
        self._sections = sections
        self._department = department
        self._preferred_room = room

        # change to be taken in as parameters
        self._min_mins_per_meeting = 60
        self._max_mins_per_meeting = 120
        self._max_meetings_per_day = 1

    def __str__(self):
        coursestr = self._code + ' ' + self._name + ' '
        for lecturer in self._lecturers:
            coursestr += ' ' + lecturer.name + '   '

        return coursestr

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def lecturers(self):
        return self._lecturers

    @lecturers.setter
    def lecturers(self, lecturers):
        self._lecturers = lecturers

    @property
    def assistants(self):
        return self._assistants

    @assistants.setter
    def assistants(self, assistants):
        self._assistants = assistants

    @property
    def teaching_mins(self):
        return self._teaching_mins

    @teaching_mins.setter
    def teaching_mins(self, teaching_mins):
        self._teaching_mins = teaching_mins

    @property
    def practical_mins(self):
        return self._practical_mins

    @practical_mins.setter
    def practical_mins(self, practical_mins):
        self._practical_mins = practical_mins

    @property
    def tutorial_mins(self):
        return self._tutorial_mins

    @tutorial_mins.setter
    def tutorial_mins(self, tutorial_mins):
        self._tutorial_mins = tutorial_mins

    @property
    def sections(self):
        return self._sections

    @sections.setter
    def sections(self, sections):
        self._sections = sections

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @property
    def preferred_room(self):
        return self._preferred_room

    @preferred_room.setter
    def preferred_room(self, preferred_room):
        self._preferred_room = preferred_room

    @property
    def to_json(self):
        return dict(
            name=self.name, code=self.code,
            lecturer=self.lecturers[0],
            sections=list(map(lambda x: x.to_json(), self.sections))
        )
