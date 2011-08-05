# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Wed Aug  3 12:12:40 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(460, 274)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 251))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.source_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.source_button.setObjectName(_fromUtf8("source_button"))
        self.verticalLayout.addWidget(self.source_button)
        self.source_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.source_label.setObjectName(_fromUtf8("source_label"))
        self.verticalLayout.addWidget(self.source_label)
        self.input_files_box = QtGui.QHBoxLayout()
        self.input_files_box.setObjectName(_fromUtf8("input_files_box"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.input_files_box.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.input_files_box)
        self.target_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.target_button.setObjectName(_fromUtf8("target_button"))
        self.verticalLayout.addWidget(self.target_button)
        self.target_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.target_label.setObjectName(_fromUtf8("target_label"))
        self.verticalLayout.addWidget(self.target_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ldpi_box = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.ldpi_box.setChecked(True)
        self.ldpi_box.setObjectName(_fromUtf8("ldpi_box"))
        self.horizontalLayout.addWidget(self.ldpi_box)
        self.mdpi_box = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.mdpi_box.setChecked(True)
        self.mdpi_box.setObjectName(_fromUtf8("mdpi_box"))
        self.horizontalLayout.addWidget(self.mdpi_box)
        self.hdpi_box = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.hdpi_box.setChecked(True)
        self.hdpi_box.setObjectName(_fromUtf8("hdpi_box"))
        self.horizontalLayout.addWidget(self.hdpi_box)
        self.xhdpi_box = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.xhdpi_box.setObjectName(_fromUtf8("xhdpi_box"))
        self.horizontalLayout.addWidget(self.xhdpi_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.out_width = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.out_width.setMaximum(9999)
        self.out_width.setProperty(_fromUtf8("value"), 48)
        self.out_width.setObjectName(_fromUtf8("out_width"))
        self.horizontalLayout_2.addWidget(self.out_width)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.out_height = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.out_height.setMaximum(9999)
        self.out_height.setProperty(_fromUtf8("value"), 48)
        self.out_height.setObjectName(_fromUtf8("out_height"))
        self.horizontalLayout_2.addWidget(self.out_height)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.process_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.process_button.setObjectName(_fromUtf8("process_button"))
        self.verticalLayout.addWidget(self.process_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.source_button.setText(QtGui.QApplication.translate("MainWindow", "Choose SVG files", None, QtGui.QApplication.UnicodeUTF8))
        self.source_label.setText(QtGui.QApplication.translate("MainWindow", "Input files : ", None, QtGui.QApplication.UnicodeUTF8))
        self.target_button.setText(QtGui.QApplication.translate("MainWindow", "Choose output folder", None, QtGui.QApplication.UnicodeUTF8))
        self.target_label.setText(QtGui.QApplication.translate("MainWindow", "Output folder : ", None, QtGui.QApplication.UnicodeUTF8))
        self.ldpi_box.setText(QtGui.QApplication.translate("MainWindow", "ldpi", None, QtGui.QApplication.UnicodeUTF8))
        self.mdpi_box.setText(QtGui.QApplication.translate("MainWindow", "mdpi", None, QtGui.QApplication.UnicodeUTF8))
        self.hdpi_box.setText(QtGui.QApplication.translate("MainWindow", "hdpi", None, QtGui.QApplication.UnicodeUTF8))
        self.xhdpi_box.setText(QtGui.QApplication.translate("MainWindow", "xhdpi", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "mdpi width :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "mdpi height :", None, QtGui.QApplication.UnicodeUTF8))
        self.process_button.setText(QtGui.QApplication.translate("MainWindow", "GO !!!", None, QtGui.QApplication.UnicodeUTF8))

