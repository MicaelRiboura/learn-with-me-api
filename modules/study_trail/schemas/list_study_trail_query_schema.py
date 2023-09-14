from pydantic import BaseModel
from typing import Optional
from .study_trail_response_schema import StudyTrailResponseSchema

class ListStudyTrailsQuerySchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    title:Optional[str] = "JavaScript Básico"