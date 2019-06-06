#  Copyright (c) 2019.  Hex Inc.
#  Author: Akola Denis
#  Date: 13/04/2019
#  Time: 01:27


class Classroom(object):
    """classroom allocation class specifies the capacity of a class,the location
                
                Attributes
                ----------
                
                name : str
                ' the name of the classroom
                capacity : int
                   the capacity of the class room/the number of students the classroom c
                   an occupy a particular lecture room
                location : int
                    the location of the class room
                 
                    """

    def __init__(self, name, capacity, allowance, location='',):
        """the constructor for this class specifies the
        classroom name,the capacity,the location of the class
        """
        self._name = name
        self._capacity = capacity
        self._location = location
        self._allowance = allowance

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name and self.capacity == other.capacity and \
                   self.location == self.location
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name or self.capacity != other.capacity or \
                   self.location != self.location
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.name, self.capacity, self.location))

    def __str__(self):
        return "Room:" + self._name + '\t' + "Capacity :" \
               + str(self._capacity)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def location(self):
        return self._location

    @property
    def allowance(self):
        return self._allowance

    @location.setter
    def location(self, location):
        self._location = location

    def can_accommodate(self, size, allowance=0):
        return (self._capacity + allowance) >= size

    @property
    def to_json(self):
        model = dict(
            name=self.name,
            capacity=self.capacity,
            location=self.location,
            allowance=self.allowance
        )
        return model
