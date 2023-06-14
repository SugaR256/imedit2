from PySide6.QtWidgets import QDialog, QVBoxLayout, QGraphicsScene, QPushButton, QGraphicsRectItem, \
    QApplication, QGraphicsView, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QPen, QPainter
from PySide6.QtCore import QRectF, Qt

from gl import gl
from undo_redo import set_pixmap


class ResizableRectItem(QGraphicsRectItem):
    def __init__(self, rect):
        super().__init__(rect)
        self._start_rect = None
        self._start_pos = None
        self.setFlag(QGraphicsRectItem.ItemIsMovable, True)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsRectItem.ItemSendsGeometryChanges, True)
        self.setPen(QPen(Qt.green))

    def mousePressEvent(self, event):
        self._start_pos = event.scenePos()
        self._start_rect = self.rect()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.isSelected() and QApplication.mouseButtons() == Qt.LeftButton:
            rect = self.rect()
            if rect.bottomRight().x() - event.pos().x() < 30 and rect.bottomRight().y() - event.pos().y() < 30:
                dx = event.scenePos().x() - self._start_pos.x()
                dy = event.scenePos().y() - self._start_pos.y()
                self.setRect(QRectF(self._start_rect.x(), self._start_rect.y(), self._start_rect.width() + dx,
                                    self._start_rect.height() + dy))
            else:
                super().mouseMoveEvent(event)
        else:
            super().mouseMoveEvent(event)


class CropDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(1000, 800)

        self.view = QGraphicsView(self)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        self.pixmap = gl.pixmap

        self.scale_factor = min(
            1000 / self.pixmap.width(),
            800 / self.pixmap.height()
        )

        self.scaled_pixmap = self.pixmap.scaled(
            self.pixmap.width() * self.scale_factor,
            self.pixmap.height() * self.scale_factor,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.pixmap_item = QGraphicsPixmapItem(self.scaled_pixmap)
        self.scene.addItem(self.pixmap_item)

        self.crop_rect_item = ResizableRectItem(QRectF(0, 0, 200, 200))
        self.scene.addItem(self.crop_rect_item)

        self.button = QPushButton('Przytnij', self)
        self.button.clicked.connect(self.crop_image)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.view)
        self.layout().addWidget(self.button)

    def crop_image(self):
        rect = self.crop_rect_item.rect()

        top_left = self.crop_rect_item.mapToItem(self.pixmap_item, rect.topLeft())
        bottom_right = self.crop_rect_item.mapToItem(self.pixmap_item, rect.bottomRight())

        rect = QRectF(top_left, bottom_right)

        rect = QRectF(
            rect.x() / self.scale_factor,
            rect.y() / self.scale_factor,
            rect.width() / self.scale_factor,
            rect.height() / self.scale_factor
        )

        image = self.pixmap.toImage()

        cropped_image = image.copy(rect.toRect())
        cropped_pixmap = QPixmap.fromImage(cropped_image)
        set_pixmap(cropped_pixmap)
        self.accept()
