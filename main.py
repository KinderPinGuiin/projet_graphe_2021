from classe.Page import Page
from classe.Utilisateur import Utilisateur
from classe.graph.Graphe import Graph
import time

start_time = time.perf_counter()
test = Graph()
test.load_graph("test")
print(test.page_rank())

# print([node.get_node().get_name() for node in test.get_nodes()], test.get_lines())
# print("--- " + str(time.perf_counter() - start_time) + " seconds ---")
=======
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox
import sys
from gui.gui import Ui_MainWindow
import re

class Ui(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.show()

        self.adminFrame.hide()
        self.createButton.setEnabled(False)
        
        self.__create_model()
        self.__update_ui()
        #self.signinButton.setText('&S\'inscrire')
        self.__create_controler()
        self.setWindowTitle('Projet Graphe 2021')
        self.adminList.setSortingEnabled(True)



    def __create_model(self):
        self.model = Graph()
        self.model.load_graph("test")
        #print([node.get_node().get_name() for node in self.model.get_nodes()], self.model.get_lines())


    def __create_controler(self):

        self.nameEdit.textChanged.connect(self.__create_enable)
        self.firstnameEdit.textChanged.connect(self.__create_enable)
        self.adminList.itemSelectionChanged.connect(self.__create_enable)
        self.pageRadio.toggled.connect(self.__create_enable)
        self.userRadio.toggled.connect(self.__create_enable)

        self.createButton.clicked.connect(self.__create)
        
        self.adminListSearch.textChanged.connect(self.__filter_amdinlist)
        

    def __create_enable(self):
        b = bool(self.nameEdit.text() and
                 ((self.userRadio.isChecked() and self.firstnameEdit.text()) or
                  (self.pageRadio.isChecked() and len(self.adminList.selectedItems()) > 0 )))
        self.createButton.setEnabled(b)

    
    def __filter_amdinlist(self):
        for i in range (self.adminList.count()):
            item = self.adminList.item(i)
            pattern = self.adminListSearch.text()
            string = item.text()
            item.setHidden(re.match(pattern, string, re.IGNORECASE) == None)
                

    def __create(self):
        popup = QMessageBox()

        if self.model.get_node_by_name(self.nameEdit.text()) == None:
            if self.userRadio.isChecked():
                node = Utilisateur(self.nameEdit.text(), self.firstnameEdit.text(), int(self.ageBox.text()))

                msg = "Utilisateur créé avec succès."

            elif self.pageRadio.isChecked():
                admins = [self.model.get_node_by_name(item.text()) for item in  self.adminList.selectedItems()]
                print(admins)
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


    def __update_ui(self):
        self.adminList.clear()
        for item in self.model.get_user_dict().keys():
            self.adminList.addItem(item)


    def __admins(self):
        print([item.text() for item in self.adminList.selectedItems()])
        #print(len(self.adminList.selectedItems()))


##########################################################################


# class Ui(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(Ui, self).__init__()
#         uic.loadUi('test.ui', self)
#         self.show()

#         self.adminFrame.hide()


if __name__ == "__main__":
    sys.argv += ['--style', 'default']
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())

"""
test.add_node(Utilisateur("Dupont", "Bernard", 56))
test.add_node(Utilisateur("Dupond", "Jean", 23))
test.add_node(Page("NARUTO FAN"))
test.add_line("Dupont", "NARUTO FAN")
test.add_line("Dupont", "Dupond")
test.add_line("NARUTO FAN", "Dupont")
"""
