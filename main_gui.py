# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
# Ana del Campo Sanchez, ana.delcampo@usal.es

import sys, os
from PyQt5.QtWidgets import QApplication
# from MshBigPsxDialog import MshBigPsxDialog
from gui import gui_defines
from ParameterManager import ParametersManager
import Tools


def main():
    app = QApplication(sys.argv)

    parametersManager = ParametersManager()
    current_path = os.path.dirname(os.path.realpath(__file__))
    params_definitions_file = current_path + "/" + gui_defines.PARAMS_DEFINITION_FILE
    params_definitions_file = os.path.normpath(params_definitions_file)
    str_error = parametersManager.from_json_file(params_definitions_file)
    if str_error:
        Tools.error_msg(str_error)
        return

    from MshBigPsxDialog import MshBigPsxDialog
    dialog = MshBigPsxDialog(parametersManager)
    dialog.show()
    app.exec()


if __name__ == '__main__':
    main()
