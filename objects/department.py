#  Copyright (c) 2019.  Hex Inc.
#  Author: Akola Denis
#  Date: 13/04/2019
#  Time: 01:27

class Department(object):
    """classroom allocation class specifies the capacity of a class,the location
                    
                    Attributes
                    ----------
                    
                    name : str
                    the name of the department
                    faculty : str
                        the faculty to which the department belongs
                    college:str
                        the college to which the department belongs
                    department_code: str
                        a unique code that is used to distinctively identify a department for other departments within the same faculty and college
                    departmental_courses:list
                        a list contain the set of all courses in a department.
                    
                """

    def __init__(self, name, faculty, college, department_code, departmental_courses):
        self._name = name
        self._faculty = faculty
        self._college = college
        self._department_code = department_code
        self._departmental_courses = departmental_courses

    # the getter methods for the department class
    def get_name(self):
        return self._name

    def get_faculty(self):
        return self._faculty

    def get_college(self):
        return self._college

    def get_department_code(self):
        return self._department_code

    def get_departmental_courses(self):
        return self._departmental_courses

    def set_name(self, name):
        self._name = name

    def set_faculty(self, faculty):
        self._faculty = faculty

    def set_college(self, college):
        self._college = college

    def set_department_code(self, department_code):
        self._department_code = department_code

    def set_departmental_courses(self, departmental_courses):
        self._departmental_courses = departmental_courses

    def __str__(self):
        return " Name of department:" + self._name + "\n" + " Faculty of the department:" + self._name + "\n" + " Name of the college:" + self._college + "\n" + " Department code " + self._department_code + "\n" + " Departmental courses:" + str(
            self._departmental_courses)
