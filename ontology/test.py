from inferences import verificar_credito_aprovado

class Cliente:
    def __init__(self, nome, salario, nivel_escolar, quantidade_cartoes, dividas, saldo):
        self.nome = nome
        self.salario = salario
        self.nivel_escolar = nivel_escolar
        self.quantidade_cartoes = quantidade_cartoes
        self.dividas = dividas
        self.saldo = saldo

cliente = Cliente('João Rossi', 10, '1', 2, 20,1000)


temCredito = verificar_credito_aprovado(10, 20)

if temCredito:
    print('O cliente é elegível para crédito')
else:
    print('O cliente não é elegível para crédito')