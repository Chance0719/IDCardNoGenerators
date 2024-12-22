import sys
import Ui_IDCardGenerator
from PyQt6.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    IDCardGenerator = QWidget()
    Ui_IDCardGenerator.Ui_IDCardGenerator().setupUi(IDCardGenerator)
    IDCardGenerator.show()

    sys.exit(app.exec())