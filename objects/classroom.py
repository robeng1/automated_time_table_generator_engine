""" This class was written by Akola Mbey Denis
Date program was written: 13th April,2019
This class is designed to take care of the class or lecture rooms,
their names,their capacity and the location of each of these facilities"""

class Classroom(object):
                """classroom allocation class specifies the capacity of a class,the location
                
                Attributes
                ----------
                
                'name : str
                ' the name of the classroom
                'capacity : int
                    the capacity of the class room/the number of students the classroom can occupy a particular lecture room
                location : int
                    the location of the class room
                 
                    """

                def __init__(self,name,capacity,location ):
                    'the constructor for this class specifies the classroom name,the capacity,the location of the class'
                    self._name=name
                    self._capacity=capacity
                    self._location=location

                def set_name(self,new_name):
                    self._name=new_name

                def set_capacity(self,capacity):
                    self._capacity=capacity

                def set_location(self,location):
                    self._location=location
                
            #getter methods for the classroom class
                def get_name(self):
                    return self._name

                def get_location(self):
                    return self._location

                def get_capacity(self):
                    return self._capacity
                
                def __str__(self):
                    return "classsroom name :"+ self._name+"\n"+"size of classroom:"+str(self._capacity)+"\n" +"location of the classroom:"+self._location+"\n"  
                 
                    
                



                

