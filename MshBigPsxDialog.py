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
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog, QPushButton, QComboBox
from PyQt5.QtCore import QDir, QFileInfo
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
                 settings,
                 parametersManager,
                 parent=None):
        super().__init__(parent)
        # Load the dialog's GUI
        # loadUi("./gui/MshBigPsxDialog.ui", self)
        loadUi("MshBigPsxDialog.ui", self)
        self.settings = settings
        self.parametersManager = parametersManager
        self.initialize()

    def addProject(self):
        title = "Select Project File"
        fileName, aux = QFileDialog.getOpenFileName(self, title, self.path, "Project File (*.json)")
        if fileName:
            if not fileName in self.projects:
                self.projects.append(fileName)
                self.projectsComboBox.addItem(fileName)
                strProjects = ""
                cont = 0
                for project in self.projects:
                    if cont > 0:
                        strProjects = strProjects + gui_defines.CONST_PROJECTS_STRING_SEPARATOR
                    strProjects += project
                    cont = cont + 1
                self.settings.setValue("projects", strProjects)
                self.settings.sync()
            pos = self.projectsComboBox.findText(fileName)
            if pos >= 0:
                self.projectsComboBox.setCurrentIndex(pos)
            self.path = QFileInfo(fileName).absolutePath()
            self.settings.setValue("last_path", self.path)
            self.settings.sync()
        return

    def initialize(self):
        self.path = self.settings.value("last_path")
        current_dir = QDir.current()
        if not self.path:
            self.path = QDir.currentPath()
            self.settings.setValue("last_path", self.path)
            self.settings.sync()
        self.geoids_path = self.settings.value("geoids_path")
        if self.geoids_path:
            if not current_dir.exists(self.geoids_path):
                self.geoids_path = None
        if not current_dir.exists(self.geoids_path):
            program_files_path = os.environ["ProgramFiles"]
            geoids_path = program_files_path + "/" + gui_defines.DEFAULT_GEOIDS_PATH
            geoids_path = os.path.normpath(geoids_path)
            if current_dir.exists(geoids_path):
                self.geoids_path = geoids_path
        self.settings.setValue("geoids_path", self.geoids_path)
        self.settings.sync()
        self.conda_env_path = self.settings.value("conda_env_path")
        if self.conda_env_path:
            if not current_dir.exists(self.conda_env_path):
                self.conda_env_path = None
        self.settings.setValue("conda_env_path", self.conda_env_path)
        self.settings.sync()
        strProjects = self.settings.value("project")
        self.addProjectPushButton.clicked.connect(self.addProject)
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.projectLineEdit.clear()
        self.processPushButton.setEnabled(False)
        self.projectsComboBox.currentIndexChanged.connect(self.selectProject)
        self.projectFile = None

        self.class_path = os.path.dirname(os.path.realpath(__file__))
        # class_path = os.path.join(pluginsPath, class_path)
        self.template_path = self.class_path + gui_defines.TEMPLATE_PATH
        self.path = self.settings.value("last_path")
        current_dir = QDir.current()
        if not self.path:
            self.path = QDir.currentPath()
            self.settings.setValue("last_path", self.path)
            self.settings.sync()
        self.geoids_path = self.settings.value("geoids_path")
        if self.geoids_path:
            if not current_dir.exists(self.geoids_path):
                self.geoids_path = None
        if not current_dir.exists(self.geoids_path):
            program_files_path = os.environ["ProgramFiles"]
            geoids_path = program_files_path + "/" + gui_defines.DEFAULT_GEOIDS_PATH
            geoids_path = os.path.normpath(geoids_path)
            if current_dir.exists(geoids_path):
                self.geoids_path = geoids_path
        self.settings.setValue("geoids_path", self.geoids_path)
        self.settings.sync()
        self.conda_env_path = self.settings.value("conda_env_path")
        if self.conda_env_path:
            if not current_dir.exists(self.conda_env_path):
                self.conda_env_path = None
        self.settings.setValue("conda_env_path", self.conda_env_path)
        self.settings.sync()

        self.projects = []
        strProjects = self.settings.value("projects")
        if strProjects:
            self.projects = strProjects.split(gui_defines.CONST_PROJECTS_STRING_SEPARATOR)
        self.projectsComboBox.clear()
        self.projectsComboBox.addItem(gui_defines.CONST_NO_COMBO_SELECT)
        for project in self.projects:
            self.projectsComboBox.addItem(project)
        self.addProjectPushButton.clicked.connect(self.addProject)
        self.projectsComboBox.currentIndexChanged.connect(self.selectProject)
        self.openProjectPushButton.clicked.connect(self.openProject)
        self.closeProjectPushButton.clicked.connect(self.closeProject)
        self.saveProjectPushButton.clicked.connect(self.saveProject)
        self.processPushButton.clicked.connect(self.process)
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.projectLineEdit.clear()
        self.processPushButton.setEnabled(False)
        self.object_by_name = {}
        self.object_dlg_by_name = {}

    def closeProject(self):
        if not self.projectFile:
            return
        self.addProjectPushButton.setEnabled(True)
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.projectFile = None
        self.projectsComboBox.setEnabled(True)
        self.projectsComboBox.setCurrentIndex(0)
        for class_name in gui_defines.GUI_CLASSES:
            self.object_by_name[class_name] = None
            self.object_dlg_by_name[class_name] = None
        return

    # def closeProject(self):
    #     if not self.projectPath:
    #         return
    #     self.openProjectPushButton.setEnabled(False)
    #     self.closeProjectPushButton.setEnabled(False)
    #     self.removeProjectPushButton.setEnabled(False)
    #     self.projectFile = None
    #     # self.projectsComboBox.setEnabled(True)
    #     self.projectsComboBox.setCurrentIndex(0)
    #     return

    # def edit_class(self):

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

    def loadProjectFromJSonFile(self,
                                project_file):
        str_error = ""
        if not os.path.isfile(project_file):
            str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
            str_error += ("\nNot exists file: {}".format(project_file))
            return str_error
        f = open(project_file)
        try:
            json_content = json.load(f)
        except:
            str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
            str_error += ("\nInvalid JSON file: {}".format(project_file))
            f.close()
            return str_error
        f.close()
        # if not gui_defines.GUI_LANGUAGE_TAG in json_content:
        #     str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
        #     str_error += ("\n{} not in JSON file: {}".format(gui_defines.GUI_LANGUAGE_TAG, project_file))
        #     return str_error
        # language = json_content[gui_defines.GUI_LANGUAGE_TAG]
        gui_classes = gui_defines.GUI_CLASSES
        class_in_json_file_by_gui_class = {}
        for class_name in gui_classes:
            if class_name in json_content:
                class_in_json_file_by_gui_class[class_name] = class_name
            else:
                for class_in_json in json_content:
                    if class_name.lower() == class_in_json.lower():
                        class_in_json_file_by_gui_class[class_name] = class_in_json
        for class_name in gui_classes:
            if not class_name in class_in_json_file_by_gui_class:
                str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
                str_error += ("\nClass: {} not in JSON file: {}".format(class_name, project_file))
                return str_error
            class_name_json = class_in_json_file_by_gui_class[class_name]
            # if ((class_name != 'Project' and class_name != 'Workflow' and class_name != 'Photo'
            #         and class_name != 'Roi' and class_name != 'CameraCalibration')
            #         and class_name != "OptimizeAlignment" and class_name != "SplitTile"
            #         and class_name != "PointCloud") and class_name != "InstallRequirement":
            #     continue
            # if class_name != 'Project' and class_name != 'Workflow':
            #     continue
            json_class_content = json_content[class_name_json]
            attributes_tag = None
            attributes_tag = self.object_by_name[class_name].get_values_as_dictionary()
            values = {}
            for attributes_in_definitions in attributes_tag:
                if not attributes_in_definitions in json_class_content:
                    str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
                    str_error += ("\nAttribute: {} not in class: {} not in JSON file: {}"
                                  .format(attributes_in_definitions, class_name, project_file))
                    return str_error
                value = json_class_content[attributes_in_definitions]
                if type(attributes_tag[attributes_in_definitions]) == bool:
                    if type(value) == str:
                        if value.lower() == 'true':
                            value = True
                        elif value.lower() == 'false':
                            value = False
                        else:
                            str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
                            str_error += ("\nAttribute: {} in class: {} in JSON file: {} invalid boolean: {}"
                                          .format(attributes_in_definitions, class_name, project_file, value))
                            return str_error
                values[attributes_in_definitions] = value
            # if class_name == 'Photo' or class_name == 'Roi' or class_name == 'OptimizeAlignment'\
            #         or class_name == 'SplitTile' or class_name == 'PointCloud':
            #     yo = 1
            #     # continue
            self.object_by_name[class_name].set_values_from_dictionary(values)
        return str_error

    def openProject(self):
        self.addProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.processPushButton.setEnabled(False)
        self.projectFile = None
        projectFile = self.projectsComboBox.currentText()
        if projectFile == gui_defines.CONST_NO_COMBO_SELECT:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle(self.windowTitle)
            msgBox.setText("Select project before")
            msgBox.exec_()
            return
        for class_name in gui_defines.GUI_CLASSES:
            self.object_by_name[class_name] = None
            self.object_dlg_by_name[class_name] = None
            if class_name == gui_defines.OBJECT_CLASS_CAMERA_CALIBRATION:
                self.object_by_name[class_name] = CameraCalibration()
                # self.cameraCalibrationPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_INSTALL_REQUIREMENT:
                self.object_by_name[class_name] = InstallRequirement()
                # self.installRequirementPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_PHOTO:
                self.object_by_name[class_name] = Photo()
                # self.photoPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_POINT_CLOUD:
                self.object_by_name[class_name] = PointCloud()
                # self.pointCloudPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_PROJECT:
                self.object_by_name[class_name] = Project()
                # self.projectPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_WORKFLOW:
                self.object_by_name[class_name] = Workflow()
                # self.workflowPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_ROI:
                self.object_by_name[class_name] = Roi()
                # self.roiPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_OPTIMIZE_ALIGNMENT:
                self.object_by_name[class_name] = OptimizeAlignment()
                # self.optimizeAlignmentPushButton.setText(self.object_by_name[class_name].get_text())
            elif class_name == gui_defines.OBJECT_CLASS_SPLIT_TILE:
                self.object_by_name[class_name] = SplitTile()
                # self.splitTilePushButton.setText(self.object_by_name[class_name].get_text())
            row_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][0]
            column_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][1]
            object_title = self.object_by_name[class_name].get_text()
            self.objectsGridLayout.addWidget(QPushButton(object_title), row_in_grid_layout, column_in_grid_layout)

        # self.cameraCalibrationPushButton.clicked.connect(self.edit_cameraCalibration)
        # self.installRequirementPushButton.clicked.connect(self.edit_installRequirement)
        # self.photoPushButton.clicked.connect(self.edit_photo)
        # self.pointCloudPushButton.clicked.connect(self.edit_pointCloud)
        # self.projectPushButton.clicked.connect(self.edit_project)
        # self.workflowPushButton.clicked.connect(self.edit_workflow)
        # self.roiPushButton.clicked.connect(self.edit_roi)
        # self.optimizeAlignmentPushButton.clicked.connect(self.edit_optimizeAlignment)
        # self.splitTilePushButton.clicked.connect(self.edit_splitTile)

        # # CameraCalibration
        # self.cameraCalibration = CameraCalibration()
        # self.cameraCalibrationPushButton.setText(self.cameraCalibration.get_text())
        # self.cameraCalibrationPushButton.clicked.connect(self.edit_cameraCalibration)
        # # InstallRequirement
        # self.installRequirement = InstallRequirement()
        # self.installRequirementPushButton.setText(self.installRequirement.get_text())
        # self.installRequirementPushButton.clicked.connect(self.edit_installRequirement)
        # # Photo
        # self.photo = Photo()
        # self.photoPushButton.setText(self.photo.get_text())
        # self.photoPushButton.clicked.connect(self.edit_photo)
        # # PointCloud
        # self.pointCloud = PointCloud()
        # self.pointCloudPushButton.setText(self.pointCloud.get_text())
        # self.pointCloudPushButton.clicked.connect(self.edit_pointCloud)
        # # Project
        # self.project = Project()
        # self.projectPushButton.setText(self.project.get_text())
        # self.projectPushButton.clicked.connect(self.edit_project)
        # # # Workflow
        # self.workflow = Workflow()
        # self.workflowPushButton.setText(self.workflow.get_text())
        # self.workflowPushButton.clicked.connect(self.edit_workflow)
        # # Roi
        # self.roi = Roi()
        # self.roiPushButton.setText(self.roi.get_text())
        # self.roiPushButton.clicked.connect(self.edit_roi)
        # # OptimizeAlignment
        # self.optimizeAlignment = OptimizeAlignment()
        # self.optimizeAlignmentPushButton.setText(self.optimizeAlignment.get_text())
        # self.optimizeAlignmentPushButton.clicked.connect(self.edit_optimizeAlignment)
        # # SplitTile
        # self.splitTile = SplitTile()
        # self.splitTilePushButton.setText(self.splitTile.get_text())
        # self.splitTilePushButton.clicked.connect(self.edit_splitTile)

        for class_name in gui_defines.GUI_CLASSES:
            row_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][0]
            column_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][1]
            object_title = self.object_by_name[class_name].get_text()
            obj_push_button = QPushButton(object_title)
            self.objectsGridLayout.addWidget(obj_push_button, row_in_grid_layout, column_in_grid_layout)
            obj_dlg = VPyGUIGenerator.create_gui(self.object_by_name[class_name])
            obj_dlg.setWindowTitle(object_title)
            text_by_propierty = self.object_by_name[class_name].get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                obj_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.object_dlg_by_name[class_name] = obj_dlg
            self.object_by_name[class_name].set_widget(self.object_dlg_by_name[class_name])
            obj_push_button.clicked.connect(obj_dlg.exec)

        str_error = self.loadProjectFromJSonFile(projectFile)
        if str_error:
            Tools.error_msg(str_error)
            return

        self.projectFile = projectFile
        self.closeProjectPushButton.setEnabled(True)
        self.openProjectPushButton.setEnabled(False)
        self.projectsComboBox.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(True)
        self.saveProjectPushButton.setEnabled(True)


    def process(self):
        output_file = self.projectLineEdit.text()
        if not output_file:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle(self.windowTitle())
            msgBox.setText("Select output JSON file before")
            msgBox.exec_()
            return
        example_output_json_file_path = 'params_example_output.json'
        current_path = os.path.dirname(os.path.realpath(__file__))
        example_output_json_file_path = current_path + "\\" + example_output_json_file_path
        class_file_path = os.path.normpath(example_output_json_file_path)
        json_content = {}
        values = {}
        for class_name in self.object_by_name:
            object_values = self.object_by_name[class_name].get_values_as_dictionary()
            for object_value in object_values:
                if type(object_values[object_value]) == bool:
                    if object_values[object_value]:
                        object_values[object_value] = "True"
                    else:
                        object_values[object_value] = "False"
                propierty_widget = self.object_by_name[class_name].get_widget_propierty(object_value)
                if not propierty_widget:
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setWindowTitle(self.windowTitle())
                    msgBox.setText("Not exists widget for propierty: {} in class: {}".
                                   format(object_value, class_name))
                    msgBox.exec_()
                    return
                if isinstance(propierty_widget, QComboBox):
                    json_content = self.object_by_name[class_name].get_propierty_json_content(object_value)
                    if not json_content:
                        msgBox = QMessageBox(self)
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setWindowTitle(self.windowTitle())
                        msgBox.setText("Not exists json content for propierty: {} in class: {}".
                                       format(object_value, class_name))
                        msgBox.exec_()
                        return
                    json_values = json_content[gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG]
                    new_value = None
                    for json_value in json_values:
                        values_language = json_values[json_value]
                        for value_language in values_language:
                            if values_language[value_language] == object_values[object_value]:
                                new_value = json_value
                                break
                    if not new_value:
                        msgBox = QMessageBox(self)
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setWindowTitle(self.windowTitle())
                        msgBox.setText("Not exists valid coincidence value for propierty: {} in class: {}".
                                       format(object_value, class_name))
                        msgBox.exec_()
                        return
                    object_values[object_value] = new_value
            values[class_name] = object_values
        json_content = values
        json_object = json.dumps(json_content, indent=4)
        with open(output_file, "w") as outfile:
            outfile.write(json_object)
        return

    def saveProject(self):
        title = "Select Project File to Save"
        previous_file = self.projectLineEdit.text()
        fileName, aux = QFileDialog.getSaveFileName(self, title, self.path, "Project File (*.json)")
        if fileName:
            self.projectLineEdit.setText(fileName)
            self.processPushButton.setEnabled(True)
        else:
            if not previous_file:
                self.processPushButton.setEnabled(False)
        return

    def selectProject(self):
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        projectFilePath = self.projectsComboBox.currentText()
        if projectFilePath == gui_defines.CONST_NO_COMBO_SELECT:
            self.projectFileEditionGroupBox.setEnabled(False)
            self.saveProjectPushButton.setEnabled(False)
            self.projectLineEdit.clear()
            self.processPushButton.setEnabled(False)
            if self.projectFile:
                self.closeProject()
        else:
            self.projectFileEditionGroupBox.setEnabled(False)
            self.openProjectPushButton.setEnabled(True)
            self.closeProjectPushButton.setEnabled(False)
            self.removeProjectPushButton.setEnabled(True)
        # if self.connectionFileName:
        #     self.openProject()
        return
