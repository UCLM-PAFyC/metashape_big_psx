# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
# Ana del Campo Sanchez, ana.delcampo@usal.es

import sys
from PyQt5.QtWidgets import QApplication
from MshBigPsxDialog import MshBigPsxDialog

app = QApplication(sys.argv)
dialog = MshBigPsxDialog()
dialog.show()
app.exec()
