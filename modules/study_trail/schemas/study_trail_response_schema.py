from pydantic import BaseModel
from typing import List
from .item_response_schema import ItemResponseSchema

class StudyTrailResponseSchema(BaseModel):
    """ Define como uma nova trilha de estudos deve ser representada
    """
    id:int = 1
    title:str = "JavaScript Básico"
    description:str = "Aprenda os fundamentos da linguagem e seus primeiros projetos."
    items:List[ItemResponseSchema]