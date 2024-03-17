import sys
import database
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget
from controllers.controladora_principal import VistaPrincipal
from models.modelos import *

app = QApplication(sys.argv)

inicio = VistaPrincipal()




app.exec() 

if __name__ == "__main__":
    # Base.metadata.drop_all(database.link)
    try:
        Base.metadata.create_all(database.link)

    except Exception as e:
        print("seguimos adelante")
