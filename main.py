import sys
import Ui_IDCardGenerator
import test
from PyQt6.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    IDCardGenerator = QWidget()
    ui = Ui_IDCardGenerator.Ui_IDCardGenerator()
    ui.setupUi(IDCardGenerator)
    IDCardGenerator.show()

    sys.exit(app.exec())