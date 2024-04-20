from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel
from analysis.modulo_ds import dame_graficas_diamantes
from views.ui_vista_diamantes import Ui_VistaDiamantes

class CustomFigureCanvas(FigureCanvas):
    def __init__(self, figure, parent=None):
        super().__init__(figure)
        self.setParent(parent)

class Diamantes(QWidget, Ui_VistaDiamantes):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        
    def dame_vista(self, nombre_sprint, tp_sprint, ruta_diamantes):

        total_horas_trackeadas, cat_mayor_tiempo, act_mayor_tiempo, prct_tiempo_track, graf1, graf2, graf3, graf4 = (
            dame_graficas_diamantes(ruta_diamantes)) 
        
        self.Layout_stats.addWidget(QLabel(total_horas_trackeadas))
        self.Layout_stats.addWidget(QLabel(cat_mayor_tiempo))
        self.Layout_stats.addWidget(QLabel(act_mayor_tiempo))
        self.Layout_stats.addWidget(QLabel(prct_tiempo_track))
        self.Layout_stats.addWidget(QLabel('hola'))
        
        canvas1 = CustomFigureCanvas(graf3)
        canvas2 = CustomFigureCanvas(graf1)
        canvas3 = CustomFigureCanvas(graf4)
        canvas4 = CustomFigureCanvas(graf2)
        
        self.Layout_graf1_Act.addWidget(canvas1)
        self.Layout_graf2_CatBar.addWidget(canvas2)
        self.Layout_graf3_CatPie.addWidget(canvas3)
        self.Layout_graf4_CatPlot.addWidget(canvas4)
        