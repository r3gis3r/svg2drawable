#!/usr/bin/python
# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from windowUi import Ui_MainWindow

import util

# Create a class for our main window
class Main(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.source_files = None
		self.target_folder = None

		self.connect(self.ui.source_button, QtCore.SIGNAL('clicked()'), self.open_source)
		self.connect(self.ui.target_button, QtCore.SIGNAL('clicked()'), self.open_target)
		self.connect(self.ui.process_button, QtCore.SIGNAL('clicked()'), self.process)
		
		self.update_go_button()

	def update_go_button(self):
		self.ui.process_button.setEnabled(self.source_files is not None and self.target_folder is not None)
	
	def update_preview(self):
		#Clear old
		box_l = self.ui.input_files_box
		while box_l.count():
			it = box_l.takeAt(0)
			w = it.widget()
			if w is not None:
				w.deleteLater()
		for f in self.source_files:
			label = QtGui.QLabel(self.ui.verticalLayoutWidget)
			pix = QtGui.QPixmap(f)
			pix = pix.scaled(100, 100)
			label.setPixmap(pix)
			self.ui.input_files_box.addWidget(label)

	def update_target_folder_label(self):
		self.ui.target_label.setText(self.target_folder)

	def open_source(self):
		self.source_files = QtGui.QFileDialog.getOpenFileNames(self, self.tr('Select source SVG file'), "./", self.tr("svg file (*.svg)"))
		for f in self.source_files:
			print "selected : ", f
		self.update_go_button()
		self.update_preview()

	def open_target(self):
		self.target_folder =  QtGui.QFileDialog.getExistingDirectory(self, self.tr('Select output android res directory'))
		self.update_target_folder_label()
		self.update_go_button()

	def process(self):
		w = self.ui.out_width.value()
		h = self.ui.out_height.value()
		u_ldpi = self.ui.ldpi_box.isChecked()
		u_mdpi = self.ui.mdpi_box.isChecked()
		u_hdpi = self.ui.hdpi_box.isChecked()
		u_xhdpi = self.ui.xhdpi_box.isChecked()
		print u_ldpi, u_xhdpi
		for f in self.source_files:
			util.svg_to_drawables(unicode(f), unicode(self.target_folder), mdpi_width=w, mdpi_height=h, export_ldpi=u_ldpi, export_mdpi=u_mdpi, export_hdpi=u_hdpi, export_xhdpi=u_xhdpi)

def main():
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()


