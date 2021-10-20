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
        return cell.get_node().get_name()

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

    def get_increasing_name_nodes(self):
        sorted_keys = sorted(self.__merge_keys(), key=str.lower)
        return [self.get_node_by_name(x) for x in sorted_keys]

    # Commandes

    def add_node(self, node: Sommet) -> None:
        assert node is not None

        nodes = self.get_nodes()
        node_name = node.get_name()

        if not self.is_node_in(node):
            cell = GraphCellule(node, list[Sommet])
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

    def add_line(self, node1: Sommet, node2: Sommet) -> bool:
        if not self.__check_2_nodes(node1, node2):
            return False
        self.__get_succ(node1).append(node2)
        return True

    def delete_line(self, node1: Sommet, node2: Sommet) -> bool:
        if not self.__check_2_nodes(node1, node2):
            return False
        self.__get_succ(node1).remove(node2)

    # Outils

    """
    Renvoie la cellule correspondante au sommet de nom name. Renvoie la cellule
    si celle-ci est trouvée et None sinon.
    """
    def __get_cell_by_name(self, name: str) -> GraphCellule:
        node_index = self.get_user_dict().get(name) or self.get_page_dict().get(name)
        if node_index is not None:
            return self.get_nodes()[node_index]
        return None

    """
    Renvoie la liste des clés du dictionnaire __page_dict fusionnée à la liste
    des clés de __user_dict.
    """
    def __merge_keys(self):
        return list(self.__page_dict.keys()) + list(self.__user_dict.keys())

    def __update_dict(self, index: int) -> None:
        # TODO
        return None

    """
    Teste l'existence de 2 noeuds dans le graphe et vérifie qu'ils ne sont pas
    nuls. Arrête le programme si l'un des deux noeuds est nul, renvoie True si
    les deux noeuds existent dans le graphe et False sinon.
    """
    def __check_2_nodes(self, node1: Sommet, node2: Sommet) -> bool:
        assert node1 is not None and node2 is not None
        if not self.is_node_in(node1) or not self.is_node_in(node2):
            return False
        return True

    """
    Renvoie les successeurs du sommet node.
    """
    def __get_succ(self, node: Sommet) -> list[Sommet]:
        return self.__get_cell_by_name(node.get_name()).get_succ_list()
