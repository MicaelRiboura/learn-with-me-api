from pydantic import BaseModel

class CreateStudyTrailResponseSchema(BaseModel):
    """ Define como uma nova trilha de estudos deve ser representada
    """
    id:int = 1
    title:str = "JavaScript Básico"
    description:str = "Aprenda os fundamentos da linguagem e seus primeiros projetos."