from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from common import pil_to_pixmap, pixmap_to_pil
from gl import gl
from undo_redo import set_pixmap


class SingleEnhancerDialog(QDialog):
    def __init__(self, enhancer, title: str):
        super(SingleEnhancerDialog, self).__init__(gl.main_window)
        self.setWindowTitle(title)
        self.enhancer = enhancer
        ver_layout = QVBoxLayout()

        hor_layout1 = QHBoxLayout()

        self.original_pixmap = gl.pixmap
        self.pil = pixmap_to_pil(gl.pixmap)

        self.current_percentage = QLabel(None)
        self.current_percentage.setText('0%')
        hor_layout1.addWidget(self.current_percentage)

        self.slider = QSlider(Qt.Horizontal, None)
        self.slider.setRange(-100, 100)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(lambda value: self.current_percentage.setText(f'{value}%'))
        self.slider.valueChanged.connect(lambda: self.adjust_image_property(False, False, True))
        hor_layout1.addWidget(self.slider)

        ver_layout.addLayout(hor_layout1)

        hor_layout2 = QHBoxLayout()

        ok_button = QPushButton('Ok', None)
        ok_button.clicked.connect(self.accept)

        cancel_button = QPushButton('Anuluj', None)
        cancel_button.clicked.connect(self.reject)

        hor_layout2.addWidget(ok_button)
        hor_layout2.addWidget(cancel_button)

        ver_layout.addLayout(hor_layout2)

        self.setLayout(ver_layout)

    def adjust_image_property(self, apply_undo: bool, refresh_histogram: bool, fast: bool):

        new_value = 1 + (self.slider.value() / 100)
        enhancer = self.enhancer(self.pil)

        pil_im = enhancer.enhance(new_value)

        new_pixmap = pil_to_pixmap(pil_im)
        set_pixmap(new_pixmap, apply_undo, refresh_histogram, fast)

    def accept(self):
        self.adjust_image_property(True, True, False)
        gl.history.append(self.original_pixmap)
        gl.future = None
        super(SingleEnhancerDialog, self).accept()

    def reject(self):
        set_pixmap(self.original_pixmap, False)
        super(SingleEnhancerDialog, self).reject()
