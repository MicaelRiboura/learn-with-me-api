from modules.shared.config.db_sqlite import Session
from modules.user.daos.user_dao_alchemy import UserDAO
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO

def get_study_trail(query):
    try:
        session = Session()
        
        user_dao = UserDAO()
        study_trail_dao = StudyTrailDAO()

        study_trail = study_trail_dao.find_by_id(query.id, session)

        if not study_trail:
            error_msg = "Trilha de estudo não encontrada!"
            return {"message": error_msg}, 404

        study_trail_serialized = study_trail.serialize()
        study_trail_serialized['user'] = user_dao.find_by_id(study_trail_serialized['user'], session).serialize()
        del study_trail_serialized['user']['study_trails']
        
        return study_trail_serialized, 200
            
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível listar as trilha de estudos!"

        return {"message": error_msg}, 404