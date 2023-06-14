from common import pixmap_to_pil, pil_to_pixmap
from gl import gl
from undo_redo import set_pixmap


def apply_filter(fil):
    image = pixmap_to_pil(gl.pixmap)

    filtered_image = image.filter(fil)

    filtered = pil_to_pixmap(filtered_image)

    set_pixmap(filtered)
