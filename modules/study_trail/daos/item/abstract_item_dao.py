from abc import ABC, abstractmethod


class AbstractItemDAO(ABC):
    @abstractmethod
    def create(self, form, study_trail, session):
        raise NotImplementedError

    @abstractmethod
    def find_by_study_trail(self, study_trail):
        raise NotImplementedError
    
    @abstractmethod
    def find_one(self, id):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError