from pydantic import BaseModel

class Patients(BaseModel):
    id: int
    name: str
    age: int
    dni: str
    active: bool