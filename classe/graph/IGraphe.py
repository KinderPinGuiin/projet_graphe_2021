import fileinput

from classe.graph.Sommet import Sommet


class IGraphe:

    # Requetes

    def nb_nodes(self) -> int:
        pass

    def nb_lines(self) -> int:
        pass

    def get_nodes(self) -> Sommet:
        pass

    """
    Renvoie la liste des noms de pages et des utilisateurs triée dans l'ordre
    croissant.
    """
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

    def get_page_dict(self) -> dict:
        pass
    
    def get_user_dict(self) -> dict:
        pass

    def get_node_by_name(self, name: str) -> Sommet:
        pass

    def get_nb_pages(self):
        pass

    def get_nb_users(self):
        pass

    """
    Renvoie l'age moyen des utilisateurs arrondi à l'entier près.
    """
    def get_avg_age(self):
        pass

    """
    Renvoie un dictionnaire associant chaque page à ces administrateurs.
    """
    def get_admins(self):
        pass

    def save_graph(self, name: str) -> fileinput:
        pass

    def load_graph(self, name: str):
        pass

    # Commandes

    def delete_node(self, node: Sommet) -> None:
        pass

    def add_node(self, node: Sommet) -> None:
        pass

    def delete_line(self):
        pass

    def add_line(self, node1: Sommet, node2: Sommet):
        pass
