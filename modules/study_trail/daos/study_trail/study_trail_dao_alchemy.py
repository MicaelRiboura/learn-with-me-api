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
    
    def find_all(self, session=Session()):
        study_trails = session.query(StudyTrail).all()
        print('study_trails: ', study_trails)

        study_trails_serialized = []
        if study_trails:
            for study_trail in study_trails:
                study_trails_serialized.append(study_trail.serialize())
        
        print('study_trails_serialized: ', study_trails_serialized)

        return study_trails_serialized
    
    def find_by_title(self, title, session = Session()):
        study_trails = session.query(StudyTrail).filter(StudyTrail.title == title)
        study_trails_serialized = []
        if study_trails:
            for study_trail in study_trails:
                study_trails_serialized.append(study_trail.serialize())
        return study_trails_serialized
    
    def find_by_user(self, user, session = Session()):
        study_trails = session.query(StudyTrail).filter(StudyTrail.user == user)
        study_trails_serialized = []
        if study_trails:
            for study_trail in study_trails:
                study_trails_serialized.append(study_trail.serialize())
        return study_trails_serialized
    
    def find_by_id(self, id, session = Session()):
        study_trail = session.query(StudyTrail).filter(StudyTrail.id == id).first()

        return study_trail
    
    def delete(self, id, session = Session()):
        return