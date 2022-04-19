from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
import qrcode

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(QSize(410,150))
        self.setMaximumSize(410,150)
        self.setMinimumSize(410,150)
        self.layout=QHBoxLayout()
        self.setWindowTitle('QrCode Dönüştürücü')



        self.label=QLabel(self)
        self.label.setText('QrCode \n Dönüştürücü')
        self.label.setStyleSheet("color:red; font-weight:bold; font-size:12pt")
        self.lineedit=QLineEdit(self)
        self.lineedit.setText('Dönüştürmek İstedğiniz Linki Buraya Giriniz')
        self.button=QPushButton(self)
        self.button.setText('Dönüştür')
        self.button.setStyleSheet('color:green')




        self.label.setGeometry(QRect(130,1,120,50))
        self.lineedit.setGeometry(QRect(1,110,350,30))
        self.button.setGeometry(QRect(355,110,50,30))

        self.button.clicked.connect(self.tap)



    def tap(self):
        girdi=self.lineedit.text()
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        qr.add_data(girdi)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.show()

        


        

uygulama = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
uygulama.exec_()
