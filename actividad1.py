import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QGridLayout, QWidget, QAction
from PyQt5.QtGui import QPixmap

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visor de Imágenes')
        self.setGeometry(100, 100, 400, 350)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        central_widget.setLayout(layout)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Archivo')

        open_action = QAction('&Abrir Imagen', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Abrir una imagen')
        open_action.triggered.connect(self.openImage)
        fileMenu.addAction(open_action)

        open_button = QPushButton('Abrir Imagen', self)
        open_button.clicked.connect(self.openImage)
        layout.addWidget(open_button, 0, 0)

        self.label = QLabel(self)
        layout.addWidget(self.label, 1, 0)

        self.show()

    def openImage(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Imagen", "", "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.label.setPixmap(pixmap.scaled(self.label.size(), aspectRatioMode=True))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageViewer()
    sys.exit(app.exec_())