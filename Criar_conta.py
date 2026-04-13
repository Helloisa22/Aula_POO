# Será a criacao zero do nosso excel
from Cliente import Cliente
import pandas as pd

class Criar_conta:
    def __init__(self, nome_cliente, cpf, tipo_conta):
        #Atributos
        # Quais os atributos precisamos para criar uma conta ????????

        numero_conta = 0
        agencia = 400
        extrato_bancario = 0

        # Intancio o cliente
        self.cliente = Cliente(nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario)

    def salvar_excel(self, caminho_excel):
        dados_cliente = {
            "nome_cliente": [self.cliente.nome_cliente],
            "cpf": [self.cliente.cpf],
            "tipo_conta": [self.cliente.tipo_conta],
            "numero_conta": [self.cliente.numero_conta],
            "agencia": [self.cliente.agencia],
            "extrato_bancario": [self.cliente.extrato_bancario],
        }

        excel = pd.DataFrame(dados_cliente)
        return excel