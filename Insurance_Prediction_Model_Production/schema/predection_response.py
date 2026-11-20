
from pydantic import BaseModel , Field
from typing import Dict

#  'predicted_category':predicted_class,
#         'confidence':round(confidence, 4),
#         'class_probablities':class_probs


class PredectionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted insurance premium category",
        examples=['High']
    )
    confidence: float= Field(
        ...,
        description="Model's confidence score for the predicted class (range 0 to 1)",
        examples=[0.8432]
    )
    class_probablities: Dict[str , float] = Field(
        ...,
        description = "Probablity distribution across all possible classes",
        examples=[{"Low": 0.3, "Medium": 0.34, "High": 0.36}]
    )