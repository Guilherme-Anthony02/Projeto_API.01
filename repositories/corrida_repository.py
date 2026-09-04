from sqlalchemy.orm import Session
from models.corrida_model import Corrida

class CorridaRepository:
    #listar todas as pessoas
    def listar(self, db: Session):
        return db.query(Corrida).all()
    
    #cadastro Corrida
    def cadastar(self, db: Session, corrida):
        nova_corrida = Corrida(
            descricaoCorrida = corrida.descricaoCorrida,
            dataCorrida = corrida.dataCorrida,
            distancia5km = corrida.distancia5km,
            distancia10km = corrida.distancia10km,
            distancia25km = corrida.distancia25km
        )

        db.add(nova_corrida)
        db.commit()
        db.refresh(nova_corrida)

        return nova_corrida
    
    #listar corrida por id
    def corrida_id(self, db: Session, id: int):
        return db.query(Corrida).filter(Corrida.idCorrida == id).first()
    
    #alterar pessoa
    def alterar (self, db: Session, id: int, corrida):
        corrida_bd = self.corrida_id(db, id)

        corrida_bd.descricaoCorrida = corrida.descricaoCorrida
        corrida_bd.dataCorrida = corrida.dataCorrida
        corrida_bd.distancia5km = corrida.distancia5km
        corrida_bd.distancia10km = corrida.distancia10km
        corrida_bd.distancia25km = corrida.distancia25km
        
        db.commit()
        db.refresh(corrida_bd)
        
        return corrida_bd
    
    #excluir pessoa
    def excluir (self, db: Session, id: int):
       corrida_bd = self.corrida_id(db, id)
       
       db.delete(corrida_bd)
       db.commit()

       return{"Mensagem": "Corrida Excluída com Sucesso!!"}
   