import sys
from custome_errors import *
sys.excepthook = my_excepthook
import update
import gui
import guiTools
from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        layout=qt.QVBoxLayout()
        self.cities=qt.QListWidget()
        self.regions=gui.jsonContorl.get()
        self.cities.addItems(self.regions)
        self.cities.setAccessibleName(_("cities"))
        self.cities.setContextMenuPolicy(qt2.Qt.ContextMenuPolicy.CustomContextMenu)
        self.cities.customContextMenuRequested.connect(self.context)
        qt1.QShortcut("delete",self).activated.connect(self.delete)
        layout.addWidget(self.cities)
        self.get=qt.QPushButton(_("get times"))
        self.get.setDefault(True)
        self.get.clicked.connect(lambda:gui.Get(self,self.regions[self.cities.currentItem().text()],self.cities.currentItem().text()).exec())
        self.add=qt.QPushButton(_("add city"))
        self.add.setDefault(True)
        self.add.clicked.connect(lambda:gui.Add(self).exec())
        layout.addWidget(self.get)
        layout.addWidget(self.add)
        self.setting=qt.QPushButton(_("settings"))
        self.setting.setDefault(True)
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        githup=qt1.QAction(_("Github"),self)
        cus.addAction(githup)
        githup.triggered.connect(lambda: guiTools.OpenLink(self,"https://Github.com/mesteranas"))
        X=qt1.QAction(_("x"),self)
        cus.addAction(X)
        X.triggered.connect(lambda:guiTools.OpenLink(self,"https://x.com/mesteranasm"))
        email=qt1.QAction(_("email"),self)
        cus.addAction(email)
        email.triggered.connect(lambda: guiTools.sendEmail("anasformohammed@gmail.com","project_type=GUI app={} version={}".format(app.name,app.version),""))
        Github_project=qt1.QAction(_("visite project on Github"),self)
        help.addAction(Github_project)
        Github_project.triggered.connect(lambda:guiTools.OpenLink(self,"https://Github.com/mesteranas/{}".format(settings_handler.appName)))
        Checkupdate=qt1.QAction(_("check for update"),self)
        help.addAction(Checkupdate)
        Checkupdate.triggered.connect(lambda:update.check(self))
        licence=qt1.QAction(_("license"),self)
        help.addAction(licence)
        licence.triggered.connect(lambda: Licence(self))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
        if settings_handler.get("update","autoCheck")=="True":
            update.check(self,message=False)
    def closeEvent(self, event):
        gui.jsonContorl.save(self.regions)
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def context(self):
        menu=qt.QMenu(self)
        delete=qt1.QAction(_("delete"),self)
        delete.triggered.connect(self.delete)
        menu.addAction(delete)
        menu.exec()
    def delete(self):
        try:
            del(self.regions[self.cities.currentItem().text()])
            self.cities.clear()
            self.cities.addItems(self.regions.keys())
            guiTools.speak(_("deleted"))
        except:
            guiTools.speak(_("error"))
App=qt.QApplication([])
w=main()
w.show()
App.exec()