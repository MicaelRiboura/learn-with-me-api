from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from modules.shared.config.model.base import Base
from modules.shared.config.model.serializer import Serializer
from modules.study_trail.models.study_trail import StudyTrail

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250), unique=True)
    password = Column(String(250))
    study_trails = relationship('StudyTrail')

    def __init__(self, name:str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


    def add_study_trail(self, study_trail: StudyTrail):
        self.study_trails.append(study_trail)

    def serialize(self, has_items=False):
        user = Serializer.serialize(self)
        user['study_trails'] = Serializer.serialize_list(user['study_trails'])

        if not has_items:
            for study_trail in user['study_trails']:
                del study_trail['items']
        else:
            for study_trail in user['study_trails']:
                study_trail['items'] = Serializer.serialize_list(study_trail['items'])

        return user