from classe.graph.Sommet import Sommet
from classe.graph.IGraphe import IGraphe
from classe.Utilisateur import Utilisateur
from classe.Page import Page
from classe.graph.GraphCellule import GraphCellule


class Graph(IGraphe):
    def __init__(self):
        self.__nodes = list[GraphCellule]
        self.__page_dict = dict([("Les colos de Bernard", Page("Les colos de Bernard"))])
        self.__user_dict = dict([("Dupont", Utilisateur("Dupont", "Bernard", 56))])

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
        node_index = self.get_user_dict().get(name) or self.get_page_dict().get(name)
        if node_index is not None:
            return self.get_nodes()[node_index].get_node()
        return node_index

    def get_nb_pages(self) -> int:
        return len(self.get_page_dict())

    def get_nb_users(self) -> int:
        return len(self.get_user_dict())

    def is_node_in(self, node: Sommet) -> bool:
        return node.get_name() in self.get_user_dict() or \
                node.get_name() in self.get_page_dict()

    def get_avg_age(self):
        total = 0
        for user in self.__user_dict.itervalues():
            total += user.get_age()

        return int(total / self.__user_dict.length())

    def get_admins(self):
        admins_names = dict()
        for page in self.__page_dict.itervalues():
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
                self.get_page_dict()[node_name] = nodes.index(cell)
            else:
                self.get_user_dict()[node_name] = nodes.index(cell)

    def delete_node(self, node: Sommet) -> None:
        assert node != None

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

    def __update_dict(self, index: int) -> None:
        # TODO
        return None

    # Outils

    """
    Renvoie la liste des clés du dictionnaire __page_dict fusionnée à la liste
    des clés de __user_dict.
    """

    def __merge_keys(self):
        keys = self.__page_dict.keys()
        keys.append(self.__user_dict.keys())
        return keys
