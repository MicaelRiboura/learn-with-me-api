from abc import ABC, abstractmethod


class AbstractItemDAO(ABC):
    @abstractmethod
    def create(self, form, study_trail, session):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError