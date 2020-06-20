"""
QLineEdit综合案例
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        # 使用整数校验器
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)  # 不超过9999
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial', 20))

        # 使用浮点数校验器
        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        # 使用掩码
        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        # 文本变化时触发的事件
        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        # 带密码的输入框
        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)

        # 只读模式
        edit6 = QLineEdit('hellow pyqt5')
        edit6.setReadOnly(True)

        # 创建表单页面
        formLayout = QFormLayout()
        formLayout.addRow('整数验证', edit1)
        formLayout.addRow('浮点数验证', edit2)
        formLayout.addRow('掩码', edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('带密码的文本', edit5)
        formLayout.addRow('只读模式', edit6)

        self.setLayout(formLayout)
        self.setWindowTitle("QLineEditDemo")

    def textChanged(self, text):
        print('输入的内容：{}'.format(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())