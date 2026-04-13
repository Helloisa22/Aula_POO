from Cliente import Cliente
#    arquivo.py    o nome da nossa classe
import pandas as pd
import os
from Criar_conta import Criar_conta

caminho_excel = "cliente_banco_Tabajara.xlsx"

print("================================================")
print("                 BANCO TABAJARA")
print("                                 ")
print("                 Escolha uma opção")
print("                 1 - Criar conta")
print("                 2 - Acessar conta")
print("================================================\n")
opcao = int(input("R: "))

if opcao == 1:
    print("Opcao 1 selecionada")
    nome_cliente = str(input("Nome completo: "))
    cpf = int(input("CPF: "))
    tipo_conta  = str(input("Tipo da conta que deseja criar:  "))

    if os.path.exists(caminho_excel):
        df = pd.read_excel(caminho_excel)
    else:
        df = pd.DataFrame() 

        #  Instancia a classe com os dados do usuário
        conta = Criar_conta(nome_cliente, cpf, tipo_conta)

        #  Chama o método que retorna o DataFrame do novo cliente
        novo_dado = conta.salvar_excel(caminho_excel)

    # Concatena dados na linha
    df = pd.concat([df, novo_dado], ignore_index=True)

    # salva o excel para criar conta e adicionar conta
    df.to_excel(caminho_excel, index=False)

    print("Cliente cadastrado com sucesso")


elif opcao == 2:
    print("Opcao 2 selecionada")






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