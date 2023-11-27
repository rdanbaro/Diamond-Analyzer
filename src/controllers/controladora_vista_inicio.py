from views.ui_vista_inicio import Ui_VistaInicio
from PySide6.QtWidgets import QMainWindow
from controllers.controladora_principal import VistaPrincipal


class VistaInicio(QMainWindow, Ui_VistaInicio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exitButton.clicked.connect(self.exit)
        self.sprintAnalysisButton.clicked.connect(self.sprint_analysis)




    def exit(self):
        self.close()

    def sprint_analysis(self):
        self.vista_principal = VistaPrincipal()
        self.vista_principal.show()
        self.close()