from PySide6.QtWidgets import QInputDialog
from PIL import ImageFilter

from common import pixmap_to_pil, pil_to_pixmap
from gl import gl
from undo_redo import set_pixmap


def apply_gaussian_blur():
    blur_radius, ok = QInputDialog.getInt(None, 'Rozmycie Gaussa', 'Wprowadź promień rozmycia', 10, 1, 50, 1)
    if not ok:
        return

    image = pixmap_to_pil(gl.pixmap)

    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

    blurred = pil_to_pixmap(blurred_image)

    set_pixmap(blurred, True, True)
