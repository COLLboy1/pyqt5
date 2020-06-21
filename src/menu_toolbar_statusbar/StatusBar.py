"""
创建和使用状态栏
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("状态栏演示")
        self.resize(300, 200)

        layout = QVBoxLayout()
        self.buttun1 = QPushButton("状态栏显示")
        self.buttun1.clicked.connect(self.processTirgger)
        layout.addWidget(self.buttun1)
        self.setLayout(layout)

        # bar = self.menuBar()
        # file = bar.addMenu("file")
        # file.addAction('show')
        # file.triggered.connect(self.processTirgger)
        #
        # self.setCentralWidget(QTextEdit())
        # self.statusBar = QStatusBar()

    def processTirgger(self, q):
        if q.text() == "show":
            self.statusBar.showMessage('菜单被点击了', 5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec_())