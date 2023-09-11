from abc import ABC, abstractmethod


class AbstractUserDAO(ABC):
    @abstractmethod
    def create(self, study_trail):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, id):
        raise NotImplementedError