from PySide6.QtGui import QPixmap, QTransform

from gl import gl
from undo_redo import set_pixmap


def rotate_pixmap(direction: str):
    image = gl.pixmap.toImage()

    transform = QTransform()

    if direction == 'left':
        transform.rotate(-90)
    else:
        transform.rotate(90)

    rotated_image = image.transformed(transform)

    rotated_pixmap = QPixmap.fromImage(rotated_image)

    set_pixmap(rotated_pixmap)
