from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, Date

from database import Base

class Corrida(Base):
    __tablename__ = "corrida"

    idCorrida = Column(Integer, primary_key=True, index=True)
    descricaoCorrida = Column(String(200))
    dataCorrida = Column(Date)
    distancia5km = Column(Boolean)
    distancia10km = Column(Boolean)
    distancia25km = Column(Boolean)
    
    
