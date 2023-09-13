from pydantic import BaseModel

class CreateStudyTrailSchema(BaseModel):
    """ Define como uma nova trilha de estudos de um usuário a ser inserida deve ser representada
    """

    title:str = "JavaScript Básico"
    description:str = "Aprenda os fundamentos da linguagem e seus primeiros projetos."
    user_id:int = 1
