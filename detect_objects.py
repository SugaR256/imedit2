from PySide6.QtWidgets import QTableWidgetItem
from imageai.Detection import ObjectDetection
import os
from gl import gl

from common import pixmap_to_pil


def detect_objects():
    pil = pixmap_to_pil(gl.pixmap)

    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, 'retinanet.pth'))
    detector.loadModel()

    detections = detector.detectObjectsFromImage(input_image=pil, output_type='array')

    items_list = gl.main_window.ui.itemsList

    items_list.setColumnCount(2)
    items_list.setRowCount(len(detections[1]))

    for index, item in enumerate(detections[1]):
        items_list.setItem(index, 0, QTableWidgetItem(item['name']))
        items_list.setItem(index, 1, QTableWidgetItem(str(item['percentage_probability']) + '%'))
