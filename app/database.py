import os
from dotenv import load_dotenv

import motor.motor_asyncio
from bson.objectid import ObjectId

load_dotenv()
USER = os.getenv("MONGO_USER")
PASS = os.getenv("MONGO_PW")
DB = os.getenv("MONGO_DEF_DB")
PORT = os.getenv("MONGO_PORT")
MONGO_DETAILS = f"mongodb://{USER}:{PASS}@mongodb:{PORT}/{DB}"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client["admin"]

car_collection = database.get_collection("car_collection")

# A
def car_helper(car) -> dict:
    return {
        "id": str(car["_id"]),
        "propietario": car["propietario"],
        "placa": car["placa"],
        "compania": car["compania"],
        "caja": car["caja"],
        "year": car["year"],
    }

# Listar bus
async def retrieve_cars():
    cars = []
    async for car in car_collection.find():
        cars.append(car_helper(car))
    return cars

# Add nuevo bus en la base de datos
async def add_car(car_data: dict) -> dict:
    car = await car_collection.insert_one(car_data)
    new_car = await car_collection.find_one({"_id": car.inserted_id})
    return car_helper(new_car)

# Listar bus/taxi por id
async def retrieve_car(id: str) -> dict:
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        return car_helper(car)

# Actualizar info bus/taxi por id
async def update_car(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        updated_car = await car_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_car:
            return True
        return False

# Eliminar bus/taxi de la base
async def delete_car(id: str):
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        await car_collection.delete_one({"_id": ObjectId(id)})
        return True

