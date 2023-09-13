from modules.user.daos.user_dao_alchemy import UserDAO
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO 

from sqlalchemy.exc import IntegrityError

def create_study_trail(form):
    try:
        study_trail_dao = StudyTrailDAO()

        study_trail_response = study_trail_dao.create(form)

        if study_trail_response == None:
            error_msg = "Usuário não encontrado!"
            return {"mesage": error_msg}, 404
        
        return study_trail_response, 200

    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível salvar nova trilha de estudos!"

        return {"mesage": error_msg}, 400