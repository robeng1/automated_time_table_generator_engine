#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 13/04/2019
#  Time: 01:27

class Lecturer(object):
    #TODO add validation to setter methods
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

    def __init__(self,name,lect_id,title,department,email="",off_num="", phone_num="",\
         hours=[],rank = 0):

        self._name = name
        self._id = lect_id
        self._title = title
        self._department = department
        self._email =  email
        self._phone_number =phone_num
        self._office_number = off_num
        self._office_hours = hours
        self._rank = rank 
    
    def __str__(self):
        pass
        
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name = name

    def get_id(self):
        return self._id

    def set_id(self,id):
        self._id = id

    def get_title(self):
        return self._title

    def set_title(self,department):
        self._department = department

    def get_department(self):
        return self._department

    def set_department(self,department):
        self._department = department
    
    def get_email(self):
        return self._email

    def set_email(self,email):
        self._email = email

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self,number):
        self._phone_number = number
    
    def get_office_number(self):
        return self._office_number
    
    def set_office_number(self,number):
        self._office_number = number

    def set_office_hours(self,hours):
        self._office_hours = hours

    def get_office_hours(self):
        return self._office_hours

    def set_rank(self,rank=-1):
        self._rank = rank

    def get_rank(self):
        return self._rank


