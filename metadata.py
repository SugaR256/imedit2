from PySide6.QtGui import QPixmap, QImage

from gl import gl
import os
import datetime
import time
from win32_setctime import setctime


def refresh_metadata(*args):
    ui = gl.main_window.ui
    if len(args) > 0:
        width, height, depth = image_info(gl.pixmap)
        ui.widthLabel.setText(str(width) + ' px')
        ui.heightLabel.setText(str(height) + ' px')
        ui.depthLabel.setText(str(depth) + ' b')
        if args[0] is not QPixmap:
            path = args[0]
            ui.sizeLabel.setText(file_size_in_bytes(path))
            creation_date, modification_date = get_file_dates(path)
            ui.creationDate.setDateTime(creation_date)
            ui.modificationDate.setDateTime(modification_date)


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G']:
        if abs(num) < 1024.0:
            return "%.0f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.0f %s%s" % (num, 'T', suffix)


def file_size_in_bytes(file_path):
    byte_size = os.path.getsize(file_path)
    return sizeof_fmt(byte_size)


def image_info(img):
    if isinstance(img, QPixmap):
        image = img.toImage()
    else:
        image = QImage(img)

    width = image.width()
    height = image.height()
    depth = image.depth()

    return width, height, depth


def get_file_dates(file_path):
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)

    creation_date = datetime.datetime.fromtimestamp(creation_time)
    modification_date = datetime.datetime.fromtimestamp(modification_time)

    return creation_date, modification_date


def set_file_dates(file_path, creation_date, modification_date):
    if creation_date is not None:
        creation_time = time.mktime(creation_date.toPython().timetuple())
    else:
        creation_time = time.mktime(gl.main_window.ui.creationDate.dateTime().toPython().timetuple())
    if modification_date is not None:
        modification_time = time.mktime(modification_date.toPython().timetuple())
    else:
        modification_time = time.mktime(gl.main_window.ui.modificationDate.dateTime().toPython().timetuple())
    setctime(file_path, creation_time)
    os.utime(file_path, (modification_time, modification_time))
