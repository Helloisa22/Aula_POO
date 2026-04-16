# A evolucao de um dicionário é criação de uma classe
# __init__ Construtor > Cria um molde dos dados do cliente, o objetivo é conseguir transferir dados por todos os arquivos python
class Cliente:
    def __init__(self, nome_cliente, cpf, tipo_conta, numero_conta=0, agencia=400, extrato_bancario=0):
        # Atributos
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.extrato_bancario = extrato_bancario

    # Metodos
    def __str__(self):
        return f"Nome: {self.nome_cliente} | CPF: {self.cpf} | Tipo Conta: {self.tipo_conta} | Numero Conta: {self.numero_conta} | Agencia: {self.agencia} | Extrato bancario: {self.extrato_bancario}"
    
    # Metodo
    def dicionario_cliente(self):
        return {chave: [valor] for chave, valor in self.__dict__.items()}
    
    