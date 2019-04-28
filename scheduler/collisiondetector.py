#  Copyright (c) 2019.  Hex Inc.
#  Author: Kumbong Hermann
#  Date: 22/04/2019
#  Time: 20:27

class CollisionDetector:

    def __init__(self,timetable):
        self.timetable = timetable

    def lecturer_clashes(self):
        #the same lecturer is having classes at the same  time
        return self.timetable.lecturer_clashes()
    
    def section_clashes(self):
        #the same section is having clashes at the same time
        #watchout for courses like electives where the same
        #section can be taking  the lecture at the same time
        return self.timetable.section_clashes()

    #not necessary now it is not possible to add two lecture with the current algorith
    def room_clashes(self):
        #not necessrary our scheduling mechanism and timetable datastructure 
        #already obviates the need to later check for room clashes
        pass