# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
# Ana del Campo Sanchez, ana.delcampo@usal.es

import os
from math import floor
import re
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog
from gui.VPyFormGenerator.VPyGUIGenerator import VPyGUIGenerator
from datetime import datetime, date, time
from gui.Project import Project
from gui import gui_defines

from gui.kekse.kekse import ProtoKeks
from PyQt5 import QtCore, QtWidgets

class MshBigPsxDialog(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Load the dialog's GUI
        loadUi("MshBigPsxDialog.ui", self)
        self.initialize()

    def initialize(self):
        self.class_path = os.path.dirname(os.path.realpath(__file__))
        # class_path = os.path.join(pluginsPath, class_path)
        self.template_path = self.class_path + gui_defines.TEMPLATE_PATH
        self.project = Project()
        # Project
        self.projectPushButton.clicked.connect(self.edit_project)
        return

    def edit_project(self):
        project_dlg = VPyGUIGenerator.create_gui(self.project)
        # project_dlg.show()
        project_dlg.exec()
