from pydantic import BaseModel
from typing import List
from .study_trail_response_schema import StudyTrailResponseSchema

class ListStudyTrailsSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    study_trails:List[StudyTrailResponseSchema]