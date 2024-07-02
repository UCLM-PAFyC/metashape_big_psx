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
from gui.CameraCalibration import CameraCalibration
from gui.InstallRequirement import InstallRequirement
from gui.Photo import Photo
from gui.PointCloud import PointCloud
from gui.Project import Project
from gui.Roi import Roi
from gui.Workflow import Workflow
from gui.OptimizeAlignment import OptimizeAlignment
from gui.SplitTile import SplitTile
from gui import gui_defines
from ParameterManager import ParametersManager

from gui.kekse.kekse import ProtoKeks
from PyQt5 import QtCore, QtWidgets

import json
import Tools

class MshBigPsxDialog(QDialog):
    """Employee dialog."""

    def __init__(self,
                 parametersManager,
                 parent=None):
        super().__init__(parent)
        # Load the dialog's GUI
        # loadUi("./gui/MshBigPsxDialog.ui", self)
        loadUi("MshBigPsxDialog.ui", self)
        self.parametersManager = parametersManager
        self.initialize()

    def initialize(self):
        self.class_path = os.path.dirname(os.path.realpath(__file__))
        # class_path = os.path.join(pluginsPath, class_path)
        self.template_path = self.class_path + gui_defines.TEMPLATE_PATH
        self.processPushButton.clicked.connect(self.process)
        # CameraCalibration
        self.cameraCalibration = CameraCalibration()
        self.cameraCalibrationPushButton.setText(self.cameraCalibration.get_text())
        self.cameraCalibrationPushButton.clicked.connect(self.edit_cameraCalibration)
        self.cameraCalibration_dlg = None
        # InstallRequirement
        self.installRequirement = InstallRequirement()
        self.installRequirementPushButton.setText(self.installRequirement.get_text())
        self.installRequirementPushButton.clicked.connect(self.edit_installRequirement)
        self.installRequirement_dlg = None
        # Photo
        self.photo = Photo()
        self.photoPushButton.setText(self.photo.get_text())
        self.photoPushButton.clicked.connect(self.edit_photo)
        self.photo_dlg = None
        # PointCloud
        self.pointCloud = PointCloud()
        self.pointCloudPushButton.setText(self.pointCloud.get_text())
        self.pointCloudPushButton.clicked.connect(self.edit_pointCloud)
        self.pointCloud_dlg = None
        # Project
        self.project = Project()
        self.projectPushButton.setText(self.project.get_text())
        self.projectPushButton.clicked.connect(self.edit_project)
        self.project_dlg = None
        # # Workflow
        self.workflow = Workflow()
        self.workflowPushButton.setText(self.workflow.get_text())
        self.workflowPushButton.clicked.connect(self.edit_workflow)
        self.workflow_dlg = None
        # Roi
        self.roi = Roi()
        self.roiPushButton.setText(self.roi.get_text())
        self.roiPushButton.clicked.connect(self.edit_roi)
        self.roi_dlg = None
        # OptimizeAlignment
        self.optimizeAlignment = OptimizeAlignment()
        self.optimizeAlignmentPushButton.setText(self.optimizeAlignment.get_text())
        self.optimizeAlignmentPushButton.clicked.connect(self.edit_optimizeAlignment)
        self.optimizeAlignment_dlg = None
        # SplitTile
        self.splitTile = SplitTile()
        self.splitTilePushButton.setText(self.splitTile.get_text())
        self.splitTilePushButton.clicked.connect(self.edit_splitTile)
        self.splitTile_dlg = None
        return

    def edit_cameraCalibration(self):
        if not self.cameraCalibration_dlg:
            self.cameraCalibration_dlg = VPyGUIGenerator.create_gui(self.cameraCalibration)
            self.cameraCalibration_dlg.setWindowTitle(self.cameraCalibration.get_text())
            text_by_propierty = self.cameraCalibration.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.cameraCalibration_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.cameraCalibration.set_widget(self.cameraCalibration_dlg)
        # roi_dlg.show()
        self.cameraCalibration_dlg.exec()

    def edit_installRequirement(self):
        if not self.installRequirement_dlg:
            self.installRequirement_dlg = VPyGUIGenerator.create_gui(self.installRequirement)
            self.installRequirement_dlg.setWindowTitle(self.installRequirement.get_text())
            text_by_propierty = self.installRequirement.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.installRequirement_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.installRequirement.set_widget(self.installRequirement_dlg)
        # roi_dlg.show()
        self.installRequirement_dlg.exec()

    def edit_photo(self):
        if not self.photo_dlg:
            self.photo_dlg = VPyGUIGenerator.create_gui(self.photo)
            self.photo_dlg.setWindowTitle(self.photo.get_text())
            text_by_propierty = self.photo.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.photo_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.photo.set_widget(self.photo_dlg)
        # photo_dlg.show()
        self.photo_dlg.exec()

    def edit_optimizeAlignment(self):
        if not self.optimizeAlignment_dlg:
            self.optimizeAlignment_dlg = VPyGUIGenerator.create_gui(self.optimizeAlignment)
            self.optimizeAlignment_dlg.setWindowTitle(self.optimizeAlignment.get_text())
            text_by_propierty = self.optimizeAlignment.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.optimizeAlignment_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.optimizeAlignment.set_widget(self.optimizeAlignment_dlg)
        # roi_dlg.show()
        self.optimizeAlignment_dlg.exec()

    def edit_pointCloud(self):
        if not self.pointCloud_dlg:
            self.pointCloud_dlg = VPyGUIGenerator.create_gui(self.pointCloud)
            self.pointCloud_dlg.setWindowTitle(self.pointCloud.get_text())
            text_by_propierty = self.pointCloud.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.pointCloud_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.pointCloud.set_widget(self.pointCloud_dlg)
        # project_dlg.show()
        self.pointCloud_dlg.exec()

    def edit_project(self):
        if not self.project_dlg:
            self.project_dlg = VPyGUIGenerator.create_gui(self.project)
            self.project_dlg.setWindowTitle(self.project.get_text())
            text_by_propierty = self.project.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.project_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.project.set_widget(self.project_dlg)
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
            self.roi.set_widget(self.roi_dlg)
        # roi_dlg.show()
        self.roi_dlg.exec()

    def edit_splitTile(self):
        if not self.splitTile_dlg:
            self.splitTile_dlg = VPyGUIGenerator.create_gui(self.splitTile)
            self.splitTile_dlg.setWindowTitle(self.splitTile.get_text())
            text_by_propierty = self.splitTile.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.splitTile_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.splitTile.set_widget(self.splitTile_dlg)
        # roi_dlg.show()
        self.splitTile_dlg.exec()

    def edit_workflow(self):
        if not self.workflow_dlg:
            self.workflow_dlg = VPyGUIGenerator.create_gui(self.workflow)
            self.workflow_dlg.setWindowTitle(self.workflow.get_text())
            text_by_propierty = self.workflow.get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                self.workflow_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.workflow.set_widget(self.workflow_dlg)
        # project_dlg.show()
        self.workflow_dlg.exec()

    def process(self):
        example_output_json_file_path = 'params_example_output.json'
        current_path = os.path.dirname(os.path.realpath(__file__))
        example_output_json_file_path = current_path + "\\" + example_output_json_file_path
        class_file_path = os.path.normpath(example_output_json_file_path)
        json_content = {}
        # project
        # if not self.project_dlg:
        #     str_error = MshBigPsxDialog.__name__ + "." + self.process.__name__
        #     str_error += ("\nSelect Project parameters before")
        #     Tools.error_msg(str_error)
        #     return
        project_values = self.project.get_values_as_dictionary()
        workflow_value = self.workflow.get_values_as_dictionary()
        photo_values = self.photo.get_values_as_dictionary()
        roi_values = self.roi.get_values_as_dictionary()
        cameraCalibration_values = self.cameraCalibration.get_values_as_dictionary()
        optimizeAlignment_values = self.optimizeAlignment.get_values_as_dictionary()
        splitTile_values = self.splitTile.get_values_as_dictionary()
        pointCloud_values = self.pointCloud.get_values_as_dictionary()
        installRequirement_values = self.installRequirement.get_values_as_dictionary()

        json_object = json.dumps(json_content, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        return