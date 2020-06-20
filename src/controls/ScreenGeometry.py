import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

# 创建按钮点击事件
def onClick_Button():
    print("1")
    print("widget.x()={}".format(widget.x()))
    print("widget.y()={}".format(widget.y()))
    print("widget.width()={}".format(widget.width()))
    print("widget.height()={}".format(widget.height()))

    print("2")
    print("widget.geometry()={}".format(widget.geometry().x()))
    print("widget.geometry()={}".format(widget.geometry().y()))
    print("widget.geometry.width()={}".format(widget.geometry().width()))
    print("widget.geometry.height()={}".format(widget.geometry().height()))

    print("3")
    print("widget.frameGeometry()={}".format(widget.frameGeometry().x()))
    print("widget.frameGeometry()={}".format(widget.frameGeometry().y()))
    print("widget.frameGeometry.width()={}".format(widget.frameGeometry().width()))
    print("widget.frameGeometry.height()={}".format(widget.frameGeometry().height()))

# 创建按钮
widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)

widget.resize(300, 240)  # 设置工作区的尺寸
widget.move(250, 250)
widget.setWindowTitle("屏幕坐标系")

widget.show()
sys.exit(app.exec_())

