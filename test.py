import sys
from PyQt6.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.provinceSel = QComboBox(self)
        self.provinceSel.setObjectName("provinceSel")
        self.provinceSel.addItems(["Option 1", "Option 2", "Option 3", "Option 4",
                                   "Option 5", "Option 6", "Option 7", "Option 8",
                                   "Option 9", "Option 10", "Option 11", "Option 12"])

        # Set maximum visible items to 10 using stylesheet
        self.provinceSel.setStyleSheet("QComboBox QAbstractItemView { max-height: 150px; }")

        layout.addWidget(self.provinceSel)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
