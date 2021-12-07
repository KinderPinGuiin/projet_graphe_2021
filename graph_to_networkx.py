import networkx as nx
from pyvis.network import Network
import re

from classe.graph.Sommet import Sommet
from classe.Page import Page
from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph


# Renvoie la transposition d'un graphe de type Graph
# à un graphe orienté de networkX
def graph_to_netX(G: Graph,):
    # Initialisation du grapge orienté
    GX = nx.DiGraph()
    # Ajout des noeud
    for nodes in G.get_nodes():
        if isinstance(nodes.get_node(), Utilisateur):
            GX.add_node(nodes.get_node().get_name(),
                        firstname=nodes.get_node().get_firstname(),
                        lastname=nodes.get_node().get_name(),
                        fullname=get_fullname(nodes.get_node()),
                        title=display_attribute(nodes.get_node()),
                        age=nodes.get_node().get_age(),
                        value=len(nodes.get_succ_list()),
                        type="Utilisateur")
        else:
            GX.add_node(nodes.get_node().get_name(),
                        name=nodes.get_node().get_name(),
                        title=display_attribute(nodes.get_node()),
                        shape="box",
                        type="Page")
    # Ajout des noeuds
    GX.add_edges_from(G.get_lines())

    return GX


# Creation d'un fichier html de nom name contenant représentation du graphe G
def create_graph_html(G: Graph, name: str):
    filename = name + ("" if name.endswith(".html") else ".html")
    # Initialisation du graphe pyvis oriente
    graphepyvis = Network(directed=True)
    graphepyvis.repulsion()
    # Tranformation de notre graphe en un graphe utilisable par pyvis
    graphepyvis.from_nx(graph_to_netX(G))
    graphepyvis.write_html(filename)
    # Change le CSS du fichier pour qu'il s'adapte au conteneur
    f = open(filename, "r")
    f_content = ""
    pattern = re.compile(r"[ \t]+(width|height): ([0-9]+px)")
    for line in f:
        new_line = line
        search = pattern.search(line)
        if search:
            new_line = line.replace(search.group(2), "100%")
        f_content += new_line
    f.close()
    f = open(filename, "w")
    f.write(f_content)
            


# ------ Outils ------


# Renvoie l'intégralité du nom d'un sommet
def get_fullname(S: Sommet):
    if isinstance(S, Utilisateur):
        return S.get_firstname() + " " + S.get_name()
    else:
        return S.get_name()


# Renvoie le nom de tous les admins d'une page
def get_name_admin(page: Page):
    str = "Admin : </br>"
    for admin in page.get_admins():
        str += "- "
        str += admin.get_name()
        str += "</br>"
    return str


# Renvoie les attributs d'un sommet sous format html
def display_attribute(S: Sommet):
    if isinstance(S, Utilisateur):
        attributes = get_fullname(S)
        attributes += "</br>"
        attributes += "---------- </br>"
        attributes += "Nom : "
        attributes += S.get_name()
        attributes += "</br>"
        attributes += "Prenom : "
        attributes += S.get_firstname()
        attributes += "</br>"
        attributes += "Age : "
        attributes += str(S.get_age())
        attributes += "</br>"
        return attributes
    else:
        attributes = get_fullname(S)
        attributes += "</br>"
        attributes += "---------- </br>"
        attributes += "Nom : "
        attributes += S.get_name()
        attributes += "</br>"
        attributes += get_name_admin(S)
        return attributes


# ------ Partie de test (temp) ------
# test = Graph()
# test.random_graph(100, 50)
# test.save_graph("tmp")
# test.add_node(Utilisateur("Dupont", "Bernard", 56))
# test.add_node(Utilisateur("Dupond", "Jean", 23))
# test.add_node(Utilisateur("Boucher", "Pierre", 49))
# test.add_node(Utilisateur("Marmion", "Compagnon", 57))
# test.add_node(Utilisateur("Michel", "Clothilde", 23))
# test.add_node(Utilisateur("Alacoque", "Bois", 23))
# test.add_node(Page("NARUTO FAN", [test.get_node_by_name(
#     "Dupont"), test.get_node_by_name("Michel")]))
# test.add_line("Dupont", "NARUTO FAN")
# test.add_line("Dupont", "Dupond")
# test.add_line("NARUTO FAN", "Dupont")
# test.add_line("Dupont", "Marmion")
# test.add_line("Michel", "Alacoque")
# test.add_line("Boucher", "Dupond")

# print(test.get_lines())
# print(test.get_nodes())

# create_graph_html(test, "graphe_temp.html")

# print("Test display_attribute :")
# print(display_attribute(test.get_node_by_name("Dupond")))

# graphnetx = nx.DiGraph()
# graphepyvis = Network(directed=True)
# graphepyvis.from_nx(graph_to_netX(test))

# graphepyvis.write_html("graphe_temp.html")
# graphepyvis.show("test.html")
