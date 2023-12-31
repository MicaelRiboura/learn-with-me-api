from modules.shared.config.db_sqlite import Session
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO

def delete_study_trail(query):
    try:
        session = Session()
        
        study_trail_dao = StudyTrailDAO()

        response = study_trail_dao.delete(query.id, session)

        if not response:
            error_msg = "Trilha de estudo não encontrada!"
            return {"message": error_msg}, 404

        success_msg = "Trilha de estudo removida com sucesso!"
        return {"message": success_msg}, 404
            
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível deletar a trilha de estudo!"

        return {"message": error_msg}, 404