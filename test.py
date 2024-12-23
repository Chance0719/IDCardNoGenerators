from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PyQt6.QtCore import pyqtSlot
import sys


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化组合框
        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        # 添加选项到第一个组合框
        self.combo1.addItems(['Option 1', 'Option 2', 'Option 3'])

        # 设置布局并添加组件
        layout = QVBoxLayout()
        layout.addWidget(self.combo1)
        layout.addWidget(self.combo2)
        self.setLayout(layout)

        # 连接第一个组合框的信号到自定义槽函数
        self.combo1.currentIndexChanged.connect(self.update_second_combo)
        self.combo1.currentTextChanged.connect(self.on_text_changed)

    def update_second_combo(self, index):
        print(f"update_second_combo called with index: {index}")  # 调试信息
        try:
            self.combo2.clear()  # 清除所有项

            if index == 0:  # Option 1
                self.combo2.addItems(['Suboption 1.1', 'Suboption 1.2'])
            elif index == 1:  # Option 2
                self.combo2.addItems(['Suboption 2.1', 'Suboption 2.2', 'Suboption 2.3'])
            elif index == 2:  # Option 3
                self.combo2.addItems(['Suboption 3.1'])
        except Exception as e:
            print(f"An error occurred in update_second_combo: {e}")

    def on_text_changed(self, text):
        print(f"on_text_changed called with text: {text}")  # 调试信息
        try:
            print(f"Selected text from combo1: {text}")
        except Exception as e:
            print(f"An error occurred in on_text_changed: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())