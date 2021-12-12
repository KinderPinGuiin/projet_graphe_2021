# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(871, 633))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.gridGroupBox.setMaximumSize(QtCore.QSize(193, 16777215))
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.gridGroupBox)
        self.verticalGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userRadio = QtWidgets.QRadioButton(self.verticalGroupBox)
        self.userRadio.setChecked(True)
        self.userRadio.setObjectName("userRadio")
        self.verticalLayout.addWidget(self.userRadio)
        self.pageRadio = QtWidgets.QRadioButton(self.verticalGroupBox)
        self.pageRadio.setObjectName("pageRadio")
        self.verticalLayout.addWidget(self.pageRadio)
        self.gridLayout.addWidget(self.verticalGroupBox, 0, 0, 1, 1)
        self.ageFrame = QtWidgets.QFrame(self.gridGroupBox)
        self.ageFrame.setEnabled(True)
        self.ageFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.ageFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ageFrame.setObjectName("ageFrame")
        self.ageLayout = QtWidgets.QVBoxLayout(self.ageFrame)
        self.ageLayout.setObjectName("ageLayout")
        self.ageLabel = QtWidgets.QLabel(self.ageFrame)
        self.ageLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ageLabel.setObjectName("ageLabel")
        self.ageLayout.addWidget(self.ageLabel)
        self.ageBox = QtWidgets.QSpinBox(self.ageFrame)
        self.ageBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ageBox.setProperty("showGroupSeparator", False)
        self.ageBox.setMinimum(1)
        self.ageBox.setSingleStep(1)
        self.ageBox.setDisplayIntegerBase(10)
        self.ageBox.setObjectName("ageBox")
        self.ageLayout.addWidget(self.ageBox)
        self.gridLayout.addWidget(self.ageFrame, 4, 0, 1, 1)
        self.adminFrame = QtWidgets.QFrame(self.gridGroupBox)
        self.adminFrame.setMinimumSize(QtCore.QSize(0, 103))
        self.adminFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.adminFrame.setObjectName("adminFrame")
        self.adminLayout = QtWidgets.QVBoxLayout(self.adminFrame)
        self.adminLayout.setObjectName("adminLayout")
        self.adminLabel = QtWidgets.QLabel(self.adminFrame)
        self.adminLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.adminLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.adminLabel.setObjectName("adminLabel")
        self.adminLayout.addWidget(self.adminLabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.adminListSearch = QtWidgets.QLineEdit(self.adminFrame)
        self.adminListSearch.setMaximumSize(QtCore.QSize(16777215, 20))
        self.adminListSearch.setFrame(False)
        self.adminListSearch.setObjectName("adminListSearch")
        self.verticalLayout_2.addWidget(self.adminListSearch)
        self.adminList = QtWidgets.QListWidget(self.adminFrame)
        self.adminList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.adminList.setDragEnabled(False)
        self.adminList.setDragDropOverwriteMode(False)
        self.adminList.setAlternatingRowColors(False)
        self.adminList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.adminList.setMovement(QtWidgets.QListView.Static)
        self.adminList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.adminList.setViewMode(QtWidgets.QListView.ListMode)
        self.adminList.setUniformItemSizes(False)
        self.adminList.setWordWrap(False)
        self.adminList.setSelectionRectVisible(True)
        self.adminList.setObjectName("adminList")
        self.verticalLayout_2.addWidget(self.adminList)
        self.adminLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.adminFrame, 5, 0, 1, 1)
        self.firstnameFrame = QtWidgets.QFrame(self.gridGroupBox)
        self.firstnameFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.firstnameFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.firstnameFrame.setObjectName("firstnameFrame")
        self.firstnameLayout = QtWidgets.QVBoxLayout(self.firstnameFrame)
        self.firstnameLayout.setObjectName("firstnameLayout")
        self.firstnameLabel = QtWidgets.QLabel(self.firstnameFrame)
        self.firstnameLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.firstnameLabel.setObjectName("firstnameLabel")
        self.firstnameLayout.addWidget(self.firstnameLabel)
        self.firstnameEdit = QtWidgets.QLineEdit(self.firstnameFrame)
        self.firstnameEdit.setMaxLength(20)
        self.firstnameEdit.setObjectName("firstnameEdit")
        self.firstnameLayout.addWidget(self.firstnameEdit)
        self.gridLayout.addWidget(self.firstnameFrame, 3, 0, 1, 1)
        self.createButton = QtWidgets.QPushButton(self.gridGroupBox)
        self.createButton.setObjectName("createButton")
        self.gridLayout.addWidget(self.createButton, 7, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridGroupBox)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 6, 0, 1, 1)
        self.nameFrame = QtWidgets.QFrame(self.gridGroupBox)
        self.nameFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.nameFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nameFrame.setObjectName("nameFrame")
        self.nameLayout = QtWidgets.QVBoxLayout(self.nameFrame)
        self.nameLayout.setObjectName("nameLayout")
        self.nameLabel = QtWidgets.QLabel(self.nameFrame)
        self.nameLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.nameLabel.setObjectName("nameLabel")
        self.nameLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.nameFrame)
        self.nameEdit.setMaxLength(20)
        self.nameEdit.setObjectName("nameEdit")
        self.nameLayout.addWidget(self.nameEdit)
        self.gridLayout.addWidget(self.nameFrame, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(5, 4)
        self.gridLayout.setRowStretch(6, 2)
        self.horizontalLayout_3.addWidget(self.gridGroupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.graphTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.graphTab)
        self.verticalGroupBox_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_5.setContentsMargins(1, 0, 1, 1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridFrame_3 = QtWidgets.QFrame(self.verticalGroupBox_2)
        self.gridFrame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.gridFrame_3.setObjectName("gridFrame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridFrame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.gridFrame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineNbBox = QtWidgets.QSpinBox(self.gridFrame_3)
        self.lineNbBox.setReadOnly(True)
        self.lineNbBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.lineNbBox.setMaximum(1000)
        self.lineNbBox.setObjectName("lineNbBox")
        self.gridLayout_3.addWidget(self.lineNbBox, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.gridFrame_3)
        self.linesList = QtWidgets.QListWidget(self.verticalGroupBox_2)
        self.linesList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.linesList.setObjectName("linesList")
        self.verticalLayout_5.addWidget(self.linesList)
        self.gridLayout_5.addWidget(self.verticalGroupBox_2, 1, 0, 1, 1)
        self.verticalGroupBox1 = QtWidgets.QGroupBox(self.graphTab)
        self.verticalGroupBox1.setMaximumSize(QtCore.QSize(250, 16777215))
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_3.setContentsMargins(1, 0, 1, 1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridFrame_2 = QtWidgets.QFrame(self.verticalGroupBox1)
        self.gridFrame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.gridFrame_2.setObjectName("gridFrame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridFrame_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.nodeNbBox = QtWidgets.QSpinBox(self.gridFrame_2)
        self.nodeNbBox.setReadOnly(True)
        self.nodeNbBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.nodeNbBox.setMaximum(1000)
        self.nodeNbBox.setObjectName("nodeNbBox")
        self.gridLayout_2.addWidget(self.nodeNbBox, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.gridFrame_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.nodesSortCombo = QtWidgets.QComboBox(self.verticalGroupBox1)
        self.nodesSortCombo.setObjectName("nodesSortCombo")
        self.nodesSortCombo.addItem("")
        self.nodesSortCombo.addItem("")
        self.nodesSortCombo.addItem("")
        self.nodesSortCombo.addItem("")
        self.nodesSortCombo.addItem("")
        self.verticalLayout_6.addWidget(self.nodesSortCombo)
        self.nodesList = QtWidgets.QListWidget(self.verticalGroupBox1)
        self.nodesList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.nodesList.setObjectName("nodesList")
        self.verticalLayout_6.addWidget(self.nodesList)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.gridLayout_5.addWidget(self.verticalGroupBox1, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.graphTab)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBox)
        self.webEngineView.setProperty("url", QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_7.addWidget(self.webEngineView)
        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 2, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.tabWidget.addTab(self.graphTab, "")
        self.usersTab = QtWidgets.QWidget()
        self.usersTab.setObjectName("usersTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.usersTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_4 = QtWidgets.QWidget(self.usersTab)
        self.widget_4.setMaximumSize(QtCore.QSize(190, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6.addWidget(self.widget_4, 2, 0, 1, 1)
        self.deleteNodeButton = QtWidgets.QPushButton(self.usersTab)
        self.deleteNodeButton.setMaximumSize(QtCore.QSize(190, 16777215))
        self.deleteNodeButton.setObjectName("deleteNodeButton")
        self.gridLayout_6.addWidget(self.deleteNodeButton, 3, 0, 1, 1)
        self.gridGroupBox_2 = QtWidgets.QGroupBox(self.usersTab)
        self.gridGroupBox_2.setMaximumSize(QtCore.QSize(190, 16777215))
        self.gridGroupBox_2.setObjectName("gridGroupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridGroupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.userNbBox = QtWidgets.QSpinBox(self.gridGroupBox_2)
        self.userNbBox.setReadOnly(True)
        self.userNbBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.userNbBox.setMaximum(1000)
        self.userNbBox.setObjectName("userNbBox")
        self.gridLayout_4.addWidget(self.userNbBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.gridGroupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.avgAgeBox = QtWidgets.QSpinBox(self.gridGroupBox_2)
        self.avgAgeBox.setReadOnly(True)
        self.avgAgeBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.avgAgeBox.setMaximum(1000)
        self.avgAgeBox.setObjectName("avgAgeBox")
        self.gridLayout_4.addWidget(self.avgAgeBox, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.gridGroupBox_2, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.detailsGroupBox = QtWidgets.QGroupBox(self.usersTab)
        self.detailsGroupBox.setMaximumSize(QtCore.QSize(690, 16777215))
        self.detailsGroupBox.setObjectName("detailsGroupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.detailsGroupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formGroupBox = QtWidgets.QGroupBox(self.detailsGroupBox)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(30, -1, 30, -1)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.nameDisplay = QtWidgets.QLineEdit(self.formGroupBox)
        self.nameDisplay.setReadOnly(True)
        self.nameDisplay.setObjectName("nameDisplay")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameDisplay)
        self.label_6 = QtWidgets.QLabel(self.formGroupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.firstnameDisplay = QtWidgets.QLineEdit(self.formGroupBox)
        self.firstnameDisplay.setReadOnly(True)
        self.firstnameDisplay.setObjectName("firstnameDisplay")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstnameDisplay)
        self.label_7 = QtWidgets.QLabel(self.formGroupBox)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.ageDisplay = QtWidgets.QSpinBox(self.formGroupBox)
        self.ageDisplay.setReadOnly(True)
        self.ageDisplay.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ageDisplay.setMaximum(1000)
        self.ageDisplay.setObjectName("ageDisplay")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ageDisplay)
        self.verticalLayout_10.addWidget(self.formGroupBox, 0, QtCore.Qt.AlignVCenter)
        self.verticalGroupBox_3 = QtWidgets.QGroupBox(self.detailsGroupBox)
        self.verticalGroupBox_3.setObjectName("verticalGroupBox_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_13.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pageAdminList = QtWidgets.QListWidget(self.verticalGroupBox_3)
        self.pageAdminList.setObjectName("pageAdminList")
        self.verticalLayout_13.addWidget(self.pageAdminList)
        self.verticalLayout_10.addWidget(self.verticalGroupBox_3)
        self.verticalGroupBox2 = QtWidgets.QGroupBox(self.detailsGroupBox)
        self.verticalGroupBox2.setObjectName("verticalGroupBox2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalGroupBox2)
        self.verticalLayout_11.setContentsMargins(1, -1, 1, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_15.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.deleteLineCombo = QtWidgets.QComboBox(self.verticalGroupBox2)
        self.deleteLineCombo.setObjectName("deleteLineCombo")
        self.deleteLineCombo.addItem("")
        self.verticalLayout_15.addWidget(self.deleteLineCombo)
        self.widget_2 = QtWidgets.QWidget(self.verticalGroupBox2)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_15.addWidget(self.widget_2)
        self.deleteLineButton = QtWidgets.QPushButton(self.verticalGroupBox2)
        self.deleteLineButton.setObjectName("deleteLineButton")
        self.verticalLayout_15.addWidget(self.deleteLineButton)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.line = QtWidgets.QFrame(self.verticalGroupBox2)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(0, 6, 0, -1)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.nodeCombo = QtWidgets.QComboBox(self.verticalGroupBox2)
        self.nodeCombo.setPlaceholderText("")
        self.nodeCombo.setObjectName("nodeCombo")
        self.nodeCombo.addItem("")
        self.verticalLayout_12.addWidget(self.nodeCombo)
        self.widget_3 = QtWidgets.QWidget(self.verticalGroupBox2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_12.addWidget(self.widget_3)
        self.addLineButton = QtWidgets.QPushButton(self.verticalGroupBox2)
        self.addLineButton.setObjectName("addLineButton")
        self.verticalLayout_12.addWidget(self.addLineButton)
        self.horizontalLayout.addLayout(self.verticalLayout_12)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addWidget(self.verticalGroupBox2)
        self.gridLayout_6.addWidget(self.detailsGroupBox, 0, 1, 4, 1)
        self.verticalGroupBox3 = QtWidgets.QGroupBox(self.usersTab)
        self.verticalGroupBox3.setMaximumSize(QtCore.QSize(190, 16777215))
        self.verticalGroupBox3.setObjectName("verticalGroupBox3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalGroupBox3)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.userCombo = QtWidgets.QComboBox(self.verticalGroupBox3)
        self.userCombo.setObjectName("userCombo")
        self.userCombo.addItem("")
        self.verticalLayout_4.addWidget(self.userCombo)
        self.gridLayout_6.addWidget(self.verticalGroupBox3, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 4)
        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_6.setRowStretch(2, 3)
        self.tabWidget.addTab(self.usersTab, "")
        self.PagesTab = QtWidgets.QWidget()
        self.PagesTab.setObjectName("PagesTab")
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.PagesTab)
        self.horizontalGroupBox_2.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.pageNbBox = QtWidgets.QSpinBox(self.horizontalGroupBox_2)
        self.pageNbBox.setReadOnly(True)
        self.pageNbBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pageNbBox.setMaximum(1000)
        self.pageNbBox.setObjectName("pageNbBox")
        self.horizontalLayout_2.addWidget(self.pageNbBox)
        self.formGroupBox_2 = QtWidgets.QGroupBox(self.PagesTab)
        self.formGroupBox_2.setGeometry(QtCore.QRect(30, 207, 401, 71))
        self.formGroupBox_2.setObjectName("formGroupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox_2)
        self.formLayout_2.setContentsMargins(30, -1, 30, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.formGroupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.namePageDisplay = QtWidgets.QLineEdit(self.formGroupBox_2)
        self.namePageDisplay.setReadOnly(True)
        self.namePageDisplay.setObjectName("namePageDisplay")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.namePageDisplay)
        self.verticalGroupBox_4 = QtWidgets.QGroupBox(self.PagesTab)
        self.verticalGroupBox_4.setGeometry(QtCore.QRect(30, 300, 401, 281))
        self.verticalGroupBox_4.setObjectName("verticalGroupBox_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalGroupBox_4)
        self.verticalLayout_14.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.listAdmin = QtWidgets.QListWidget(self.verticalGroupBox_4)
        self.listAdmin.setObjectName("listAdmin")
        self.verticalLayout_14.addWidget(self.listAdmin)
        self.verticalGroupBox_5 = QtWidgets.QGroupBox(self.PagesTab)
        self.verticalGroupBox_5.setGeometry(QtCore.QRect(20, 90, 190, 75))
        self.verticalGroupBox_5.setMaximumSize(QtCore.QSize(190, 16777215))
        self.verticalGroupBox_5.setObjectName("verticalGroupBox_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalGroupBox_5)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pageCombo = QtWidgets.QComboBox(self.verticalGroupBox_5)
        self.pageCombo.setObjectName("pageCombo")
        self.pageCombo.addItem("")
        self.verticalLayout_8.addWidget(self.pageCombo)
        self.tabWidget.addTab(self.PagesTab, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_3.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOutil = QtWidgets.QMenu(self.menuBar)
        self.menuOutil.setObjectName("menuOutil")
        MainWindow.setMenuBar(self.menuBar)
        self.actionCharger_un_graphe = QtWidgets.QAction(MainWindow)
        self.actionCharger_un_graphe.setObjectName("actionCharger_un_graphe")
        self.actionFermer = QtWidgets.QAction(MainWindow)
        self.actionFermer.setObjectName("actionFermer")
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setObjectName("actionA_propos")
        self.actionSauvegarder = QtWidgets.QAction(MainWindow)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionCharger = QtWidgets.QAction(MainWindow)
        self.actionCharger.setObjectName("actionCharger")
        self.actionGraphe_al_atoire = QtWidgets.QAction(MainWindow)
        self.actionGraphe_al_atoire.setObjectName("actionGraphe_al_atoire")
        self.menuFichier.addAction(self.actionSauvegarder)
        self.menuFichier.addAction(self.actionCharger)
        self.menuOutil.addAction(self.actionGraphe_al_atoire)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuOutil.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.userRadio.toggled['bool'].connect(self.firstnameFrame.show) # type: ignore
        self.userRadio.toggled['bool'].connect(self.ageFrame.show) # type: ignore
        self.userRadio.toggled['bool'].connect(self.adminFrame.hide) # type: ignore
        self.pageRadio.toggled['bool'].connect(self.firstnameFrame.hide) # type: ignore
        self.pageRadio.toggled['bool'].connect(self.ageFrame.hide) # type: ignore
        self.pageRadio.toggled['bool'].connect(self.adminFrame.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.userRadio, self.pageRadio)
        MainWindow.setTabOrder(self.pageRadio, self.nameEdit)
        MainWindow.setTabOrder(self.nameEdit, self.firstnameEdit)
        MainWindow.setTabOrder(self.firstnameEdit, self.ageBox)
        MainWindow.setTabOrder(self.ageBox, self.adminListSearch)
        MainWindow.setTabOrder(self.adminListSearch, self.adminList)
        MainWindow.setTabOrder(self.adminList, self.createButton)
        MainWindow.setTabOrder(self.createButton, self.nodeNbBox)
        MainWindow.setTabOrder(self.nodeNbBox, self.nodesSortCombo)
        MainWindow.setTabOrder(self.nodesSortCombo, self.nodesList)
        MainWindow.setTabOrder(self.nodesList, self.lineNbBox)
        MainWindow.setTabOrder(self.lineNbBox, self.linesList)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projet Graphe 2021"))
        self.userRadio.setText(_translate("MainWindow", "Utilisateur"))
        self.pageRadio.setText(_translate("MainWindow", "Page"))
        self.ageLabel.setText(_translate("MainWindow", "Age"))
        self.adminLabel.setText(_translate("MainWindow", "Admins"))
        self.adminListSearch.setPlaceholderText(_translate("MainWindow", "Filtrer ..."))
        self.adminList.setSortingEnabled(False)
        self.firstnameLabel.setText(_translate("MainWindow", "Prénom"))
        self.createButton.setText(_translate("MainWindow", "Créer"))
        self.nameLabel.setText(_translate("MainWindow", "Nom"))
        self.verticalGroupBox_2.setTitle(_translate("MainWindow", "Arcs"))
        self.label_2.setText(_translate("MainWindow", "Nombre: "))
        self.verticalGroupBox1.setTitle(_translate("MainWindow", "Sommets"))
        self.label.setText(_translate("MainWindow", "Nombre: "))
        self.nodesSortCombo.setItemText(0, _translate("MainWindow", "-- Trier par --"))
        self.nodesSortCombo.setItemText(1, _translate("MainWindow", "Nom croissant"))
        self.nodesSortCombo.setItemText(2, _translate("MainWindow", "Nom décroissant"))
        self.nodesSortCombo.setItemText(3, _translate("MainWindow", "Degré croissant"))
        self.nodesSortCombo.setItemText(4, _translate("MainWindow", "Degré décroissant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("MainWindow", "Graphe"))
        self.deleteNodeButton.setText(_translate("MainWindow", "Supprimer"))
        self.label_3.setText(_translate("MainWindow", "Nombre: "))
        self.label_8.setText(_translate("MainWindow", "Age moyen: "))
        self.formGroupBox.setTitle(_translate("MainWindow", "Détails"))
        self.label_5.setText(_translate("MainWindow", "Nom: "))
        self.label_6.setText(_translate("MainWindow", "Prénom: "))
        self.label_7.setText(_translate("MainWindow", "Age: "))
        self.verticalGroupBox_3.setTitle(_translate("MainWindow", "Page(s) administrée(s)"))
        self.verticalGroupBox2.setTitle(_translate("MainWindow", "Gérer les arcs vers les sommets"))
        self.deleteLineCombo.setItemText(0, _translate("MainWindow", "-- Sélectionner --"))
        self.deleteLineButton.setText(_translate("MainWindow", "Supprimer"))
        self.nodeCombo.setItemText(0, _translate("MainWindow", "-- Sélectionner --"))
        self.addLineButton.setText(_translate("MainWindow", "Ajouter"))
        self.verticalGroupBox3.setTitle(_translate("MainWindow", "Sélectionner un Utilisateur"))
        self.userCombo.setItemText(0, _translate("MainWindow", "-- Sélectionner --"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usersTab), _translate("MainWindow", "Utilisateurs"))
        self.label_4.setText(_translate("MainWindow", "Nombre: "))
        self.formGroupBox_2.setTitle(_translate("MainWindow", "Détails"))
        self.label_10.setText(_translate("MainWindow", "Nom: "))
        self.verticalGroupBox_4.setTitle(_translate("MainWindow", "Administateurs :"))
        self.verticalGroupBox_5.setTitle(_translate("MainWindow", "Sélectionner une page"))
        self.pageCombo.setItemText(0, _translate("MainWindow", "-- Sélectionner --"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PagesTab), _translate("MainWindow", "Pages"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuOutil.setTitle(_translate("MainWindow", "Outil"))
        self.actionCharger_un_graphe.setText(_translate("MainWindow", "Charger un graphe"))
        self.actionFermer.setText(_translate("MainWindow", "Fermer"))
        self.actionA_propos.setText(_translate("MainWindow", "A propos"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder..."))
        self.actionCharger.setText(_translate("MainWindow", "Charger..."))
        self.actionGraphe_al_atoire.setText(_translate("MainWindow", "Graphe aléatoire"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
