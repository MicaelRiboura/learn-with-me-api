from pydantic import BaseModel

class UserSchema(BaseModel):
    """ Define como um usuário deve ser representado
    """

    name:str = "Micael"
    email:str = "micael@gmail.com"
    password:str = "123456"
