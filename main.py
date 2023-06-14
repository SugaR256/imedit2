from PIL import ImageEnhance, ImageFilter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
import sys

import undo_redo
from apply_filter import apply_filter
from crop_image_dialog import CropDialog
from detect_objects import detect_objects
from gaussian_blur import apply_gaussian_blur
from gl import gl
from mainwindow import MainWindow
from metadata import refresh_metadata, set_file_dates
from rotate import rotate_pixmap
from single_enhancer_dialog import SingleEnhancerDialog


def open_image():
    file_name = \
        QFileDialog.getOpenFileName(gl.main_window, 'Wybierz obraz', '', 'Pliki obrazów (*.jpg *.gif *.svg *.png)')[0]
    if file_name != '':
        undo_redo.set_pixmap(QPixmap(file_name), enable_undo=False)
        gl.file_name = file_name
        gl.main_window.ui.originalImageField.setPixmap(
            gl.pixmap.scaled(gl.main_window.ui.originalImageField.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        refresh_metadata(file_name)


def save_image():
    if gl.pixmap is None:
        return
    gl.pixmap.save(gl.file_name)
    gl.main_window.ui.originalImageField.setPixmap(
        gl.pixmap.scaled(gl.main_window.ui.originalImageField.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    refresh_metadata(gl.file_name)


def save_image_as():
    if gl.pixmap is None:
        return
    file_name = \
        QFileDialog.getSaveFileName(gl.main_window, 'Zapisz obraz', '', 'Pliki obrazów (*.jpg *.gif *.svg *.png)')[0]
    if file_name != '':
        gl.pixmap.save(file_name)
        gl.main_window.ui.originalImageField.setPixmap(
            gl.pixmap.scaled(gl.main_window.ui.originalImageField.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        refresh_metadata(file_name)


if __name__ == '__main__':
    app = QApplication()
    gl.main_window = MainWindow()
    ui = gl.main_window.ui

    ui.openButton.clicked.connect(open_image)
    ui.saveAsButton.clicked.connect(save_image_as)
    ui.contrastButton.clicked.connect(
        lambda: SingleEnhancerDialog(ImageEnhance.Contrast, 'Kontrast').exec() if gl.pixmap is not None else None)
    ui.brightnessButton.clicked.connect(
        lambda: SingleEnhancerDialog(ImageEnhance.Brightness, 'Jasność').exec() if gl.pixmap is not None else None)
    ui.saturationButton.clicked.connect(
        lambda: SingleEnhancerDialog(ImageEnhance.Color, 'Saturacja').exec() if gl.pixmap is not None else None)
    ui.sharpnessButton.clicked.connect(
        lambda: SingleEnhancerDialog(ImageEnhance.Sharpness, 'Ostrość').exec() if gl.pixmap is not None else None)
    ui.cropButton.clicked.connect(lambda: CropDialog().exec() if gl.pixmap is not None else None)
    ui.saveButton.clicked.connect(save_image)
    ui.undoButton.clicked.connect(undo_redo.undo_action)
    ui.redoButton.clicked.connect(undo_redo.redo_action)
    ui.creationDate.dateTimeChanged.connect(lambda date_time: set_file_dates(gl.file_name, date_time, None) if gl.file_name is not None else None)
    ui.modificationDate.dateTimeChanged.connect(lambda date_time: set_file_dates(gl.file_name, None, date_time) if gl.file_name is not None else None)
    ui.blurButton.clicked.connect(lambda: apply_gaussian_blur() if gl.pixmap is not None else None)
    ui.turnLeftButton.clicked.connect(lambda: rotate_pixmap('left') if gl.pixmap is not None else None)
    ui.turnRightButton.clicked.connect(lambda: rotate_pixmap('right') if gl.pixmap is not None else None)
    ui.findEdgesButton.clicked.connect(lambda: apply_filter(ImageFilter.FIND_EDGES()) if gl.pixmap is not None else None)
    ui.enhanceEdgesButton.clicked.connect(lambda: apply_filter(ImageFilter.EDGE_ENHANCE_MORE()) if gl.pixmap is not None else None)
    ui.identifyButton.clicked.connect(lambda: detect_objects() if gl.pixmap is not None else None)

    gl.main_window.show()
    sys.exit(app.exec())
