from modules.shared.config.db_sqlite import Session
from modules.study_trail.daos.item.item_dao_alchemy import ItemDAO

def delete_item(query):
    try:
        session = Session()
        
        item_dao = ItemDAO()

        response = item_dao.delete(query.id, session)

        if not response:
            error_msg = "Item de estudo não encontrada!"
            return {"mesage": error_msg}, 404

        success_msg = "Item de estudo removida com sucesso!"
        return {"mesage": success_msg}, 404
            
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível deletar o item de estudo!"

        return {"mesage": error_msg}, 404