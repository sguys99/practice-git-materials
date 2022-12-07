import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,
                             QMessageBox)
from PyQt5.QtGui import QIcon


class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.btn1=QPushButton('Message',self)
        self.btn1.clicked.connect(self.activateMessage)
        
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
        
    def activateMessage(self):
        QMessageBox.information(self,"information","Button clicked!")
        
        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    view=Calculator()
    sys.exit(app.exec_())