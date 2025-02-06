from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel
from analysis.modulo_ds import dame_graficas_diamantes
from views.ui_vista_entreno import Ui_VistaEntreno
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


class Entrenos(QWidget, Ui_VistaEntreno):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
    def dame_vista(self, id, nombre_sprint, tp_sprint, ruta_diamantes):

            
            
            response = requests.get(API_URL+f'/sprint_entrenos_stats/{id}')
            
            if response.status_code == 200:
                
                musculo_mas_entrenado, musculo_mnos_entrenado, total_dias_entreno, rutinas_mas_entrenadas, total_rondas, total_series, ejercicio_mas_series, ejercicio_mnos_series = (response.json())
                
                
            
            
                response2 = requests.get(API_URL+f'/sprint_entrenos_graf/{id}')
                
                

            if response2.status_code == 200:
                with zipfile.ZipFile(io.BytesIO(response2.content)) as zip_file:
                    zip_file.extractall()
            
            
                with open('graficoEntreno1.pkl', 'rb') as f:
                        graf1 = pickle.load(f)
                with open('graficoEntreno2.pkl', 'rb') as f:
                        graf2 = pickle.load(f) 
                
            
                canvas1 = FigureCanvas(graf1)
                canvas2 = FigureCanvas(graf2)
                
            
            else:
                print("Error al descargar las figuras")
        
            
            
            
            
            self.Layout_estadisticas.addWidget(QLabel(musculo_mas_entrenado))
            self.Layout_estadisticas.addWidget(QLabel(musculo_mnos_entrenado))
            self.Layout_estadisticas.addWidget(QLabel(total_dias_entreno))
            self.Layout_estadisticas.addWidget(QLabel(rutinas_mas_entrenadas))
            self.Layout_estadisticas.addWidget(QLabel(total_rondas))
            self.Layout_estadisticas.addWidget(QLabel(total_series))
            self.Layout_estadisticas.addWidget(QLabel(ejercicio_mas_series))
            self.Layout_estadisticas.addWidget(QLabel(ejercicio_mnos_series))
            #self.Layout_estadisticas.addWidget(QLabel(total_repeticiones_x_ejercicio))
        
            
            self.Layout_graf1.addWidget(canvas1)
            self.Layout_graf2.addWidget(canvas2)
                