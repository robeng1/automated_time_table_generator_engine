#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 01:27

class Course:
    #TODO add validation to setter methods       
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

    def __init(self,name,code,lecturers,assistants,t_mins,p_mins,\
        tut_mins,department,sections,room):
        self._name = name
        self._code = code
        self._lecturers
        self._assistants = assistants
        self._teaching_mins = t_mins
        self._practical_mins = p_mins
        self._tutorial_mins = tut_mins
        self._sections = sections
        self._department  = department
        self._preferred_room = room

    def __str__(self):
        pass
        
    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_code(self):
        return self._code

    def set_code(self,code):
        self._code = code  

    def get_lecturers(self):
        return self._lecturers

    def set_lecturers(self,lecturers):
        self._lecturers = lecturers  
 
    def get_assistants(self):
        return self._assistants

    def set_assistants(self,assistants):
        self._assistants = assistants
    
    def get_teaching_mins(self):
        return self._teaching_mins

    def set_teaching_mins(self,teaching_mins):
        self._teaching_mins = teaching_mins
    
    def get_practical_mins(self):
        return self._practical_mins

    def set_practical_mins(self,practical_mins):
        self._practical_mins = practical_mins
    
    def get_tutorial_mins(self):
        return self._tutorial_mins

    def set_tutorial_mins(self,tutorial_mins):
        self._tutorial_mins = tutorial_mins
    
    def get_sections(self):
        return self._sections

    def set_sections(self,sections):
        self._sections = sections
    
    def get_department(self):
        return self._department

    def set_department(self,department):
        self._department = department
    
    def get_preferred_room(self):
        return self._preferred_room

    def set_preferred_room(self,preferred_room):
        self._preferred_room = preferred_room

    