from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from modules.shared.config.model.base import Base
from modules.shared.config.model.serializer import Serializer
from modules.study_trail.models.study_trail import StudyTrail

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    password = Column(String(250))
    study_trails = relationship('StudyTrail')

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


    def add_study_trail(self, study_trail: StudyTrail):
        self.study_trails.append(study_trail)

    def serialize(self):
        user = Serializer.serialize(self)
        del user['password']
        return user