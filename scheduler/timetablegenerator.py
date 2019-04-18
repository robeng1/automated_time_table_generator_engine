#takes in a list of all curriculum items and an empty timetable
#creates lectures from the curriculum items
#tries to assign all lectures
#assigns lectures till list is empty or till there is no possible means to assign 
# left over lectures

#****************************************************************#
# take care of segmentation in general timetable

#from .../objects/timetable import Timetable
class TIme_table_generator(object):
   
    def __init__(self,timetable,lectures):
        #validates timetable and lectures
        
        self.timetable = timetable
        self.unscheduled_lectures = lectures
        self.scheduled_lectures = []

    def generate_timetable(self):
        #modify to take in constraints 
        for lecture in self.unscheduled_lectures:
            #first look for the best free slot in which the lecture can fit
            #remember that best fit for now can return None hence leading to raised exception here
            timetableslot = self.timetable.bestfit(lecture,True)
            
            #try adding course to that slot if succeded
            #mark the lecture as scheduled
            
            if timetableslot != None:
            #ensure all timetableslots are assigned a day in timetable constructor
                if self.timetable.add_lecture(timetableslot.day,lecture,timetableslot,True):
                    self.unscheduled_lectures.remove(lecture)
                    self.scheduled_lectures.append(lecture)
            else: #if no best fit slot is found
                #get all the occupied slots that the lecture can fit in
                
                #first order permutation
                #check if any of them can fit in any of the free slots
                #if yes move it to that free slot and stop
                
                #if none is found then we have permute among the occupied slots
                    # find an occupied slot which cannot contain the lecture but 
                    # can be moved to free slot and there is a slot that can  
                occuppied = self.timetable.occuppied_slots()

            

    def schudule_lecture(self,lecture):
        #modify to take in constraints
        pass


