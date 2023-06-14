import io

from PIL import Image
from PySide6.QtCore import QByteArray, QBuffer, QIODevice
from PySide6.QtGui import QPixmap, QImage


def pil_to_pixmap(pil_image: Image) -> QPixmap:
    bytes_buf = io.BytesIO()
    pil_image.save(bytes_buf, format='PNG')
    bytes_buf.seek(0)
    qimage = QImage.fromData(bytes_buf.read(), 'PNG')
    return QPixmap.fromImage(qimage)


def pixmap_to_pil(pixmap: QPixmap) -> Image:
    qimage = pixmap.toImage()
    ba = QByteArray()
    buffer = QBuffer(ba)
    buffer.open(QIODevice.WriteOnly)
    qimage.save(buffer, 'PNG')
    pil_im = Image.open(io.BytesIO(ba.data()))
    return pil_im
