from owlready2 import get_ontology, sync_reasoner_pellet

# Carregar a ontologia
onto = get_ontology("C:/git/podecredito-api/ontology/credit-ontology.owl").load()

# Acessar uma classe da ontologia (por exemplo, Cliente)
Cliente = onto.Cliente

# Criar um novo indivíduo da classe Cliente
novo_cliente = Cliente("cliente1")

# Definir propriedades para o novo indivíduo
novo_cliente.salario.append(10)
novo_cliente.dividas.append(20)

# Rodar o raciocinador Pellet
with sync_reasoner_pellet():
    # Exibir classes inferidas para o indivíduo
    print("Classes inferidas:", novo_cliente.is_a)

    # Exibir propriedades inferidas
    for prop in novo_cliente.get_properties():
        print(f"{prop}: {novo_cliente[prop]}")
