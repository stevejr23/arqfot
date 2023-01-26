from fastapi import FastAPI
from app.routes import router as BysRuta

app = FastAPI(
    title="Microservico utilizando docker, mongodb y fastapi",
    description="Trabajo de arquitectura de software"
)

app.include_router(BysRuta,tags=["Bus"], prefix="/bus")

@app.get("/", tags=["Inicio"])
async def read_root():
    return {"Bienvenidos": "Tabajo de Arquitectura de Softwate colocar la ruta /docs"}
