from pydantic import BaseModel, Field
from typing import Optional


class BusSchema(BaseModel):
    propietario: str = Field(...)
    placa: str = Field(...)
    compania: str = Field(...)
    caja: str = Field(...)
    year: int = Field(...)

    class Config:
        schema_extra = {
            "ejemplo": {
                "propietario": "Luis Danilo",
                "placa": "LBA-1234",
                "compania": "Cariamanga",
                "caja": "Manual",
                "year": 2020,
            }
        }

class UpdateBusModel(BaseModel):
    propietario: Optional[str]
    placa: Optional[str]
    compania: Optional[str]
    caja: Optional[str]
    year: Optional[int]

    class Config:
        schema_extra = {
            "ejemplo": {
                "propietario": "Luis Danilo",
                "placa": "LBA-1234",
                "compania": "Cariamanga",
                "caja": "Manual",
                "year": 2020,
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
