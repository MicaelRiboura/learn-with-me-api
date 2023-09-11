from pydantic import BaseModel
from typing import Optional, List
from ..models import User
from modules.study_trail.schemas import StudyTrailSchema

class UserResponseSchema(BaseModel):
    """ Define como um usuário será retornado: usuário + trilhas de estudo.
    """
    id: int = 1
    name: str = "User"
    email: str = "user@gmail.com"
    password: str = "123456"
    study_trails:List[StudyTrailSchema]