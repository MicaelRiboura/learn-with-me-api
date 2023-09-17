from pydantic import BaseModel
from typing import Optional, List
from .item_response_schema import ItemResponseSchema
from modules.user.schemas import UserResponseSchema

class StudyTrailResponseSchema(BaseModel):
    """ Define como uma trilha de estudos deve ser representada
    """
    id:int = 1
    title:str = "JavaScript Básico"
    description:str = "Aprenda os fundamentos da linguagem e seus primeiros projetos."
    items:Optional[List[ItemResponseSchema]]
    user: Optional[UserResponseSchema]