from views.ui_vista_formulario import Ui_Form
from PySide6.QtWidgets import QWidget

class Formulario(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)



    def form_validator(self):
        sprint = self.entry_nombre_sprint.text()
        tipo_sprint_seleccionado = ''

        intenso = self.radioButton_intenso
        standard = self.radioButton_standard
        largo = self.radioButton_largo

        if intenso.isChecked():
            tipo_sprint_seleccionado = intenso.text()
        if standard.isChecked():
            tipo_sprint_seleccionado = standard.text()
        if largo.isChecked():
            tipo_sprint_seleccionado = largo.text()

        metas = self.entry_metas.text()
        habitos = self.entry_habitos.text()
        diamantes = self.entry_diamantes.text()
        entrenamiento = self.entry_entrenamiento.text()

        print(sprint, tipo_sprint_seleccionado, metas,
              habitos, diamantes, entrenamiento, sep='\n')

        
        # self.controladora_formulario = ControladoraFormulario(self.vista_formulario)
