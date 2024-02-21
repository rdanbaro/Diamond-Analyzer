from views.ui_vista_principal import Ui_MainWindow
from controllers.controladora_formulario import Formulario
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from controllers.controladora_review import SprintReview
from controllers.controladora_vista_inicio import VistaInicio
from controllers.controladora_vista_general import VistaGeneral

class VistaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        self.setupUi(self)
        
        self.vista_inicio = VistaInicio()
        self.vista_formulario = Formulario()
        self.vista_review = SprintReview()
        self.vista_general = VistaGeneral()

        self.vista_inicio.show()


        self.vista_inicio.sprintAnalysisButton.clicked.connect(self.mostrar_form)
        self.vista_inicio.statsButton.clicked.connect(self.mostrar_vista_general)
        self.vista_inicio.exitButton.clicked.connect(self.cerrar_inicio)
        



       

        self.vista_formulario.boton_aceptar.clicked.connect(
            self.validar_form)
        self.vista_formulario.boton_cancelar.clicked.connect(
            self.cancelar_form)



        self.vista_review.Boton_Siguiente.clicked.connect(self.sprint_analysis_siguiente)


    #Métodos Vista de Inicio
    def mostrar_form(self):
        self.show()
        self.contenedor_form.addWidget(self.vista_formulario)
        self.vista_inicio.close()

    def mostrar_vista_general(self):
        self.vista_inicio.close()
        self.vista_general.mostrar_sprint_guardados()
        self.contenedor_form.addWidget(self.vista_general)
        self.showMaximized()
        

    def cerrar_inicio(self):
        self.vista_inicio.close()
    


    
    

    #Métodos Vista Formulario
    def validar_form(self):
        validador, nombre_sprint, tp_sprint, ruta_objs, ruta_habitos, ruta_diamond, ruta_entreno = self.vista_formulario.form_validator() 
        if validador:  
            self.contenedor_form.removeWidget(self)
            self.vista_formulario.deleteLater()
            self.vista_review.dame_info_view(nombre_sprint, tp_sprint, ruta_objs)
            self.contenedor_form.addWidget(self.vista_review)  
    
    def cancelar_form(self):
        self.close()
        self.contenedor_form.removeWidget(self)
        self.vista_formulario.deleteLater()
        self.vista_inicio.show()

    
    
    
    #Métodos Vista Sprint Review
    def sprint_analysis_siguiente(self):
        self.contenedor_form.removeWidget(self)
        self.vista_review.deleteLater()
        self.close()
        self.vista_general.mostrar_sprint_guardados()
        self.contenedor_form.addWidget(self.vista_general)
        self.showMaximized()
        