from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, joinedload
from app import db
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy.dialects.postgresql import JSONB


class BaseModel(db.Model):
    __abstract__ = True

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        return {'data': list(map(lambda x: x.to_json(), cls.query.all()))}

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
            return {
                'username': x.username,
                'password': x.password
            }

        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

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


class ModuleModel(BaseModel):
    __tablename__ = 'module'
    title = db.Column(db.String(25))
    code = db.Column(db.String(6), primary_key=True)
    teaching = db.Column(db.Integer)
    practicals = db.Column(db.Integer)
    credit = db.Column(db.Integer)
    first_examiner = db.Column(db.String(60))
    second_examiner = db.Column(db.String(60))
    department = db.Column(db.String(30))
    year = db.Column(db.String(4))
    sections = relationship('SectionModel', back_populates='module')

    def to_json(self):
        json_module = {
            'title': self.title,
            'code': self.code,
            'teaching': self.teaching,
            'practicals': self.practicals,
            'credit': self.credit,
            'first_examiner': self.first_examiner,
            'second_examiner': self.second_examiner,
            'department': self.department,
            'year': self.year
        }
        return json_module

    @classmethod
    def find_module_by_course_code(cls, code):
        return cls.query.filter_by(code=code).first()

    @classmethod
    def return_for_gen(cls):
        return cls.query.options(joinedload('sections')).all()


class SectionModel(BaseModel):
    __tablename__ = 'section'
    klass = db.Column(db.String(50), primary_key=True)
    code = db.Column(db.String(5), ForeignKey('module.code'))
    shared = db.Column(db.BOOLEAN, default=False)
    module = relationship('ModuleModel', back_populates="sections")

    def to_json(self):
        json_model = {
            'class': self.klass,
            'code': self.code,
            'shared': self.shared,
        }
        return json_model

    @classmethod
    def find_by_klass(cls, kls):
        return cls.query.filter_by(klass=kls)


class ClassRoomModel(BaseModel):
    name = db.Column(db.String(10), primary_key=True)
    capacity = db.Column(db.Integer)
    location = db.Column(JSONB)

    def to_json(self):
        json_model = {
            'name': self.name,
            'capacity': self.capacity,
            'location': self.location,
        }
        return json_model

    @classmethod
    def find_room(cls, name ):
        return cls.query.filter_by(name=name).first()
