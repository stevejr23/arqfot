from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Query

from app.database import (
    retrieve_cars,
    add_car,
    retrieve_car,
    update_car,
    delete_car,
)

from app.models import ErrorResponseModel, ResponseModel, BusSchema, UpdateBusModel

router = APIRouter()

@router.post("/", response_description="bus agg en la base")
async def add_car_data(car: BusSchema = Body(...)):
    car = jsonable_encoder(car)
    new_car = await add_car(car)
    return ResponseModel(new_car, "bus agg correctamente.")

@router.get("/", response_description="bus recuperado")
async def get_cars():
    cars = await retrieve_cars()
    if cars:
        return ResponseModel(cars, "datos del bus recuperados correctamente")
    return ResponseModel(cars, "Lista vacía")


@router.get("/{id}", response_description="bus recuperado")
async def get_car_data(id):
    car = await retrieve_car(id)
    if car:
        return ResponseModel(car, "datos del bus recuperados correctamente")
    return ErrorResponseModel("Se ha producido un error", 404, "El dato no existe.")


@router.delete("/{id}", response_description="dato borrado de la base")
async def delete_car_data(id: str):
    deleted_car = await delete_car(id)
    if deleted_car:
        return ResponseModel(
           "Bys con id: {} eliminado".format(id), "bus eliminado con éxito"
        )
    return ErrorResponseModel(
        "Se ha producido un error", 404, "el bys con id {0} no existe".format(id)
    )


@router.put("/{id}")
async def update_car_data(id: str, req: UpdateBusModel = Body(...)):
    req = {key: val for key, val in req.dict().items() if val is not None}
    updated_car = await update_car(id, req)
    if updated_car:
        return ResponseModel(
            "bus con id: {} nombre la actualizado se ha realizado correctamente".format(id),
            "bys actualizado con éxito",
        )
    return ErrorResponseModel(
        "Se ha producido un error",
        404,
        "Se ha producido un error al actualizar los datos bus",
    )
