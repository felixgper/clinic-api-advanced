from pydantic import BaseModel

class Appointments(BaseModel):
    appointment_id: int
    patient_id: int
    doctor_id: int
    date: str