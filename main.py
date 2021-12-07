from typing import Match
from classe.Page import Page
from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph

from graph_to_networkx import create_graph_html

from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
from gui.gui import Ui_MainWindow
import re
import os 

"""
Modidication gui.py:
  class Ui_MainWindow(object): -> class Ui_MainWindow(QtWidgets.QMainWindow):
"""

class Ui(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.show()

        self.__create_model()
        self.__create_controler()

        # Panneau de création de sommets
        self.adminFrame.hide()
        self.adminList.setSortingEnabled(True)
        self.createButton.setEnabled(False)
        
        # Le nom du fichier html contenant la modélisation du graphe
        self.graph_filename = "graph.html"

        # Tab Utilisateurs
        self.detailsGroupBox.setEnabled(False)
        self.deleteNodeButton.setEnabled(False)
        self.deleteLineButton.setEnabled(False)
        self.addLineButton.setEnabled(False)

        self.ADD = 0
        self.DELETE = 1

        # Synchronisation avec le fichier json
        self.isSync = True

        self.__update_ui()


    # Création du graph
    def __create_model(self):
        self.model = Graph()


    # Création des controleurs des éléments graphiques
    def __create_controler(self):

        # Panneau de création de Sommets
        self.nameEdit.textChanged.connect(self.__create_enable)
        self.firstnameEdit.textChanged.connect(self.__create_enable)
        self.adminList.itemSelectionChanged.connect(self.__create_enable)
        self.pageRadio.toggled.connect(self.__create_enable)
        self.userRadio.toggled.connect(self.__create_enable)
        self.createButton.clicked.connect(self.__create)
        self.adminListSearch.textChanged.connect(self.__filter_amdinlist)
        
        # Tab Graphe
        self.nodesSortCombo.activated.connect(self.__display_nodesList)

        # Tab Utilisateurs
        self.userCombo.activated.connect(self.__user_details_setup)
        self.deleteNodeButton.clicked.connect(self.__delete_node)
        self.nodeCombo.activated.connect(self.__line_buttons_setup)
        self.deleteLineCombo.activated.connect(self.__line_buttons_setup)
        self.addLineButton.clicked.connect(self.__add_line)
        self.deleteLineButton.clicked.connect(self.__delete_line)

        # Barre de menu
        self.actionCharger.triggered.connect(self.__handle_load)
        self.actionSauvegarder.triggered.connect(self.__handle_save)


    # Raffraichissement de l'interface utilisateur
    def __update_ui(self):
        # Actualisation de la modélisation du graphe
        create_graph_html(self.model, self.graph_filename)
        self.webEngineView.setHtml(open("./" + self.graph_filename, 'r').read())
        
        # Panneau de création de sommets
        self.nameEdit.setText('')
        self.firstnameEdit.setText('')
        self.ageBox.setValue(self.ageBox.minimum())

        # Tab Utilisateurs
        self.userNbBox.setValue(self.model.get_nb_users())
        self.avgAgeBox.setValue(self.model.get_avg_age())
        
        self.userCombo.clear()
        self.userCombo.addItem("-- Sélectionner --")
        self.adminList.clear()
        for item in self.model.get_user_dict().keys():
            self.adminList.addItem(item)
            self.userCombo.addItem(item)
        self.userCombo.setCurrentText(self.nameDisplay.text())
        self.__user_details_setup()



        # Tab Graphe
        self.nodeNbBox.setValue(self.model.get_nb_pages() + self.model.get_nb_users())
        self.__display_nodesList()

        self.lineNbBox.setValue(self.model.nb_lines())
        self.__display_linesList()
        

    # Slot: activation bouton de création de sommet
    def __create_enable(self):
        b = bool(self.nameEdit.text() and
                 ((self.userRadio.isChecked() and self.firstnameEdit.text()) or
                  (self.pageRadio.isChecked() and len(self.adminList.selectedItems()) > 0 )))
        self.createButton.setEnabled(b)

    # Slot: Paramétrage du bloc de détails sur un Utilisateur
    def __user_details_setup(self):
        self.pageAdminList.clear()
        if self.userCombo.currentIndex() == 0:
            self.detailsGroupBox.setDisabled(True)
            self.deleteNodeButton.setDisabled(True)
            self.deleteLineButton.setDisabled(True)
            self.nameDisplay.setText("")
            self.firstnameDisplay.setText("")
            self.ageDisplay.setValue(0)
        else:
            self.detailsGroupBox.setDisabled(False)
            self.deleteNodeButton.setDisabled(False)
            user = self.model.get_node_by_name(self.userCombo.currentText())

            self.nameDisplay.setText(user.get_name())
            self.firstnameDisplay.setText(user.get_firstname())
            self.ageDisplay.setValue(user.get_age())

            admins_dict = self.model.get_admins()
            for key in admins_dict:
                if user in admins_dict[key]:
                    self.pageAdminList.addItem(key)

            self.nodeCombo.clear()
            self.nodeCombo.addItem("-- Sélectionner --")
            node1 = self.model.get_user_dict()[self.nameDisplay.text()]

            for item in self.model.get_nodes():
                node2 = item.get_node()
                if node2.get_name() != node1.get_node().get_name() and \
                    not node2 in node1.get_succ_list():
                    self.nodeCombo.addItem(node2.get_name())
            
            self.deleteLineCombo.clear()
            self.deleteLineCombo.addItem("-- Sélectionner --")
            for item in node1.get_succ_list():
                self.deleteLineCombo.addItem(item.get_name())

    # Slot: activation bouton de création et suppression de liens
    def __line_buttons_setup(self):
        self.deleteLineButton.setDisabled(self.deleteLineCombo.currentIndex() == 0)
        self.addLineButton.setDisabled(self.nodeCombo.currentIndex() == 0)


    # Slot: filtre d'admins
    def __filter_amdinlist(self):
        for i in range (self.adminList.count()):
            item = self.adminList.item(i)
            pattern = self.adminListSearch.text()
            string = item.text()
            item.setHidden(re.match(pattern, string, re.IGNORECASE) == None)
                
    # Slot: création de sommets
    def __create(self):
        self.isSync = False
        popup = QMessageBox()

        if self.model.get_node_by_name(self.nameEdit.text()) == None:
            if self.userRadio.isChecked():
                node = Utilisateur(self.nameEdit.text(), self.firstnameEdit.text(), int(self.ageBox.text()))

                msg = "Utilisateur créé avec succès."

            elif self.pageRadio.isChecked():
                admins = [self.model.get_node_by_name(item.text()) for item in  self.adminList.selectedItems()]
                node = Page(self.nameEdit.text(), admins)

                msg = "Page créée avec succès."

            self.model.add_node(node)

            popup.setWindowTitle("Succès")
            popup.setText(msg)
            popup.setIcon(QMessageBox.Information)

            self.__update_ui()

        else:
            
            popup.setWindowTitle("Erreur")
            popup.setText("Ce nom existe déjà.")
            popup.setStandardButtons(QMessageBox.Close)
            popup.setIcon(QMessageBox.Critical)

        x = popup.exec_()

    # Slot: affichage de la liste des sommets
    def __display_nodesList(self):
        self.nodesList.clear()
        index = self.nodesSortCombo.currentIndex()
        list = []

        if index == 1:
            list = self.model.get_increasing_name_nodes()
        elif index == 2:
            list = self.model.get_decreasing_name_nodes()
        elif index == 3:
            list = self.model.get_increasing_degree_nodes()
        elif index == 4: 
            list = self.model.get_decreasing_degree_nodes()

        for i in list:
            self.nodesList.addItem(i.get_name())

    # Slot: affichage de la liste des liens
    def __display_linesList(self):
        self.linesList.clear()
        
        for i in self.model.get_lines():
            src, dst = i
            self.linesList.addItem(src + " -> " + dst)

    # Slot: suppression d'un sommet
    def __delete_node(self):
        self.isSync = False
        name = self.nameDisplay.text()
        popup = QMessageBox()
        popup.setWindowTitle("Supprimer le sommet ?")
        popup.setText("Vous êtes sur le point de supprimer le sommet " + name)
        popup.setInformativeText("Voulez vous continuer ?")
        popup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        popup.setIcon(QMessageBox.Question)
        res = popup.exec_()
        if res == QMessageBox.Yes:
            self.model.delete_node(self.model.get_node_by_name(name))
            self.userCombo.setCurrentIndex(0)
            self.__user_details_setup()
            self.__update_ui()

    # Slot: ajout d'un lien
    def __add_line(self):
        src = self.nameDisplay.text()
        dst = self.nodeCombo.currentText()

        self.__manage_line(src, dst, self.ADD)

    # Slot: suppression d'un arc
    def __delete_line(self):
        self.isSync = False
        src = self.nameDisplay.text()
        dst = self.deleteLineCombo.currentText()

        self.__manage_line(src, dst, self.DELETE)

    def __manage_line(self, src: str, dst: str, action: int):
        self.isSync = False
        popup = QMessageBox()
        try:
            if action == self.ADD:
                self.model.add_line(src, dst)
                actn = " ajouté "
            elif action == self.DELETE:
                self.model.delete_line(src, dst)
                actn = " supprimé "
                
            popup.setWindowTitle("Succès")
            popup.setText("Arc de " + src + " vers " + dst + actn + "avec succès.")
            popup.setIcon(QMessageBox.Information)
        except:
            if action == self.ADD:
                actn = "L'ajout"
            elif action == self.DELETE:
                actn = "La suppression"
            popup.setWindowTitle("Erreur")
            popup.setText( actn + " de l'arc " + src + " vers " + dst + " a échouée.")
            popup.setIcon(QMessageBox.Critical)
        popup.exec_()
        self.__user_details_setup()
        self.__update_ui()
    
    # Slot: gestion du chargement d'un graphe
    def __handle_load(self):
        file = QFileDialog.getOpenFileName(self, "Charger un graphe", filter="JSON (*.json)")
        if file[0].endswith(".json"):
            self.model.load_graph(file[0])
            self.__update_ui()
        elif not file[0] == "":
            msg = QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Veuillez sélectionner un fichier .json")
            msg.exec_()
    
    # Slot: gestion de la sauvegarde d'un graphe
    def __handle_save(self):
        self.isSync = True
        file = QFileDialog()
        file.setAcceptMode(QFileDialog.AcceptSave)
        if file.exec_():
            self.model.save_graph(file.selectedFiles()[0])

    


    # Redéfinission de la fermeture de l'application
    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        if not self.isSync:
            popup = QMessageBox()
            popup.setWindowTitle("Attention !")
            popup.setText("Cette action va entraîner la perte des données non sauvegardées.")
            popup.setInformativeText("Voulez-vous continuer ?")
            popup.setIcon(QMessageBox.Warning)
            popup.setStandardButtons(QMessageBox.Save | QMessageBox.No | QMessageBox.Yes)
            popup.setDefaultButton(QMessageBox.No)

            
            x = popup.exec_()
            if x == QMessageBox.No:
                e.ignore()
            else:
                os.remove(self.graph_filename)
                if x == QMessageBox.Save:
                    self.__handle_save()
                e.accept()
        else:
            os.remove(self.graph_filename)
            e.accept()
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyle('Macintosh')
    window = Ui()
    sys.exit(app.exec())
