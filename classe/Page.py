from classe.graph.Sommet import Sommet
from classe.Utilisateur import Utilisateur


class Page(Sommet):
    def __init__(self, name: str, admins: list[Utilisateur] = []):
        Sommet.__init__(self, name)
        self.__admins = admins

    def get_admins(self):
        return self.__admins
