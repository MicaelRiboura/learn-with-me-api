from pydantic import BaseModel

class GetStudyTrailSchema(BaseModel):
    """ Define o que é necessário ser inserido para ser retornada uma Trilha de Estudos.
    """
    id:int = 1