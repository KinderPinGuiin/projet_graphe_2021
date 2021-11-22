import unittest

from classe.Page import Page
from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph


class GraphTests(unittest.TestCase):

    # Tests

    def test_init(self):
        graph = Graph()
        # Test si le graphe est vide
        self.assertEqual(
            graph.nb_nodes(), 0,
            "Le graphe est censé être vide"
        )
        # Test le nombre d'arête
        self.assertEqual(
            graph.nb_lines(), 0,
            "Le graphe ne doit pas posséder d'arêtes"
        )
        print("\n-----\nPost initialisation : Ok.\n-----")

    def test_insert(self):
        graph = self.__create_graph()
        # Test nb pages / utilisateurs
        self.assertEqual(
            graph.get_nb_users(), 1,
            "Il devrait y avoir 1 utilisateur dans le graphe"
        )
        self.assertEqual(
            graph.get_nb_pages(), 1,
            "Il devrait y avoir 1 page dans le graphe"
        )
        print("\n-----\nPost insertion sommet : Ok.\n-----")

    def test_add_line(self):
        graph = self.__create_graph()
        # Test nb d'arêtes
        self.assertEqual(
            graph.nb_lines(), 1,
            "Il devrait y avoir 1 arête dans le graphe"
        )
        print("\n-----\nPost insertion arête : Ok.\n-----")

    def test_delete(self):
        graph = self.__create_graph()
        # Suppression de l'utilisateur
        graph.delete_node(graph.get_node_by_name("Dupond"))
        # Test nb utilisateur / pages
        self.assertEqual(
            graph.get_nb_users(), 0,
            "L'utilisateur aurait dû être supprimé"
        )
        self.assertEqual(
            graph.get_nb_pages(), 1,
            "La page n'aurait pas dû être supprimée"
        )
        print("\n-----\nPost suppression sommet : Ok.\n-----")

    def test_delete_line(self):
        graph = self.__create_graph()
        # Suppression arête
        graph.delete_line("Dupond", "Coloriages de Jean")
        # Test nb d'arêtes
        self.assertEqual(
            graph.nb_lines(), 0,
            "Il ne devrait plus y avoir d'arête dans le graphe"
        )
        print("\n-----\nPost suppression arête : Ok.\n-----")

    # Outils

    def __create_graph(self) -> Graph:
        graph = Graph()
        # Ajout d'un utilisateur
        jean = Utilisateur("Dupond", "Jean", 30)
        graph.add_node(jean)
        # Ajout d'une page
        graph.add_node(Page("Coloriages de Jean", jean))
        # Ajout d'une liaison
        graph.add_line("Dupond", "Coloriages de Jean")
        return graph


if __name__ == '__main__':
    unittest.main()
