"""
颜色对话框: QColorDialog
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("颜色对话框")

        layout = QVBoxLayout()
        self.colorbutton = QPushButton('选择颜色')
        self.colorbutton.clicked.connect(self.getColor)
        layout.addWidget(self.colorbutton)

        self.colorlabel = QLabel('Hello, 测试字体例子')
        layout.addWidget(self.colorlabel)

        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(p.WindowText, color)
        self.colorlabel.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())