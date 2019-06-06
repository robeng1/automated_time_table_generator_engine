#  Copyright (c) 2019.  Hex Inc.
#  Author: Akola Denis
#  Date: 13/04/2019
#  Time: 01:27


class Classroom(object):
    """classroom albuilding class specifies the capacity of a class,the building
                
                Attributes
                ----------
                
                name : str
                ' the name of the classroom
                capacity : int
                   the capacity of the class room/the number of students the classroom c
                   an occupy a particular lecture room
                building : int
                    the building of the class room
                 
                    """

    def __init__(self, name, capacity, building,allowance):
        """the constructor for this class specifies the
        classroom name,the capacity,the building of the class
        """
        self._name = name

        if capacity:
            self._capacity = int(capacity)
        else:
            self._capacity = 0
        self._building = building

        if allowance:
            self._allowance = int(allowance)
        else:
            self._allowance = 0

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name and self.capacity == other.capacity and \
                   self.building == self.building
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name or self.capacity != other.capacity or \
                   self.building != self.building
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.name, self.capacity, self.building))

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
    def allowance(self):
        return self._allowance

    @allowance.setter
    def allowance(self, allowance):
        if allowance:
            self._allowance = int(allowance)
        else:
            self._allowance = 0

    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, building):
        self._building = building

    def can_accommodate(self, size, allowance=0):
        return (self._capacity + self._allowance) >= size
