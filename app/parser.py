from flask_restful import reqparse

module_parser = reqparse.RequestParser()
module_parser.add_argument(
    'name',
    type=str,
    required=True,
    help="Name is required"

)

module_parser.add_argument(
    'code',
    type=str,
    required=True,
    help="Code is required"

)
module_parser.add_argument(
    'teaching',
    type=int,
    required=True,
    help="Teaching is required"
)

module_parser.add_argument(
    'practicals',
    type=int,
    required=True,
    help="Practicals is required"
)
module_parser.add_argument(
    'credit',
    type=int,
    required=True,
    help="Credit hours is required"
)

module_parser.add_argument(
    'first_examiner',
    type=str,
    required=True,
    help="Credit hours is required"
)

module_parser.add_argument(
    'second_examiner',
    type=str,
    required=False,
    help="Fallback examiner in case the first examiner is unavailable"
)

section_parser = reqparse.RequestParser()
section_parser.add_argument(
    'klass',
    type=str,
    required=True,
    help="the class for this course"
)

section_parser.add_argument(
    'code',
    type=str,
    required=True,
    help="course code for this section"
)

section_parser.add_argument(
    'shared',
    type=bool,
    required=False,
    help="set this to indicate that this is a shared a course, defaults to false"
)

classroom_parser=reqparse.RequestParser()
classroom_parser.add_argument(
    'name',
    type=str,
    required=True,
    help="name of the classroom"
)

classroom_parser.add_argument(
    'capacity',
    type=int,
    required=True,
    help="number of people classroom can contain"
)

classroom_parser.add_argument(
    'location',
    type=str,
    required=True

)
classroom_parser.add_argument(
    'allowance',
    type=int,
    required=True
)

classroom_parser.add_argument(
    'group_name',
    type=str,
    required=True
)

classroom_group_parser=reqparse.RequestParser()
classroom_group_parser.add_argument(
    'name',
    type=str,
    required=True
)

department_parser = reqparse.RequestParser()
department_parser.add_argument(
    'name',
    type=str,
    required=True,
)

lecturer_parser = reqparse.RequestParser()
lecturer_parser.add_argument(
    'title',
    type=str,
    required=True
)

lecturer_parser.add_argument(
    'name',
    type=str,
    required=True
)

lecturer_parser.add_argument(
    'id',
    type=int,
    required=True
)

lecturer_parser.add_argument(
    'office',
    type=str,
    required=True
)

lecturer_parser.add_argument(
    'email',
    type=str,
    required=True
)

lecturer_parser.add_argument(
    'department',
    type=str,
    required=True
)
