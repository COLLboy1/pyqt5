"""
按钮控件(QPushButton)

QPushButton
AToolButton
QRadioButton
QCheckBox
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QPushButtonDemo(QWidget):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("按钮控件")

        layout = QVBoxLayout()

        self.button1 = QPushButton("第一个按钮")
        self.button1.setText('First Button1')
        # 让按钮处于选中状态
        self.button1.setCheckable(True)
        self.button1.toggle()

        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))

        layout.addWidget(self.button1)

        # 在问本前面显示图像
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap("./images/1.jpg")))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda :self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400, 400)

    def buttonState(self):
        if self.button1.isCheckable():
            print("被选中")
        else:
            print("未被选中")

    def whichButton(self, btn):
        print('ok')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())