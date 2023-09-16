from pydantic import BaseModel

class CreateItemSchema(BaseModel):
    """ Define como um item de uma trilha de estudos a ser inserido deve ser representado
    """

    title:str = "Como fazer o primeiro Hello World"
    description:str = "Aprenda o comando inicial para qualquer linguagem de programação para começar com o pé direito."
    type:str = "video"
    resource:str = "https://youtu.be/HdunotFeGas?si=BP6HZvGWG-wrEvG7"
    study_trail_id:int = 1
