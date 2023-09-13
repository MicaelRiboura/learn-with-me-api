from abc import ABC, abstractmethod


class AbstractStudyTrailDAO(ABC):
    @abstractmethod
    def create(self, study_trail):
        raise NotImplementedError

    @abstractmethod
    def find_all(self):
        raise NotImplementedError

    @abstractmethod
    def find_by_title(self, title):
        raise NotImplementedError

    @abstractmethod
    def find_by_user(self, user):
        raise NotImplementedError
    
    @abstractmethod
    def find_one(self, id):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError