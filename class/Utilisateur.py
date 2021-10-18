from graph.Sommet import Sommet


class Utilisateur(Sommet):
    def __init__(self, lastname, firstname, age):
        super(lastname)
        self.__firstname = firstname
        self.__age = age

    def get_firstname(self):
        return self.__firstname

    def get_age(self):
        return self.__age