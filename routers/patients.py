from fastapi import APIRouter, HTTPException
from models.patients import Patients

router = APIRouter(prefix= "/patients",
                   tags= ["patients"],
                   responses= {404 : {"message" : "No encontrado"}}
                   )

list_patients = []

@router.get("/")
async def get_patients():
    if not list_patients:
        raise HTTPException(status_code= 404, detail= "NO SE ENCONTRO PACIENTES")
    return list_patients

@router.get("/{id}")
async def get_patients(id : int):
    if search_id(id) is None:
        raise HTTPException(status_code= 404, detail= "ID NO ENCONTRADO")
    return search_id(id)

@router.post("/")
async def post_patients(patient: Patients):
    existing = search_id(patient.id)
    if existing is not None:
        raise HTTPException(status_code= 409, detail= "EL ID YA EXISTE")
    if patient.age < 0:
        raise HTTPException(status_code= 409, detail = "LA EDAD ES MENOR A 0 AÑOS")
    if len(patient.dni) != 8 or not patient.dni.isdigit():
        raise HTTPException(status_code= 409, detail= "EL DNI TIENE QUE TENER 8 DIGITOS")
    list_patients.append(patient)
    return patient

@router.put("/{id}")
async def put_patients(id: int, patient: Patients):
    
    if patient.age < 0:
        raise HTTPException(status_code= 409, detail = "LA EDAD ES MENOR A 0 AÑOS")
    if len(patient.dni) != 8 or not patient.dni.isdigit():
        raise HTTPException(status_code= 409, detail= "EL DNI TIENE QUE TENER 8 DIGITOS")
    for index, value in enumerate(list_patients):
        if value.id == id:
            list_patients[index] = patient
            return patient
    raise HTTPException(status_code= 409, detail= "NO SE PUDO ACTUALIZAR PACIENTE")

@router.delete("/{id}")
async def delete_patients(id: int):
    for index, value in enumerate(list_patients):
        if value.id == id:
            del list_patients[index]
            return {"message" : "SE ELEMINO PACIENTE"}
    raise HTTPException(status_code= 409, detail= "NO SE PUDO ACTUALIZAR PACIENTE")


def search_id(id: int):
    for patient in list_patients:
        if patient.id == id:
            return patient
    return None

