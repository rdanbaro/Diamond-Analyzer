from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel
from analysis.modulo_ds import dame_graficas_habitos
from views.ui_vista_habitos import Ui_VistaHabitos

import json
from io import StringIO

from apiConfig import API_URL
import requests
import zipfile
import pickle
import io
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

class Habitos(QWidget, Ui_VistaHabitos):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def dame_vista(self, id, nombre_sprint, tp_sprint, ruta_habitos):

        # habit_max_frec, habit_min_frec, dia_max_frec, dia_min_frec, habit_maxRch, prct_habits, graf1, graf2, graf3 = (
        #     dame_graficas_habitos(ruta_habitos))
        
        def limpiar_string(texto):
            return ''.join(char for char in texto if ord(char) < 128)
        
        
        
        response = requests.get(API_URL+f'sprint_habitos_stats/{id}')
        
        if response.status_code == 200:
            
            habit_max_frec, habit_min_frec, dia_max_frec, dia_min_frec, habit_maxRch, prct_habits, graf3, longitud = (response.json())
            
            print("Tipo de graf3:", graf3)
         
            graf3 = graf3[1:-1].split(',')
           #graf3 = graf3.sort_values(by='datos', ascending=False)
           #graf3[['habito', 'valor']] = graf3['datos'].str.rsplit(n=1, expand=True)
            #raf3 = graf3.drop('datos', axis=1)    # if isinstance(graf3, str):
        #     graf3 = eval(graf3)
    
        # # Ahora crea el DataFrame
        # graf3 = pd.DataFrame.from_records(graf3)

        response2 = requests.get(API_URL+f'sprint_habitos_graf/{id}')
        
        response2 = requests.get(API_URL+f'sprint_habitos_graf/{id}')

        if response2.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response2.content)) as zip_file:
                zip_file.extractall()
        
        
            # # Crear instancias de Figure y FigureCanvas con las figuras descargadas
            # graf1 = plt.imread('figura1.png')
            # graf2 = plt.imread('figura2.png')
            
            # fig1 =Figure()
            # ax1 = fig1.add_subplot(111)
            # ax1.imshow(graf1)
            # ax1.axis('off')
            
            # fig2 =Figure()
            # ax2 = fig2.add_subplot(111)
            # ax2.imshow(graf2)
            # ax2.axis('off')
             
            with open('figura1.pkl', 'rb') as f:
                fig1 = pickle.load(f)
            with open('figura2.pkl', 'rb') as f:
                fig2 = pickle.load(f) 
             
             
                    
            # Crear instancias de FigureCanvas con las figuras
            canvas1 = FigureCanvas(fig1)
            canvas2 = FigureCanvas(fig2)
            #canvas3 = FigureCanvas(graf3)
            
        else:
            print("Error al descargar las figuras")
            
        
        
        
        
        
        
        # canvas1 = FigureCanvas(graf1)
        # canvas2 = FigureCanvas(graf2)
        

        self.Layout_stats.addWidget(QLabel(habit_max_frec))
        self.Layout_stats.addWidget(QLabel(habit_min_frec))
        self.Layout_stats.addWidget(QLabel(dia_max_frec))
        self.Layout_stats.addWidget(QLabel(dia_min_frec))
        self.Layout_stats.addWidget(QLabel(habit_maxRch))
        self.Layout_stats.addWidget(QLabel(prct_habits))

        

        self.Layout_graf1.addWidget(canvas1)
        self.Layout_graf2.addWidget(canvas2)

        print("graf3:", graf3)
        
        for i in range(longitud):
            if i >= longitud/2:
                self.Layout_graf3_2.addWidget(QLabel(graf3[i]))
            else:
                self.Layout_graf3_1.addWidget(QLabel(graf3[i]))
