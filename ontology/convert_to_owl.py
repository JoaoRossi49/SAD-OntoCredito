from rdflib import Graph

# Carrega o arquivo Turtle
g = Graph()
g.parse("C:/git/podecredito-api/ontology/credit-ontology.ttl", format="ttl")

# Salva em formato RDF/XML (OWL)
g.serialize("C:/git/podecredito-api/ontology/credit-ontology.owl", format="xml")