from graph.Sommet import Sommet


class GraphCellule:

    def __init__(self, s : Sommet, ls : list[Sommet]) -> None:
        self.__node = s
        self.__succ_list = ls

    def get_node(self) -> Sommet:
        return self.__node

    def get_succ_list(self) -> list[Sommet]:
        return self.__succ_list
