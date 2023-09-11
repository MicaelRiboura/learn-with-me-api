from ..daos.user_dao_alchemy import UserDAO

def create_user(form):
    try:
        userDAO = UserDAO()

        user = userDAO.create(form)
        print('response: ', user)
        return user, 200

    except IntegrityError as e:
        error_msg = "Usuário de mesmo e-mail já salvo na base!"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível salvar novo usuário :/"
        # logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400