from models.doctors import Doctors
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix= "/doctors",
                   tags= ["doctors"],
                   responses= {404: {"message" : "NO ENCONTRADO"}})

list_doctors = []

@router.get("/")
async def get_doctors():
    if not list_doctors:
        raise HTTPException(status_code= 404, detail= "NO SE ENCONTRO LISTA DE DOCTORES")
    return list_doctors

@router.get("/{id}")
async def get_doctors(id: int):
    if search_id(id) is None:
        raise HTTPException(status_code= 404, detail= "NO SE ENCONTRO ID DEL DOCTOR")
    return search_id(id)

@router.post("/")
async def post_doctors(doctor : Doctors):
    existing_doctor = search_id(doctor.id)
    if len(doctor.specialty.strip()) == 0:
        raise HTTPException(status_code= 409, detail= "LA ESPECIALIDAD NO PUEDE IR VACIA")
    if existing_doctor is not None:
        raise HTTPException(status_code= 409, detail= "ID DE DOCTOR YA EXISTE")
    list_doctors.append(doctor)
    return doctor

@router.put("/{id}")
async def put_doctors(id: int, doctor: Doctors):

    for index, value in enumerate(list_doctors):
        if value.id == id:
            list_doctors[index] = doctor
            return doctor
    raise HTTPException(status_code= 409, detail= "NO SE PUDO ACTUALIZAR DOCTOR")

@router.delete("/{id}")
async def delete_doctors(id: int):
    for index, value in enumerate(list_doctors):
        if value.id == id:
            del list_doctors[index]
            return {"message" : "SE ELIMINO DOCTOR"}
    raise HTTPException(status_code= 409, detail= "NO SE PUDO ACTUALIZAR DOCTOR")

def search_id(id : int):
    for doctor in list_doctors:
        if doctor.id == id:
            return doctor
    return None