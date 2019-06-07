from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, joinedload, backref
from app import db
from passlib.hash import pbkdf2_sha256 as sha256


class BaseModel(db.Model):
    __abstract__ = True

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        return list(map(lambda x: x.to_json(), cls.query.all()))

    @classmethod
    def return_all_raw(cls):
        return cls.query.all()


class UserModel(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return dict(username=x.username, password=x.password)

        return dict(users=list(map(lambda x: to_json(x), UserModel.query.all())))

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except IOError:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)


class ClassRoomGroupModel(BaseModel):
    __tablename__ = 'roomgroup'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    rooms = relationship(
        'ClassRoomModel',
        # Use cascade='delete,all' to propagate the deletion of a group onto its rooms
        backref=backref('roomgroup', uselist=True, cascade='delete, all'),
    )

    def to_json(self):
        model = dict(id=self.id, groupName=self.name, rooms=list(map(lambda x: x.to_json(), self.rooms)))
        return model

    @classmethod
    def find_by_name(cls, name):
        result = cls.query.filter_by(name=name).first()
        return result.to_json()


class ClassRoomModel(BaseModel):
    __tablename__ = 'classroom'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    capacity = db.Column(db.Integer)
    location = db.Column(db.String(50))
    allowance = db.Column(db.Integer)
    group = db.Column(db.Integer, ForeignKey('roomgroup.id'))

    def to_json(self):
        json_model = dict(
            id=self.id,
            name=self.name,
            capacity=self.capacity,
            location=self.location,
            allowance=self.allowance,
            groupName=self.group.name,
        )
        return json_model

    @classmethod
    def find_room(cls, name):
        return cls.query.filter_by(name=name).first()


class DepartmentModel(BaseModel):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    name = db.Column(db.String(50), unique=True)
    lecturers = relationship(
        'LecturerModel',
        # Use cascade='delete,all' to propagate the deletion of a group onto its rooms
        backref=backref('lecturer', uselist=True, cascade='delete, all'),
    )
    courses = relationship(
        'CourseModel',
        backref=backref('course', uselist=True, cascade='delete, all'),
    )
    sections = relationship(
        'SectionModel',
        backref=backref('section', uselist=True, cascade='delete, all'),
    )

    def to_json(self):
        model = dict(
            id=self.id,
            name=self.name,
            code=self.code,
            lecturers=list(map(lambda x: x.to_json(), self.lecturers)),
            courses=list(map(lambda x: x.to_json(), self.courses)),
            sections=list(map(lambda x: x.to_json(), self.sections))
        )
        return model

    @classmethod
    def find_department(cls, code):
        return cls.query.filter_by(name=code).first()

    @classmethod
    def find_department_cc(cls, code):
        return cls.query.filter_by(code=code).first()


class LecturerModel(BaseModel):
    __tablename__ = 'lecturer'
    id = db.Column(db.Integer, primary_key=True)
    stuff_id = db.Column(db.Integer, unique=True)
    title = db.Column(db.String(10))
    name = db.Column(db.String(50))
    department = db.Column(db.Integer, ForeignKey('department.id'))
    email = db.Column(db.String(30), unique=True)
    office = db.Column(db.String(20))

    def to_json(self):
        model = dict(
            id=self.id,
            stuff_id=self.stuff_id,
            title=self.title,
            name=self.name,
            department=self.department,
            email=self.email,
            office=self.office,
        )
        return model

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(ID=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


class CourseModel(BaseModel):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department_code = db.Column(db.String(10))
    code = db.Column(db.String(6))
    teaching = db.Column(db.Integer)
    practicals = db.Column(db.Integer)
    credit = db.Column(db.Integer)
    tutorial = db.Column(db.Integer, default=0)
    first_examiner = db.Column(db.String(60))
    second_examiner = db.Column(db.String(60), default="")
    year = db.Column(db.Integer)
    department = db.Column(db.Integer, ForeignKey('department.id'))
    sections = relationship(
        'SectionModel',
        secondary='section_course_link',
    )

    __table_args = (
        db.UniqueConstraint(name, department_code, year)
    )

    def to_json(self):
        json_module = dict(
            id=self.id,
            name=self.name,
            dept_code=self.department_code,
            code=self.code,
            teaching=self.teaching,
            practicals=self.practicals,
            credit=self.credit,
            tutorial=self.tutorial,
            first_examiner=self.first_examiner,
            second_examiner=self.second_examiner,
            department=self.department,
            year=self.year,
            sections=list(map(lambda x: x.to_json(), self.sections)),
        )
        return json_module

    @classmethod
    def find_module_by_course_code(cls, code):
        return cls.query.filter_by(code=code).first()

    @classmethod
    def find_cons(cls, name, code, year):
        return cls.query.filter_by(name=name, department_code=code, year=year)

    @classmethod
    def return_for_gen(cls):
        return cls.query.options(joinedload('sections')).all()


class SectionModel(BaseModel):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    department = db.Column(db.Integer, ForeignKey('department.id'))
    year = db.Column(db.Integer)
    size = db.Column(db.Integer)
    courses = relationship('CourseModel', secondary='section_course_link')

    __table_args__ = (
        db.UniqueConstraint(name, year),
    )

    def to_json(self):
        return dict(
            ID=self.id,
            name=self.name,
            size=self.size,
            year=self.year,
            department=self.department,
            courses=list(map(lambda x: x.to_json(), self.courses)),
        )

    @classmethod
    def find_by_name(cls, kls):
        return cls.query.filter_by(name=kls)


class SectionCourseThroughModel(db.Model):
    __tablename__ = 'section_course_link'
    course_id = db.Column(db.Integer, ForeignKey('course.id'), primary_key=True)
    section_id = db.Column(db.Integer, ForeignKey('section.id'), primary_key=True)


class FlatTimeTableModel(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String)
    department_code = db.Column(db.String)
    course_code = db.Column(db.Integer)
    teaching = db.Column(db.Integer)
    practicals = db.Column(db.Integer)
    credit = db.Column(db.Integer)
    tutorial = db.Column(db.Integer, default=0)
    first_examiner = db.Column(db.String(60))
    lecturer_title = db.Column(db.String(5))
    year = db.Column(db.Integer)
    section_department = db.Column(db.String)
    size = db.Column(db.Integer)

    def to_json(self):
        json_module = dict(
            id=self.id,
            course_name=self.course_name,
            department_code=self.department_code,
            course_code=self.course_code,
            teaching=self.teaching,
            practicals=self.practicals,
            credit=self.credit,
            tutorial=self.tutorial,
            first_examiner=self.first_examiner,
            lecturer_title=self.lecturer_title,
            section_department=self.section_department,
            year=self.year,
            size=self.size
        )
        return json_module
