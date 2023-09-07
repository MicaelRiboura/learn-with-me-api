from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modules.shared.config.model.base import Base
from modules.study_trail.models.item import Item

class StudyTrail(Base):
    __tablename__ = 'study_trail'

    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    description = Column(String(500))
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    itens = relationship('Item')

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


    def add_item(self, item: Item):
        self.itens.append(item)