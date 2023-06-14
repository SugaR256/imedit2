from PySide6.QtCore import Qt

from gl import gl
from histogram import refresh_histogram


def set_pixmap(pixmap, enable_undo=True, refresh_hist=True, fast=False):
    if enable_undo:
        gl.history.append(gl.pixmap)
        gl.main_window.ui.undoButton.setEnabled(enable_undo)
        gl.main_window.ui.redoButton.setEnabled(False)
        gl.future = None
    gl.pixmap = pixmap
    gl.main_window.ui.imageField.setPixmap(
        pixmap.scaled(gl.main_window.ui.imageField.size(), Qt.KeepAspectRatio, Qt.FastTransformation if fast else Qt.SmoothTransformation))
    if refresh_hist:
        refresh_histogram()


def undo_action():
    if len(gl.history) == 0:
        return
    gl.future = gl.pixmap
    set_pixmap(gl.history[-1], enable_undo=False, refresh_hist=True)
    gl.history = gl.history[:-1]
    gl.main_window.ui.undoButton.setEnabled(len(gl.history) > 0)
    gl.main_window.ui.redoButton.setEnabled(True)


def redo_action():
    if gl.future is None:
        return
    gl.history.append(gl.pixmap)
    set_pixmap(gl.future, enable_undo=False, refresh_hist=True)
    gl.future = None
    gl.main_window.ui.undoButton.setEnabled(True)
    gl.main_window.ui.redoButton.setEnabled(False)
