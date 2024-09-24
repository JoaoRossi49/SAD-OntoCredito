from owlready2 import *

onto = get_ontology("C:\git\podecredito-api\ontology\credit-ontology.rdf").load()

def infer_credit_eligibility(cliente):
    with onto:
        # Criar uma instância de cliente na ontologia
        individuo_cliente = onto.Cliente()
        individuo_cliente.temSalario = [cliente.salario]
        individuo_cliente.temDividas = [cliente.dividas]
        individuo_cliente.temSaldo = [cliente.saldo]
        
        # Regras ou classes definidas na ontologia serão inferidas automaticamente
        sync_reasoner()

        # Verificar se o cliente está em uma classe de aprovação de crédito
        if individuo_cliente in onto.CréditoAprovado.instances():
            return True
        else:
            return False
