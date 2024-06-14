import json
import os
from pathlib import Path
from gui import gui_defines


class BuildClassesDefinition:
    def __init__(self):
        self.definitions_file = None

    def build_class_file(self,
                         class_name,
                         json_class_content):
        str_error = ""
        current_path = os.path.dirname(os.path.realpath(__file__))
        class_file_path = current_path + gui_defines.GUI_CLASSES_PATH
        class_file_path = os.path.normpath(class_file_path)
        if not os.path.exists(class_file_path):
            os.makedirs(class_file_path)
            if not os.path.exists(class_file_path):
                str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                str_error += ("\nError making Classes path: {}".format(class_file_path))
                return str_error
        class_file = class_file_path + "/" + class_name + ".py"
        class_file = os.path.normpath(class_file)
        f = open(class_file, "w")
        f.write('from . import gui_defines\n')
        f.write('\nclass {}:\n'.format(class_name))
        f.write('\tdef __init__(self):\n')
        propierty_field_definition = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DEFINITION_TAG
        propierty_field_type = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_TYPE_TAG
        propierty_field_default = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DEFAULT_TAG
        propierty_field_decimalS = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DECIMALS_TAG
        propierty_field_maximum = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_MAXIMUM_TAG
        propierty_field_minimum = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_MINIMUM_TAG
        propierty_field_single_step = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_SINGLE_STEP_TAG
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
            propierty_name = propierty_name.lower()
            if not propierty_field_type in json_propierty_content:
                str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_type))
                return str_error
            propierty_type = json_propierty_content[propierty_field_type]
            if not propierty_field_default in json_propierty_content:
                str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_default))
                return str_error
            propierty_default_value = str(json_propierty_content[propierty_field_default])
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                if propierty_default_value != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TRUE \
                        and propierty_default_value != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_FALSE:
                    str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, field: {} must be {} or {}"
                                  .format(class_name, propierty_name, propierty_field_default,
                                          gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TRUE,
                                          gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_FALSE))
                    return str_error
            text = '\t\tself.__' + propierty_name.lower() + " = "
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG:
                values_content = json_propierty_content[propierty_type]
                text += "["
                pos_default_in_values_content = -1
                cont = 0
                for value_tag in values_content:
                    value = values_content[value_tag]
                    if value == propierty_default_value:
                        text += ('\'{}\''.format(value))
                        pos_default_in_values_content = cont
                        break
                    cont = cont + 1
                if pos_default_in_values_content == -1:
                    str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, field: {}, "
                                  "default value: {} is not in valid values"
                                  .format(class_name, propierty_name, propierty_field_type,
                                          propierty_default_value))
                cont = 0
                for value_tag in values_content:
                    if cont == pos_default_in_values_content:
                        cont = cont + 1
                        continue
                    value = values_content[value_tag]
                    text += (' ,\' {}\''.format(value))
                    cont = cont + 1
                text += "]"
                text += "\n"
                f.write(text)
                continue
            if propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                text += '\"'
            text += propierty_default_value
            if propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                text += '\"'
            text += "\n"
            f.write(text)
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
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
                str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_definition))
                return str_error
            propierty_definition = json_propierty_content[propierty_field_definition]
            if not propierty_field_type in json_propierty_content:
                str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
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
                    str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_decimalS))
                    return str_error
                propierty_decimals = json_propierty_content[propierty_field_decimalS]
                if not propierty_field_minimum in json_propierty_content:
                    str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_minimum))
                    return str_error
                propierty_minimum = json_propierty_content[propierty_field_minimum]
                if not propierty_field_maximum in json_propierty_content:
                    str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_maximum))
                    return str_error
                propierty_maximum = json_propierty_content[propierty_field_maximum]
                if not propierty_field_single_step in json_propierty_content:
                    str_error = BuildClassesDefinition.__name__ + "." + self.build_class_file.__name__
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

        f.close()
        return str_error

    def set_from_json_file(self,
                           definitions_file):
        str_error = ""
        if not os.path.isfile(definitions_file):
            str_error = BuildClassesDefinition.__name__ + "." + self.set_from_json_file.__name__
            str_error += ("\nNot exists file: {}".format(definitions_file))
            return str_error
        f = open(definitions_file)
        try:
            json_content = json.load(f)
        except:
            str_error = BuildClassesDefinition.__name__ + "." + self.set_from_json_file.__name__
            str_error += ("\nInvalid JSON file: {}".format(definitions_file))
            f.close()
            return str_error
        f.close()
        gui_classes = gui_defines.GUI_CLASSES
        for class_name in gui_classes:
            if not class_name in json_content:
                str_error = BuildClassesDefinition.__name__ + "." + self.set_from_json_file.__name__
                str_error += ("\nClass: {} not in JSON file: {}".format(class_name, definitions_file))
                f.close()
                return str_error
            if class_name != 'Project' and class_name != 'Workflow' and class_name != 'Photo':
                continue
            json_class_content = json_content[class_name]
            str_error = self.build_class_file(class_name,
                                              json_class_content)
            if str_error:
                return str_error
        return str_error
