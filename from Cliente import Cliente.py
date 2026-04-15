from Cliente import Cliente
#    arquivo.py    o nome da nossa classe
from Criar_conta import Criar_conta
from Adicionar_conta import Adicionar_conta
import pandas as pd
import os

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

    df = pd.DataFrame()
    
    if os.path.exists(caminho_excel): # true
        print("Arquivo ja existe")
        df = pd.read_excel(caminho_excel)

        adicionar = Adicionar_conta(nome_cliente, cpf, tipo_conta)
        novo_dado = adicionar.adicionar(df)

    else: # false
        print("Arquivo nao existe")

        # Instancio para manipular os dados adicionados pelo cliente
        conta = Criar_conta(nome_cliente, cpf, tipo_conta)

        # Identifico o caminho do excel e chamo a funcao salvar_excel
        novo_dado = conta.salvar_excel(caminho_excel)


    #Concat para inserir uma nova linha no excel com os dados digitados pelo
    df = pd.concat([df, novo_dado], ignore_index=True)

    df.to_excel(caminho_excel, index=False)
    

elif opcao == 2:
    print("Opcao 2 selecionada")






from Cliente import Cliente
import pandas as pd

class Adicionar_conta:
    def __init__(self, nome_cliente, cpf, tipo_conta):
        numero_conta = 0
        agencia = 400
        extrato_bancario = 0
        self.cliente = Cliente(nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario)

    def adicionar(self, excel):
        nova_linha = len(excel)
        ultima_linha = excel.iloc[-1]  # pega os dados da última linha

        dados_cliente = {
            "nome_cliente": [self.cliente.nome_cliente],
            "cpf": [self.cliente.cpf],
            "tipo_conta": [self.cliente.tipo_conta],
            "numero_conta": ultima_linha["numero_conta"] + 1,  # incrementa
            "agencia": ultima_linha["agencia"] + 1,            # incrementa
            "extrato_bancario": [self.cliente.extrato_bancario],
        }

        novo_dado = pd.DataFrame(dados_cliente)
        return novo_dado