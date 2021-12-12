import unittest
import os

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

    def test_save_load(self):
        graph = self.__create_graph()
        # Sauvegarde et recharge le graph
        graph.save_graph("_tmp_test.json")
        graph.load_graph("_tmp_test.json")
        # Suppression du fichier
        os.remove("_tmp_test.json")
        # Lancement des tests
        self.assertEqual(
            graph.nb_lines(), 1, 
            "Le graph est corrompu après sauvegarde (Nombre invalide d'arête)"
        )
        self.assertEqual(
            graph.nb_nodes(), 2, 
            "Le graph est corrompu après sauvegarde (Nombre invalide de sommet)"
        )
        print("\n-----\nPost sauvegarde / chargement du graph : Ok.\n-----")

    def test_shortest_distance(self):
        graph = self.__create_graph()
        graph.add_node(Utilisateur("Test", "Test", 20))
        # Vérifie les plus courtes distances des sommets
        self.assertEqual(
            graph.shortest_distance("Dupond"), {
                "Coloriages de Jean": 1,
                "Dupond": 0,
                "Test": 1000000
            },
            "L'algorithme des distances les plus courtes ne renvoie pas le bon"
            + " résultat"
        )
        print("\n-----\nPost distances les plus courtes : Ok.\n-----")
    
    def test_random_graph(self):
        graph = Graph()
        graph.random_graph(512, 463)
        # Vérifie le nombre d'arêtes et de sommets
        self.assertEqual(
            graph.nb_nodes(), 512,
            "Le graphe aléatoire ne contient pas le bon nombre de sommet"
        )
        self.assertEqual(
            graph.nb_lines(), 463,
            "Le graphe aléatoire ne contient pas le bon nombre d'arêtes"
        )
        print("\n-----\nPost graphe aléatoire : Ok.\n-----")

    # Outils

    def __create_graph(self) -> Graph:
        graph = Graph()
        # Ajout d'un utilisateur
        jean = Utilisateur("Dupond", "Jean", 30)
        graph.add_node(jean)
        # Ajout d'une page
        graph.add_node(Page("Coloriages de Jean", [jean]))
        # Ajout d'une liaison
        graph.add_line("Dupond", "Coloriages de Jean")
        return graph


if __name__ == '__main__':
    unittest.main()
