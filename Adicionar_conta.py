from Cliente import Cliente
import pandas as pd

class Adicionar_conta:
    def __init__(self, nome_cliente, cpf, tipo_conta):

        # Criando molde da classe cliente para manipular dados digitados pelo usuario
        self.cliente = Cliente(nome_cliente, cpf, tipo_conta)

    def adicionar(self, caminho_excel):
        nova_linha = len(caminho_excel) # visao da nova linha do excel
        ultima_linha = caminho_excel.iloc[-1]

        dados_cliente = self.cliente.dicionario_cliente()

        dados_cliente["numero_conta"] = ultima_linha["numero_conta"] + 1
        dados_cliente["agencia"] = ultima_linha["agencia"] + 1


        novo_dado = pd.DataFrame(dados_cliente)
        return novo_dado

