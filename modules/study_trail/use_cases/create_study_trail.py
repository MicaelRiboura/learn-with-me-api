from modules.shared.config.db_sqlite import Session
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO 
from modules.user.daos.user_dao_alchemy import UserDAO 

def create_study_trail(form):
    try:
        session = Session()

        user_dao = UserDAO()

        user = user_dao.find_by_id(form.user_id, session)

        if not user:
            error_msg = "Usuário não encontrado!"
            return {"mesage": error_msg}, 404
        
        study_trail_dao = StudyTrailDAO()

        study_trail_response = study_trail_dao.create(form, user, session)
        
        return study_trail_response, 200

    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível salvar nova trilha de estudos!"

        return {"mesage": error_msg}, 400