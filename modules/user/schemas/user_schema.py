from pydantic import BaseModel
from typing import Optional
from ..models import User

class UserSchema(BaseModel):
    """ Define como uma nova trilha de estudos a ser inserido deve ser representado
    """

    email:str = "micael@gmail.com"
    password:str = "123456"
