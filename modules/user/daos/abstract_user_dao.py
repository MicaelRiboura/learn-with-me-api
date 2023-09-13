from abc import ABC, abstractmethod


class AbstractUserDAO(ABC):
    @abstractmethod
    def create(self, study_trail):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, email):
        raise NotImplementedError