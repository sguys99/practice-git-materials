class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)