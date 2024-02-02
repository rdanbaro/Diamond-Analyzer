from views.ui_vista_formulario import Ui_Form
from PySide6.QtWidgets import QWidget

class Formulario(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)




