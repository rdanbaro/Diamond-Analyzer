from views.ui_vista_formulario import Ui_Form
from PySide6.QtWidgets import QWidget
import database
from models.modelos import Sprint

import requests

class Formulario(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.ruta=' '
    def form_validator(self):
        form_valido = True
        try:
            # Obtener el texto del campo de entrada del nombre del sprint
            sprint = self.entry_nombre_sprint.text().strip()
            # Consultar si el nombre del sprint ya existe en la base de datos
            if database.sesion.query(Sprint).filter_by(nombre_sprint=sprint).first():
                form_valido = False
                raise ValueError("El nombre del sprint introducido ya existe")
    
            if not sprint:
                form_valido = False
                raise ValueError("El campo de nombre de sprint no puede estar vacío")
    
            # Obtener el tipo de sprint seleccionado
            tipo_sprint_seleccionado = ''
            intenso = self.radioButton_intenso
            standard = self.radioButton_standard
            largo = self.radioButton_largo
    
            if intenso.isChecked():
                tipo_sprint_seleccionado = 'Intenso'
            elif standard.isChecked():
                tipo_sprint_seleccionado = 'Standard'
            elif largo.isChecked():
                tipo_sprint_seleccionado = 'Largo'
            else:
                form_valido = False
                raise ValueError("Debe seleccionar un tipo de sprint")
    
            # Obtener el texto del campo de entrada de las metas
            metas = self.entry_metas.text().strip()
            
            if not metas:
                form_valido = False
                raise ValueError("El campo de metas no puede estar vacío")
    
            # Obtener el texto del campo de entrada de los hábitos
            habitos = self.entry_habitos.text().strip()
            if not habitos:
                form_valido = False
                raise ValueError("El campo de hábitos no puede estar vacío")
    
            # Obtener el texto del campo de entrada de los diamantes
            diamantes = self.entry_diamantes.text().strip()
            if not diamantes:
                form_valido = False
                raise ValueError("El campo de diamantes no puede estar vacío")
    
            # Obtener el texto del campo de entrada del entrenamiento
            entrenamiento = self.entry_entrenamiento.text().strip()
            if not entrenamiento:
                form_valido = False
                raise ValueError("El campo de entrenamiento no puede estar vacío")

           

            # Imprimir los valores obtenidos
            print(sprint, tipo_sprint_seleccionado, metas, habitos, diamantes, entrenamiento, sep='\n')
        except ValueError as ve:
            # Mostrar mensaje de error
            print(f"Error: {ve}")
        except Exception as e:
            # Mostrar un mensaje de error
            print("Ha ocurrido un error al validar el formulario.")
            print(e)

        if form_valido:
            # Crear una nueva fila en la tabla Sprint
            #new_sprint = Sprint(nombre_sprint=sprint, tipo=tipo_sprint_seleccionado, data_metas_objetivos=metas,
            #                    data_Habitos=habitos, data_Diamantes=diamantes, data_Entrenamiento=entrenamiento)
    
            ## Agregar la nueva fila a la sesión
            #database.sesion.add(new_sprint)
    
            # Confirmar los cambios en la base de datos
            #database.sesion.commit()
            sprint = {
                "nombre": sprint,
                "tipo": tipo_sprint_seleccionado,
                "ruta_metas_objetivos": metas,
                "ruta_habitos": habitos,
                "ruta_entrenamiento": entrenamiento,
                "ruta_diamantes": diamantes
            }
            

            # URL de la API
            url = "http://127.0.0.1:8000/sprints/"

            response = requests.post(url, json=sprint)

            if response.status_code == 201:
                # Obtener el ID del objeto creado
                id_objeto = response.json()["id"]
                print("Objeto creado con ID:", id_objeto)
            else:
                print("Error:", response.status_code)
                    
                
            return form_valido, sprint, tipo_sprint_seleccionado, metas, habitos, diamantes, entrenamiento 
        else:
            return form_valido, 0, 0, 0, 0, 0, 0    

        
        
        

        
        # self.controladora_formulario = ControladoraFormulario(self.vista_formulario)




