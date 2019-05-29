from flask_restful import reqparse

moduleParser = reqparse.RequestParser()
moduleParser.add_argument(
    'name',
    type=str,
    required=True,
    help="Name is required"

)

moduleParser.add_argument(
    'code',
    type=str,
    required=True,
    help="Code is required"

)
moduleParser.add_argument(
    'teaching',
    type=int,
    required=True,
    help="Teaching is required"
)

moduleParser.add_argument(
    'practicals',
    type=int,
    required=True,
    help="Practicals is required"
)
moduleParser.add_argument(
    'credit',
    type=int,
    required=True,
    help="Credit hours is required"
)

moduleParser.add_argument(
    'first_examiner',
    type=str,
    required=True,
    help="Credit hours is required"
)

moduleParser.add_argument(
    'second_examiner',
    type=str,
    required=False,
    help="Fallback examiner in case the first examiner is unavailable"
)

sectionParser = reqparse.RequestParser()
sectionParser.add_argument(
    'klass',
    type=str,
    required=True,
    help="the class for this course"
)

sectionParser.add_argument(
    'code',
    type=str,
    required=True,
    help="course code for this section"
)

sectionParser.add_argument(
    'shared',
    type=bool,
    required=False,
    help="set this to indicate that this is a shared a course, defaults to false"
)
