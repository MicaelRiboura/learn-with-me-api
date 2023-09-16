from pydantic import BaseModel

class GetStudyTrailSchema(BaseModel):
    """ Define o que é necessário ser inserido para ser retornada uma trilha de estudos.
    """
    id:int = 1