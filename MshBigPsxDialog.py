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
from gui.Workflow import Workflow
from gui.Photo import Photo
from gui.Roi import Roi
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
        # Project
        self.project = Project()
        self.projectPushButton.setText(self.project.get_text())
        self.projectPushButton.clicked.connect(self.edit_project)
        self.project_dlg = None
        # Workflow
        self.workflow = Workflow()
        self.workflowPushButton.setText(self.workflow.get_text())
        self.workflowPushButton.clicked.connect(self.edit_workflow)
        self.workflow_dlg = None
        # Photo
        self.photo = Photo()
        self.photoPushButton.setText(self.photo.get_text())
        self.photoPushButton.clicked.connect(self.edit_photo)
        self.photo_dlg = None
        # ROI
        self.roi = Roi()
        self.roiPushButton.setText(self.roi.get_text())
        self.roiPushButton.clicked.connect(self.edit_roi)
        self.roi_dlg = None
        return

    def edit_photo(self):
        if not self.photo_dlg:
            self.photo_dlg = VPyGUIGenerator.create_gui(self.photo)
            self.photo_dlg.setWindowTitle(self.photo.get_text())
            text_by_propierty = self.photo.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.photo_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
        # photo_dlg.show()
        self.photo_dlg.exec()

    def edit_project(self):
        if not self.project_dlg:
            self.project_dlg = VPyGUIGenerator.create_gui(self.project)
            self.project_dlg.setWindowTitle(self.project.get_text())
            text_by_propierty = self.project.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.project_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
        # project_dlg.show()
        self.project_dlg.exec()

    def edit_roi(self):
        if not self.roi_dlg:
            self.roi_dlg = VPyGUIGenerator.create_gui(self.roi)
            self.roi_dlg.setWindowTitle(self.roi.get_text())
            text_by_propierty = self.roi.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.roi_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
        # roi_dlg.show()
        self.roi_dlg.exec()

    def edit_workflow(self):
        if not self.workflow_dlg:
            self.workflow_dlg = VPyGUIGenerator.create_gui(self.workflow)
            self.workflow_dlg.setWindowTitle(self.workflow.get_text())
            text_by_propierty = self.workflow.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.workflow_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
        # project_dlg.show()
        self.workflow_dlg.exec()
