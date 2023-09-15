from modules.shared.config.db_sqlite import Session
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO

def get_study_trail(query):
    try:
        session = Session()
        
        study_trail_dao = StudyTrailDAO()

        study_trail = study_trail_dao.find_by_id(query.id, session)

        if not study_trail:
            error_msg = "Trilha de estudo não encontrada!"
            return {"mesage": error_msg}, 404

        return study_trail.serialize(), 200
            
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível listar as trilha de estudos!"

        return {"mesage": error_msg}, 404