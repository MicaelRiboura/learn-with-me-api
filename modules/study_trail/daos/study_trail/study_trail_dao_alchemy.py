from modules.shared.config.db_sqlite import Session
from modules.user.models import User
from modules.study_trail.models import StudyTrail
from .abstract_study_trail_dao import AbstractStudyTrailDAO

class StudyTrailDAO(AbstractStudyTrailDAO):
    def create(self, form):
        session = Session()

        user = session.query(User).filter(User.id == form.user_id).first()
        
        if not user:
            return None
        
        study_trail = StudyTrail(
            title=form.title,
            description=form.description,
        )
    
        user.add_study_trail(study_trail)
        session.commit()

        user_serialized = user.serialize(has_items=True)

        return user_serialized['study_trails'][len(user_serialized['study_trails']) - 1]
    
    def find_all(self):
        return
    
    def find_by_title(self, title):
        return
    
    def find_by_user(self, user):
        return
    
    def find_one(self, id):
        return
    
    def delete(self, id):
        return