# 显示控件提示信息

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip("今天是<b>星期六</b>")
        self.setGeometry(300, 300, 200, 300)
        self.setWindowTitle("设置控件提示信息")

        # 添加Button
        self.button1 = QPushButton("这是我的按钮")
        # 将信号与槽关联
        self.button1.setToolTip("这是一个按钮")

        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())