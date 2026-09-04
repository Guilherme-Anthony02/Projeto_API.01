from pydantic import BaseModel
from datetime import date

class CorridaSchema(BaseModel):
    descricaoCorrida : str
    dataCorrida: date
    distancia5km: bool
    distancia10km: bool
    distancia25km: bool


    