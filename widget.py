import sys  #Allows interaction with the system
import cv2  #Handles image processing tasks such as reading images, converting to grayscale, applying filters, and drawing contours
from PySide6.QtWidgets import (
    QApplication,  #Manages application-wide settings and control, like event handling and GUI initialization
    QMainWindow,   #Serves as the main window of the application, providing a structure for adding widgets
    QLabel,        #Displays text or images in the GUI, such as the loaded image or result
    QPushButton,   #Represents a clickable button in the GUI, used to trigger actions like loading an image or counting cells
    QFileDialog,   #Opens a dialog for selecting an image file
    QVBoxLayout,   #Organizes the layout by embedding the Matplotlib canvas in the GUI
    QHBoxLayout,   #This layout is useful for organizing buttons or widgets horizontally.
    QWidget,       #Serves as a container for other widgets and can also act as a standalone window.
    QDialog,       #It can be modal (blocking input to other windows) or modeless, depending on the use case.

)  #Includes GUI widgets like QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QDialog to build the user interface
from PySide6.QtGui import QPixmap  #QPixmap displays images in the GUI
from PySide6.QtCore import Qt  # It is essential for defining behaviors and properties in PySide6 applications.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
#Used for creating and embedding plots into the GUI. The FigureCanvasQTAgg class integrates Matplotlib figures into the PySide6 interface

matplotlib.use('QtAgg')  # Use a Qt-compatible backend


class CellCounterApp(QMainWindow):
    def __init__(self):  #Loads the UI file, Sets up references to GUI components, Connects button signals to corresponding methods, Creates a Matplotlib canvas for displaying image processing results
        super().__init__()

        self.setWindowTitle("Cell Counter") #Set the title and minimum size of the main window
        self.setMinimumSize(800, 600)

        # Görüntü etiketi ve sonuç etiketi
        self.image_label = QLabel("No Image Loaded") #Create the image label to display loaded images
        self.image_label.setAlignment(Qt.AlignCenter) #"No Image Loaded" is the default text, and the label is centered with fixed dimensions
        self.image_label.setFixedSize(600, 400)

        self.result_label = QLabel("Cell Count: N/A") #Create the result label to display the cell count
        self.result_label.setAlignment(Qt.AlignCenter) # The default text is "Cell Count: N/A", and the label is centered

        # Butonlar
        self.load_button = QPushButton("Load Image") #Create buttons for loading an image and counting cells
        self.count_button = QPushButton("Count Cells") # The "Count Cells" button is disabled initially until an image is loaded
        self.count_button.setEnabled(False)

        self.load_button.clicked.connect(self.load_image) #Connect button clicks to their respective event handlers
        self.count_button.clicked.connect(self.count_cells)

        #Initialize and set up the layout for the main window components
        self.init_layout()

        #Initialize image data attributes
        self.image_path = None
        self.original_image = None

    def init_layout(self):
        """Create the layout structure."""
        #Create a vertical layout for the image and result labels
        image_layout = QVBoxLayout()
        image_layout.addWidget(self.image_label) #Add the image label to the layout
        image_layout.addWidget(self.result_label) #Add the result label to the layout

        #Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_button) # Add the load button and count button to the button layout
        button_layout.addWidget(self.count_button)

        #Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(image_layout) #Add image and result layout to main layout
        main_layout.addLayout(button_layout) #Add button layout to main layout

        #Set the widget
        container = QWidget()
        container.setLayout(main_layout) #Set the main layout to the container widget
        self.setCentralWidget(container) #Set the container widget as the central widget of the window

    def load_image(self):
        """Load the image."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.image_path = file_path #Set the image path
            self.original_image = cv2.imread(self.image_path) #Read the image using OpenCV

            #Scale the image and add it to the label
            pixmap = QPixmap(self.image_path).scaled(
                self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio
            ) #Scale the image to fit the label size while keeping aspect ratio
            self.image_label.setPixmap(pixmap) #Set the scaled image to the label
            self.result_label.setText("Cell Count: N/A") #Set the initial result label text
            self.count_button.setEnabled(True) #Enable the "Count Cells" button

    def count_cells(self):
        """Detect and count cells."""
        if self.original_image is None:
            return

        #Convert the image to grayscale
        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

        #Apply Gaussian blur to the grayscale image to reduce noise and smooth the image
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)

        #Apply thresholding to create a binary image
        _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV) #This applies a binary threshold, converting pixel values: those above 127 to 0 (black) and those below to 255 (white), with cv2.THRESH_BINARY_INV inverting the result to highlight objects of interest

        #Find contours in the binary image
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get the number of detected contours
        cell_count = len(contours) #Counts how many contours were found
        self.result_label.setText(f"Cell Count: {cell_count}")

        #Draw the contours on the original image
        output_image = self.original_image.copy()
        cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)
        #-1: Indicates that all detected contours should be drawn and useful for visualizing every detected cell or object
        #(0, 255, 0): Represents the color green in BGR format (Blue, Green, Red), Green is commonly used for overlays because it contrasts well against most image backgrounds
        #2: Specifies the thickness of the contour lines in pixels, A thickness of 2 ensures the contours are clearly visible without overwhelming the image details

        #Show the graphs in a new window
        self.show_graph(output_image)

    def show_graph(self, output_image):
        """Show the graphs in a new window."""
        graph_window = QDialog(self) #Create a new dialog window for displaying the graph
        graph_window.setWindowTitle("Cell Count Graph")
        graph_window.setMinimumSize(1200, 600) #Set the minimum size for the graph window

        #Create a new FigureCanvas with a figure size of 16x8 inches
        canvas = FigureCanvas(plt.figure(figsize=(16, 8))) #16x8 inches provides a wide and clear view for the graph

        #Create a vertical layout for the graph window and add the canvas widget to it
        layout = QVBoxLayout(graph_window)
        layout.addWidget(canvas)

        #Create a Matplotlib figure
        canvas.figure.clear() #Clear previous figures
        ax1 = canvas.figure.add_subplot(1, 2, 1) #(rows,columns,index)  #1, 2 creates a single-row, two-column layout to display two images side by side, 1 specifies the subplot for the original image, placed in the first position of the grid
        ax1.set_title("Original Image")
        ax1.imshow(cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)) #Convert from BGR to RGB

        ax2 = canvas.figure.add_subplot(1, 2, 2) #(rows,columns,index)  #1, 2 creates a single-row, two-column layout to display two images side by side, 2 specifies the subplot for the processed (contoured) image, placed in the second position of the grid
        ax2.set_title("Contours")
        ax2.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))

        #Update the canvas
        canvas.draw()

        #Execute the dialog window and display it
        graph_window.exec()


if __name__ == "__main__":  #Entry point of the application
    app = QApplication(sys.argv) #Create the application instance
    window = CellCounterApp() #Create an instance of the CellCounterApp
    window.show() #Show the main window
    app.exec() #Start the event loop to handle user interactions












