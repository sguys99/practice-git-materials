class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        pass
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
        self.view.btn2.clicked.connect(self.view.clearMessage)
        
    def sum(self, a, b):
        return a+b