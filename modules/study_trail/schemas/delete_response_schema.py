from pydantic import BaseModel


class DeleteResponseSchema(BaseModel):
    """ Define o que é retornado ao deletar um registro.
    """
    mesage: str
