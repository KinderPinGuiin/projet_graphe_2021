import json
from typing import Callable, Union

import faker

from classe.Utilisateur import Utilisateur
from classe.graph.Sommet import Sommet
from classe.graph.IGraphe import IGraphe
from classe.Page import Page
from classe.graph.GraphCellule import GraphCellule
import random
from faker import *


class Graph(IGraphe):
    # Constructeur
    def __init__(self):
        self.__nodes = list[GraphCellule]()
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
        assert name is not None
        cell = self.__get_cell_by_name(name)
        if cell is None:
            return None
        return cell.get_node()

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

        return 0 if total == 0 else int(total / len(self.__user_dict))

    def get_admins(self):
        admins_names = dict()
        for page in self.__page_dict.values():
            page_name = page.get_node().get_name()
            admins_names[page_name] = list[str]()
            for user in page.get_node().get_admins():
                admins_names[page_name].append(user)

        return admins_names


    def get_lines(self):
        result = []
        for nodes_src in self.__nodes:
            for nodes_dst in nodes_src.get_succ_list():
                result.append(
                    (nodes_src.get_node().get_name(), nodes_dst.get_name())
                )

        return result

    def get_increasing_name_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: cell.get_node().get_name())

    def get_decreasing_name_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: cell.get_node().get_name(), True)

    def get_increasing_degree_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: len(cell.get_succ_list()))

    def get_decreasing_degree_nodes(self) -> list[Sommet]:
        return self.__sort_nodes(lambda cell: len(cell.get_succ_list()), True)

    # Commandes

    def add_node(self, node: Sommet) -> bool:
        assert node is not None

        nodes = self.get_nodes()
        node_name = node.get_name()

        if not self.is_node_in(node):
            cell = GraphCellule(node, list[Sommet]())
            nodes.append(cell)

            if isinstance(node, Page):
                self.get_page_dict()[node_name] = cell
            else:
                self.get_user_dict()[node_name] = cell
            return True
        else:
            return False

    def delete_node(self, node: Sommet) -> None:
        assert node is not None

        node_name = node.get_name()

        if self.is_node_in(node):
            if isinstance(node, Page):
                cell = self.get_page_dict().get(node_name)
                del self.get_page_dict()[node_name]
            else:
                cell = self.get_user_dict().get(node_name)
                del self.get_user_dict()[node_name]
            del self.__nodes[self.__nodes.index(cell)]

    def add_line(self, node1: str, node2: str) -> bool:
        if node2 in [node.get_name() for node in self.__get_succ_list(node1)]:
            return False
        if node1 == node2:
            return False
        if not self.__check_2_nodes(node1, node2):
            return False
        self.__get_succ_list(node1).append(self.get_node_by_name(node2))
        return True

    def delete_line(self, node1: str, node2: str) -> bool:
        if not self.__check_2_nodes(node1, node2):
            return False
        self.__get_succ_list(node1).remove(self.get_node_by_name(node2))

    def save_graph(self, name: str):
        # Ouverture du fichier
        file = open(name + ("" if name.endswith(".json") else ".json"), "w")
        # Cr??ation du dictionnaire
        graph_dict = self.__create_graph_dict()
        # Parse le dict en JSON et l'??crit dans le fichier
        file.write(json.dumps(graph_dict, indent=4))
        file.close()

    def load_graph(self, name: str):
        # Reset le graphe
        self.__nodes = list[GraphCellule]()
        self.__page_dict = dict()
        self.__user_dict = dict()
        # Ouvre le fichier et parse le JSON
        file = open(name + ("" if name.endswith(".json") else ".json"), "r")
        graph_dict = json.loads(file.read())
        # Re-cr???? le graphe
        self.__create_graph_from_dict(graph_dict)
        file.close()

    def page_rank(self) -> dict:
        if self.nb_nodes() == 0:
            return
        page_rank = dict()
        for node in (self.__page_dict | self.__user_dict):
            page_rank[node] = 1
        i = 0
        while i <= 100:
            for node in page_rank:
                u_sum = 0
                for u in self.__incoming_neighbour(node):
                    u_sum += page_rank[u] / self.__page_rank_degree(u)
                page_rank[node] = (0.15 / self.nb_nodes()) + 0.85 * u_sum
                i += 1
        return page_rank

    def shortest_distance(self, s: str):
        dist = dict()
        for node in (self.__page_dict | self.__user_dict):
            dist[node] = 1000000
        dist[s] = 0
        p = [node.get_node().get_name() for node in self.get_nodes()]
        while len(p) > 0:
            min = 1000000
            u = ""
            for node in p:
                if dist[node] <= min:
                    min = dist[node]
                    u = node
            p.remove(u)
            for v in self.__outgoing_neighbour(u):
                alt = dist[u] + 1
                if alt <= dist[v]:
                    dist[v] = alt
        return dist

    def random_graph(self, nb_node: int, nb_lines: int):
        # Reset le graphe
        self.__nodes = list[GraphCellule]()
        self.__page_dict = dict()
        self.__user_dict = dict()
        # Utilise la librairie Faker afin de g??n??rer des sommets al??atoires
        # https://faker.readthedocs.io/en/master/
        Faker.seed(0)
        fake = Faker("fr_FR")
        i = 0
        while i < nb_node:
            # Cr???? un utilisateur (80% de chance)
            if random.randint(1, 10) <= 8:
                r = self.add_node(
                    Utilisateur(
                        fake.last_name(), 
                        fake.first_name(), 
                        random.randint(13, 100)
                    )
                )
                if r:
                    i += 1
            else:
                # Cr???? une page seulement s'il y a un utilisateur dans le graphe
                if self.get_nb_users() > 0:
                    rand_usr = random.choice(list(self.__user_dict.values()))
                    r = self.add_node(
                        Page(
                            fake.sentence(nb_words=3),
                            [rand_usr.get_node()]
                        )
                    )
                    if r:
                        i += 1
        # Ar??tes al??atoires
        i = 0
        user_list = list((self.__user_dict).values())
        user_page_list = list((self.__user_dict | self.__page_dict).values())
        while i < nb_lines:
            rand_node_1 = random.choice(user_list).get_node().get_name()
            rand_node_2 = random.choice(user_page_list).get_node().get_name()
            if self.add_line(rand_node_1, rand_node_2):
                i += 1

    # Outils

    """
    Renvoie la cellule correspondante au sommet de nom name. Renvoie la cellule
    si celle-ci est trouv??e et None sinon.
    """
    def __get_cell_by_name(self, name: str) -> GraphCellule:
        cell = self.get_user_dict().get(name) or self.get_page_dict().get(name)
        if cell is None:
            return None
        node_index = self.__nodes.index(cell)
        if node_index is not None:
            return self.get_nodes()[node_index]
        return None

    """
    Renvoie la liste des sommets associ??s au graphe tri??s par nom de mani??re
    croissante si reverse vaut True, et de mani??re d??croissante sinon.
    """
    def __sort_nodes(self, key: Callable, reverse: bool = False) -> list[Sommet]:
        sorted_cells = sorted(self.__nodes, key=key, reverse=reverse)
        return [cell.get_node() for cell in sorted_cells]

    """
    Teste l'existence de 2 noeuds dans le graphe et v??rifie qu'ils ne sont pas
    nuls. Arr??te le programme si l'un des deux noeuds est nul, renvoie True si
    les deux noeuds existent dans le graphe et False sinon.
    """
    def __check_2_nodes(self, node1_str: str, node2_str: str) -> bool:
        assert node1_str is not None and node1_str is not None
        if ((node1_str in self.__user_dict)
            or (node1_str in self.__page_dict)) \
                and ((node2_str in self.__user_dict)
                     or (node2_str in self.__page_dict)):
            return True
        return False

    """
    Renvoie les successeurs du sommet node. Renvoie None si node n'a pas de
    successeur.
    """
    def __get_succ_list(self, node: str) -> list[Sommet]:
        cell = self.__get_cell_by_name(node)
        if cell is None:
            return None
        return cell.get_succ_list()

    """
    Cr???? un dictionnaire contenant toutes les infos du graphe.
    """
    def __create_graph_dict(self):
        graph_dict = dict()
        for cell in self.__nodes:
            node = cell.get_node()
            graph_dict[node.get_name()] = {
                "type": "p" if isinstance(node, Page) else "u",
                "succ": [succ.get_name() for succ in cell.get_succ_list()]
            }
            if isinstance(node, Page):
                graph_dict[node.get_name()]["admins"] = \
                    [admin.get_name() for admin in node.get_admins()]
            else:
                graph_dict[node.get_name()]["firstname"] = node.get_firstname()
                graph_dict[node.get_name()]["age"] = node.get_age()
        return graph_dict

    """
    Cr???? le graphe de l'instance courante via le dictionnaire graph_dict.
    """
    def __create_graph_from_dict(self, graph_dict: dict):
        for node_name in graph_dict:
            # Cr??ation du sommet s'il n'est pas d??j?? dans le graphe
            if self.get_node_by_name(node_name) is None:
                self.__create_dict_node(graph_dict, node_name)
            # Cr??ation de ses ar??tes
            for succ in graph_dict[node_name]["succ"]:
                # Si le successeur n'est pas dans le graphe on l'ajoute
                if self.get_node_by_name(succ) is None:
                    self.__create_dict_node(graph_dict, succ)
                self.add_line(node_name, succ)

    def __create_dict_node(self, graph_dict: dict, node_name: str):
        if graph_dict[node_name]["type"] == "u":
            user = Utilisateur(
                node_name,
                graph_dict[node_name]["firstname"],
                graph_dict[node_name]["age"]
            )
            self.add_node(user)
        else:
            admins = []
            for admin_name in graph_dict[node_name]["admins"]:
                if self.get_node_by_name(admin_name) is None:
                    self.__create_dict_node(graph_dict, admin_name)
                admins.append(self.get_node_by_name(admin_name))
            page = Page(
                node_name,
                admins
            )
            self.add_node(page)

    """
    Renvoie le degr?? sortant du sommet de nom node_name.
    """
    def __outgoing_degree(self, node_name: str) -> int:
        cell = self.__get_cell_by_name(node_name)
        return len(cell.get_succ_list())

    """
    Renvoie le degr?? entrant du sommet de nom node_name.
    """
    def __incoming_degree(self, node_name: str) -> int:
        incoming_nodes = 0
        for cell in self.__nodes:
            for node in cell.get_succ_list():
                if node.get_name() == node_name:
                    incoming_nodes += 1
        return incoming_nodes

    """
    Renvoie le degr?? sortant du sommet de nom node_name ou son degr?? entrant si
    le sortant vaut 0.
    """
    def __page_rank_degree(self, node_name: str) -> int:
        outgoing_degree = self.__outgoing_degree(node_name)
        return outgoing_degree if outgoing_degree > 0 \
            else self.__incoming_degree(node_name)

    """
    Renvoie l'ensemble des noms des voisins entrants du noeud de nom node_name
    """
    def __outgoing_neighbour(self, node_name: str) -> list[str]:
        cell = self.__get_cell_by_name(node_name)
        return [node.get_name() for node in cell.get_succ_list()]

    """
    Renvoie l'ensemble des noms des voisins sortants du noeud de nom node_name
    """
    def __incoming_neighbour(self, node_name: str) -> list[str]:
        out_neighbours = []
        for cell in self.__nodes:
            for node in cell.get_succ_list():
                if node.get_name() == node_name:
                    out_neighbours.append(cell.get_node().get_name())
        return out_neighbours

