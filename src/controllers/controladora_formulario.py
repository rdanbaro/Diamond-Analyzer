from views.ui_vista_formulario import Ui_Form
from PySide6.QtWidgets import QWidget

class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)




