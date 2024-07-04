from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class Workflow:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'Flujo de trabajo'
		self.__text_by_propierty['cleanprevious'] = 'Reseteo directorio previo'
		self.__widget_by_propierty['cleanprevious'] = None
		self.__cleanprevious = True
		self.__cleanprevious_value = True
		self.__text_by_propierty['initialize'] = 'Project inicialización'
		self.__widget_by_propierty['initialize'] = None
		self.__initialize = True
		self.__initialize_value = True
		self.__text_by_propierty['preprocess'] = 'Project preproceso'
		self.__widget_by_propierty['preprocess'] = None
		self.__preprocess = True
		self.__preprocess_value = True
		self.__text_by_propierty['optimize'] = 'Optimización de OI'
		self.__widget_by_propierty['optimize'] = None
		self.__optimize = True
		self.__optimize_value = True
		self.__text_by_propierty['split'] = 'Partición del proyecto'
		self.__widget_by_propierty['split'] = None
		self.__split = True
		self.__split_value = True
		self.__text_by_propierty['pointcloud'] = 'Construcción de nube de puntos'
		self.__widget_by_propierty['pointcloud'] = None
		self.__pointcloud = True
		self.__pointcloud_value = True
		self.__text_by_propierty['dems'] = 'Construcción de los modelos digitales de elevaciones'
		self.__widget_by_propierty['dems'] = None
		self.__dems = True
		self.__dems_value = True
		self.__text_by_propierty['orthomosaic'] = 'Construcción del ortomosaico'
		self.__widget_by_propierty['orthomosaic'] = None
		self.__orthomosaic = True
		self.__orthomosaic_value = True
		self.__text_by_propierty['report'] = 'Construcción del informe'
		self.__widget_by_propierty['report'] = None
		self.__report = True
		self.__report_value = True
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['CleanPrevious'] = self.__cleanprevious_value
		values['Initialize'] = self.__initialize_value
		values['Preprocess'] = self.__preprocess_value
		values['Optimize'] = self.__optimize_value
		values['Split'] = self.__split_value
		values['PointCloud'] = self.__pointcloud_value
		values['DEMs'] = self.__dems_value
		values['Orthomosaic'] = self.__orthomosaic_value
		values['Report'] = self.__report_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def cleanprevious(self):
		return self.__cleanprevious

	@cleanprevious.setter
	def cleanprevious(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la limpieza del trabajo anterior'):
		self.__cleanprevious = value

	def set_cleanprevious_value(self):
		propierty_cleanprevious_widget = self.__widget_by_propierty['cleanprevious'] 
		if isinstance(propierty_cleanprevious_widget, QSpinBox):
			self.__cleanprevious_value = propierty_cleanprevious_widget.value()
		elif isinstance(propierty_cleanprevious_widget, QDoubleSpinBox):
			self.__cleanprevious_value = propierty_cleanprevious_widget.value()
		elif isinstance(propierty_cleanprevious_widget, QComboBox):
			self.__cleanprevious_value = propierty_cleanprevious_widget.currentText()
		elif isinstance(propierty_cleanprevious_widget, QLineEdit):
			self.__cleanprevious_value = propierty_cleanprevious_widget.text()
		elif isinstance(propierty_cleanprevious_widget, QCheckBox):
			self.__cleanprevious_value = propierty_cleanprevious_widget.isChecked()

	@property
	def initialize(self):
		return self.__initialize

	@initialize.setter
	def initialize(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación del proyecto e importación de los datos de entrada'):
		self.__initialize = value

	def set_initialize_value(self):
		propierty_initialize_widget = self.__widget_by_propierty['initialize'] 
		if isinstance(propierty_initialize_widget, QSpinBox):
			self.__initialize_value = propierty_initialize_widget.value()
		elif isinstance(propierty_initialize_widget, QDoubleSpinBox):
			self.__initialize_value = propierty_initialize_widget.value()
		elif isinstance(propierty_initialize_widget, QComboBox):
			self.__initialize_value = propierty_initialize_widget.currentText()
		elif isinstance(propierty_initialize_widget, QLineEdit):
			self.__initialize_value = propierty_initialize_widget.text()
		elif isinstance(propierty_initialize_widget, QCheckBox):
			self.__initialize_value = propierty_initialize_widget.isChecked()

	@property
	def preprocess(self):
		return self.__preprocess

	@preprocess.setter
	def preprocess(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta el cosido y alineamiento inicial'):
		self.__preprocess = value

	def set_preprocess_value(self):
		propierty_preprocess_widget = self.__widget_by_propierty['preprocess'] 
		if isinstance(propierty_preprocess_widget, QSpinBox):
			self.__preprocess_value = propierty_preprocess_widget.value()
		elif isinstance(propierty_preprocess_widget, QDoubleSpinBox):
			self.__preprocess_value = propierty_preprocess_widget.value()
		elif isinstance(propierty_preprocess_widget, QComboBox):
			self.__preprocess_value = propierty_preprocess_widget.currentText()
		elif isinstance(propierty_preprocess_widget, QLineEdit):
			self.__preprocess_value = propierty_preprocess_widget.text()
		elif isinstance(propierty_preprocess_widget, QCheckBox):
			self.__preprocess_value = propierty_preprocess_widget.isChecked()

	@property
	def optimize(self):
		return self.__optimize

	@optimize.setter
	def optimize(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la optimización del alineamiento inicial con puntos de apoyo'):
		self.__optimize = value

	def set_optimize_value(self):
		propierty_optimize_widget = self.__widget_by_propierty['optimize'] 
		if isinstance(propierty_optimize_widget, QSpinBox):
			self.__optimize_value = propierty_optimize_widget.value()
		elif isinstance(propierty_optimize_widget, QDoubleSpinBox):
			self.__optimize_value = propierty_optimize_widget.value()
		elif isinstance(propierty_optimize_widget, QComboBox):
			self.__optimize_value = propierty_optimize_widget.currentText()
		elif isinstance(propierty_optimize_widget, QLineEdit):
			self.__optimize_value = propierty_optimize_widget.text()
		elif isinstance(propierty_optimize_widget, QCheckBox):
			self.__optimize_value = propierty_optimize_widget.isChecked()

	@property
	def split(self):
		return self.__split

	@split.setter
	def split(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la partición del trabajo en tiles'):
		self.__split = value

	def set_split_value(self):
		propierty_split_widget = self.__widget_by_propierty['split'] 
		if isinstance(propierty_split_widget, QSpinBox):
			self.__split_value = propierty_split_widget.value()
		elif isinstance(propierty_split_widget, QDoubleSpinBox):
			self.__split_value = propierty_split_widget.value()
		elif isinstance(propierty_split_widget, QComboBox):
			self.__split_value = propierty_split_widget.currentText()
		elif isinstance(propierty_split_widget, QLineEdit):
			self.__split_value = propierty_split_widget.text()
		elif isinstance(propierty_split_widget, QCheckBox):
			self.__split_value = propierty_split_widget.isChecked()

	@property
	def pointcloud(self):
		return self.__pointcloud

	@pointcloud.setter
	def pointcloud(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación y exportación de la nube de puntos densa'):
		self.__pointcloud = value

	def set_pointcloud_value(self):
		propierty_pointcloud_widget = self.__widget_by_propierty['pointcloud'] 
		if isinstance(propierty_pointcloud_widget, QSpinBox):
			self.__pointcloud_value = propierty_pointcloud_widget.value()
		elif isinstance(propierty_pointcloud_widget, QDoubleSpinBox):
			self.__pointcloud_value = propierty_pointcloud_widget.value()
		elif isinstance(propierty_pointcloud_widget, QComboBox):
			self.__pointcloud_value = propierty_pointcloud_widget.currentText()
		elif isinstance(propierty_pointcloud_widget, QLineEdit):
			self.__pointcloud_value = propierty_pointcloud_widget.text()
		elif isinstance(propierty_pointcloud_widget, QCheckBox):
			self.__pointcloud_value = propierty_pointcloud_widget.isChecked()

	@property
	def dems(self):
		return self.__dems

	@dems.setter
	def dems(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación y exportación de los modelos digitales de elevaciones'):
		self.__dems = value

	def set_dems_value(self):
		propierty_dems_widget = self.__widget_by_propierty['dems'] 
		if isinstance(propierty_dems_widget, QSpinBox):
			self.__dems_value = propierty_dems_widget.value()
		elif isinstance(propierty_dems_widget, QDoubleSpinBox):
			self.__dems_value = propierty_dems_widget.value()
		elif isinstance(propierty_dems_widget, QComboBox):
			self.__dems_value = propierty_dems_widget.currentText()
		elif isinstance(propierty_dems_widget, QLineEdit):
			self.__dems_value = propierty_dems_widget.text()
		elif isinstance(propierty_dems_widget, QCheckBox):
			self.__dems_value = propierty_dems_widget.isChecked()

	@property
	def orthomosaic(self):
		return self.__orthomosaic

	@orthomosaic.setter
	def orthomosaic(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación y exportación del orthomosaico'):
		self.__orthomosaic = value

	def set_orthomosaic_value(self):
		propierty_orthomosaic_widget = self.__widget_by_propierty['orthomosaic'] 
		if isinstance(propierty_orthomosaic_widget, QSpinBox):
			self.__orthomosaic_value = propierty_orthomosaic_widget.value()
		elif isinstance(propierty_orthomosaic_widget, QDoubleSpinBox):
			self.__orthomosaic_value = propierty_orthomosaic_widget.value()
		elif isinstance(propierty_orthomosaic_widget, QComboBox):
			self.__orthomosaic_value = propierty_orthomosaic_widget.currentText()
		elif isinstance(propierty_orthomosaic_widget, QLineEdit):
			self.__orthomosaic_value = propierty_orthomosaic_widget.text()
		elif isinstance(propierty_orthomosaic_widget, QCheckBox):
			self.__orthomosaic_value = propierty_orthomosaic_widget.isChecked()

	@property
	def report(self):
		return self.__report

	@report.setter
	def report(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la exportación del informe de resultados'):
		self.__report = value

	def set_report_value(self):
		propierty_report_widget = self.__widget_by_propierty['report'] 
		if isinstance(propierty_report_widget, QSpinBox):
			self.__report_value = propierty_report_widget.value()
		elif isinstance(propierty_report_widget, QDoubleSpinBox):
			self.__report_value = propierty_report_widget.value()
		elif isinstance(propierty_report_widget, QComboBox):
			self.__report_value = propierty_report_widget.currentText()
		elif isinstance(propierty_report_widget, QLineEdit):
			self.__report_value = propierty_report_widget.text()
		elif isinstance(propierty_report_widget, QCheckBox):
			self.__report_value = propierty_report_widget.isChecked()

	def set_values_from_dictionary(self, values):
		self.__cleanprevious_value = values['CleanPrevious']
		self.__cleanprevious = values['CleanPrevious']
		self.__initialize_value = values['Initialize']
		self.__initialize = values['Initialize']
		self.__preprocess_value = values['Preprocess']
		self.__preprocess = values['Preprocess']
		self.__optimize_value = values['Optimize']
		self.__optimize = values['Optimize']
		self.__split_value = values['Split']
		self.__split = values['Split']
		self.__pointcloud_value = values['PointCloud']
		self.__pointcloud = values['PointCloud']
		self.__dems_value = values['DEMs']
		self.__dems = values['DEMs']
		self.__orthomosaic_value = values['Orthomosaic']
		self.__orthomosaic = values['Orthomosaic']
		self.__report_value = values['Report']
		self.__report = values['Report']
		return

	def set_widget(self, widget):
		self.__widget = widget
		propierty_cleanprevious_widget = self.__widget.get_widget('cleanprevious')
		if isinstance(propierty_cleanprevious_widget, QSpinBox):
			propierty_cleanprevious_widget.valueChanged.connect(self.set_cleanprevious_value)
		elif isinstance(propierty_cleanprevious_widget, QDoubleSpinBox):
			propierty_cleanprevious_widget.valueChanged.connect(self.set_cleanprevious_value)
		elif isinstance(propierty_cleanprevious_widget, QComboBox):
			propierty_cleanprevious_widget.currentIndexChanged.connect(self.set_cleanprevious_value)
		elif isinstance(propierty_cleanprevious_widget, QLineEdit):
			propierty_cleanprevious_widget.editingFinished.connect(self.set_cleanprevious_value)
			propierty_cleanprevious_widget.textChanged.connect(self.set_cleanprevious_value)
		elif isinstance(propierty_cleanprevious_widget, QCheckBox):
			propierty_cleanprevious_widget.stateChanged.connect(self.set_cleanprevious_value)
		self.__widget_by_propierty['cleanprevious'] = propierty_cleanprevious_widget
		propierty_initialize_widget = self.__widget.get_widget('initialize')
		if isinstance(propierty_initialize_widget, QSpinBox):
			propierty_initialize_widget.valueChanged.connect(self.set_initialize_value)
		elif isinstance(propierty_initialize_widget, QDoubleSpinBox):
			propierty_initialize_widget.valueChanged.connect(self.set_initialize_value)
		elif isinstance(propierty_initialize_widget, QComboBox):
			propierty_initialize_widget.currentIndexChanged.connect(self.set_initialize_value)
		elif isinstance(propierty_initialize_widget, QLineEdit):
			propierty_initialize_widget.editingFinished.connect(self.set_initialize_value)
			propierty_initialize_widget.textChanged.connect(self.set_initialize_value)
		elif isinstance(propierty_initialize_widget, QCheckBox):
			propierty_initialize_widget.stateChanged.connect(self.set_initialize_value)
		self.__widget_by_propierty['initialize'] = propierty_initialize_widget
		propierty_preprocess_widget = self.__widget.get_widget('preprocess')
		if isinstance(propierty_preprocess_widget, QSpinBox):
			propierty_preprocess_widget.valueChanged.connect(self.set_preprocess_value)
		elif isinstance(propierty_preprocess_widget, QDoubleSpinBox):
			propierty_preprocess_widget.valueChanged.connect(self.set_preprocess_value)
		elif isinstance(propierty_preprocess_widget, QComboBox):
			propierty_preprocess_widget.currentIndexChanged.connect(self.set_preprocess_value)
		elif isinstance(propierty_preprocess_widget, QLineEdit):
			propierty_preprocess_widget.editingFinished.connect(self.set_preprocess_value)
			propierty_preprocess_widget.textChanged.connect(self.set_preprocess_value)
		elif isinstance(propierty_preprocess_widget, QCheckBox):
			propierty_preprocess_widget.stateChanged.connect(self.set_preprocess_value)
		self.__widget_by_propierty['preprocess'] = propierty_preprocess_widget
		propierty_optimize_widget = self.__widget.get_widget('optimize')
		if isinstance(propierty_optimize_widget, QSpinBox):
			propierty_optimize_widget.valueChanged.connect(self.set_optimize_value)
		elif isinstance(propierty_optimize_widget, QDoubleSpinBox):
			propierty_optimize_widget.valueChanged.connect(self.set_optimize_value)
		elif isinstance(propierty_optimize_widget, QComboBox):
			propierty_optimize_widget.currentIndexChanged.connect(self.set_optimize_value)
		elif isinstance(propierty_optimize_widget, QLineEdit):
			propierty_optimize_widget.editingFinished.connect(self.set_optimize_value)
			propierty_optimize_widget.textChanged.connect(self.set_optimize_value)
		elif isinstance(propierty_optimize_widget, QCheckBox):
			propierty_optimize_widget.stateChanged.connect(self.set_optimize_value)
		self.__widget_by_propierty['optimize'] = propierty_optimize_widget
		propierty_split_widget = self.__widget.get_widget('split')
		if isinstance(propierty_split_widget, QSpinBox):
			propierty_split_widget.valueChanged.connect(self.set_split_value)
		elif isinstance(propierty_split_widget, QDoubleSpinBox):
			propierty_split_widget.valueChanged.connect(self.set_split_value)
		elif isinstance(propierty_split_widget, QComboBox):
			propierty_split_widget.currentIndexChanged.connect(self.set_split_value)
		elif isinstance(propierty_split_widget, QLineEdit):
			propierty_split_widget.editingFinished.connect(self.set_split_value)
			propierty_split_widget.textChanged.connect(self.set_split_value)
		elif isinstance(propierty_split_widget, QCheckBox):
			propierty_split_widget.stateChanged.connect(self.set_split_value)
		self.__widget_by_propierty['split'] = propierty_split_widget
		propierty_pointcloud_widget = self.__widget.get_widget('pointcloud')
		if isinstance(propierty_pointcloud_widget, QSpinBox):
			propierty_pointcloud_widget.valueChanged.connect(self.set_pointcloud_value)
		elif isinstance(propierty_pointcloud_widget, QDoubleSpinBox):
			propierty_pointcloud_widget.valueChanged.connect(self.set_pointcloud_value)
		elif isinstance(propierty_pointcloud_widget, QComboBox):
			propierty_pointcloud_widget.currentIndexChanged.connect(self.set_pointcloud_value)
		elif isinstance(propierty_pointcloud_widget, QLineEdit):
			propierty_pointcloud_widget.editingFinished.connect(self.set_pointcloud_value)
			propierty_pointcloud_widget.textChanged.connect(self.set_pointcloud_value)
		elif isinstance(propierty_pointcloud_widget, QCheckBox):
			propierty_pointcloud_widget.stateChanged.connect(self.set_pointcloud_value)
		self.__widget_by_propierty['pointcloud'] = propierty_pointcloud_widget
		propierty_dems_widget = self.__widget.get_widget('dems')
		if isinstance(propierty_dems_widget, QSpinBox):
			propierty_dems_widget.valueChanged.connect(self.set_dems_value)
		elif isinstance(propierty_dems_widget, QDoubleSpinBox):
			propierty_dems_widget.valueChanged.connect(self.set_dems_value)
		elif isinstance(propierty_dems_widget, QComboBox):
			propierty_dems_widget.currentIndexChanged.connect(self.set_dems_value)
		elif isinstance(propierty_dems_widget, QLineEdit):
			propierty_dems_widget.editingFinished.connect(self.set_dems_value)
			propierty_dems_widget.textChanged.connect(self.set_dems_value)
		elif isinstance(propierty_dems_widget, QCheckBox):
			propierty_dems_widget.stateChanged.connect(self.set_dems_value)
		self.__widget_by_propierty['dems'] = propierty_dems_widget
		propierty_orthomosaic_widget = self.__widget.get_widget('orthomosaic')
		if isinstance(propierty_orthomosaic_widget, QSpinBox):
			propierty_orthomosaic_widget.valueChanged.connect(self.set_orthomosaic_value)
		elif isinstance(propierty_orthomosaic_widget, QDoubleSpinBox):
			propierty_orthomosaic_widget.valueChanged.connect(self.set_orthomosaic_value)
		elif isinstance(propierty_orthomosaic_widget, QComboBox):
			propierty_orthomosaic_widget.currentIndexChanged.connect(self.set_orthomosaic_value)
		elif isinstance(propierty_orthomosaic_widget, QLineEdit):
			propierty_orthomosaic_widget.editingFinished.connect(self.set_orthomosaic_value)
			propierty_orthomosaic_widget.textChanged.connect(self.set_orthomosaic_value)
		elif isinstance(propierty_orthomosaic_widget, QCheckBox):
			propierty_orthomosaic_widget.stateChanged.connect(self.set_orthomosaic_value)
		self.__widget_by_propierty['orthomosaic'] = propierty_orthomosaic_widget
		propierty_report_widget = self.__widget.get_widget('report')
		if isinstance(propierty_report_widget, QSpinBox):
			propierty_report_widget.valueChanged.connect(self.set_report_value)
		elif isinstance(propierty_report_widget, QDoubleSpinBox):
			propierty_report_widget.valueChanged.connect(self.set_report_value)
		elif isinstance(propierty_report_widget, QComboBox):
			propierty_report_widget.currentIndexChanged.connect(self.set_report_value)
		elif isinstance(propierty_report_widget, QLineEdit):
			propierty_report_widget.editingFinished.connect(self.set_report_value)
			propierty_report_widget.textChanged.connect(self.set_report_value)
		elif isinstance(propierty_report_widget, QCheckBox):
			propierty_report_widget.stateChanged.connect(self.set_report_value)
		self.__widget_by_propierty['report'] = propierty_report_widget
