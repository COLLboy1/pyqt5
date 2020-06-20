"""
消息对话框：QMessageBox

1、关于对话框
2、错误对话框
3、警告对话框
4、提问对话框
5、消息对话框

有2点差异
1、显示的对话框图标可能不同
2、显示的按钮是不一样的

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QMessageBox案例")
        self.resize(300, 400)

        layout = QVBoxLayout()
        self.button1 = QPushButton()
        self.button1.setText("显示关于对话框")
        self.button1.clicked.connect(self.showDialog)
        layout.addWidget(self.button1)

        self.button2 = QPushButton()
        self.button2.setText("消息对话框")
        self.button2.clicked.connect(self.showDialog)
        layout.addWidget(self.button2)

        self.button3 = QPushButton()
        self.button3.setText("警告对话框")
        self.button3.clicked.connect(self.showDialog)
        layout.addWidget(self.button3)

        self.button4 = QPushButton()
        self.button4.setText("错误对话框")
        self.button4.clicked.connect(self.showDialog)
        layout.addWidget(self.button4)

        self.button5 = QPushButton()
        self.button5.setText("提问对话框")
        self.button5.clicked.connect(self.showDialog)
        layout.addWidget(self.button5)

        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == "显示关于对话框":
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif text == "消息对话框":
            reply = QMessageBox.information(self,'消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No)
            print(reply == QMessageBox.Yes)
        elif text == "警告对话框":
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No)
        elif text == "错误对话框":
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())