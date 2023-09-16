from pydantic import BaseModel

class StudyTrailSchema(BaseModel):
    """ Define como uma nova trilha de estudos a ser inserida deve ser representado
    """

    title:str = "JavaScript Básico"
    description:str = "Aprenda os fundamentos da linguagem e seus primeiros projetos."
