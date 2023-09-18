from ..daos.user_dao_alchemy import UserDAO

def login(form):
    try:
        userDAO = UserDAO()

        user_response = userDAO.find_by_email(form.email)

        if not user_response:
            error_msg = "Login ou senha incorretos!"
            return {"message": error_msg}, 400
        else:
            if user_response['email'] == form.email and user_response['password'] == form.password:
                del user_response['password']
                return user_response, 200
            else:
                error_msg = "Login ou senha incorretos!"
                return {"message": error_msg}, 400
            
    except Exception as e:
        # erro fora do previsto
        print('error: ', e)
        error_msg = "Erro desconhecido"
        return {"message": error_msg}, 404