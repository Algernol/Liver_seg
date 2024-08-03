import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PIL

import pydicom #pip install pydicom
import cv2 #pip install opencv-python
##import tensorflow as tf
import shutil

from mainui import Ui_MainWindow

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 创建Qt应用程序实例
    app = QApplication(sys.argv)

    # 创建一个QWidget对象，作为主窗口
    w = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)

    # data_path = r'Image/PATIENT_DICOM/image_0'
    # # 读取单张图片
    # img = pydicom.dcmread(data_path)
    # img_data = img.pixel_array
    # print(type(img_data))
    # # Normalize the pixel array to 0-255
    # pixel_array = (img.pixel_array - np.min(img.pixel_array)) / (np.max(img.pixel_array) - np.min(img.pixel_array)) * 255
    # pixel_array = pixel_array.astype(np.uint8)
    #
    # # Create QImage from pixel array
    # height, width = pixel_array.shape
    # bytes_per_line = width
    # q_image = QImage(pixel_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
    #
    # # Set the QImage to a QLabel
    # ui.or_image.setPixmap(QPixmap.fromImage(q_image))
    # ui.or_image.setScaledContents(True)  # Allow image to scale to label size


    w.show()

    # 运行Qt应用程序
    sys.exit(app.exec_())