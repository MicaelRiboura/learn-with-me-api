from modules.shared.config.db_sqlite import Session
from modules.user.daos.user_dao_alchemy import UserDAO
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO

def list_study_trails_by_user(query):
    try:
        session = Session()

        user_dao = UserDAO()
        study_trail_dao = StudyTrailDAO()

        user = user_dao.find_by_id(query.user_id, session)

        if not user:
            error_msg = "Usuário não encontrado!"
            return {"mesage": error_msg}, 404

        study_trails_response = study_trail_dao.find_by_user(user.id, session)

        return { 'study_trails': study_trails_response }, 200
        
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível listar as trilha de estudos!"

        return {"mesage": error_msg}, 404