import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)

        button = QPushButton('Get Position', self)
        button.clicked.connect(self.get_position)
        layout = QVBoxLayout()
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_position(self):
        pos = self.pos()
        print(f'Window position: x = {pos.x()}, y = {pos.y()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
