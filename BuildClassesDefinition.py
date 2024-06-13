import json
import os
from pathlib import Path
from gui import gui_defines


class BuildClassesDefinition:
    def __init__(self):
        self.definitions_file = None

    def build_class_file(self,
                         class_name,
                         json_content):
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
        class_file = class_file_path + "/" + class_name + "_debug.py"
        class_file = os.path.normpath(class_file)
        f = open(class_file, "w")
        f.write('from . import gui_defines\n')


        f.close()
        return str

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
            str_error = self.build_class_file(class_name,
                                              json_content)
            if str_error:
                return str_error

            tu = 1
        return str_error
