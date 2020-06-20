"""
现在QLineEdit控件的输入（校验器）
如限制只能输入整数，浮点数或满足一定条件的字符串
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("校验器")

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        floatLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('小数类型', floatLineEdit)
        formLayout.addRow('数字和字母类型', validatorLineEdit)

        intLineEdit.setPlaceholderText('整数')
        floatLineEdit.setPlaceholderText('浮点类型')
        validatorLineEdit.setPlaceholderText('数字和字母')

        # 整数校验器
        intValidator = QIntValidator()
        intValidator.setRange(1, 99)

        # 浮点校验器
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点后两位
        doubleValidator.setDecimals(2)

        # 字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        floatLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())