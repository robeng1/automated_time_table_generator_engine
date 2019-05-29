# takes in a list of all curriculum items and an empty timetable
# creates lectures from the curriculum items
# tries to assign all lectures
# assigns lectures till list is empty or till there is no possible means to assign
# left over lectures

# ****************************************************************#


# TODO
# modify add_lecture to take in a [] of slots
# lecture should not already be added to the same day
# lectures
from random import choice


class TimeTableGenerator(object):

    def __init__(self, timetable, lectures=None):
        # validates timetable and lectures

        if lectures is None:
            lectures = []
        lectures.sort(key=lambda lecture: lecture.duration, reverse=True)

        self.timetable = timetable
        self.unscheduled = lectures
        self.scheduled = []

    @property
    def unscheduled(self):
        return self.unscheduled

    @property
    def scheduled(self):
        return self.scheduled

    @property
    def timetable(self):
        return self.timetable

    def generate_timetable(self):
        for lecture in self.unscheduled:
            if self.schedule(lecture):
                self.scheduled.append(lecture)
                self.unscheduled.remove(lecture)
        return self.timetable

    def schedule(self, lecture):
        best_slot = self.best_fit(lecture)

        if best_slot:
            # TODO
            # modify add_lecture to merge adjaecent same slots
            return self.timetable.add_lecture(best_slot)
        else:
            # add after swapping
            return self.schedule_via_swap(lecture)

    def schedule_via_swap(self, lecture):
        occupied_slots = self.timetable.occupied_slots()

        # swap method 1. move occupied slot to free slot and lecture to its position
        can_hold = filter(lambda slot: self.can_hold(lecture, slot), occupied_slots)

        # TODO
        # add metric to select the best to move not just the first

        for slot in can_hold:
            best_slot = self.best_fit(slot.lecture)

            if best_slot:  # slot can be move to empty position
                # TODO
                # modify move_lecture to taein a [] of ttslots
                self.timetable.move_lecture(slot, best_slot)
                self.timetable.add_lecture(slot, lecture, False)

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
                        if self.timetable.move_lecture(dslot, best_slot):
                            if self.timetable.move_lecture(sslot, dslot):
                                return True

        return False

    def best_fit(self, lecture):
        free_slots = self.timetable.free_slots()

        # only slots that can hold lecture
        dest_slots = filter(lambda slot: self.can_hold(lecture, slot), free_slots)

        # TODO
        # change to get metric for obtaining the best

        if dest_slots:
            return [choice(dest_slots)]  # return a list with a single dest slot

        # we require merging slots to obtain a slot
        else:
            for ttslot in free_slots:
                # TODO
                # modify left_neighbours and right_neighbours function
                left = self.timetable.left_neighbours(ttslot)  # free contiguous left neighbours of slot
                right = self.timetable.right_neighbours(ttslot)

                all_slots = left + [ttslot] + right

                total_duration = 0

                # determine if the combined duration of all slots can accomodate lecture
                for lslot in all_slots:
                    total_duration += lslot.time_slot.duration

                if lecture.duration <= total_duration:
                    total_duration = 0

                    dest_slots = []
                    for lslot in all_slots:
                        if total_duration >= lecture.duration:
                            break
                        dest_slots.append(lslot)
                        total_duration += lslot.timetslot.duration

                    return dest_slots

    # duration check is problematic
    # remove checking for duration
    def can_hold(self, lecture, slot):
        # duration checking is problematic
        if slot.can_hold(lecture):  # here
            if self.timetable.section_is_free(lecture.curriculum_item.section, slot):
                if self.timetable.lecturers_are_free(lecture.curriculum_item.lecturers):
                    return True
        return False

    @unscheduled.setter
    def unscheduled(self, value):
        self._unscheduled = value

    @timetable.setter
    def timetable(self, value):
        self._timetable = value

    @scheduled.setter
    def scheduled(self, value):
        self._scheduled = value
