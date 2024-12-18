from views.ui_vista_review import Ui_Sprint_Review
from PySide6.QtWidgets import QWidget, QLabel, QProgressBar, QCheckBox
from analysis.modulo_ds import get_datos_metas
from PySide6.QtCore import QCoreApplication

from apiConfig import API_URL
import requests

class SprintReview(QWidget, Ui_Sprint_Review):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.valor = []

    def dame_info_view(self, id, nombre_sprint, tp_sprint, ruta_objs):
        self.label_nombre_sprint.setText(nombre_sprint)
        self.label_tipo_sprint.setText(tp_sprint)

        response = requests.get(API_URL+f'sprint_metas/{id}')
        
        if response.status_code == 200:
            data = response.json()
           
        #print("respuesta api:", data.items())
        
        ls_objs = []
        ls_requisito = []
        ls_cumplido = []
        ls_realizado = []
        
        for meta in data:
            ls_objs.append(meta['obj'])
            ls_requisito.append(meta['requisito'])
            ls_cumplido.append(meta['cumplido'])
            ls_realizado.append(meta['realizado'])
        
        
        
        # # gestion info ruta objetivos y metas
        # ls_objs, ls_requisito, ls_cumplido, ls_realizado = get_datos_metas(
        #     ruta_objs)

        # ls_cumplido = [100 if i == True else i for i in ls_cumplido]

        for i in ls_objs:
            self.Layout_metas.addWidget(QLabel(i))

        for i in ls_requisito:
            self.Layout_requisitos.addWidget(QLabel(str(i)))

        self.valor = [ls_cumplido[i]/ls_requisito[i] *
                 100 for i in range(len(ls_cumplido))]

        for i in range(len(ls_cumplido)):
            if ls_realizado[i] == True:
                progress_bar = QProgressBar()
                # Establecer el valor de la barra de progreso en función de i
                progress_bar.setValue(100)
                self.Layout_cumplidos.addWidget(progress_bar)
            else:
                progress_bar = QProgressBar()
                # Establecer el valor de la barra de progreso en función de i
                progress_bar.setValue(self.valor[i])
                self.Layout_cumplidos.addWidget(progress_bar)

        for i in ls_realizado:
            check_box = QCheckBox("")
            check_box.setChecked(i)
            check_box.setStyleSheet(
                "QCheckBox::indicator { width: 21px; height: 21px; }")
            self.Layout_checks.addWidget(check_box)

        # total_cumplido = sum(ls_cumplido)
        # total_requisito = sum(ls_requisito)
        # porcentaje_cumplimiento = total_cumplido / total_requisito * 100
        
        porcentaje_cumplimiento = sum(self.valor) / len(self.valor) 
        print(porcentaje_cumplimiento)
        #print(porcentaje_cumplimiento, total_cumplido, total_requisito, sep="\n")
        self.progreso_general.setValue(porcentaje_cumplimiento)

        if porcentaje_cumplimiento < 40:
            self.label_mensaje.setText(QCoreApplication.translate(
                "Sprint_Review", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#813d9c;\">Sigue adelante, puedes hacerlo</span></p></body></html>", None))
            # mensaje = "Sigue adelante, puedes hacerlo"
        elif 40 <= porcentaje_cumplimiento <= 70:
            self.label_mensaje.setText(QCoreApplication.translate(
                "Sprint_Review", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#813d9c;\">Buen trabajo, sigue esforzándote</span></p></body></html>", None))
            # mensaje = "Buen trabajo, sigue esforzándote"
        else:
            self.label_mensaje.setText(QCoreApplication.translate(
                "Sprint_Review", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#813d9c;\">¡Felicidades por tu gran progreso!</span></p></body></html>", None))
            # mensaje = "¡Felicidades por tu gran progreso!"

        # self.label_mensaje.setText(mensaje)
