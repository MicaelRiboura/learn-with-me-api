from pydantic import BaseModel
from typing import List
from modules.study_trail.schemas import StudyTrailSchema

class UserResponseSchema(BaseModel):
    """ Define como um usuário será retornado: usuário com suas trilhas de estudo.
    """
    id: int = 1
    name: str = "User"
    email: str = "user@gmail.com"
    study_trails:List[StudyTrailSchema]