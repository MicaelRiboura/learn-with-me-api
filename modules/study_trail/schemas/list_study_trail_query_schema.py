from pydantic import BaseModel
from typing import Optional

class ListStudyTrailsQuerySchema(BaseModel):
    """ Define o que é necessário ser inserido para ser retornado a lista de trilhas de estudos.
    """
    title:Optional[str] = "JavaScript Básico"