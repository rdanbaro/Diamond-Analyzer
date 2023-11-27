from views.ui_vista_principal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class VistaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
    