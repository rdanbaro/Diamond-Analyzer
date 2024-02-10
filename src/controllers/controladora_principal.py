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



        self.vista_review.Boton_Siguiente.clicked.connect(self.sprint_analysis_siguiente)



    #Vista Sprint Review
    def sprint_analysis(self):
        self.show()
        self.vista_inicio.close()
    
    def sprint_analysis_siguiente(self):
        self.contenedor_form.removeWidget(self)
        self.vista_review.deleteLater()





    def cerrar_inicio(self):
        self.vista_inicio.close()
    
    
    def validar_form(self):
        validador, nombre_sprint, tp_sprint, ruta_objs, ruta_habitos, ruta_diamond, ruta_entreno = self.vista_formulario.form_validator() 
        if validador:  
            self.contenedor_form.removeWidget(self)
            self.vista_formulario.deleteLater()
            self.vista_review.dame_info_view(nombre_sprint, tp_sprint, ruta_objs, ruta_habitos, ruta_diamond, ruta_entreno)
            self.contenedor_form.addWidget(self.vista_review)  
    
    def cancelar_form(self):
        self.close()
        self.vista_inicio.show()

    
