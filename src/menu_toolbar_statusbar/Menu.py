"""
创建和使用菜单;
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar()  # 获取菜单栏

        file = bar.addMenu("文件")
        file.addAction("新建")

        save = QAction("保存", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        save.triggered.connect(self.process)

    def process(self, a):
        print(self.sender().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())