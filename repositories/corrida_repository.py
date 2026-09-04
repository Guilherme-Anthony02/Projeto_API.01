from sqlalchemy.orm import Session
from models.corrida_model import Corrida

class CorridaRepository:
    #listar todas as pessoas
    def listar(self, db: Session):
        return db.query(Corrida).all()
    
    #cadastro Corrida
    def cadastar(self, db: Session, corrida):
        nova_corrida = Corrida(
            descricao_corrida = corrida.descricao_corrida,
            data_corrida = corrida.data_corrida,
            distancia_5km = corrida.distancia_5km,
            distancia_10km = corrida.distancia_10km,
            distancia_25km = corrida.distancia_25km
        )

        db.add(nova_corrida)
        db.commit()
        db.refresh(nova_corrida)

        return nova_corrida
    
    #listar corrida por id
    def corrida_id(self, db: Session, id: int):
        return db.query(Corrida).filter(Corrida.idcorrida == id).first()
    
    #alterar pessoa
    def alterar (self, db: Session, id: int, corrida):
        corrida_bd = self.corrida_id(db, id)

        corrida_bd.descricao_corrida = corrida.descricao_corrida
        corrida_bd.data_corrida = corrida.data_corrida
        corrida_bd.distancia_5km = corrida.distancia_5km
        corrida_bd.distancia_10km = corrida.distancia_10km
        corrida_bd.distancia_25km = corrida.distancia_25km
        
        db.commit()
        db.refresh(corrida_bd)
        
        return corrida_bd
    
    #excluir pessoa
    def excluir (self, db: Session, id: int):
       corrida_bd = self.corrida_id(db, id)
       
       db.delete(corrida_bd)
       db.commit()

       return{"Mensagem": "Corrida Excluída com Sucesso!!"}
   