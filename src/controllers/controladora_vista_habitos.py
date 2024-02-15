from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget
from analysis.modulo_ds import dame_graficas
from views.ui_vista_habitos import Ui_VistaHabitos

class Habitos(QWidget, Ui_VistaHabitos):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        

    def dame_vista(self, nombre_sprint, tp_sprint, ruta_habitos):
        
    
        canvas = FigureCanvas(dame_graficas(ruta_habitos))
        
        self.Layout_habitos.addWidget(canvas)

