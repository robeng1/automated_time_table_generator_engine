#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 01:27

class Lecturer(object):
    # TODO add validation to setter methods
    #     implement rank/priority for each lecturer        
    """
      A class for representing lecturers and academic staff

      ...

      Attributes
      ----------

        _name : str
      		member the full name of the lecture excluding the title (Mr, Prof, Dr)

        _id	: str
      		unique identification for each lecturer

        _title : str
      		  Lecturer's title (e.g Mr, Mrs, Miss , Prof)

        _department: department 
      		  Department to which the lecturer belongs

        _email : str
      			Lecturer's email
	  
	    _phone_number: str
				Lectuer's phonenumber
        
        _office_number: str
                Lecturer's office number
        
        _office_hours: list
                List of all the all office hours the lecturer is available out of class
        
        _rank: int
                Lecturer's priority based on their position 0...

        Contains getter and setter methods for each attribute

    """

    def __init__(self, name, lect_id, title, department="", email="", off_num="", phone_num="", \
                 hours=[], rank=0):

        self._name = name
        self._id = lect_id
        self._title = title
        self._department = department
        self._email = email
        self._phone_number = phone_num
        self._office_number = off_num
        self._office_hours = hours
        self._rank = rank

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name and self.id == other.id
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name or self.id != other.id
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.name, self.id))

    def __str__(self):

        str_rep = ''
        if self.title:
            str_rep += self.title+'. '
        
        str_rep += self._name+'\n'
        return  str_rep

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, department):
        self._department = department

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, number):
        self._phone_number = number

    @property
    def office_number(self):
        return self._office_number

    @office_number.setter
    def office_number(self, number):
        self._office_number = number

    @property
    def office_hours(self):
        return self._office_hours

    @office_hours.setter
    def office_hours(self, hours):
        self._office_hours = hours

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank=-1):
        self._rank = rank
