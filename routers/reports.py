from fastapi import APIRouter, HTTPException
from routers import doctors, patients, appointments

router = APIRouter(
    prefix="/reports",
    tags=["reports"],
    responses={404: {"message": "NO ENCONTRADO"}}
)


@router.get("/doctor/{doctor_id}/appointments")
async def report_doctor_appointments(doctor_id: int):

    # Buscar doctor
    doctor = None
    for d in doctors.list_doctors:
        if d.id == doctor_id:
            doctor = d
            break

    if doctor is None:
        raise HTTPException(status_code=404, detail="DOCTOR NO ENCONTRADO")

    # Obtener citas del doctor
    doctor_appointments = [
        app for app in appointments.list_appointments
        if app.doctor_id == doctor_id
    ]

    return {
        "doctor": doctor,
        "total_appointments": len(doctor_appointments),
        "appointments": doctor_appointments
    }

@router.get("/patient/{patient_id}/appointments")
async def report_patient_appointments(patient_id: int):

    # Buscar paciente
    patient = None
    for p in patients.list_patients:
        if p.id == patient_id:
            patient = p
            break

    if patient is None:
        raise HTTPException(status_code=404, detail="PACIENTE NO ENCONTRADO")

    # Obtener citas del paciente
    patient_appointments = [
        app for app in appointments.list_appointments
        if app.patient_id == patient_id
    ]

    return {
        "patient": patient,
        "total_appointments": len(patient_appointments),
        "appointments": patient_appointments
    }
