from typing import Callable, Union

from classe.graph.Sommet import Sommet
from classe.graph.IGraphe import IGraphe
from classe.Utilisateur import Utilisateur
from classe.Page import Page
from classe.graph.GraphCellule import GraphCellule


class Graph(IGraphe):
    def __init__(self):
        self.__nodes = list[GraphCellule]()
        self.__page_dict = dict()
        self.__user_dict = dict()

    def nb_nodes(self) -> int:
        return len(self.__nodes)

    def nb_lines(self) -> int:
        result = 0
        for i in self.get_nodes():
            result += len(i.get_succ_list())
        return result

    def get_nodes(self) -> list[GraphCellule]:
        return self.__nodes

    def get_page_dict(self) -> dict:
        return self.__page_dict

    def get_user_dict(self) -> dict:
        return self.__user_dict

    def get_node_by_name(self, name: str) -> Sommet:
        assert name is not None
        cell = self.__get_cell_by_name(name)
        if cell is None:
            return None
        return cell.get_node()

    def get_nb_pages(self) -> int:
        return len(self.get_page_dict())

    def get_nb_users(self) -> int:
        return len(self.get_user_dict())

    def is_node_in(self, node: Sommet) -> bool:
        return node.get_name() in self.get_user_dict() or \
                node.get_name() in self.get_page_dict()

    def get_avg_age(self):
        total = 0
        for cell in self.__user_dict.values():
            total += cell.get_node().get_age()

        return int(total / len(self.__user_dict))

    def get_admins(self):
        admins_names = dict()
        for page in self.__page_dict.values():
            page_name = page.get_name()
            admins_names[page_name] = list[str]
            for user in page.get_admins():
                admins_names[page_name].append(user.get_name())

        return admins_names

    def get_increasing_name_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: cell.get_node().get_name())

    def get_decreasing_name_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: cell.get_node().get_name(), True)

    def get_increasing_degree_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: len(cell.get_succ_list()))

    def get_decreasing_degree_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: len(cell.get_succ_list()), True)

    # Commandes

    def add_node(self, node: Sommet) -> None:
        assert node is not None

        nodes = self.get_nodes()
        node_name = node.get_name()

        if not self.is_node_in(node):
            cell = GraphCellule(node, list[Sommet]())
            nodes.append(cell)

            if isinstance(node, Page):
                self.get_page_dict()[node_name] = cell
            else:
                self.get_user_dict()[node_name] = cell

    def delete_node(self, node: Sommet) -> None:
        assert node is not None

        nodes = self.get_nodes()
        node_name = node.get_name()

        if self.is_node_in(node):
            if isinstance(node, Page):
                index = self.get_page_dict().get(node_name)
                del self.get_page_dict()[node_name]
            else:
                index = self.get_user_dict().get(node_name)
                del self.get_user_dict()[node_name]
            del nodes[index]
            self.__update_dict(index)

    def add_line(self, node1: str, node2: str) -> bool:
        if not self.__check_2_nodes(node1, node2):
            return False
        self.__get_succ_list(node1).append(self.get_node_by_name(node2))
        return True

    def delete_line(self, node1: str, node2: str) -> bool:
        if not self.__check_2_nodes(node1, node2):
            return False
        self.__get_succ_list(node1).remove(self.get_node_by_name(node2))
        print("Liste succ :", self.__get_succ_list(node1))

    # Outils

    """
    Renvoie la cellule correspondante au sommet de nom name. Renvoie la cellule
    si celle-ci est trouvée et None sinon.
    """
    def __get_cell_by_name(self, name: str) -> GraphCellule:
        cell = self.get_user_dict().get(name) or self.get_page_dict().get(name)
        node_index = self.__nodes.index(cell)
        if node_index is not None:
            return self.get_nodes()[node_index]
        return None

    """
    Renvoie la liste des sommets associés au graphe triés par nom de manière 
    croissante si reverse vaut True, et de manière décroissante sinon.
    """
    def __sort_nodes(self, key: Callable, reverse: bool = False) -> list[Sommet]:
        sorted_cells = sorted(self.__nodes, key=key, reverse=reverse)
        return [cell.get_node() for cell in sorted_cells]

    def __update_dict(self, index: int) -> None:
        # TODO
        return None

    """
    Teste l'existence de 2 noeuds dans le graphe et vérifie qu'ils ne sont pas
    nuls. Arrête le programme si l'un des deux noeuds est nul, renvoie True si
    les deux noeuds existent dans le graphe et False sinon.
    """
    def __check_2_nodes(self, node1_str: str, node2_str: str) -> bool:
        assert node1_str is not None and node1_str is not None
        node1 = self.get_node_by_name(node1_str)
        node2 = self.get_node_by_name(node2_str)
        if not self.is_node_in(node1) or not self.is_node_in(node2):
            return False
        return True

    """
    Renvoie les successeurs du sommet node. Renvoie None si node n'a pas de
    successeur.
    """
    def __get_succ_list(self, node: str) -> list[Sommet]:
        cell = self.__get_cell_by_name(node)
        if cell is None:
            return None
        return cell.get_succ_list()
