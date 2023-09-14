from pydantic import BaseModel

class ItemResponseSchema(BaseModel):
    """ Define como um Item de Estudo será retornado.
    """
    id:int = 1
    title:str = "Como fazer o primeiro Hello World"
    description:str = "Aprenda o comando inicial para qualquer linguagem de programação para começar com o pé direito."
    type:str = "video"
    resource:str = "https://youtu.be/HdunotFeGas?si=BP6HZvGWG-wrEvG7"