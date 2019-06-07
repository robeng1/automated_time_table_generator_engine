<<<<<<< HEAD
from unittest import TestCase, main
# import factory
from .classroom import Classroom
from .timeslot import TimeSlot
from .daytimetable import DayTimetable
from .timetableslot import TimetableSlot
from .lecturer import Lecturer
from .course import Course
from .section import Section
from .data import CurriculumItem
from .lecture import Lecture
from .timetable import Timetable

=======
#TODO
#Convert tests using print to use assertEqual()
#Look for and cover edge cases


from unittest import TestCase,main
#import factory
from classroom import Classroom
from timeslot import TimeSlot
from daytimetable import DayTimetable
from timetableslot import TimetableSlot
from lecturer import Lecturer
from course import Course
from section import Section 
from data import CurriculumItem
from lecture import Lecture
from timetable import Timetable
from copy import deepcopy
>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389

class TestTimetable(TestCase):
    def setUp(self):
        # create an empty timetable of 5 days
        classrooms = [
            Classroom('LT ', 45, 'PBOO2'),
            Classroom('PB001', 100, 'Petroleum building'),
            Classroom('Main Library ', 60, 'Admiss'),
            Classroom('Room C', 67, 'N1'),
            Classroom(' A110', 300, 'Libary')
            ]



        timeslots = [
            TimeSlot('8:00', '9:00'),
            TimeSlot('9:00', '10:00'),
            TimeSlot('10:00', '11:00'),
<<<<<<< HEAD
            TimeSlot('11:00', '12:00'),
            TimeSlot('12:00', '13:00'),
            TimeSlot('13:00', '14:00'),
            TimeSlot('14:00', '15:00'),
            TimeSlot('15:00', '16:00'),
            TimeSlot('16:00', '17:00')
        ]

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
=======
            TimeSlot('11:00','12:00'),
            TimeSlot('12:00','13:00'),
            TimeSlot('13:00', '14:00')
            ]
     
        
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389
        day_tables = []

        self.days =  days
        for day in days:
<<<<<<< HEAD
            day_tables.append(DayTimetable(classrooms, timeslots, day))

        self.timetable = Timetable(days, day_tables)
        # print(self.timetable)

    @property
    def test_day_table(self):
        pass
=======
            day_tables.append(DayTimetable(classrooms,timeslots,day)) 
       
        self.timetable = Timetable(days,day_tables)


#     @property
#     def test_day_table(self):

#         self.fail()
>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389

    def test_add_lecture(self):
<<<<<<< HEAD
        lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
        course = Course('Embedded Systems', 'COE 361')

        section = Section('ED CoE', 25, 3, 'Electrical and Electronics Engineering', 'Computer Engineering')
        c_item = CurriculumItem(section, course, lecturer)

        lecture = Lecture(c_item, 60)

        ttslot = TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'), TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'), TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'), TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'), TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture('Monday', lecture, ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday', lecture, ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday', lecture, ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday', lecture, ttslot3))
=======
        pass
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
        print(self.timetable)
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.timetableslot('Monday',ttslot1.room,ttslot1.time_slot).is_occupied,True)
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        print('############################### Add Lecture ############################')
        print(self.timetable)
        self.timetable.timetable['Monday'].remove_time_table_slot(Classroom('LT ', 45, 'PBOO2'),TimeSlot('9:00','10:00'))
        print('####################################################################')
>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389
        print(self.timetable)
        self.timetable.timetable['Monday'].move_lecture(ttslot,ttslot4)
        print(self.timetable.timetable)

<<<<<<< HEAD
=======
        self.assertNotEqual(self.timetable.timetable['Monday'],self.timetable.timetable['Tuesday'])

