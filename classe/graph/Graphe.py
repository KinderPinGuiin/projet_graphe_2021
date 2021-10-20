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

    def nb_nodes(self):
        return len(self.__nodes)

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
                admin_names[page_name].append(user.get_name())

        return admins_names

    """
    def get_increasing_name_nodes(self):
        return
    """

    # Outils

    """
    Renvoie la liste des clés du dictionnaire __page_dict fusionnée à la liste
    des clés de __user_dict.
    """
    def __merge_keys(self):
        keys = self.__page_dict.keys()
        keys.append(self.__user_dict.keys())
        return keys

