from sqlalchemy import Column, String, Integer, ForeignKey
from modules.shared.config.model.base import Base
from modules.shared.config.model.serializer import Serializer

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    type = Column(String(250))
    description = Column(String(500))
    resource = Column(String(500))
    study_trail = Column(Integer, ForeignKey('study_trail.id'), nullable=False)

    def __init__(self, title: str, type: str, description: str, resource: str):
        self.title = title
        self.type = type
        self.description = description
        self.resource = resource

    def serialize(self):
        item = Serializer.serialize(self)
        return item