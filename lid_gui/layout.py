from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import QFile, QTextStream
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 784)
        MainWindow.setStyleSheet("""
QMainWindow{
    background-color:rgb(24, 24, 27);
}
QWidget#centralwidget,QStackedWidget{
    background-color:rgb(24, 24, 27);
}
QWidget#side_bar,#sidebar_2{
    background-color:rgb(38, 38, 38);
    border-top-right-radius:10px;
    border-bottom-right-radius:10px;
    border:1px solid rgb(14, 165, 233);
    width:150px;
}
QWidget#mainWidget{
    background-color:rgb(38, 38, 38);
    border-bottom-left-radius:10px;
    border-bottom-right-radius:10px;
}
QPushButton#resultsButton,#newButton,#filesButton,#historyButton,#resetButton,#helpButton{
    border:none;
    text-align:right;
    height:40;
    width:40;
    border-radius:10px;
}
QPushButton:checked#resultsButton,QPushButton:checked#newButton,QPushButton:checked#filesButton,QPushButton:checked#historyButton,QPushButton:checked#resetButton,QPushButton:checked#helpButton{
    background-color:white;
}
QPushButton#menu{
    border:none;
    height:40;
    width:40;
    border-radius:10px;
}
QLabel#fileslabel{
    color:yellow;
}
QPushButton#resultsButton_2,QPushButton#newButton_2,QPushButton#filesButton_2,QPushButton#historyButton_2,QPushButton#resetButton_2,QPushButton#helpButton_2{
    text-align:left;
    color:rgb(14, 165, 233);
    height:40px;
    border:none;
    border-top-left-radius:10px;
    border-bottom-left-radius:10px;
}
QPushButton:checked#resultsButton_2,QPushButton:checked#newButton_2,QPushButton:checked#filesButton_2,QPushButton:checked#historyButton_2,QPushButton:checked#resetButton_2,QPushButton:checked#helpButton_2{
    background-color:rgb(63, 63, 70);
    color:white;
    font-weight:bold;
}
QLabel#mainlabel{
    color:rgb(132, 204, 22);
    font-weight:bold;
}
QWidget#toolsWidget{
    background-color:rgb(41, 37, 36);
    border-top-left-radius:10px;
    border-bottom-left-radius:10px;
    border:1px solid black;
}
QPushButton#uploadButton,#recordButton,#runButton,#stopButton,QPushButton#clearButton,QPushButton#clearButton_2,QPushButton#saveButton{
    border:none;
    height:40px;
    width:60px;
    border-radius:10px;
    color:rgb(219, 39, 119);
}
QPushButton:hover#uploadButton,QPushButton:hover#clearButton,QPushButton:hover#clearButton_2,QPushButton:hover#recordButton,QPushButton:hover#saveButton{
    background-color:black;
    color:rgb(231, 229, 228);
    font-weight:bold;
}
QPushButton:focus#uploadButton,QPushButton:focus#clearButton,QPushButton:focus#clearButton_2,QPushButton:focus#saveButton,QPushButton:focus#recordButton{
    color:rgb(219, 39, 119);
    border:1px solid rgb(219, 39, 119);
    font-weight:bold;
}
QPushButton:focus#runButton{
    border:1px solid rgb(0,170,250);
    color:rgb(0,170,250);
    font-weight:bold;
}
QPushButton:focus#stopButton{
    color:red;
    border:1px solid red;
    font-weight;
}
QPushButton:hover#runButton{
	background-color:black;
	color:rgb(0,170,250);
        font-weight:70px;
}
QPushButton:hover#stopButton{
    background-color:black;
    color:red;
    font-weight:70px;
}
QTableWidget{
    border: 1px solid yellow;
    border-collapse: collapse;
    border-radius:10px;
    width: 100%;
    background-color:rgb(63, 63, 70);
    color:white;
}
QTabWidget{
    background-color:rgb(225, 225, 225);
}
""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolsWidget = QtWidgets.QWidget(self.centralwidget)
        self.toolsWidget.setObjectName("toolsWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.toolsWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.uploadButton = QtWidgets.QPushButton(self.toolsWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(60)
        font.setFamily("Bahnschrift SemiBold")
        self.uploadButton.setFont(font)
        self.uploadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadButton.setIcon(icon)
        self.uploadButton.setIconSize(QtCore.QSize(30, 30))
        self.uploadButton.setCheckable(False)
        self.uploadButton.setAutoExclusive(True)
        self.uploadButton.setObjectName("uploadButton")
        self.horizontalLayout_3.addWidget(self.uploadButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.recordButton = QtWidgets.QPushButton(self.toolsWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(60)
        font.setFamily("Bahnschrift SemiBold")
        self.recordButton.setFont(font)
        self.recordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recordButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon_2 = QtGui.QIcon()
        icon_2.addPixmap(QtGui.QPixmap(":/Icons/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon_2)
        self.recordButton.setIconSize(QtCore.QSize(30, 30))
        self.recordButton.setCheckable(False)
        self.recordButton.setAutoExclusive(True)
        self.recordButton.setObjectName("recordButton")
        self.horizontalLayout_3.addWidget(self.recordButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.runButton = QtWidgets.QPushButton(self.toolsWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(60)
        font.setFamily("Bahnschrift SemiBold")
        self.runButton.setFont(font)
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.runButton.clicked.connect(self.switch_page2)
        icon_3 = QtGui.QIcon()
        icon_3.addPixmap(QtGui.QPixmap(":/Icons/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon_3)
        self.runButton.setIconSize(QtCore.QSize(30, 30))
        self.runButton.setCheckable(False)
        self.runButton.setAutoExclusive(True)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_3.addWidget(self.runButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.stopButton = QtWidgets.QPushButton(self.toolsWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(60)
        font.setFamily("Bahnschrift SemiBold")
        self.stopButton.setFont(font)
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon_4 = QtGui.QIcon()
        icon_4.addPixmap(QtGui.QPixmap(":/Icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon_4)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setCheckable(False)
        self.stopButton.setAutoExclusive(True)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_3.addWidget(self.stopButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3.setStretch(0, 0)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 0)
        self.horizontalLayout_3.setStretch(3, 4)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 3)
        self.horizontalLayout_3.setStretch(6, 1)
        self.horizontalLayout_3.setStretch(7, 3)
        self.horizontalLayout_3.setStretch(8, 8)
        self.gridLayout_2.addWidget(self.toolsWidget, 1, 2, 1, 1)
        self.side_bar = QtWidgets.QWidget(self.centralwidget)
        self.side_bar.setMinimumSize(50,0)
        self.side_bar.setObjectName("side_bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_bar)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newButton = QtWidgets.QPushButton(self.side_bar)
        self.newButton.setMinimumSize(QtCore.QSize(0, 0))
        self.newButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.newButton.setText("")
        icon_5 = QtGui.QIcon()
        icon_5.addPixmap(QtGui.QPixmap(":/Icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newButton.setIcon(icon_5)
        self.newButton.setIconSize(QtCore.QSize(30, 30))
        self.newButton.setToolTip("New")
        self.newButton.setToolTipDuration(3000)
        self.newButton.setCheckable(True)
        self.newButton.setAutoExclusive(True)
        self.newButton.setObjectName("newButton")
        self.verticalLayout.addWidget(self.newButton)
        self.resultsButton = QtWidgets.QPushButton(self.side_bar)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(50)
        self.resultsButton.setFont(font)
        self.resultsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultsButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.resultsButton.setText("")
        icon_6= QtGui.QIcon()
        icon_6.addPixmap(QtGui.QPixmap(":/Icons/results.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resultsButton.setIcon(icon_6)
        self.resultsButton.setIconSize(QtCore.QSize(30, 30))
        self.resultsButton.setToolTip("Show Results")
        self.resultsButton.setToolTipDuration(3000)
        self.resultsButton.setCheckable(True)
        self.resultsButton.setAutoExclusive(True)
        self.resultsButton.setObjectName("resultsButton")
        self.resultsButton.clicked.connect(self.switch_page2)
        self.verticalLayout.addWidget(self.resultsButton)
        self.filesButton = QtWidgets.QPushButton(self.side_bar)
        self.filesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filesButton.setText("")
        icon_7 = QtGui.QIcon()
        icon_7.addPixmap(QtGui.QPixmap(":/Icons/files.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filesButton.setIcon(icon_7)
        self.filesButton.setIconSize(QtCore.QSize(30, 30))
        self.filesButton.setToolTip("Selected Files")
        self.filesButton.setToolTipDuration(3000)
        self.filesButton.setCheckable(True)
        self.filesButton.setAutoExclusive(True)
        self.filesButton.setObjectName("filesButton")
        self.filesButton.clicked.connect(self.switch_page)
        self.verticalLayout.addWidget(self.filesButton)
        self.historyButton = QtWidgets.QPushButton(self.side_bar)
        self.historyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.historyButton.setText("")
        icon_8 = QtGui.QIcon()
        icon_8.addPixmap(QtGui.QPixmap(":/Icons/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.historyButton.setIcon(icon_8)
        self.historyButton.setIconSize(QtCore.QSize(30, 30))
        self.historyButton.setToolTip("History")
        self.historyButton.setToolTipDuration(3000)
        self.historyButton.setCheckable(True)
        self.historyButton.setAutoExclusive(True)
        self.historyButton.setObjectName("historyButton")
        self.verticalLayout.addWidget(self.historyButton)
        self.resetButton = QtWidgets.QPushButton(self.side_bar)
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.resetButton.setText("")
        icon_9 = QtGui.QIcon()
        icon_9.addPixmap(QtGui.QPixmap(":/Icons/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetButton.setIcon(icon_9)
        self.resetButton.setIconSize(QtCore.QSize(30, 30))
        self.resetButton.setToolTip("Reset")
        self.resetButton.setToolTipDuration(3000)
        self.resetButton.setCheckable(True)
        self.resetButton.setAutoExclusive(True)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)
        self.helpButton = QtWidgets.QPushButton(self.side_bar)
        self.helpButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.helpButton.setText("")
        icon_10 = QtGui.QIcon()
        icon_10.addPixmap(QtGui.QPixmap(":/Icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon_10)
        self.helpButton.setIconSize(QtCore.QSize(30, 30))
        self.helpButton.setToolTip("Help")
        self.helpButton.setToolTipDuration(3000)
        self.helpButton.setCheckable(True)
        self.helpButton.setAutoExclusive(True)
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout.addWidget(self.helpButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 207, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout_2.addWidget(self.side_bar, 1, 0, 2, 1)
        self.sidebar_2 = QtWidgets.QWidget(self.centralwidget)
        self.sidebar_2.setMinimumSize(QtCore.QSize(150, 0))
        self.sidebar_2.setObjectName("sidebar_2")
        self.sidebar_2.setHidden(True)
        self.gridLayout = QtWidgets.QGridLayout(self.sidebar_2)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.newButton_2 = QtWidgets.QPushButton(self.sidebar_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.newButton_2.setFont(font)
        self.newButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.newButton_2.setCheckable(True)
        self.newButton_2.setAutoExclusive(True)
        self.newButton_2.setObjectName("newButton_2")
        self.verticalLayout_4.addWidget(self.newButton_2)
        self.resultsButton_2 = QtWidgets.QPushButton(self.sidebar_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(14)
        font.setWeight(50)
        self.resultsButton_2.setFont(font)
        self.resultsButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultsButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.resultsButton_2.setCheckable(True)
        self.resultsButton_2.setAutoExclusive(True)
        self.resultsButton_2.setObjectName("resultsButton_2")
        self.resultsButton_2.clicked.connect(self.switch_page2)
        self.verticalLayout_4.addWidget(self.resultsButton_2)
        self.filesButton_2 = QtWidgets.QPushButton(self.sidebar_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(14)
        font.setWeight(50)
        self.filesButton_2.setFont(font)
        self.filesButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filesButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.filesButton_2.setCheckable(True)
        self.filesButton_2.setAutoExclusive(True)
        self.filesButton_2.setObjectName("filesButton_2")
        self.filesButton_2.clicked.connect(self.switch_page)
        self.verticalLayout_4.addWidget(self.filesButton_2)
        self.historyButton_2 = QtWidgets.QPushButton(self.sidebar_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(14)
        font.setWeight(50)
        self.historyButton_2.setFont(font)
        self.historyButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.historyButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.historyButton_2.setCheckable(True)
        self.historyButton_2.setAutoExclusive(True)
        self.historyButton_2.setObjectName("historyButton_2")
        self.verticalLayout_4.addWidget(self.historyButton_2)
        self.resetButton_2 = QtWidgets.QPushButton(self.sidebar_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(14)
        font.setWeight(50)
        self.resetButton_2.setFont(font)
        self.resetButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.resetButton_2.setCheckable(True)
        self.resetButton_2.setAutoExclusive(True)
        self.resetButton_2.setObjectName("resetButton_2")
        self.verticalLayout_4.addWidget(self.resetButton_2)
        self.helpButton_2 = QtWidgets.QPushButton(self.sidebar_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(14)
        font.setWeight(50)
        self.helpButton_2.setFont(font)
        self.helpButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.helpButton_2.setCheckable(True)
        self.helpButton_2.setAutoExclusive(True)
        self.helpButton_2.setObjectName("helpButton_2")
        self.verticalLayout_4.addWidget(self.helpButton_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout_2.addWidget(self.sidebar_2, 1, 1, 2, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setContentsMargins(0, 0, 10, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fileslabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(18)
        font.setWeight(50)
        self.fileslabel.setFont(font)
        self.fileslabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fileslabel.setOpenExternalLinks(False)
        self.fileslabel.setObjectName("fileslabel")
        self.gridLayout_3.addWidget(self.fileslabel, 0, 0, 1, 1)
        self.filestable = QtWidgets.QTableWidget(self.page)
        self.filestable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setWeight(50)
        self.filestable.setFont(font)
        self.filestable.setObjectName("filestable")
        self.filestable.setColumnCount(1)
        self.filestable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.filestable.setHorizontalHeaderItem(0, item)
        self.gridLayout_3.addWidget(self.filestable, 1, 0, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(60)
        font.setFamily("Bahnschrift SemiBold")
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon_11 = QtGui.QIcon()
        icon_11.addPixmap(QtGui.QPixmap(":/Icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon_11)
        self.clearButton.setIconSize(QtCore.QSize(30, 30))
        self.clearButton.setCheckable(False)
        self.clearButton.setAutoExclusive(True)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_3.addWidget(self.clearButton, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 2, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 15)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resultsTable = QtWidgets.QTableWidget(self.tab)
        self.resultsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setWeight(50)
        self.resultsTable.setFont(font)
        self.resultsTable.setObjectName("resultsTable")
        self.resultsTable.setColumnCount(3)
        self.resultsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.resultsTable)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resultsTable_2 = QtWidgets.QTableWidget(self.tab_2)
        self.resultsTable_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setWeight(50)
        self.resultsTable_2.setFont(font)
        self.resultsTable_2.setObjectName("resultsTable_2")
        self.resultsTable_2.setColumnCount(5)
        self.resultsTable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable_2.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_2.addWidget(self.resultsTable_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 4)
        self.saveButton = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(60)
        font.setFamily("Bahnschrift SemiBold")
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon_12 = QtGui.QIcon()
        icon_12.addPixmap(QtGui.QPixmap(":/Icons/savedd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon_12)
        self.saveButton.setIconSize(QtCore.QSize(30, 30))
        self.saveButton.setCheckable(False)
        self.saveButton.setAutoExclusive(True)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_5.addWidget(self.saveButton, 1, 1, 1, 1)
        self.clearButton_2 = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(60)
        font.setFamily("Bahnschrift SemiBold")
        self.clearButton_2.setFont(font)
        self.clearButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.clearButton_2.setIcon(icon_11)
        self.clearButton_2.setIconSize(QtCore.QSize(30, 30))
        self.clearButton_2.setCheckable(False)
        self.clearButton_2.setAutoExclusive(True)
        self.clearButton_2.setObjectName("clearButton_2")
        self.gridLayout_5.addWidget(self.clearButton_2, 1, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 2, 2, 1, 1)
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setObjectName("mainWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mainWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu = QtWidgets.QPushButton(self.mainWidget)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.menu.setText("")
        icon_13= QtGui.QIcon()
        icon_13.addPixmap(QtGui.QPixmap(":/Icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu.setIcon(icon_13)
        self.menu.setIconSize(QtCore.QSize(30, 40))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)
        self.menu.setObjectName("menu")
        self.horizontalLayout_4.addWidget(self.menu)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.mainlabel = QtWidgets.QLabel(self.mainWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(20)
        font.setWeight(50)
        self.mainlabel.setFont(font)
        self.mainlabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mainlabel.setObjectName("mainlabel")
        self.horizontalLayout_4.addWidget(self.mainlabel)
        self.horizontalLayout_4.setStretch(2, 2)
        self.gridLayout_2.addWidget(self.mainWidget, 0, 0, 1, 3)
        self.gridLayout_2.setColumnStretch(2, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.menu.toggled['bool'].connect(self.side_bar.setHidden) # type: ignore
        self.menu.toggled['bool'].connect(self.sidebar_2.setVisible) # type: ignore
        self.newButton.toggled['bool'].connect(self.newButton_2.setChecked) # type: ignore
        self.newButton_2.toggled['bool'].connect(self.newButton.setChecked) # type: ignore
        self.resultsButton.toggled['bool'].connect(self.resultsButton_2.setChecked) # type: ignore
        self.resultsButton_2.toggled['bool'].connect(self.resultsButton.setChecked) # type: ignore
        self.filesButton.toggled['bool'].connect(self.filesButton_2.setChecked) # type: ignore
        self.filesButton_2.toggled['bool'].connect(self.filesButton.setChecked) # type: ignore
        self.historyButton.toggled['bool'].connect(self.historyButton_2.setChecked) # type: ignore
        self.historyButton_2.toggled['bool'].connect(self.historyButton.setChecked) # type: ignore
        self.resetButton.toggled['bool'].connect(self.resetButton_2.setChecked) # type: ignore
        self.resetButton_2.toggled['bool'].connect(self.resetButton.setChecked) # type: ignore
        self.helpButton.toggled['bool'].connect(self.helpButton_2.setChecked) # type: ignore
        self.helpButton_2.toggled['bool'].connect(self.helpButton.setChecked) # type: ignore
        self.helpButton_2.toggled['bool'].connect(self.helpButton.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uploadButton.setText(_translate("MainWindow", "Upload"))
        self.recordButton.setText(_translate("MainWindow", "Record"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.newButton_2.setText(_translate("MainWindow", "New"))
        self.resultsButton_2.setText(_translate("MainWindow", "Results"))
        self.filesButton_2.setText(_translate("MainWindow", "Files"))
        self.historyButton_2.setText(_translate("MainWindow", "History"))
        self.resetButton_2.setText(_translate("MainWindow", "Reset"))
        self.helpButton_2.setText(_translate("MainWindow", "Help"))
        self.fileslabel.setText(_translate("MainWindow", "  Selected Files"))
        item = self.filestable.horizontalHeaderItem(0)
        if item is None:
            item = QtWidgets.QTableWidgetItem()
            self.filestable.setHorizontalHeaderItem(0, item)
        item.setText(_translate("MainWindow", "Files"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        item = self.resultsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Files"))
        item = self.resultsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Language"))
        item = self.resultsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Confidence"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Results"))
        item = self.resultsTable_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Files"))
        item = self.resultsTable_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Language 1"))
        item = self.resultsTable_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Confidence 1"))
        item = self.resultsTable_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Language 2"))
        item = self.resultsTable_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Confidence 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Details"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.clearButton_2.setText(_translate("MainWindow", "Clear"))
        self.mainlabel.setText(_translate("MainWindow", "Language Identifier"))
    
    def switch_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_page2(self):
        self.stackedWidget.setCurrentIndex(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #app.setStyleSheet(open('/home/projectstudent/Desktop/gui/layout.qss').read())
    MainWindow.show()
    sys.exit(app.exec_())

