# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1929, 960)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(-1, -1, 96, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(1500, 0))
        self.label.setSizeIncrement(QtCore.QSize(1500, 920))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formWidget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formWidget_2.sizePolicy().hasHeightForWidth())
        self.formWidget_2.setSizePolicy(sizePolicy)
        self.formWidget_2.setObjectName("formWidget_2")
        self.formLayout_9 = QtWidgets.QFormLayout(self.formWidget_2)
        self.formLayout_9.setContentsMargins(-1, 33, 4, 40)
        self.formLayout_9.setHorizontalSpacing(6)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_move = QtWidgets.QLabel(self.formWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_move.sizePolicy().hasHeightForWidth())
        self.label_move.setSizePolicy(sizePolicy)
        self.label_move.setObjectName("label_move")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_move)
        self.label_dx = QtWidgets.QLabel(self.formWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dx.sizePolicy().hasHeightForWidth())
        self.label_dx.setSizePolicy(sizePolicy)
        self.label_dx.setObjectName("label_dx")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_dx)
        self.label_dy = QtWidgets.QLabel(self.formWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dy.sizePolicy().hasHeightForWidth())
        self.label_dy.setSizePolicy(sizePolicy)
        self.label_dy.setObjectName("label_dy")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_dy)
        self.button_move = QtWidgets.QPushButton(self.formWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_move.sizePolicy().hasHeightForWidth())
        self.button_move.setSizePolicy(sizePolicy)
        self.button_move.setObjectName("button_move")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.button_move)
        self.entry_move_dx = QtWidgets.QLineEdit(self.formWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_move_dx.sizePolicy().hasHeightForWidth())
        self.entry_move_dx.setSizePolicy(sizePolicy)
        self.entry_move_dx.setObjectName("entry_move_dx")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.entry_move_dx)
        self.entry_move_dy = QtWidgets.QLineEdit(self.formWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_move_dy.sizePolicy().hasHeightForWidth())
        self.entry_move_dy.setSizePolicy(sizePolicy)
        self.entry_move_dy.setObjectName("entry_move_dy")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.entry_move_dy)
        self.verticalLayout_3.addWidget(self.formWidget_2)
        self.formWidget = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formWidget.sizePolicy().hasHeightForWidth())
        self.formWidget.setSizePolicy(sizePolicy)
        self.formWidget.setObjectName("formWidget")
        self.formLayout_8 = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout_8.setContentsMargins(-1, -1, -1, 1)
        self.formLayout_8.setHorizontalSpacing(50)
        self.formLayout_8.setVerticalSpacing(6)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_zoom_x = QtWidgets.QLabel(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_zoom_x.sizePolicy().hasHeightForWidth())
        self.label_zoom_x.setSizePolicy(sizePolicy)
        self.label_zoom_x.setObjectName("label_zoom_x")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_zoom_x)
        self.label_zoom_y = QtWidgets.QLabel(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_zoom_y.sizePolicy().hasHeightForWidth())
        self.label_zoom_y.setSizePolicy(sizePolicy)
        self.label_zoom_y.setObjectName("label_zoom_y")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_zoom_y)
        self.label_zoom = QtWidgets.QLabel(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_zoom.sizePolicy().hasHeightForWidth())
        self.label_zoom.setSizePolicy(sizePolicy)
        self.label_zoom.setObjectName("label_zoom")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_zoom)
        self.label_kx = QtWidgets.QLabel(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_kx.sizePolicy().hasHeightForWidth())
        self.label_kx.setSizePolicy(sizePolicy)
        self.label_kx.setObjectName("label_kx")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_kx)
        self.label_ky = QtWidgets.QLabel(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ky.sizePolicy().hasHeightForWidth())
        self.label_ky.setSizePolicy(sizePolicy)
        self.label_ky.setObjectName("label_ky")
        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_ky)
        self.button_zoom = QtWidgets.QPushButton(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_zoom.sizePolicy().hasHeightForWidth())
        self.button_zoom.setSizePolicy(sizePolicy)
        self.button_zoom.setObjectName("button_zoom")
        self.formLayout_8.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.button_zoom)
        self.entry_zoom_x = QtWidgets.QLineEdit(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_zoom_x.sizePolicy().hasHeightForWidth())
        self.entry_zoom_x.setSizePolicy(sizePolicy)
        self.entry_zoom_x.setObjectName("entry_zoom_x")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.entry_zoom_x)
        self.entry_zoom_y = QtWidgets.QLineEdit(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_zoom_y.sizePolicy().hasHeightForWidth())
        self.entry_zoom_y.setSizePolicy(sizePolicy)
        self.entry_zoom_y.setObjectName("entry_zoom_y")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.entry_zoom_y)
        self.entry_kx = QtWidgets.QLineEdit(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_kx.sizePolicy().hasHeightForWidth())
        self.entry_kx.setSizePolicy(sizePolicy)
        self.entry_kx.setObjectName("entry_kx")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.entry_kx)
        self.entry_ky = QtWidgets.QLineEdit(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_ky.sizePolicy().hasHeightForWidth())
        self.entry_ky.setSizePolicy(sizePolicy)
        self.entry_ky.setObjectName("entry_ky")
        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.entry_ky)
        self.verticalLayout_3.addWidget(self.formWidget)
        self.formWidget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formWidget_3.sizePolicy().hasHeightForWidth())
        self.formWidget_3.setSizePolicy(sizePolicy)
        self.formWidget_3.setObjectName("formWidget_3")
        self.formLayout_10 = QtWidgets.QFormLayout(self.formWidget_3)
        self.formLayout_10.setContentsMargins(-1, 27, -1, 69)
        self.formLayout_10.setVerticalSpacing(6)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_rotate = QtWidgets.QLabel(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rotate.sizePolicy().hasHeightForWidth())
        self.label_rotate.setSizePolicy(sizePolicy)
        self.label_rotate.setObjectName("label_rotate")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_rotate)
        self.label_rotate_x = QtWidgets.QLabel(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rotate_x.sizePolicy().hasHeightForWidth())
        self.label_rotate_x.setSizePolicy(sizePolicy)
        self.label_rotate_x.setObjectName("label_rotate_x")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_rotate_x)
        self.entry_rotate_x = QtWidgets.QLineEdit(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_rotate_x.sizePolicy().hasHeightForWidth())
        self.entry_rotate_x.setSizePolicy(sizePolicy)
        self.entry_rotate_x.setObjectName("entry_rotate_x")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.entry_rotate_x)
        self.label_rotate_y = QtWidgets.QLabel(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rotate_y.sizePolicy().hasHeightForWidth())
        self.label_rotate_y.setSizePolicy(sizePolicy)
        self.label_rotate_y.setObjectName("label_rotate_y")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_rotate_y)
        self.entry_rotate_y = QtWidgets.QLineEdit(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_rotate_y.sizePolicy().hasHeightForWidth())
        self.entry_rotate_y.setSizePolicy(sizePolicy)
        self.entry_rotate_y.setObjectName("entry_rotate_y")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.entry_rotate_y)
        self.label_angle = QtWidgets.QLabel(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_angle.sizePolicy().hasHeightForWidth())
        self.label_angle.setSizePolicy(sizePolicy)
        self.label_angle.setObjectName("label_angle")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_angle)
        self.entry_angle = QtWidgets.QLineEdit(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_angle.sizePolicy().hasHeightForWidth())
        self.entry_angle.setSizePolicy(sizePolicy)
        self.entry_angle.setObjectName("entry_angle")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.entry_angle)
        self.button_rotate = QtWidgets.QPushButton(self.formWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rotate.sizePolicy().hasHeightForWidth())
        self.button_rotate.setSizePolicy(sizePolicy)
        self.button_rotate.setObjectName("button_rotate")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.button_rotate)
        self.verticalLayout_3.addWidget(self.formWidget_3)
        self.button_recover_first = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_recover_first.sizePolicy().hasHeightForWidth())
        self.button_recover_first.setSizePolicy(sizePolicy)
        self.button_recover_first.setObjectName("button_recover_first")
        self.verticalLayout_3.addWidget(self.button_recover_first)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_move.clicked.connect(lambda: self.move_image())
        self.button_zoom.clicked.connect(lambda: self.zoom_image())
        self.button_rotate.clicked.connect(lambda: self.rotate_image())
        self.button_recover_first.clicked.connect(lambda: self.draw_first_image())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_move.setText(_translate("MainWindow", "Перемещение"))
        self.label_dx.setText(_translate("MainWindow", "dx      "))
        self.label_dy.setText(_translate("MainWindow", "dy"))
        self.button_move.setText(_translate("MainWindow", "Выполнить\n"
"перемещение"))
        self.label_zoom_x.setText(_translate("MainWindow", "Xm"))
        self.label_zoom_y.setText(_translate("MainWindow", "Ym"))
        self.label_zoom.setText(_translate("MainWindow", "Масштабирование"))
        self.label_kx.setText(_translate("MainWindow", "kx"))
        self.label_ky.setText(_translate("MainWindow", "ky"))
        self.button_zoom.setText(_translate("MainWindow", "Выполнить\n"
"масштабирование"))
        self.label_rotate.setText(_translate("MainWindow", "Поворот"))
        self.label_rotate_x.setText(_translate("MainWindow", "Rx"))
        self.label_rotate_y.setText(_translate("MainWindow", "Ry"))
        self.label_angle.setText(_translate("MainWindow", "Угол"))
        self.button_rotate.setText(_translate("MainWindow", "Выполнить\n"
"поворот"))
        self.button_recover_first.setText(_translate("MainWindow", "Восстановить\n"
"изображение"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())