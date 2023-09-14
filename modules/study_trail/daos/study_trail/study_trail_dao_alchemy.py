from modules.shared.config.db_sqlite import Session
from modules.study_trail.models import StudyTrail
from .abstract_study_trail_dao import AbstractStudyTrailDAO

class StudyTrailDAO(AbstractStudyTrailDAO):
    def create(self, form, user, session = Session()):
        study_trail = StudyTrail(
            title=form.title,
            description=form.description,
        )
    
        user.add_study_trail(study_trail)
        session.commit()

        user_serialized = user.serialize()

        return user_serialized['study_trails'][len(user_serialized['study_trails']) - 1]
    
    def find_all(self):
        return
    
    def find_by_title(self, title):
        return
    
    def find_by_user(self, user):
        return
    
    def find_by_id(self, id, session):
        study_trail = session.query(StudyTrail).filter(StudyTrail.id == id).first()

        return study_trail
    
    def delete(self, id):
        return