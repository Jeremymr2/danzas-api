from pydantic import BaseModel, validator
from datetime import date, datetime

class ExpresionBase(BaseModel):
    expresion: str | None = None
    fecha: date | None = None
    resolucion: str | None = None
    departamento: str | None = None
    provincia: str | None = None
    distrito: str | None = None
    clasificacion: str | None = None
    contenido: str | None = None

    @validator('fecha', pre=True)
    def parse_fecha(cls, value):
        if value:
            return datetime.strptime(value, '%d-%m-%Y').date()
        return value

class ExpresionCreate(ExpresionBase):
    pass

class Expresion(ExpresionBase):
    #id: int

    class Config:
        orm_mode = True
