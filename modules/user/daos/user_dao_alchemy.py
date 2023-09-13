from .abstract_user_dao import AbstractUserDAO
from modules.user.models import User
from modules.shared.config.db_sqlite import Session
from modules.shared.config.model.serializer import Serializer

class UserDAO(AbstractUserDAO):
    def create(self, form):
        user = User(
            name=form.name,
            email=form.email, 
            password=form.password
        )

        session = Session()
        
        session.add(user)
        session.commit()

        return user.serialize()
    
    def find_by_email(self, email):
        session = Session()

        user = session.query(User).filter(User.email == email).first()

        if not user:
            return None

        user_serialized = user.serialize()

        return user_serialized

    def find_by_id(self, id, session=Session()):
        user = session.query(User).filter(User.id == id).first()

        return user