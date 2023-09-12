from pydantic import BaseModel

class UserLoginSchema(BaseModel):
    """ Define como deve ser a estrutura que representa o login.
    """
    email: str = "micael@gmail.com"
    password: str = "123456"