from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel
from analysis.modulo_ds import dame_graficas
from views.ui_vista_habitos import Ui_VistaHabitos

class Habitos(QWidget, Ui_VistaHabitos):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        

    def dame_vista(self, nombre_sprint, tp_sprint, ruta_habitos):
        
        
        habit_max_frec, habit_min_frec, dia_max_frec, dia_min_frec, habit_maxRch, prct_habits, graf1, graf2, graf3 = (dame_graficas(ruta_habitos))
        canvas1 = FigureCanvas(graf1)
        canvas2 = FigureCanvas(graf2)
        #canvas3 = FigureCanvas(graf3)
        
        self.Layout_stats.addWidget(QLabel(habit_max_frec))
        self.Layout_stats.addWidget(QLabel(habit_min_frec))
        self.Layout_stats.addWidget(QLabel(dia_max_frec))
        self.Layout_stats.addWidget(QLabel(dia_min_frec))
        self.Layout_stats.addWidget(QLabel(habit_maxRch))
        self.Layout_stats.addWidget(QLabel(prct_habits))

        # for value in [habit_max_frec, habit_min_frec, dia_max_frec, dia_min_frec, habit_maxRch, prct_habits]:
        #     if isinstance(value, list):
        #         value_str = ' \n '.join(map(str, value))
        #         self.Layout_stats.addWidget(QLabel(value_str))
        #     else:
        #         self.Layout_stats.addWidget(QLabel(str(value)))




        self.Layout_graf1.addWidget(canvas1)
        self.Layout_graf2.addWidget(canvas2)
        
        for i in range(len(graf3.index)):
            if i >= len(graf3.index)/2:
                self.Layout_graf3_2.addWidget(QLabel(graf3.index[i]))
            else:    
                self.Layout_graf3_1.addWidget(QLabel(graf3.index[i]))