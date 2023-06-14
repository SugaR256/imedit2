from PySide6.QtWidgets import QWidget
from ui_form import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
