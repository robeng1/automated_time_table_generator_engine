# takes in a list of all curriculum items and an empty timetable
# creates lectures from the curriculum items
# tries to assign all lectures
# assigns lectures till list is empty or till there is no possible means to assign
# left over lectures

# ****************************************************************#

# TODO VERY IMPORTANT
# Change the selection for the best choice from a random selection and perform computation based on some
# metric

# TODO
# modify add_lecture to take in a [] of slots
# lecture should not already be added to the same day

from unittest import TestCase, main
# import factory
from objects.classroom import Classroom
from objects.timeslot import TimeSlot
from objects.daytimetable import DayTimetable
from objects.timetableslot import TimetableSlot
from objects.lecturer import Lecturer
from objects.course import Course
from objects.section import Section
from objects.data import CurriculumItem
from objects.lecture import Lecture
from copy import deepcopy
from random import choice
from objects.timetable import Timetable
import math
from copy import deepcopy
import csv

from app.models import FlatTimeTableModel
from sqlalchemy.exc import SQLAlchemyError, InvalidRequestError, DBAPIError

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in days:
    pass


class TimeTableGenerator(object):
    WEIGHT_DAY_OF_WEEK = 1.15
    WEIGHT_PERIOD_OF_DAY = 1.25
    WEIGHT_SIZE_OF_CLASSROOM = 1.1
    WEIGHT_SECTION_LECTURES = 1.3
    WEIGHT_LECTURER_LECTURES = 1.25
    WEIGHT_OTHER_ROOMS = 1.15
    WEIGHT_LECTURES_ON_DAY = 1.25

    TOTAL_WEIGHT = WEIGHT_DAY_OF_WEEK + WEIGHT_PERIOD_OF_DAY + WEIGHT_SIZE_OF_CLASSROOM + WEIGHT_SECTION_LECTURES + \
                   WEIGHT_LECTURER_LECTURES + WEIGHT_OTHER_ROOMS + WEIGHT_LECTURES_ON_DAY

    def __init__(self, timetable, lectures=[]):
        # validates
        # timetable and lectures

        lectures.sort(key=lambda lecture: lecture.duration, reverse=True)

        self._timetable = deepcopy(timetable)
        self._unscheduled = deepcopy(lectures)
        self._scheduled = []

        # for lecture in self._unscheduled:
        # print(lecture)
        # self.unscheduled.remove(lecture)
        # self.scheduled.append(lecture)
        csv.register_dialect('myDialect',
                             delimiter=',',
                             skipinitialspace=True)

    @staticmethod
    def day_multipliers(days):
        # Day factors determine how priority for the days in assinged
        # Give a higher priority to days in the middle
        # Reduce the priority by 0.5 as we move away from the centre

        # Example the weights for ['mon','tues','wed','thurs','fri'] are [1,1.5,2,1.5,1]
        MAX_WEIGHT = 2
        DIFF_FACTOR = 0.5
        length = len(days)
        weights = [None] * length  # fill the list with nones

        if length % 2:  # if it is odd
            mid = length // 2  # floor due to zero based index
            weights[mid] = MAX_WEIGHT  # arbirary constant for now

            for i in range(0, mid):
                weights[i] = MAX_WEIGHT - (mid - (i)) * DIFF_FACTOR
                weights[-(i + 1)] = weights[i]
        else:
            mid = length // 2
            weights[mid] = MAX_WEIGHT
            weights[mid - 1] = MAX_WEIGHT

            for i in range(0, mid - 1):
                weights[i] = MAX_WEIGHT - (mid - (i + 1)) * DIFF_FACTOR
                weights[-(i + 1)] = weights[i]

        return weights

    @staticmethod
    def period_multipliers(periods):
        # Day factors determine how priority for the days in assinged
        # Give a higher priority to days in the middle
        # Reduce the priority by 0.5 as we move away from the centre
        MAX_WEIGHT = 2
        FORWARD_DIFF_FACTOR = 0.25
        BACKWARD_DIFF_FACTOR = 0.15

        length = len(days)
        weights = [None] * length  # fill the list with nones

        if length % 2:  # if it is odd
            mid = length // 2  # floor due to zero based index
            weights[mid] = MAX_WEIGHT  # arbirary constant for now

            for i in range(0, mid):
                weights[i] = MAX_WEIGHT - (mid - (i)) * BACKWARD_DIFF_FACTOR
                weights[-(i + 1)] = MAX_WEIGHT - (mid - (i)) * FORWARD_DIFF_FACTOR
        else:
            mid = length // 2
            weights[mid] = MAX_WEIGHT
            weights[mid - 1] = MAX_WEIGHT

            for i in range(0, mid - 1):
                weights[i] = MAX_WEIGHT - (mid - (i + 1)) * BACKWARD_DIFF_FACTOR
                weights[-(i + 1)] = MAX_WEIGHT - (mid - (i)) * FORWARD_DIFF_FACTOR

        return weights

    @staticmethod
    def size_diff_multiplier(size_diff):
        MAX_WEIGHT = 2
        DIFF_FACTOR = 0.25

        return MAX_WEIGHT - DIFF_FACTOR * (size_diff // 10)

    # Change both lecture mutlitplier methods to take a diff factor
    @staticmethod
    def section_lectures_multiplier(lectures):
        MAX_WEIGHT = 2
        DIFF_FACTOR = 0.5

        return MAX_WEIGHT - DIFF_FACTOR * (lectures)

    @staticmethod
    def lecturer_lectures_multiplier(lectures):
        MAX_WEIGHT = 2
        DIFF_FACTOR = 0.45

        return MAX_WEIGHT - DIFF_FACTOR * (lectures)

    @staticmethod
    def room_lectures_multiplier(lectures):
        MAX_WEIGHT = 2
        DIFF_FACTOR = 0.25

        return MAX_WEIGHT - DIFF_FACTOR * (lectures // 20)

    @staticmethod
    def day_lectures_multiplier(lectures):
        MAX_WEIGHT = 2
        DIFF_FACTOR = 0.15

        return MAX_WEIGHT - DIFF_FACTOR * (lectures // 20)

    @staticmethod
    def size_diff(lecture, ttslot):
        return (ttslot.room.capacity - lecture.curriculum_item.section.size)

    @property
    def unscheduled(self):
        return self._unscheduled

    @property
    def scheduled(self):
        return self._scheduled

    @property
    def timetable(self):
        return self._timetable

    def generate_timetable(self):
        for lecture in self._unscheduled:
            if self.schedule(lecture):
                self._scheduled.append(lecture)
                print('Scheduled')
                # self._unscheduled.remove(lecture)
            else:
                print('Failed to schedule')
        return self._timetable

    def schedule(self, lecture):
        best_slot = self.best_fit(lecture)
        # print('#### Before ######')
        # print(lecture,best_slot)

        if best_slot:
            # TODO
            # modify add_lecture to merge adjaecent same slots
            if self._timetable.add_lecture(best_slot.day, lecture, best_slot):
                return True
        else:
            # add after swapping
            return self.schedule_via_swap(lecture)

    def schedule_via_swap(self, lecture):
        occupied_slots = self._timetable.occupied_slots()

        # swap method 1. move occupied slot to free slot and lecture to its position
        can_hold = filter(lambda slot: self.can_hold(lecture, slot), occupied_slots)

        # TODO
        # add metric to select the best to move not just the first

        for slot in can_hold:
            best_slot = self.best_fit(slot.lecture)

            if best_slot:  # slot can be move to empty position
                # TODO
                # modify move_lecture to taein a [] of ttslots
                self._timetable.move_lecture(slot, best_slot)
                self._timetable.add_lecture(slot, lecture, False)

                return True

        # if swap method 1 fails use second order swapping
        # move slot that cannot hold lecture to free slot
        # move slot that can hold lecture to its place
        # move lecture to place of slot that can hold lecture

        cannot_hold = filter(lambda slot: not self.can_hold(lecture, slot), occupied_slots)

        for dslot in cannot_hold:
            best_slot = self.best_fit(dslot.lecture)

            if best_slot:  # can be moved to a free slot
                for sslot in can_hold:
                    if self.can_hold(sslot.lecture, dslot):
                        # has a can_hold slot that can take it's place
                        if self._timetable.move_lecture(dslot, best_slot):
                            if self._timetable.move_lecture(sslot, dslot):
                                return True

        return False

    def best_fit(self, lecture):
        free_slots = self._timetable.free_slots()

        # only slots that can hold lecture
        dest_slots = list(filter(lambda slot: self.can_hold(lecture, slot), free_slots))

        # TODO
        # change to get metric for obtaining the best

        if dest_slots:
            # sort the slots according to priority
            dest_slots.sort(key=lambda ttslot: self.priority(lecture, ttslot), reverse=False)
            return dest_slots[-1]  # return the last element on the list i.e the element with the highest
            # priority

        # we require merging slots to obtain a slot
        else:
            for ttslot in free_slots:
                # TODO
                # modify left_neighbours and right_neighbours function
                left = self._timetable.left_free_cont_neighbours(ttslot)  # free contiguous left neighbours of slot
                right = self._timetable.right_free_cont_neighbours(ttslot)

                all_slots = left + [ttslot] + right

                for slt in all_slots:
                    if slt.is_occupied:
                        continue

                total_duration = 0

                # determine if the combined duration of all slots can accomodate lecture
                for lslot in all_slots:
                    total_duration += lslot.time_slot.duration

                if lecture.duration <= total_duration:
                    total_duration = 0

                    dest_slots = []
                    for lslot in all_slots:
                        dest_slots.append(lslot)
                        total_duration += lslot.time_slot.duration
                        if total_duration >= lecture.duration:
                            break

                    # create a new temporary slot to accomodate the combination of slots

                    tslot = TimeSlot(dest_slots[0].time_slot.startstr, dest_slots[-1].time_slot.endstr)
                    tempslot = TimetableSlot(dest_slots[0].day, dest_slots[0].room, tslot)

                    # remove all dest_slots from timetable
                    for slot in dest_slots:
                        self.timetable.remove_slot(slot.day, slot.room, slot.time_slot)
                    # add temp slot to timetable
                    self.timetable.insert_slot(tempslot.day, tempslot)

                    return tempslot

    # duration check is problematic
    # remove checking for duration
    def can_hold(self, lecture, slot):
        # duration checking is problematic
        if slot.can_hold(lecture):  # here
            if self._timetable.section_is_free(slot.day, lecture.curriculum_item.section, slot.time_slot):
                if self._timetable.lecturer_is_free(slot.day, lecture.curriculum_item.lecturer, slot.time_slot):
                    if not self._timetable.c_item_on_day(day, lecture.curriculum_item):
                        return True
        return False

    def priority(self, lecture, ttslot):
        # computers the priority for a timeslot based on a number of different parameters
        # consider the day of the week

        priority = 0

        days = self.timetable.days
        day = days.index(ttslot.day)  # index of day in the week

        day_priority = self.day_multipliers(days)[day] * TimeTableGenerator.WEIGHT_DAY_OF_WEEK

        priority += day_priority

        # consider the period of the day
        # periods in the early half of the day have the highest priority
        # periods in the later half of the day have the second highest
        # followed by periods early in the morning
        # and lastly by periods in evening

        periods = self.timetable.periods(ttslot.day, ttslot.room)
        period = periods.index(ttslot)

        period_priority = self.period_multipliers(periods)[period] * TimeTableGenerator.WEIGHT_PERIOD_OF_DAY

        priority += period_priority

        # consider the difference in size between the classroom and the number of students
        # the larger the difference the lower the priority

        size_diff = self.size_diff(lecture, ttslot)
        size_diff_priority = self.size_diff_multiplier(size_diff) * TimeTableGenerator.WEIGHT_SIZE_OF_CLASSROOM

        priority += size_diff_priority

        # consider the number of lectures that the section(class) has already had for that
        # day. The more the lectures the lower the priority

        section_lectures = self.timetable.section_lectures(lecture.curriculum_item.section, ttslot.day)
        sec_lect_priority = self.section_lectures_multiplier(
            section_lectures) * TimeTableGenerator.WEIGHT_SECTION_LECTURES
        priority += sec_lect_priority

        # consider the number of lectures the lecturer has already had on that day. The more the lectures
        # the lower the priority

        lecturer_lectures = self.timetable.lecturer_lectures(lecture.curriculum_item.lecturer, ttslot.day)
        lecturer_lect_priority = self.lecturer_lectures_multiplier(
            lecturer_lectures) * TimeTableGenerator.WEIGHT_LECTURER_LECTURES
        priority += lecturer_lect_priority

        # consider the number of lectures already scheduled in that classroom on that day vs
        # the number of lectures scheduled in other classrooms on that day
        room_lectures = self.timetable.room_lectures(ttslot.room, ttslot.day)
        room_lect_priority = self.room_lectures_multiplier(room_lectures) * TimeTableGenerator.WEIGHT_OTHER_ROOMS
        priority += room_lect_priority

        # consider the total number of lectures on that day compared to the number of lectures on another
        # day
        day_lectures = self.timetable.day_lectures(ttslot.day)
        day_lect_priority = self.day_lectures_multiplier(day_lectures) * TimeTableGenerator.WEIGHT_LECTURES_ON_DAY
        priority += day_lect_priority
        # future feature
        # consider the proximity between the venue of the previous lecture the class was for and the current
        #
        priority = priority / TimeTableGenerator.TOTAL_WEIGHT
        return priority

    # @unscheduled.setter
    # def _unscheduled(self, value):
    #     self._unscheduled = value
    #
    # @timetable.setter
    # def timetable(self, value):
    #     self._timetable = value
    #
    # @scheduled.setter
    # def _scheduled(self, value):
    #     self._scheduled = value


# if __name__ == '__main__':
#
#
#     # print(json())
#     # print(generator.timetable.timetable)
#     # print(len(generator.scheduled))
#     # print(len(generator.unscheduled))
#     # print(generator.scheduled)
#
# # create a timetable generate a timetable
#
#
# # print the timetable
class Gen:
    # create a timetable to schedule lectures

    timeslots = [
        TimeSlot('8:00', '10:00'),
        TimeSlot('10:00', '12:00'),
        TimeSlot('12:00', '14:00'),
        TimeSlot('14:00', '16:00'),
        TimeSlot('16:00', '18:00')
    ]

    csv.register_dialect('myDialect',
                         delimiter=',',
                         skipinitialspace=True)
    lectures = []
    rooms = []

    # items = FlatTimeTableModel.return_all_raw()
    # for i in items:
    #     lecturer = Lecturer(
    #         i.first_examiner,
    #         None,
    #         i.lecturer_title
    #     )
    #     course = (
    #         i.course_name,
    #         i.department_code,
    #         i.course_code,
    #         i.teaching,
    #         i.practicals,
    #         i.credit,
    #         i.tutorial,
    #     )
    #
    #     section = Section(
    #         i.section_department,
    #         i.year,
    #         None,
    #         i.size,
    #     )
    #     c_item = CurriculumItem(section, course, lecturer)
    #     lecture = Lecture(c_item, 120)
    #     lectures.append(lecture)

    with open('../objects/curriculum.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile, dialect='myDialect')
        for row in reader:
            r = (dict(row))
            lecturer = Lecturer(r['Lecturer name'].strip(), r['Lecturer Id'].strip(), r['Lecturer Title'].strip())
            # lec = LecturerModel()
            # lec.name = lecturer.name
            # lec.stuff_id = r['Lecturer Id'].strip() or None
            # lec.title = r['Lecturer Title'].strip()

            course = Course(r['Course name'].strip(), r['Department code'].strip(), r['Course code'].strip(),
                            r['T'].strip(), r['P'].strip(), r['C'].strip(), r['Tutorial'].strip())
            section = Section(r['Section department'].strip(), r['Year'].strip(), r['Section code'].strip(),
                              int(r['Class size'].strip()))
            # flm = FlatTimeTableModel()
            # flm.course_code = course.course_code,
            c_item = CurriculumItem(section, course, lecturer)
            lecture = Lecture(c_item, 120)
            lectures.append(lecture)

    csvFile.close()
    with open('../objects/rooms.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile, dialect='myDialect')
        for row in reader:
            r = (dict(row))
            room = Classroom(r['Name'].strip(), int(r['Capacity'].strip()), r['Building'].strip(),
                             r['Allowance'].strip())
            rooms.append(room)
    csvFile.close()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day_tables = []

    for day in days:
        day_tables.append(DayTimetable(rooms, timeslots, day))
    timetable = Timetable(days, day_tables)
    # print(timetable)
    # create a list of lectures to be scheduled
    lecturer = Lecturer('Benjamin Kommey', 4564541, 'Mr')
    # course = Course('Opearating Systems','COE 361')

    # section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
    # c_item = CurriculumItem(section,course,lecturer)
    #
    # lecture = Lecture(c_item,60)
    # lectures = [lecture]
    #
    # lecturer = Lecturer('Yao Ming',4564541,'Mr')
    # #course = Course('Control Systems','COE 63')
    #
    # section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
    # #c_item = CurriculumItem(section,course,lecturer)
    #
    # lectures.append(Lecture(c_item,60))
    #
    # lecturer = Lecturer('J Yankey',4564541,'Mr')
    # course = Course('Software Systems','COE 371')
    #
    # section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
    # c_item = CurriculumItem(section,course,lecturer)
    #
    # lectures.append(Lecture(c_item,120))
    #
    # lecturer = Lecturer('Helle Rubie',4564541,'Mr')
    # course = Course('Embedded Systems','COE 381')
    #
    # section = Section('ED CoE',25,3,'Electrical and Electronics Engineering','Computer Engineering')
    # c_item = CurriculumItem(section,course,lecturer)
    #
    # lectures.append(Lecture(c_item,120))

    # create a timetable generator initialized to both

    generator = TimeTableGenerator(timetable, lectures)

    # #print(generator.unscheduled)

    generator.generate_timetable()

    def json(self):
        dicts = []
        days = self.generator.timetable.days
        table = self.generator.timetable.timetable
        for d in days:
            obj = table[d]
            for i in self.rooms:
                for k in obj.table[i]:
                    print(k.lecture)
                    if k.lecture is not None:
                        ci = k.lecture.curriculum_item
                        print(d)
                        print(str(k.room.name))
                        print(str(ci.section.department) + ' ' + str(ci.section.year))
                        print(str(ci.course))
                        print(str(ci.lecturer))
                        dt = dict(
                            day=d,
                            room=str(k.room.name),
                            course=str(ci.course),
                            section=str(ci.section.department) + ' ' + str(ci.section.year),
                            lecturer=str(ci.lecturer),
                            time=str(k.time_slot)

                        )
                        dicts.append(dt)
        return dicts

# if __name__ == '__main__':
#     g = Gen()
#     g.json()