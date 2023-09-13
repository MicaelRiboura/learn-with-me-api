from pydantic import BaseModel
from typing import Optional
from ..models.study_trail import StudyTrail

class StudyTrailSchema(BaseModel):
    """ Define como uma nova trilha de estudos a ser inserido deve ser representado
    """

    title:str = "JavaScript Básico"
    description:str = "Aprenda os fundamentos da linguagem e seus primeiros projetos."
