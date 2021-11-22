from classe.Page import Page
from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph

test = Graph()
test.add_node(Utilisateur("Dupont", "Bernard", 56))
test.add_node(Utilisateur("Dupond", "Jean", 23))
test.add_node(Page("NARUTO FAN"))
test.add_line("Dupont", "NARUTO FAN")
test.add_line("Dupont", "Dupond")
test.add_line("NARUTO FAN", "Dupont")

print("Nombre de personne :", test.get_nb_users())
print("Nombre de page :", test.get_nb_pages())
print("Age moyen :", test.get_avg_age())
print("Sommets triés par nom croissants :", test.get_increasing_name_nodes())
print("Sommets triés par nom décroissant :", test.get_decreasing_name_nodes())
print("Sommets triés par degré croissants :", test.get_increasing_degree_nodes())
print("Sommets triés par degré décroissant :", test.get_decreasing_degree_nodes())
print("Sommet Dupont :", test.get_node_by_name("Dupont"))
