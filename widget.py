# This Python file uses the following encoding: utf-8
import sys
import cv2
import numpy as np
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout)
from PySide6.QtGui import QPixmap, QImage
from matplotlib import pyplot as plt


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class CellCounterApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Cell Counter")
        self.setGeometry(100,100,800,600)

        # Widgets
        self.image_label = QLabel("No Image Loaded", self)
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(600, 400)

        self.result_label = QLabel("Cell Count: N/A", self)

        self.load_button = QPushButton("Load Image", self)
        self.load_button.clicked.connect(self.load_image)

        self.count_button = QPushButton("Count Cells", self)
        self.count_button.clicked.connect(self.count_cells)
        self.count_button.setEnabled(False)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.count_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Attributes
        self.image_path = None
        self.original_image = None


    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.image_path = file_path
            self.original_image = cv2.imread(self.image_path)

             # Display the image in the QLabel
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(pixmap)
            self.result_label.setText("Cell Count: N/A")
            self.count_button.setEnabled(True)

    def count_cells(self):
        if self.original_image is None:
            return

        # Process the image
        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Count cells
        cell_count = len(contours)
        self.result_label.setText(f"Cell Count: {cell_count}")

        # Draw contours on the original image
        output_image = self.original_image.copy()
        cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)

        # Show processed image using matplotlib
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.title("Original Image")
        plt.imshow(cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB))

        plt.subplot(1, 2, 2)
        plt.title("Contours")
        plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
        plt.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CellCounterApp()
    window.show()
    sys.exit(app.exec())
