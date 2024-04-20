from views.ui_vista_inicio import Ui_VistaInicio
from PySide6.QtWidgets import QMainWindow, QPushButton



class VistaInicio(QMainWindow, Ui_VistaInicio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        #self.sprintAnalysisButton.setStyleSheet("QPushButton { border: none; background-image: url(:/prefijoNuevo/Fundo transparente 1900x1900.png); }")
        self.sprintAnalysisButton.pressed.connect(self.on_enter)
        #self.sprintAnalysisButton.pressed.connect(self.on_leave)
        
    def on_enter(self):
        self.sprintAnalysisButton.setStyleSheet(u"border-image: url(:/hola/Captura desde 2024-04-07 21-04-10.png);")
    
    # def on_leave(self):
    #     self.setStyleSheet("QPushButton { border: none; background-image: url(:/hola/Captura desde 2024-04-07 21-09-40.png); }")    




    

    