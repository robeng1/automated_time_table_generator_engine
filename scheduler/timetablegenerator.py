#takes in a list of all curriculum items and an empty timetable
#creates lectures from the curriculum items
#tries to assign all lectures
#assigns lectures till list is empty or till there is no possible means to assign 
# left over lectures

#****************************************************************#
# take care of segmentation in general timetable

#from .../objects/timetable import Timetable
class Time_table_generator(object):
   
    def __init__(self,timetable,lectures):
        #validates timetable and lectures
        
        self.timetable = timetable
        self.unscheduled_lectures = lectures
        self.scheduled_lectures = []

    def generate_timetable(self):
        #modify to take in constraints 
        for lecture in self.unscheduled_lectures:
            #first look for the best free slot in which the lecture can fit
            #remember that best fit for now can return None hence leadinog to raised exception here
            timetableslot = self.timetable.bestfit(lecture,True)
            
            #try adding course to that slot if succeded
            #mark the lecture as scheduled
            
            if timetableslot != None:
            #ensure all timetableslots are assigned a day in timetable constructor
                if self.timetable.add_lecture(timetableslot.day,lecture,timetableslot,True):
                    self.unscheduled_lectures.remove(lecture)
                    self.scheduled_lectures.append(lecture)
            else: 
                relocatable = {}

                #fill relocatable with all occupied slots that can accomodate lecture
                #alongside with all possible free slots they can be moved to 
                for occupied_slot in self.timetable.occupied_slots():
                    if occupied_slot.can_hold(lecture):#implement  in timetableslot
                        for free_slot in self.timetable.free_slots():
                            possible_dest_slots = []
                            if free_slot.can_hold(occupied_slot.lecture):
                                possible_dest_slots.append(free_slot)
                        relocatable[occupied_slot] = possible_dest_slots
                
                if relocatable: #only run if relocatable slots found
                #associate occupied slots only with only the best fit dest slots 
                    for occupied_slot in relocatable.keys():#keys are occupied slots
                        dest_slots = relocatable[occupied_slot]
                        relocatable[occupied_slot] = occupied_slot.best_fit(dest_slots)#implement in timetableslot

                         #decide on which slot to remove
                         #get the best slot and move
                    best_slot = list(relocatable.keys())[0]
                    for occupied_slot in relocatable.keys():
                        #occupied slot must have a lecture
                        free_slot = relocatable[occupied_slot]
                        if ((free_slot.room.capacity - \
                            occupied_slot.lecture.curriculum_item.section.size) + \
                            (lecture.curriculum_item.section.size -\
                            occupied_slot.room.capacity)) < ((best_slot.room.capacity - \
                            best_slot.lecture.curriculum_item.section.size) + \
                            (lecture.curriculum_item.section.size -\
                            best_slot.room.capacity)) :
                            best_slot  = occupied_slot
                    
                    #move occupied lecture to free slot
                    dest_slot = relocatable[best_slot]
                    self.timetable.move_lecture(best_slot.day,best_slot,dest_slot.day,dest_slot,False)
                    self.timetable.add_lecture(best_slot.day,lecture,best_slot)

                else: #if not relocatable
                        pass
    def schudule_lecture(self,lecture):
        #modify to take in constraints
        pass

    try:
            timetableslot = self.timetableslot(timetableslot.room,timetableslot.timeslot)
            if free:#add_lecture to slot only if slot is free
                if self.lecturers_are_free(timetableslot.timetlost,lecture.curriculum_item.lecturers):
                    if self.section_is_free(lecture.curriculum_item.section,timetableslot.timeslot):
                        if timetableslot.room.can_accomodate(lecture.curriculum_item.section.size):
                            if timetableslot.timeslot.duration == lecture.duration:
                                index = self.table[timetableslot.room].index(timetableslot)
                                self.table[timetableslot.room][index] = timetableslot
                                
                                return True

                            elif timetableslot.timeslot.duration < lecture.duration:
                                #get a list of all contiguous free left neighbours
                                #get a list of all contiguous free right neighbours
                                #add left neighbours to slot until it's duration can
                                #add right neighbours to slot until it's durration can
                                left = self.free_left_neighbours(timetableslot)
                                right = self.free_right_neighbours(timetableslot)

                                #check if the right and left neighbours combined can provide the
                                #excess of time needed

                           
                                
            elif not free:#add_lecture to slot even if it is not free
                pass
        except Exception:
            return False