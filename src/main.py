import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget
from controllers.controladora_vista_inicio import VistaInicio

app = QApplication(sys.argv)

inicio = VistaInicio()
inicio.show()

app.exec()



