from app.models import CourseModel
from objects.data import CurriculumItem, Curriculum
from objects.lecture import Lecture


class DataGenerator:
    def __init__(self, data=None):

        # eagerly loads sections related to each module
        # might be slow to set up but err tin will be in memory
        if data is None:
            self.modules = CourseModel.return_all_raw()
        else:
            self.modules = data

    # private helpers for setting up data
    def _setup_curricula_items(self):
        if self.modules is not None:
            return [CurriculumItem(
                section=item.sections,
                lecturer=[item.first_examiner, item.second_examiner],
                course=item.code
            ) for item in self.modules]

    def _setup_curriculum(self):
        return Curriculum(self._setup_curricula_items())

    def _splits(self):
        splits = []
        for item in self.modules:
            # since the sections is a list
            # we just check the the first item and determines if it is a combined class
            # check only index zero cuz it's guaranteed to be present
            if item.sections[0].shared:
                while item.credit > 2:
                    splits.append((CurriculumItem(
                        section=item.sections,
                        lecturer=[item.first_examiner, item.second_examiner],
                        course=item.code
                    ), 2))
                    item.credit -= 2
                if item.credit > 0:
                    splits.append((CurriculumItem(
                        section=item.sections,
                        lecturer=[item.first_examiner, item.second_examiner],
                        course=item.code
                    ), item.credit))
            else:
                # here the class is not a combined class
                if len(item.sections) > 1:
                    while item.credit > 2:
                        for i in item.sections:
                            splits.append((CurriculumItem(
                                section=i,
                                lecturer=[item.first_examiner, item.second_examiner],
                                course=item.code
                            ), 2))
                        item.credit -= 2
                    if item.credit > 0:
                        for i in item.sections:
                            splits.append((CurriculumItem(
                                section=i,
                                lecturer=[item.first_examiner, item.second_examiner],
                                course=item.code
                            ), item.credit))
        if len(splits) != 0:
            return splits

    @property
    def lectures(self):
        tuples = self._splits()
        return [Lecture(c_item=i[0], duration=i[1]) for i in tuples]
