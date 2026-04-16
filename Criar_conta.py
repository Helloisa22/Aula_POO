# Será a criacao zero do nosso excel
from Cliente import Cliente
import pandas as pd

class Criar_conta:
    def __init__(self, nome_cliente, cpf, tipo_conta):
        #Atributos
        # Quais os atributos precisamos para criar uma conta ????????

        # Intancio o cliente
        self.cliente = Cliente(nome_cliente, cpf, tipo_conta)

    def salvar_excel(self, caminho_excel):
        dados_cliente = self.cliente.dicionario_cliente()

        excel = pd.DataFrame(dados_cliente)
        return excel