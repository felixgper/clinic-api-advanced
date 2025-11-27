from models.appointments import Appointments
from models.doctors import Doctors
from models.patients import Patients
from routers import doctors, patients
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix= "/appointments",
                   tags= ["appointments"],
                   responses= {404: {"message" : "NO ENCONTRADO"}})

list_appointments = []

@router.get("/")
async def get_appointments():
    if not list_appointments:
        raise HTTPException(status_code= 404, detail= "CITA NO ENCONTRADA")
    return list_appointments

@router.get("/{appointment_id}")
async def get_appintments(appointment_id : int):
    if search_id(appointment_id) is None:
        raise HTTPException(status_code= 404, detail= "NO SE ENCONTRO ID")
    return search_id(appointment_id)

@router.post("/")
async def post_appointments(appointment : Appointments):
    
    #Verificamos que el doctor exista
    doctor_exists = None
    
    for doctor in doctors.list_doctors:
        if appointment.doctor_id == doctor.id:
            doctor_exists = doctor
            break
        
    if not doctor_exists:
        raise HTTPException(status_code= 404, detail= "DOCTOR NO EXISTE")
    
    #Verificamos que el paciente exista
    patient_exists = None
    
    for patient in patients.list_patients:
        if appointment.patient_id == patient.id:
            patient_exists = patient
            break
        
    if not patient_exists:
        raise HTTPException(status_code= 404, detail= "NO EXISTE PACIENTE")
    
    if not doctor_exists.active or not patient_exists.active:
        raise HTTPException(status_code=409, detail="PACIENTE O DOCTOR INACTIVO")
    
    for appo in list_appointments:
        if appo.patient_id == appointment.patient_id and appo.date == appointment.date:
            raise HTTPException(status_code=409, detail="EL PACIENTE YA TIENE UNA CITA EN ESA FECHA")

    for app in list_appointments:
        if app.doctor_id == appointment.doctor_id and app.date == appointment.date:
            raise HTTPException(status_code=409, detail="EL DOCTOR YA TIENE UNA CITA EN ESA FECHA")
    
    # 6. Registrar la cita
    list_appointments.append(appointment)
    return {
        "message": "Cita registrada",
        "patient": patient_exists,
        "doctor": doctor_exists,
        "appointment": appointment
    }



def search_id(appointment_id: int):
    for appointment in list_appointments:
        if appointment.id == appointment_id:
            return appointment
    return None