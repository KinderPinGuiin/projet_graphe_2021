from Sommet import Sommet
from IGraphe import IGraphe
from Utilisateur import Utilisateur
from Page import Page
from graph.GraphCellule import GraphCellule


class Graph(IGraphe):
    def __init__(self):
        self.__nodes = list[GraphCellule]
        self.__page_dict = dict()
        self.__user_dict = dict()

    # Requetes

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
        if node_index != None:
            return self.get_nodes()[node_index].get_node()
        return node_index
    

    def get_nb_pages(self) -> int:
        return len(self.get_page_dict())


    def get_nb_users(self) -> int:
        return len(self.get_user_dict())


    def is_node_in(self, node: Sommet) -> bool:
        return node.get_name() in self.get_user_dict() or \
                node.get_name() in self.get_page_dict()

    # Commandes

    def add_node(self, node: Sommet) -> None:
        assert node != None

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
            