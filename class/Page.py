from graph.Sommet import Sommet


class Page(Sommet):
    def __init__(self, name, admins=[]):
        super(name)
        self.__admins = admins

    def get_admins(self):
        return self.__admins
