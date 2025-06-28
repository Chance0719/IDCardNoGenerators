import sys, os

from PyQt6.QtGui import QIcon

import Ui_IDCardGenerator
import test
from PyQt6.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    IDCardGenerator = QWidget()
    ui = Ui_IDCardGenerator.Ui_IDCardGenerator()
    ui.setupUi(IDCardGenerator)
    p = os.path.realpath(sys.path[0])
    p = p.replace(r'\base_library.zip', '')
    IDCardGenerator.setWindowIcon(QIcon(p + '/icon/card3.ico'))
    IDCardGenerator.show()


    sys.exit(app.exec())