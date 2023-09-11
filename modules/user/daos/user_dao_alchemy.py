from .abstract_user_dao import AbstractUserDAO
from modules.user.models import User
from modules.shared.config.db_sqlite import Session

class UserDAO(AbstractUserDAO):
    def create(self, form):
        user = User(
            email=form.email, 
            password=form.password
        )

        session = Session()
        
        session.add(user)
        session.commit()

        return user.serialize()
    
    def find_by_id(self, id):
        return