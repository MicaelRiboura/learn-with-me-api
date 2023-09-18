from ..daos.user_dao_alchemy import UserDAO
from sqlalchemy.exc import IntegrityError

def create_user(form):
    try:
        userDAO = UserDAO()

        user = userDAO.create(form)
        
        return user, 200

    except IntegrityError as e:
        error_msg = "Usuário de mesmo e-mail já salvo na base!"
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível salvar novo usuário :/"
        # logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 400