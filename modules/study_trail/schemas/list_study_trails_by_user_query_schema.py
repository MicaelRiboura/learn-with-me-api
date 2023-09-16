from pydantic import BaseModel

class ListStudyTrailsByUserQuerySchema(BaseModel):
    """ Define o que é necessário ser inserido para ser retornado a lista de trilhas de estudos por usuário.
    """
    user_id:int = 1