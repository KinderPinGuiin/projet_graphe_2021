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

    def nb_nodes(self):
        return len(self.__nodes)

    