>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389
    def test_move_lecture(self):
        print('############################################## Testing Move Lecture ######################')
        print('##########################################################################################')
        print('##########################################################################################')
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 = TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('9:00', '10:00'))
        ttslot5 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('16:00', '17:00'))
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        print('############################ Before Moving lecture to another slot ##########################')
        print(self.timetable)
        #moving lecture to another slot (existing and free) on the same day
        print('############################ Moving lecture to another slot on same day##########################')
        self.timetable.move_lecture(ttslot.day,ttslot,ttslot4.day,ttslot4)
        print(self.timetable)

        # move lecture to another (non existant) slot on the same day
        print('############### Move Lecture to another slot (non existant) on the same day ###############')
        self.assertFalse(print(self.timetable.move_lecture(ttslot.day,ttslot,ttslot5.day,ttslot5)))
        print(self.timetable)
        
        # move lecture to another slot (existing and free) on a different day
        print('################## move lecture to another slot (existing and free) on a different day ##########')
        #self.assertTrue(self.timetable.move_lecture(ttslot.day,ttslot,'Friday',TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))))
        print(self.timetable)

        # move lecture to another slot (non existant ) on a different day
        print('################## move lecture to another slot (non existant ) on a different day on a different day ##########')
        self.assertFalse(self.timetable.move_lecture(ttslot.day,ttslot,'Monday',TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('18:00', '19:00'))))
        print(self.timetable)

        # move lecture to the same slot on the same day
        print('################## move lecture to the same slot on the same day ##########')
        self.assertFalse(self.timetable.move_lecture(ttslot.day,ttslot,ttslot.day,ttslot))
        print(self.timetable)


        # Move lecture to the same slot (existing and free) on a different day
        print('################## Move lecture to the same slot (existing and free) on a different dayy ##########')
        #self.assertTrue(self.timetable.move_lecture(ttslot.day,ttslot,'Friday',TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))))
        print(self.timetable)


        # move lecture to another slot (existing and occupied) on the same day



        # move lecture to another slot (existing and occpied) on the on a different day


    
        pass

    def test_swap_lectures(self):
        pass
        #Test later, not called in generator at the moment
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        print(self.timetable)
       
       #test cases

       #swapping with invalid parameters
                ####################Expected results for all cases##########################
                # No lecture should be moved
                # return false 
                # No exception should be raised
                ############################################################################
            #invadlid days
                #invalid day1
                #self.assertFalse(self.timetable.swap_lectures('Saturday',ttslot))
                #invalid day2

            #invalid slots
                #invalid slot1
                #invalid slot2

       #swapping with one empty slot
                ####################Expected results for all cases##########################
                # No lecture should be moved
                # return false 
                # No exception should be raised
                ############################################################################
            #empty source slot

            #empty desitnation slot


       #swapping with both empty slots
                 ####################Expected results for all cases##########################
                # No lecture should be moved
                # return false 
                # No exception should be raised
                ############################################################################

       #swapping on the same day
                 ####################Expected results for all cases##########################
                # Move lecture in case of same slot
                # Dont move in case of different slots
                # return True if different slots and false in same 
                # No exception should be raised
                ############################################################################
            #same slot  @property
    def test_day_table(self):
        pass
        
    # def test_add_lecture(self):
    #     pass
    #     lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
    #     course = CourseModel('Embedded Systems','COE 361')

    #     section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
    #     c_item = CurriculumItem(section,course,lecturer)

    #     lecture = Lecture(c_item,60)
        
    #     ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
    #     ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
    #     ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
    #     ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
    #     ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
    #     print(self.timetable)
    #     self.assertTrue(self.timetable.timetable['Monday'].add_lecture(lecture,ttslot))
    #     self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
    #     self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
    #     self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
    #     print('############################### Add Lecture ############################')
    #     print(self.timetable)
    #     self.timetable.timetable['Monday'].remove_time_table_slot(Classroom('LT ', 45, 'PBOO2'),TimeSlot('9:00','10:00'))
    #     print('####################################################################')
    #     print(self.timetable)
    #     self.timetable.timetable['Monday'].move_lecture(ttslot,ttslot4)
    #     print(self.timetable)

    #     self.assertNotEqual(self.timetable.timetable['Monday'],self.timetable.timetable['Tuesday'])

    # def test_move_lecture(self):
    #     pass
    #     lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
    #     course = CourseModel('Embedded Systems','COE 361')

    #     section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
    #     c_item = CurriculumItem(section,course,lecturer)

    #     lecture = Lecture(c_item,60)
        
    #     ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
    #     ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
    #     ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
    #     ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
    #     ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('9:00', '10:00'))
    #     self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
    #     self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
    #     self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
    #     self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
    #     print('############################ Before Moving lecture to another slot on same day##########################')
    #     print(self.timetable)
    #     #moving lecture to another slot (existing and free) on the same day
    #     print('############################ Moving lecture to another slot on same day##########################')
    #     self.timetable.move_lecture(ttslot.day,ttslot,ttslot4.day,ttslot4)
    #     print(self.timetable)

        #move lecture to another (non existant) slot on the same day


        #move lecture to another slot (existing and free) on a different day


        #move lecture to another slot (non existant ) on the same day


        #move lecture to the same slot on the same day



        #Move lecture to the same slot (existing and free) on a different day


        #move lecture to another slot (existing and occupied) on the same day



        #move lecture to another slot (existing and occpied) on the on a different day

    # def test_swap_lectures(self):
    #     pass
    #     # #Test later, not called in generator at the moment
    #     # lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
    #     # course = CourseModel('Embedded Systems','COE 361')

    #     # section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
    #     # c_item = CurriculumItem(section,course,lecturer)

    #     # lecture = Lecture(c_item,60)
        
    #     # ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
    #     # ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
    #     # ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
    #     # ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
    #     # self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
    #     # self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
    #     # self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
    #     # self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
    #     # print(self.timetable)
       
    #    #test cases

    #    #swapping with invalid parameters
    #             ####################Expected results for all cases##########################
    #             # No lecture should be moved
    #             # return false 
    #             # No exception should be raised
    #             ############################################################################
    #         #invadlid days
    #             #invalid day1
    #             #self.assertFalse(self.timetable.swap_lectures('Saturday',ttslot))
    #             #invalid day2

    #         #invalid slots
    #             #invalid slot1
    #             #invalid slot2

    #    #swapping with one empty slot
    #             ####################Expected results for all cases##########################
    #             # No lecture should be moved
    #             # return false 
    #             # No exception should be raised
    #             ############################################################################
    #         #empty source slot

    #         #empty desitnation slot


    #    #swapping with both empty slots
    #              ####################Expected results for all cases##########################
    #             # No lecture should be moved
    #             # return false 
    #             # No exception should be raised
    #             ############################################################################

    #    #swapping on the same day
    #              ####################Expected results for all cases##########################
    #             # Move lecture in case of same slot
    #             # Dont move in case of different slots
    #             # return True if different slots and false in same 
    #             # No exception should be raised
    #             ############################################################################
    #         #same slot 


    #         #different slot
            

    #    #swapping accross days
    #             ####################Expected results for all cases##########################
    #             # Move lecture
    #             # Dont move in case of different slots
    #             # return True
    #             # No exception should be raised
    #             ############################################################################
    #         #same slot

    #         #different slot



    def test_remove_lecture(self):
        print('################################### Test Removing Lectures ###############################')
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
        print(self.timetable)
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        print(self.timetable)
        self.assertTrue(self.timetable.remove_lecture(ttslot.day,ttslot))
        self.assertTrue(self.timetable.remove_lecture(ttslot1.day,ttslot1))
        self.assertTrue(self.timetable.remove_lecture(ttslot2.day,ttslot2))
        self.assertTrue(self.timetable.remove_lecture(ttslot3.day,ttslot3))
        self.assertFalse(self.timetable.remove_lecture(ttslot4.day,ttslot4))
        print(self.timetable)
        
        print('####################################################################')
        print(self.timetable)
        self.timetable.timetable['Monday'].move_lecture(ttslot,ttslot4)

    def test_remove_all(self):
        print('################################### Test Removing Lectures ###############################')
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
        
        #print(self.timetable)
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        #print('############################## Before Adding Lecture ###########################')
        #print(self.timetable)
        #print('############################# After Removing Lecture #############################')
        self.assertTrue(self.timetable.remove_all())
        #print(self.timetable)

    def test_occupied_slots(self):
        print('################################### Testing Occupied Slots ###############################')
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
        
        #print(self.timetable)
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        
        slots = self.timetable.occupied_slots()

        for slot in slots:
            print(slot.lecture)

    def test_free_slots(self):
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
        
        #print(self.timetable)
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        print("############ Testing Free Slots##############################")
        slots = self.timetable.free_slots()

        for slot in slots:
            print(slot)

    def test_all_slots(self):
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
        
        #print(self.timetable)
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        print("############ Testing All Slots##############################")
        slots = self.timetable.all_slots()

        for slot in slots:
            print(slot)

    def test_lecturer_is_free(self):
