# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(913, 600)
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-20, 130, 1038, 412))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_label = QLabel(self.horizontalLayoutWidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(600, 400))
        self.image_label.setMaximumSize(QSize(800, 600))
        self.image_label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.image_label)

        self.result_label = QLabel(self.horizontalLayoutWidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(200, 50))
        self.result_label.setMaximumSize(QSize(400, 100))
        self.result_label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.result_label)

        self.load_button = QPushButton(self.horizontalLayoutWidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setMinimumSize(QSize(100, 40))
        self.load_button.setMaximumSize(QSize(150, 50))

        self.horizontalLayout.addWidget(self.load_button)

        self.count_button = QPushButton(self.horizontalLayoutWidget)
        self.count_button.setObjectName(u"count_button")
        self.count_button.setEnabled(False)
        self.count_button.setMinimumSize(QSize(100, 40))
        self.count_button.setMaximumSize(QSize(150, 50))

        self.horizontalLayout.addWidget(self.count_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.image_label.setText(QCoreApplication.translate("Widget", u"No Image Loaded", None))
        self.result_label.setText(QCoreApplication.translate("Widget", u"Cell Count: N/A", None))
        self.load_button.setText(QCoreApplication.translate("Widget", u"Load Image", None))
        self.count_button.setText(QCoreApplication.translate("Widget", u"Count Cells", None))
    # retranslateUi

