from pydantic import BaseModel

class ListStudyTrailsByUserQuerySchema(BaseModel):
    """ Define o que deve ser inserido para mostrar a lista de trilhas de estudo .
    """
    user_id:int = 1