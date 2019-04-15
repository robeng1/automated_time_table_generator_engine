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

        self.name = name
        self.id = lect_id
        self.title = title
        self.department = department
        self.email =  email
        self.phone_number =phone_num
        self.office_number = off_num
        self.office_hours = hours
        self.rank = rank 
    
    def __str__(self):
        pass
        
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self,name):
        self.name = name
    @property
    def id(self):
        return self.id

    @id.setter
    def id(self,id):
        self.id = id

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self,department):
        self.department = department

    @property
    def department(self):
        return self.department

    @department.setter
    def department(self,department):
        self.department = department
    
    @property
    def email(self):
        return self.email

    @email.setter
    def email(self,email):
        self.email = email

    @property
    def phone_number(self):
        return self.phone_number

    @phone_number.setter
    def phone_number(self,number):
        self.phone_number = number
    
    @property
    def office_number(self):
        return self.office_number
    
    @office_number.setter
    def office_number(self,number):
        self.office_number = number

    @property
    def office_hours(self):
        return self.office_hours

    @office_hours.setter
    def office_hours(self,hours):
        self.office_hours = hours

    @property
    def rank(self):
        return self.rank

    @rank.setter
    def rank(self,rank=-1):
        self.rank = rank


