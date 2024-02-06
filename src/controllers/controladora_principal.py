from views.ui_vista_principal import Ui_MainWindow
from controllers.controladora_formulario import Formulario
from PySide6.QtWidgets import QMainWindow, QWidget
from controllers.controladora_review import SprintReview
from controllers.controladora_vista_inicio import VistaInicio

class VistaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        self.setupUi(self)
    
        self.vista_inicio = VistaInicio()
        self.vista_formulario = Formulario()
        self.vista_review = SprintReview()

        self.vista_inicio.show()

        self.vista_inicio.exitButton.clicked.connect(self.cerrar_inicio)
        self.vista_inicio.sprintAnalysisButton.clicked.connect(self.sprint_analysis)





        self.contenedor_form.addWidget(self.vista_formulario)

        self.vista_formulario.boton_aceptar.clicked.connect(
            self.validar_form)
        self.vista_formulario.boton_cancelar.clicked.connect(
            self.cancelar_form)

    


    def sprint_analysis(self):
        self.show()
        self.vista_inicio.close()
    
    def cerrar_inicio(self):
        self.vista_inicio.close()
    
    
    def validar_form(self): 
        if self.vista_formulario.form_validator():  # Verificar si el validador devuelve True
            self.contenedor_form.removeWidget(self)
            self.vista_formulario.deleteLater()
            self.contenedor_form.addWidget(self.vista_review)  
    
    def cancelar_form(self):
        self.close()
        self.vista_inicio.show()

    