<<<<<<< HEAD
        pass

=======
        lecturer = Lecturer('Benjamin Kommey',4564541,'Mr')
        course = Course('Embedded Systems','COE 361')

        section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
        c_item = CurriculumItem(section,course,lecturer)

        lecture = Lecture(c_item,60)
        
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        ttslot1 =TimetableSlot('Tuesday', Classroom(' A110', 300, 'Libary'),TimeSlot('9:00', '10:00'))
        ttslot2 = TimetableSlot('Thursday', Classroom('Room C', 67, 'N1'),TimeSlot('10:00', '11:00'))
        ttslot3 = TimetableSlot('Friday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('11:00', '12:00'))
        ttslot4 =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('10:00', '11:00'))
        
        #print(self.timetable)
        self.assertTrue(self.timetable.add_lecture('Monday',lecture,ttslot))
        self.assertTrue(self.timetable.add_lecture('Tuesday',lecture,ttslot1))
        self.assertTrue(self.timetable.add_lecture('Thursday',lecture,ttslot2))
        self.assertTrue(self.timetable.add_lecture('Friday',lecture,ttslot3))
        print("############ Testing All Slots##############################")

        self.assertFalse(self.timetable.lecturer_is_free('Monday',lecturer,TimeSlot('8:00', '9:00')))
        self.assertTrue(self.timetable.lecturer_is_free('Monday',lecturer,TimeSlot('9:00', '10:00')))
        self.assertFalse(self.timetable.lecturer_is_free('Tuesday',lecturer,TimeSlot('9:00', '10:00')))
        self.assertTrue(self.timetable.lecturer_is_free('Tuesday',lecturer,TimeSlot('8:00', '9:00')))
        self.assertFalse(self.timetable.lecturer_is_free('Thursday',lecturer,TimeSlot('10:00', '11:00')))
        self.assertTrue(self.timetable.lecturer_is_free('Thursday',lecturer,TimeSlot('9:00', '10:00')))
        self.assertFalse(self.timetable.lecturer_is_free('Friday',lecturer,TimeSlot('11:00', '12:00')))
        self.assertTrue(self.timetable.lecturer_is_free('Friday',lecturer,TimeSlot('18:00', '19:00')))
        
    
