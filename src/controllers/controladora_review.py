from views.ui_vista_review import Ui_Sprint_Review
from PySide6.QtWidgets import QWidget

class SprintReview(QWidget, Ui_Sprint_Review):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
