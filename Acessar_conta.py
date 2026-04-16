import pandas as pd
from Cliente import Cliente

class Acessar_conta:
    def __init__(self, cpf, numero_conta):
        self.cliente = Cliente(cpf, numero_conta, tipo_conta="")

    # Metodo
    def validar_banco(self, caminho_excel):
        df = pd.read_excel(caminho_excel)

        cliente_encontrado = df[
            (df["cpf"] == self.cliente.cpf) &
            (df["numero_conta"] == self.cliente.numero_conta)
        ]

        # Se o cliente for encontrado então mostrar a mensagem Bem-vindo e trazer os dados solicitados
        if not cliente_encontrado.empty:
            print("Bem-vindo ao banco Tabajara")
        else:
            print("Usuário não encontrado, tentar novamente ou realizar o cadastro")
