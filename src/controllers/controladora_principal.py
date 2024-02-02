from views.ui_vista_principal import Ui_MainWindow
from controllers.controladora_formulario import Formulario
from PySide6.QtWidgets import QMainWindow, QWidget
from controllers.controladora_review import SprintReview

class VistaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.show()

        self.vista_formulario = Formulario()
        self.vista_review = SprintReview()

        self.contenedor_form.addWidget(self.vista_formulario)

        self.vista_formulario.boton_aceptar.clicked.connect(
            self.probando_entradas)

    def probando_entradas(self):
        sprint = self.vista_formulario.entry_nombre_sprint.text()
        tipo_sprint_seleccionado = ''

        intenso = self.vista_formulario.radioButton_intenso
        standard = self.vista_formulario.radioButton_standard
        largo = self.vista_formulario.radioButton_largo

        if intenso.isChecked():
            tipo_sprint_seleccionado = intenso.text()
        if standard.isChecked():
            tipo_sprint_seleccionado = standard.text()
        if largo.isChecked():
            tipo_sprint_seleccionado = largo.text()

        metas = self.vista_formulario.entry_metas.text()
        habitos = self.vista_formulario.entry_habitos.text()
        diamantes = self.vista_formulario.entry_diamantes.text()
        entrenamiento = self.vista_formulario.entry_entrenamiento.text()

        print(sprint, tipo_sprint_seleccionado, metas,
              habitos, diamantes, entrenamiento, sep='\n')

        self.contenedor_form.removeWidget(self.vista_formulario)
        self.vista_formulario.deleteLater()
        self.contenedor_form.addWidget(self.vista_review)
        # self.controladora_formulario = ControladoraFormulario(self.vista_formulario)
