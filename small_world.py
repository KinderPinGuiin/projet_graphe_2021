import sys

from classe.graph.Graphe import Graph

def small_world(nb_nodes: int, nb_lines: int, dangling_nodes: bool) -> bool:
    graph = Graph()
    # Création du graphe aléatoire
    print("Génération du graphe aléatoire...")
    graph.random_graph(nb_nodes, nb_lines)
    # Compare chaque sommet avec les autres et vérifie les distances les plus
    # courtes
    print("Parcours des sommets...")
    for node in graph.get_nodes():
        for distance in \
          graph.shortest_distance(node.get_node().get_name()).values():
            if distance > 6 and (not dangling_nodes or distance != 1000000):
                return False
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "USAGE : python small_world.py <Nombre sommets> <Nombre arêtes>",
            "[Prendre les noeuds seuls en compte]"
        )
        exit(0)
    if small_world(int(sys.argv[1]), int(sys.argv[2]), len(sys.argv) > 3):
        print(
            "Pour un graphe aléatoire de", sys.argv[1], "noeuds et", 
            sys.argv[2], "arêtes, l'hypothèse des réseaux small world est",
            "potentiellement vérifiée !"
        )
    else:
        print(
            "Pour un graphe aléatoire de", sys.argv[1], "noeuds et", 
            sys.argv[2], "arêtes, l'hypothèse des réseaux small world n'est",
            "pas vérifiée."
        )
