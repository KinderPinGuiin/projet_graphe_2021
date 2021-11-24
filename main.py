from classe.Page import Page
from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph

test = Graph()
"""
test.add_node(Utilisateur("Dupont", "Bernard", 56))
test.add_node(Utilisateur("Dupond", "Jean", 23))
test.add_node(Page("NARUTO FAN"))
test.add_line("Dupont", "NARUTO FAN")
test.add_line("Dupont", "Dupond")
test.add_line("NARUTO FAN", "Dupont")
"""

test.load_graph("test")
print([node.get_node().get_name() for node in test.get_nodes()], test.nb_lines())
