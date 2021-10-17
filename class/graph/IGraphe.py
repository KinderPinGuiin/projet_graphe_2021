import fileinput

from Sommet import Sommet


class IGraphe:

    # Requetes

    def nb_nodes(self) -> int:
        pass

    def nb_lines(self) -> int:
        pass

    def get_nodes(self) -> Sommet:
        pass

    def get_increasing_name_nodes(self) -> Sommet:
        pass

    def get_decreasing_name_nodes(self) -> Sommet:
        pass

    def get_increasing_degree_nodes(self) -> Sommet:
        pass

    def get_decreasing_degree_nodes(self) -> Sommet:
        pass

    def get_lines(self):
        pass

    def get_node_by_name(self, name: str):
        pass

    def get_nb_pages(self):
        pass

    def get_nb_users(self):
        pass

    def get_avg_age(self):
        pass

    def get_admins(self):
        pass

    def save_graph(self, name: str) -> fileinput:
        pass

    def load_graph(self, name: str):
        pass

    # Commandes

    def delete_node(self, name: str):
        pass

    def add_node(self, name: str) -> Sommet:
        pass

    def delete_line(self):
        pass

    def add_line(self, node1: Sommet, node2: Sommet):
        pass
