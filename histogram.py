import io
import numpy as np
from matplotlib import pyplot as plt
from PySide6.QtGui import QPixmap

from gl import gl


def refresh_histogram():
    image = gl.pixmap.toImage()

    ptr = image.bits()
    arr = np.frombuffer(ptr, np.uint8).reshape((image.height(), image.width(), 4))

    gray = np.mean(arr[..., :3], axis=-1)

    plt.figure(figsize=(10, 5))

    hist, bins = np.histogram(gray, bins=256, range=(0, 256))
    plt.plot(bins[:-1], hist, color='black')

    plt.axis('off')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()
    buf.seek(0)

    result_pixmap = QPixmap()
    result_pixmap.loadFromData(buf.read(), 'png')

    gl.main_window.ui.histogramLabel.setPixmap(result_pixmap)



