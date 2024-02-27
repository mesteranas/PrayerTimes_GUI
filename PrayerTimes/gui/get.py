import aladhan
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Get(qt.QDialog):
    def __init__(self,p,countryCode,city):
        super().__init__(p)
        self.setWindowTitle(_("get prayer times"))
        self.times=qt.QListWidget()
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.times)
        try:
            client=aladhan.Client(aladhan.City(city,countryCode))
            adhans = client.get_today_times()
            for adhan in adhans:
                self.times.addItem(adhan.get_en_name() + adhan.readable_timing(show_date=False))
        except Exception as e:
            qt.QMessageBox.information(self,_("error"),_("please try later"))