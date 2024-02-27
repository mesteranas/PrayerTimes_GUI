import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Add(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("add city"))
        layout=qt.QFormLayout(self)
        self.country=qt.QComboBox()
        self.country.addItems(guiTools.dictionarys.countries.values())
        layout.addRow(_("select country"),self.country)
        self.city=qt.QLineEdit()
        layout.addRow(_("your city"),self.city)
        self.add=qt.QPushButton(_("add"))
        self.add.clicked.connect(self.on_add)
        layout.addWidget(self.add)
        self.coun={}
        for key,value in guiTools.dictionarys.countries.items():
            self.coun[value]=key
        self.p=p
    def on_add(self):
        self.p.regions[self.city.text()]=self.coun[self.country.currentText()]
        self.p.cities.clear()
        self.p.cities.addItems(self.p.regions.keys())
        self.close()