from ..daos.user_dao_alchemy import UserDAO

def login(form):
    try:
        userDAO = UserDAO()

        user = userDAO.find_by_email(form.email)

        print('user: ', user)

        if not user:
            error_msg = "Login ou senha incorretos!"
            return {"mesage": error_msg}, 400
        else:
            if user.email == form.email and user.password == form.password:
                return user.serialize(), 200
            else:
                error_msg = "Login ou senha incorretos!"
                return {"mesage": error_msg}, 400
            
    except Exception as e:
        # erro fora do previsto
        print('error: ', e)
        error_msg = "Erro desconhecido"
        return {"mesage": error_msg}, 500