from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph

test = Graph()
test.add_node(Utilisateur("Dupont", "Bernard", 56))
print(test.get_nb_users())
