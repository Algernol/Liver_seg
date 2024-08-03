import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from mainui import Ui_MainWindow

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 创建Qt应用程序实例
    app = QApplication(sys.argv)

    # 创建一个QWidget对象，作为主窗口
    w = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)

    w.show()

    # 运行Qt应用程序
    sys.exit(app.exec_())