from sqlalchemy import Column, Integer, String, DECIMAL, Date

from database import Base

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60))
    cpf = Column(Integer)
    data_nascimento = Column(Date)
    peso = Column(Integer)
    altura = Column(DECIMAL(10,2))
    sexo = Column(String(1))
    cep = Column(Integer)
    ruaLogradouro = Column(String(100))
    bairro = Column(String(20))
    cidade = Column(String(70))
    uf = Column(String(2))
    
    
   

