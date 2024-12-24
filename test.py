import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(0, 0, 400, 300)

        layout = QVBoxLayout()
        button = QPushButton("Open Dialog")
        button.clicked.connect(self.open_dialog)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_dialog(self):
        dialog = QDialog(self)  # 将主窗口作为父窗口传递给对话框
        dialog.setWindowTitle('Centered Dialog')

        layout = QVBoxLayout()
        label = QLabel("This is a centered dialog.")
        layout.addWidget(label)
        dialog.setLayout(layout)

        # 使用 exec() 方法使对话框模态显示
        dialog.exec()

        # 让对话框居中显示在主窗口内
        self.center_on_parent(dialog)

    def center_on_parent(self, dialog):
        frame_geometry = dialog.frameGeometry()
        parent_center = self.geometry().center()
        frame_geometry.moveCenter(parent_center)
        dialog.move(frame_geometry.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())