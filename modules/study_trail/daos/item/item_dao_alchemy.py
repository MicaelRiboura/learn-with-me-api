from modules.shared.config.db_sqlite import Session
from modules.study_trail.models import Item
from .abstract_item_dao import AbstractItemDAO

class ItemDAO(AbstractItemDAO):
    def create(self, form, study_trail, session = Session()):
        item = Item(
            title=form.title,
            type=form.type,
            description=form.description,
            resource=form.resource,
        )
    
        study_trail.add_item(item)
        session.commit()

        study_trail_serialized = study_trail.serialize()

        return study_trail_serialized['items'][len(study_trail_serialized['items']) - 1]
    
    def delete(self, id, session=Session()):
        count = session.query(Item).filter(Item.id == id).delete()
        session.commit()
        
        if not count:
            return False
        
        return True