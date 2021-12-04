from classe.Page import Page
from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph
import time

start_time = time.perf_counter()
test = Graph()
test.load_graph("test")
print(test.page_rank())

# print([node.get_node().get_name() for node in test.get_nodes()], test.get_lines())
# print("--- " + str(time.perf_counter() - start_time) + " seconds ---")