>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389
    def test_timetableslot(self):
        ttslot =  TimetableSlot('Monday', Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        self.assertEqual(self.timetable.timetableslot(ttslot.day,ttslot.room,ttslot.time_slot),ttslot)

    def test_best_fit(self):
        for day in self.days:
            self.assertTrue(self.timetable.day_is_valid(day))
        self.assertFalse(self.timetable.day_is_valid('Saturday'))

    def test_remove_slot(self):
        print('##################################### TEST_REMOVE_SLOT##############################')
        self.timetable.remove_slot('Monday',Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        self.timetable.remove_slot('Monday',Classroom('LT ', 45, 'PBOO2'),TimeSlot('9:00', '10:00'))
        self.timetable.remove_slot('Wednesday',Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        self.timetable.remove_slot('Thursday',Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '9:00'))
        print(self.timetable)
        print('################################# INSERT SLOT #####################################')
        self.timetable.insert_slot('Monday',TimetableSlot('Monday',Classroom('LT ', 45, 'PBOO2'),TimeSlot('8:00', '10:00')))
        print(self.timetable)

    def test_insert_slot(self):
        #tested in remove_slot()
        pass

<<<<<<< HEAD
    def test_lecturer_clashes(self):
        pass

    def test_section_clashes(self):
        pass


if __name__ == '__main__':
    main()
=======
    #  def test_first_fit(self):
    #      pass

#     def test_day_is_valid(self):
#         pass

#     def test_lecturer_clashes(self):
#         pass
    
#     def test_section_clashes(self):
#         pass
    
if __name__ == '__main__':
    main()

>>>>>>> 4434ae1f824149787cc07a68879f82b15d83f389
