from pydantic import BaseModel

class DeleteItemSchema(BaseModel):
    """ Define o que é necessário ser inserido para ser removido um item na trilha de estudos.
    """
    id:int = 1