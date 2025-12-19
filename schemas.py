from pydantic import BaseModel

class CropRequest(BaseModel):
    state : str
    district:str
    N:float
    P:float
    K:float
    pH:float
class ModelRequest(BaseModel):
    N:float
    P:float
    K:float
    temperature: int
    humidity: int
    pH:float
    rainfall:float
class GPTRequest(BaseModel):
    State:int
    District:int