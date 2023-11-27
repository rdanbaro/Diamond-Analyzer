from views.ui_vista_principal import Ui_MainWindow
from controllers.controladora_formulario import Formulario
from PySide6.QtWidgets import QMainWindow, QWidget

class VistaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.show()    

        self.vista_formulario = Formulario()
        
        self.contenedor_form.addWidget(self.vista_formulario)
        
        #self.controladora_formulario = ControladoraFormulario(self.vista_formulario)
        
        
        
        
        