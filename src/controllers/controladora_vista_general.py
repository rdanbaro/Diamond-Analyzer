from PySide6.QtCore import Qt
from views.ui_vista_general import Ui_GeneralView
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
import database
from models.modelos import Sprint
from controllers.controladora_review import SprintReview
from controllers.controladora_vista_habitos import Habitos
from controllers.controladora_vista_diamantes import Diamantes

import requests
from apiConfig import API_URL

class VistaGeneral(QWidget, Ui_GeneralView):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.lista_botones = []

        self.layout_contenedor_metas = QVBoxLayout()
        self.tab_metas.setLayout(self.layout_contenedor_metas)

        self.layout_contenedor_habitos = QVBoxLayout()
        self.tab_3.setLayout(self.layout_contenedor_habitos)
        
        self.layout_contenedor_diamantes = QVBoxLayout()
        self.tab_2.setLayout(self.layout_contenedor_diamantes)

        self.layout_sprints = QVBoxLayout()
        self.layout_sprints.setAlignment(Qt.AlignTop)
        self.widget_2 = QWidget()
        self.widget_2.setLayout(self.layout_sprints)
        

        self.scrollArea.setWidget(self.widget_2)

        self.vista_metas = SprintReview()
        self.vista_habitos = Habitos()
        self.vista_diamantes = Diamantes()

    def mostrar_sprint(self, titulo):
        sprint = database.sesion.query(Sprint).filter(
            Sprint.nombre_sprint == titulo).first()
        
        response = requests.get(API_URL+f'sprints/{titulo}')
        
        if response.status_code == 200:
            data = response.json()
        
        self.layout_contenedor_metas.removeWidget(self.vista_metas)
        self.vista_metas.deleteLater()

        self.vista_metas = SprintReview()
        self.vista_metas.Boton_Siguiente.deleteLater()
        self.vista_metas.dame_info_view(
            data['id'], data['nombre'], data['tipo'], data["ruta_metas_objetivos"])
        self.layout_contenedor_metas.addWidget(self.vista_metas)

        self.layout_contenedor_habitos.removeWidget(self.vista_habitos)
        self.vista_habitos.deleteLater()
        self.vista_habitos = Habitos()
        self.vista_habitos.dame_vista(
            data['id'], data['nombre'], data['tipo'], data["ruta_habitos"])
        self.layout_contenedor_habitos.addWidget(self.vista_habitos)
        
        self.layout_contenedor_diamantes.removeWidget(self.vista_diamantes)
        self.vista_diamantes.deleteLater()
        self.vista_diamantes = Diamantes()
        self.vista_diamantes.dame_vista(
            data['id'], data['nombre'], data['tipo'], data["ruta_diamantes"])
        self.layout_contenedor_diamantes.addWidget(self.vista_diamantes)
        

    def mostrar_sprint_guardados(self):
        #sprints = database.sesion.query(Sprint).all()
        
        response = requests.get(API_URL+'sprints/')
        
        if response.status_code == 200:
            data = response.json()
           
        #print("respuesta api:", data.items())
        
        for sprint in data:
            button = QPushButton(sprint['nombre'])
            button.setMinimumSize(265, 30)
            self.lista_botones.append(button)

            

        list(map(lambda i: self.layout_sprints.addWidget(i), self.lista_botones))
        
        list(map(lambda boton: boton.clicked.connect(
            lambda: self.mostrar_sprint(boton.text())), self.lista_botones))

        