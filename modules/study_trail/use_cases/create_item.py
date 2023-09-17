from modules.shared.config.db_sqlite import Session
from modules.study_trail.daos.study_trail.study_trail_dao_alchemy import StudyTrailDAO
from modules.study_trail.daos.item.item_dao_alchemy import ItemDAO

def create_item(form):
    try:
        session = Session()

        study_trail_dao = StudyTrailDAO()

        study_trail = study_trail_dao.find_by_id(form.study_trail_id, session)

        if not study_trail:
            error_msg = "Trilha de estudo não encontrada!"
            return {"message": error_msg}, 404
        
        item_dao = ItemDAO()

        item_response = item_dao.create(form, study_trail, session)
        
        return item_response, 200

    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível salvar novo item na trilha de estudos!"

        return {"message": error_msg}, 400