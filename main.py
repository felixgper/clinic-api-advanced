from fastapi import FastAPI
from routers import doctors, patients, appointments, reports

app = FastAPI(
    title="API Clínica",
    description="Sistema de gestión de doctores, pacientes y citas",
    version="1.0.0"
)

app.include_router(doctors.router)
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(reports.router)

@app.get("/")
def root():
    return {"message": "API Clínica funcionando correctamente 🚀"}
