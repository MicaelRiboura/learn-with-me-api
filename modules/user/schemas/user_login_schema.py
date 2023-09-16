from pydantic import BaseModel

class UserLoginSchema(BaseModel):
    """ Define o que deve ser inserido ao realizar o login.
    """
    email: str = "micael@gmail.com"
    password: str = "123456"