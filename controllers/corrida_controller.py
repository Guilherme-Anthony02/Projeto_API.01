from services.corrida_service import CorridaService

class CorridaController:
    #método construtor
    def __init__(self):
        self.servico = CorridaService()
    
    #controler listar
    def listar(self, db):
        return self.servico.listar(db)

    #controler listar_id
    def listar_id(self, db, id):
        return self.servico.listar_id(db, id)
    
    #controle cadastrar
    def cadastrar(self, db, pessoa):
        return self.servico.cadastrar(db, pessoa)

  # controller alterar pessoa
    def alterar(self, db, id, pessoa):
        return self.servico.alterar(db, id, pessoa)


    # controller excluir pessoa
    def excluir(self, db, id):
        return self.servico.excluir(db, id)