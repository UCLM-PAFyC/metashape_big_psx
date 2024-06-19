import json
import os
from pathlib import Path
from gui import gui_defines


class ParametersManager:
    def __init__(self):
        self.json_file = None
        self.json_content = None
        self.parameters = gui_defines.parameters

    def build_parameter_file(self,
                             class_name,
                             language,
                             json_class_content):
        str_error = ""
        current_path = os.path.dirname(os.path.realpath(__file__))
        class_file_path = current_path + gui_defines.GUI_CLASSES_PATH
        class_file_path = os.path.normpath(class_file_path)
        if not os.path.exists(class_file_path):
            os.makedirs(class_file_path)
            if not os.path.exists(class_file_path):
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nError making Classes path: {}".format(class_file_path))
                return str_error
        class_file = class_file_path + "/" + class_name + ".py"
        class_file = os.path.normpath(class_file)
        f = open(class_file, "w")
        f.write('from PyQt5.QtWidgets import QDoubleSpinBox, QComboBox, QLineEdit, QCheckBox\n')
        f.write('from . import gui_defines\n')
        f.write('\nclass {}:\n'.format(class_name))
        f.write('\tdef __init__(self):\n')
        f.write('\t\tself.__text_by_propierty = {}\n')
        f.write('\t\tself.__widget_by_propierty = {}\n')
        propierty_field_definition = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DEFINITION_TAG
        propierty_field_type = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_TYPE_TAG
        propierty_field_default = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DEFAULT_TAG
        propierty_field_decimalS = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DECIMALS_TAG
        propierty_field_maximum = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_MAXIMUM_TAG
        propierty_field_minimum = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_MINIMUM_TAG
        propierty_field_single_step = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_SINGLE_STEP_TAG
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                if not language in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists language: {}"
                                  .format(class_name, gui_defines.GUI_CLASSES_TEXT_TAG, language))
                    return str_error
                text = '\t\tself.__' + propierty_name.lower() + " = \'" + json_propierty_content[language] + "\'"
                text += "\n"
                f.write(text)
                continue
            if not gui_defines.GUI_CLASSES_TEXT_TAG in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, gui_defines.GUI_CLASSES_TEXT_TAG))
                return str_error
            propierty_name = propierty_name.lower()
            if not language in json_propierty_content[gui_defines.GUI_CLASSES_TEXT_TAG]:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, in field: {}, not exists language: {}"
                              .format(class_name, propierty_name, gui_defines.GUI_CLASSES_TEXT_TAG, language))
                return str_error
            f.write('\t\tself.__text_by_propierty[\'{}\'] = \'{}\'\n'.
                    format(propierty_name, json_propierty_content[gui_defines.GUI_CLASSES_TEXT_TAG][language]))
            f.write('\t\tself.__widget_by_propierty[\'{}\'] = None\n'.format(propierty_name))
            propierty_type = json_propierty_content[propierty_field_type]
            if not propierty_field_type in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_type))
                return str_error
            propierty_type = json_propierty_content[propierty_field_type]
            if not propierty_field_default in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_default))
                return str_error
            propierty_default_value = str(json_propierty_content[propierty_field_default])
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                if propierty_default_value != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TRUE \
                        and propierty_default_value != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_FALSE:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, field: {} must be {} or {}"
                                  .format(class_name, propierty_name, propierty_field_default,
                                          gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TRUE,
                                          gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_FALSE))
                    return str_error
            text = '\t\tself.__' + propierty_name.lower() + " = "
            text_value = '\t\tself.__' + propierty_name.lower() + gui_defines.GUI_CLASSES_PROPIERTY_VALUE_SUFFIX + " = "
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG:
                values_content = json_propierty_content[propierty_type]
                text += "["
                pos_default_in_values_content = -1
                cont = 0
                for value_tag in values_content:
                    value_content = values_content[value_tag]
                    if not language in value_content:
                        str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                        str_error += ("\nFor class: {}, in attribute: {}, in field: {}, "
                                      "in value: {}, not exists language: {}"
                                      .format(class_name, propierty_name,
                                              propierty_field_definition, value_tag, language))
                        return str_error
                    value = value_content[language]
                    if value == propierty_default_value:
                        text += ('\'{}\''.format(value))
                        text_value += ('\'{}\''.format(value))
                        pos_default_in_values_content = cont
                        break
                    cont = cont + 1
                if pos_default_in_values_content == -1:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, field: {}, "
                                  "default value: {} is not in valid values"
                                  .format(class_name, propierty_name, propierty_field_type,
                                          propierty_default_value))
                cont = 0
                for value_tag in values_content:
                    if cont == pos_default_in_values_content:
                        cont = cont + 1
                        continue
                    value_content = values_content[value_tag]
                    if not language in value_content:
                        str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                        str_error += ("\nFor class: {}, in attribute: {}, in field: {}, "
                                      "in value: {}, not exists language: {}"
                                      .format(class_name, propierty_name,
                                              propierty_field_definition, value_tag, language))
                        return str_error
                    value = value_content[language]
                    text += (' ,\' {}\''.format(value))
                    cont = cont + 1
                text += "]"
                text += "\n"
                f.write(text)
                text_value += "\n"
                f.write(text_value)
                continue
            if propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                text += '\"'
                text_value += '\"'
            text += propierty_default_value
            text_value += propierty_default_value
            if propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                text += '\"'
                text_value += '\"'
            text += "\n"
            text_value += "\n"
            f.write(text)
            f.write(text_value)
        f.write('\t\tself.__widget = None\n')
        f.write('\n\tdef get_values_as_dictionary(self):\n')
        f.write('\t\tvalues = {}\n')
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                continue
            f.write('\t\tvalues[\'{}\'] = self.__{}{}\n'
                    .format(propierty_name, propierty_name.lower(),
                            gui_defines.GUI_CLASSES_PROPIERTY_VALUE_SUFFIX))
        f.write('\t\treturn values\n')
        f.write('\n\tdef get_text(self):\n')
        f.write('\t\treturn self.__text\n')
        f.write('\n\tdef get_text_by_propierty(self):\n')
        f.write('\t\treturn self.__text_by_propierty\n')
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                continue
            propierty_name = propierty_name.lower()
            propiertyIsString = False
            propiertyIsReal = False
            propiertyIsFolder = False
            propiertyIsFileOpen = False
            propiertyIsFileSave = False
            propiertyIsInteger = False
            propiertyIsValuesList = False
            propiertyIsBoolean = False
            if not propierty_field_definition in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_definition))
                return str_error
            if not language in json_propierty_content[propierty_field_definition]:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, in field: {}, not exists language: {}"
                              .format(class_name, propierty_name,
                                      propierty_field_definition, language))
                return str_error
            propierty_definition = json_propierty_content[propierty_field_definition][language]
            if not propierty_field_type in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_type))
                return str_error
            propierty_type = json_propierty_content[propierty_field_type]
            propierty_text = ('widget:QLineEdit, toolTip:{}'.format(propierty_definition))
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                propiertyIsBoolean = True
                propierty_text = ('widget:QCheckBox, toolTip:{}'
                                  .format(propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_STRING_TAG:
                propiertyIsString = True
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG:
                propiertyIsReal = True
                if not propierty_field_decimalS in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_decimalS))
                    return str_error
                propierty_decimals = json_propierty_content[propierty_field_decimalS]
                if not propierty_field_minimum in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_minimum))
                    return str_error
                propierty_minimum = json_propierty_content[propierty_field_minimum]
                if not propierty_field_maximum in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_maximum))
                    return str_error
                propierty_maximum = json_propierty_content[propierty_field_maximum]
                if not propierty_field_single_step in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_single_step))
                    return str_error
                propierty_single_step = json_propierty_content[propierty_field_single_step]
                propierty_text = (
                    'widget:QDoubleSpinBox, decimals:{}, minimum:{}, maximum:{}, singleStep:{}, toolTip:{}'
                    .format(propierty_decimals, propierty_minimum,
                            propierty_maximum, propierty_single_step, propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG:
                propiertyIsInteger = True
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG:
                propiertyIsValuesList = True
                propierty_text = (
                    'widget:QComboBox, toolTip:{}'.format(propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_FOLDER_TAG:
                propiertyIsFolder = True
                propierty_text = ('widget:file, type:folder, toolTip:{}'.format(propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_FILE_OPEN_TAG:
                propiertyIsFileOpen = True
                propierty_text = ('widget:file, toolTip:{}'.format(propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_FILE_SAVE_TAG:
                propiertyIsFileSave = True
            f.write('\n\t@property\n')
            f.write('\tdef {}(self):\n'.format(propierty_name))
            f.write('\t\treturn self.__{}\n'.format(propierty_name))
            f.write('\n\t@{}.setter\n'.format(propierty_name))
            f.write('\tdef {}(self, value: \'{}\'):\n'.format(propierty_name.lower(), propierty_text))
            f.write('\t\tself.__{} = value\n'.format(propierty_name.lower()))
            # if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
            #     f.write('\n\tdef set_{}_value(self,int):\n'.format(propierty_name))
            # else:
            #     f.write('\n\tdef set_{}_value(self):\n'.format(propierty_name))
            f.write('\n\tdef set_{}_value(self):\n'.format(propierty_name))
            f.write('\t\tpropierty_{}_widget = self.__widget_by_propierty[\'{}\'] \n'
                    .format(propierty_name, propierty_name))
            f.write('\t\tif isinstance(propierty_{}_widget, QDoubleSpinBox):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.value()\n'
                    .format(propierty_name,propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QComboBox):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.currentText()\n'
                    .format(propierty_name,propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QLineEdit):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.text()\n'
                    .format(propierty_name,propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QCheckBox):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.isChecked()\n'
                    .format(propierty_name,propierty_name))



        f.write('\n\tdef set_widget(self, widget):\n')
        f.write('\t\tself.__widget = widget\n')
        for propierty_name in json_class_content:
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                continue
            f.write('\t\tpropierty_{}_widget = self.__widget.get_widget(\'{}\')\n'
                    .format(propierty_name.lower(), propierty_name.lower()))
            f.write('\t\tif isinstance(propierty_{}_widget, QDoubleSpinBox):\n'.format(propierty_name.lower()))
            f.write('\t\t\tpropierty_{}_widget.valueChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name.lower(), propierty_name.lower()))
            f.write('\t\telif isinstance(propierty_{}_widget, QComboBox):\n'.format(propierty_name.lower()))
            f.write('\t\t\tpropierty_{}_widget.currentIndexChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name.lower(), propierty_name.lower()))
            f.write('\t\telif isinstance(propierty_{}_widget, QLineEdit):\n'.format(propierty_name.lower()))
            f.write('\t\t\tpropierty_{}_widget.editingFinished.connect(self.set_{}_value)\n'
                    .format(propierty_name.lower(), propierty_name.lower()))
            f.write('\t\t\tpropierty_{}_widget.textChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name.lower(), propierty_name.lower()))
            f.write('\t\telif isinstance(propierty_{}_widget, QCheckBox):\n'.format(propierty_name.lower()))
            f.write('\t\t\tpropierty_{}_widget.stateChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name.lower(), propierty_name.lower()))

            f.write('\t\tself.__widget_by_propierty[\'{}\'] = propierty_{}_widget\n'
                    .format(propierty_name.lower(), propierty_name.lower()))

        f.close()
        return str_error

    def from_json_file(self,
                       definitions_file):
        str_error = ""
        if not os.path.isfile(definitions_file):
            str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
            str_error += ("\nNot exists file: {}".format(definitions_file))
            return str_error
        f = open(definitions_file)
        try:
            json_content = json.load(f)
        except:
            str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
            str_error += ("\nInvalid JSON file: {}".format(definitions_file))
            f.close()
            return str_error
        f.close()
        if not gui_defines.GUI_LANGUAGE_TAG in json_content:
            str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
            str_error += ("\n{} not in JSON file: {}".format(gui_defines.GUI_LANGUAGE_TAG, definitions_file))
            return str_error
        language = json_content[gui_defines.GUI_LANGUAGE_TAG]
        gui_classes = gui_defines.GUI_CLASSES
        for class_name in self.parameters:
            if not class_name in json_content:
                str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
                str_error += ("\nClass: {} not in JSON file: {}".format(class_name, definitions_file))
                return str_error
            if class_name != 'Project' and class_name != 'CameraCalibration':
                continue
            # if class_name != 'Project' and class_name != 'Workflow' and class_name != 'Photo'\
            #         and class_name != 'Roi' and class_name != 'CameraCalibration':
            #     continue
            json_class_content = json_content[class_name]
            str_error = self.build_parameter_file(class_name,
                                                  language,
                                                  json_class_content)
            if str_error:
                return str_error
            self.parameters[class_name][gui_defines.PARAMETER_JSON_CONTENT] = json_class_content
        self.json_file = definitions_file
        self.json_content = json_content
        return str_error
