from PySide6.QtCore import Qt
from views.ui_vista_general import Ui_GeneralView
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
import database
from models.modelos import Sprint
from controllers.controladora_review import SprintReview
from controllers.controladora_vista_habitos import Habitos

class VistaGeneral(QWidget, Ui_GeneralView):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.lista_botones = []

        self.layout_contenedor_metas = QVBoxLayout()
        self.tab_metas.setLayout(self.layout_contenedor_metas)

        self.layout_contenedor_habitos = QVBoxLayout()
        self.tab_2.setLayout(self.layout_contenedor_habitos)



        
        self.layout_sprints = QVBoxLayout()
        self.layout_sprints.setAlignment(Qt.AlignTop)
        self.widget_2 = QWidget()
        self.widget_2.setLayout(self.layout_sprints)
        #self.widget_2.setObjectName(u"widget_2")
        
        
        self.scrollArea.setWidget(self.widget_2)
        
        self.vista_metas = SprintReview()
        self.vista_habitos = Habitos()  
        

    def mostrar_sprint(self, titulo):
        sprint = database.sesion.query(Sprint).filter(Sprint.nombre_sprint == titulo).first()
        self.layout_contenedor_metas.removeWidget(self.vista_metas)
        self.vista_metas.deleteLater()
        
        self.vista_metas = SprintReview()
        #self.vista_metas.removeWidget(self.vista.Boton_Siguiente)
        self.vista_metas.Boton_Siguiente.deleteLater()
        self.vista_metas.dame_info_view(sprint.nombre_sprint, sprint.tipo, sprint.data_metas_objetivos)
        self.layout_contenedor_metas.addWidget(self.vista_metas)
        
        self.layout_contenedor_habitos.removeWidget(self.vista_habitos)
        self.vista_habitos.deleteLater()
        self.vista_habitos = Habitos()
        self.vista_habitos.dame_vista(sprint.nombre_sprint, sprint.tipo, sprint.data_Habitos)
        self.layout_contenedor_habitos.addWidget(self.vista_habitos)

        



    def mostrar_sprint_guardados(self):
        sprints = database.sesion.query(Sprint).all()
        for sprint in sprints:
            button = QPushButton(sprint.nombre_sprint)
            button.setMinimumSize(265,30)
            
            # Configurar el botón según sea necesario
            # Por ejemplo, conectarlo a una función de manejo de clic
            
            self.lista_botones.append(button)

            # button.clicked.connect(lambda checked, nombre_sprint=sprint.nombre_sprint: self.mostrar_prompt(nombre_sprint))
            # self.scrollAreaWidgetContents.layout().addWidget(button)
            # self.lista_botones.append(button)

        list(map(lambda i: self.layout_sprints.addWidget(i), self.lista_botones))
        #boton_texto = self.lista_botones[0].text()
        #print(boton_texto)
        #self.lista_botones[0].clicked.connect(lambda: self.mostrar_sprint(boton_texto))
        
        list(map(lambda boton: boton.clicked.connect(
            lambda: self.mostrar_sprint(boton.text())), self.lista_botones))