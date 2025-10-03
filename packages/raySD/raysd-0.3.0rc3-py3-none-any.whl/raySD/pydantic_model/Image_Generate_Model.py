from pydantic import BaseModel, model_validator
from typing import List, Dict, Any, Optional

class ImageGenerateModel(BaseModel):
    image: bytes = None
    gender: int = -1
    age: int = 0

# class ImageGenerateModel(BaseModel):
#     image: str = ""
#     gender: int = -1
#     age: int = 0

class ImageGenerateModelV2(BaseModel):
    image: bytes = None
    gender: int = -1
    age: int = 0
    image_name: str = ""