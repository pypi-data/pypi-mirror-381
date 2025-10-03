from typing import Any, Dict, Optional, TypedDict

class PredictResponse(TypedDict, total=False):
    score: float
    # classification only:
    class_: str  # we’ll remap "class" -> "class_"
    proba: list[float]
    # metadata from server (optional):
    model_id: str
    model_name: str
    version: int
    task_type: str