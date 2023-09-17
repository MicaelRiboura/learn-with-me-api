
from modules.shared.config.db_sqlite import Session
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO

def list_study_trails(query):

    try:
        session = Session()

        study_trail_dao = StudyTrailDAO()

        if query.title and query.title != '':
            study_trails_response = study_trail_dao.find_by_title(title=query.title, session=session)
        else:
            study_trails_response = study_trail_dao.find_all(session=session)

        return {'study_trails': study_trails_response }, 200
    
    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível listar as trilha de estudos!"

        return {"message": error_msg}, 404