from pydantic import BaseModel

class Doctors(BaseModel):
    id: int
    name: str
    specialty: str
    active: bool