from abc import ABC


class Sommet(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
