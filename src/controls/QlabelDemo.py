"""
Qlabel控件
setAlignment()：设置文本的对齐方式
setIndent()：设置文本缩进
text(): 获取文本内容
setBuddy(): 设置伙伴关系
setText(): 设置文本内容
selectedText(): 返回所选择的字符
setWoedWrap(): 是指是否允许换行

Qlabel常用的信号(事件)：
1、当鼠标滑过Qlabel控件时触发：linkHovered
2、当鼠标点击Qlabel控件时触发：linkActivated

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt

class QlabelDemo(QWidget):
    def __init__(self):
        super(QlabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font corlor=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)

        # 创建调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        # 设置居中对齐
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用python GUI程序</a>")

        label3.setToolTip('这是一个图像标签')
        label3.setPixmap(QPixmap("./images/1.jpg"))
        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText('<a href="http://182.92.235.234">感谢关注我的个人网站</a>')
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkClicked)

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle("Qlabel控件演示")
        self.setGeometry(100, 300, 200, 300)

    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发事件")

    def linkClicked(self):
        print("当鼠标点击label4标签时，触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelDemo()
    main.show()
    sys.exit(app.exec_())