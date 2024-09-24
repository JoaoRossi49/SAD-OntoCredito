from inferences import infer_credit_eligibility

class Cliente:
    def __init__(self, nome, salario, nivel_escolar, quantidade_cartoes, dividas, saldo):
        self.nome = nome
        self.salario = salario
        self.nivel_escolar = nivel_escolar
        self.quantidade_cartoes = quantidade_cartoes
        self.dividas = dividas
        self.saldo = saldo

cliente = Cliente('João Rossi', 1400, '1', 2, 300,1000)


temCredito = infer_credit_eligibility(cliente)

if temCredito:
    print('O cliente é elegível para crédito')
else:
    print('O cliente não é elegível para crédito')