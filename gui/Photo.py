from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class Photo:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'Imágenes'
		self.__text_by_propierty['path'] = 'Ruta imágenes'
		self.__widget_by_propierty['path'] = None
		self.__path = ""
		self.__path_value = ""
		self.__text_by_propierty['locationaccuracy2d'] = 'Precisión 2D de OE'
		self.__widget_by_propierty['locationaccuracy2d'] = None
		self.__locationaccuracy2d = 0.08
		self.__locationaccuracy2d_value = 0.08
		self.__text_by_propierty['locationaccuracyheight'] = 'Precisión Z de OE'
		self.__widget_by_propierty['locationaccuracyheight'] = None
		self.__locationaccuracyheight = 0.12
		self.__locationaccuracyheight_value = 0.12
		self.__text_by_propierty['method'] = 'Fuente OE'
		self.__widget_by_propierty['method'] = None
		self.__method = ['EXIF' ,' Fichero CSV']
		self.__method_value = 'EXIF'
		self.__text_by_propierty['epsg'] = 'Código EPSG'
		self.__widget_by_propierty['epsg'] = None
		self.__epsg = "4326"
		self.__epsg_value = "4326"
		self.__text_by_propierty['eopath'] = 'Ruta OE'
		self.__widget_by_propierty['eopath'] = None
		self.__eopath = ""
		self.__eopath_value = ""
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['Path'] = self.__path_value
		values['LocationAccuracy2D'] = self.__locationaccuracy2d_value
		values['LocationAccuracyHeight'] = self.__locationaccuracyheight_value
		values['Method'] = self.__method_value
		values['EPSG'] = self.__epsg_value
		values['EoPath'] = self.__eopath_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def path(self):
		return self.__path

	@path.setter
	def path(self, value: 'widget:file, type:folder, toolTip:Ruta del directorio donde se localizan las imágenes'):
		self.__path = value

	def set_path_value(self):
		propierty_path_widget = self.__widget_by_propierty['path'] 
		if isinstance(propierty_path_widget, QSpinBox):
			self.__path_value = propierty_path_widget.value()
		elif isinstance(propierty_path_widget, QDoubleSpinBox):
			self.__path_value = propierty_path_widget.value()
		elif isinstance(propierty_path_widget, QComboBox):
			self.__path_value = propierty_path_widget.currentText()
		elif isinstance(propierty_path_widget, QLineEdit):
			self.__path_value = propierty_path_widget.text()
		elif isinstance(propierty_path_widget, QCheckBox):
			self.__path_value = propierty_path_widget.isChecked()

	@property
	def locationaccuracy2d(self):
		return self.__locationaccuracy2d

	@locationaccuracy2d.setter
	def locationaccuracy2d(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:5.0, singleStep:0.01, toolTip:Precisión horizontal de la orientación externa de las imágenes en metros'):
		self.__locationaccuracy2d = value

	def set_locationaccuracy2d_value(self):
		propierty_locationaccuracy2d_widget = self.__widget_by_propierty['locationaccuracy2d'] 
		if isinstance(propierty_locationaccuracy2d_widget, QSpinBox):
			self.__locationaccuracy2d_value = propierty_locationaccuracy2d_widget.value()
		elif isinstance(propierty_locationaccuracy2d_widget, QDoubleSpinBox):
			self.__locationaccuracy2d_value = propierty_locationaccuracy2d_widget.value()
		elif isinstance(propierty_locationaccuracy2d_widget, QComboBox):
			self.__locationaccuracy2d_value = propierty_locationaccuracy2d_widget.currentText()
		elif isinstance(propierty_locationaccuracy2d_widget, QLineEdit):
			self.__locationaccuracy2d_value = propierty_locationaccuracy2d_widget.text()
		elif isinstance(propierty_locationaccuracy2d_widget, QCheckBox):
			self.__locationaccuracy2d_value = propierty_locationaccuracy2d_widget.isChecked()

	@property
	def locationaccuracyheight(self):
		return self.__locationaccuracyheight

	@locationaccuracyheight.setter
	def locationaccuracyheight(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:5.0, singleStep:0.01, toolTip:Precisión vertical de la orientación externa de las imágenes en metros'):
		self.__locationaccuracyheight = value

	def set_locationaccuracyheight_value(self):
		propierty_locationaccuracyheight_widget = self.__widget_by_propierty['locationaccuracyheight'] 
		if isinstance(propierty_locationaccuracyheight_widget, QSpinBox):
			self.__locationaccuracyheight_value = propierty_locationaccuracyheight_widget.value()
		elif isinstance(propierty_locationaccuracyheight_widget, QDoubleSpinBox):
			self.__locationaccuracyheight_value = propierty_locationaccuracyheight_widget.value()
		elif isinstance(propierty_locationaccuracyheight_widget, QComboBox):
			self.__locationaccuracyheight_value = propierty_locationaccuracyheight_widget.currentText()
		elif isinstance(propierty_locationaccuracyheight_widget, QLineEdit):
			self.__locationaccuracyheight_value = propierty_locationaccuracyheight_widget.text()
		elif isinstance(propierty_locationaccuracyheight_widget, QCheckBox):
			self.__locationaccuracyheight_value = propierty_locationaccuracyheight_widget.isChecked()

	@property
	def method(self):
		return self.__method

	@method.setter
	def method(self, value: 'widget:QComboBox, toolTip:Fuente de la que se importarán las orientaciones externas de las imágenes'):
		self.__method = value

	def set_method_value(self):
		propierty_method_widget = self.__widget_by_propierty['method'] 
		if isinstance(propierty_method_widget, QSpinBox):
			self.__method_value = propierty_method_widget.value()
		elif isinstance(propierty_method_widget, QDoubleSpinBox):
			self.__method_value = propierty_method_widget.value()
		elif isinstance(propierty_method_widget, QComboBox):
			self.__method_value = propierty_method_widget.currentText()
		elif isinstance(propierty_method_widget, QLineEdit):
			self.__method_value = propierty_method_widget.text()
		elif isinstance(propierty_method_widget, QCheckBox):
			self.__method_value = propierty_method_widget.isChecked()

	@property
	def epsg(self):
		return self.__epsg

	@epsg.setter
	def epsg(self, value: 'widget:QLineEdit, toolTip:Código EPSG con el que se importarán las imágenes'):
		self.__epsg = value

	def set_epsg_value(self):
		propierty_epsg_widget = self.__widget_by_propierty['epsg'] 
		if isinstance(propierty_epsg_widget, QSpinBox):
			self.__epsg_value = propierty_epsg_widget.value()
		elif isinstance(propierty_epsg_widget, QDoubleSpinBox):
			self.__epsg_value = propierty_epsg_widget.value()
		elif isinstance(propierty_epsg_widget, QComboBox):
			self.__epsg_value = propierty_epsg_widget.currentText()
		elif isinstance(propierty_epsg_widget, QLineEdit):
			self.__epsg_value = propierty_epsg_widget.text()
		elif isinstance(propierty_epsg_widget, QCheckBox):
			self.__epsg_value = propierty_epsg_widget.isChecked()

	@property
	def eopath(self):
		return self.__eopath

	@eopath.setter
	def eopath(self, value: 'widget:file, toolTip:Ruta del archivo CSV con las orientaciones externas'):
		self.__eopath = value

	def set_eopath_value(self):
		propierty_eopath_widget = self.__widget_by_propierty['eopath'] 
		if isinstance(propierty_eopath_widget, QSpinBox):
			self.__eopath_value = propierty_eopath_widget.value()
		elif isinstance(propierty_eopath_widget, QDoubleSpinBox):
			self.__eopath_value = propierty_eopath_widget.value()
		elif isinstance(propierty_eopath_widget, QComboBox):
			self.__eopath_value = propierty_eopath_widget.currentText()
		elif isinstance(propierty_eopath_widget, QLineEdit):
			self.__eopath_value = propierty_eopath_widget.text()
		elif isinstance(propierty_eopath_widget, QCheckBox):
			self.__eopath_value = propierty_eopath_widget.isChecked()

	def set_values_from_dictionary(self, values):
		self.__path_value = values['Path']
		self.__path = values['Path']
		self.__locationaccuracy2d_value = values['LocationAccuracy2D']
		self.__locationaccuracy2d = values['LocationAccuracy2D']
		self.__locationaccuracyheight_value = values['LocationAccuracyHeight']
		self.__locationaccuracyheight = values['LocationAccuracyHeight']
		self.__method_value = values['Method']
		self.__method = values['Method']
		self.__epsg_value = values['EPSG']
		self.__epsg = values['EPSG']
		self.__eopath_value = values['EoPath']
		self.__eopath = values['EoPath']
		return

	def set_widget(self, widget):
		self.__widget = widget
		propierty_path_widget = self.__widget.get_widget('path')
		if isinstance(propierty_path_widget, QSpinBox):
			propierty_path_widget.valueChanged.connect(self.set_path_value)
		elif isinstance(propierty_path_widget, QDoubleSpinBox):
			propierty_path_widget.valueChanged.connect(self.set_path_value)
		elif isinstance(propierty_path_widget, QComboBox):
			propierty_path_widget.currentIndexChanged.connect(self.set_path_value)
		elif isinstance(propierty_path_widget, QLineEdit):
			propierty_path_widget.editingFinished.connect(self.set_path_value)
			propierty_path_widget.textChanged.connect(self.set_path_value)
		elif isinstance(propierty_path_widget, QCheckBox):
			propierty_path_widget.stateChanged.connect(self.set_path_value)
		self.__widget_by_propierty['path'] = propierty_path_widget
		propierty_locationaccuracy2d_widget = self.__widget.get_widget('locationaccuracy2d')
		if isinstance(propierty_locationaccuracy2d_widget, QSpinBox):
			propierty_locationaccuracy2d_widget.valueChanged.connect(self.set_locationaccuracy2d_value)
		elif isinstance(propierty_locationaccuracy2d_widget, QDoubleSpinBox):
			propierty_locationaccuracy2d_widget.valueChanged.connect(self.set_locationaccuracy2d_value)
		elif isinstance(propierty_locationaccuracy2d_widget, QComboBox):
			propierty_locationaccuracy2d_widget.currentIndexChanged.connect(self.set_locationaccuracy2d_value)
		elif isinstance(propierty_locationaccuracy2d_widget, QLineEdit):
			propierty_locationaccuracy2d_widget.editingFinished.connect(self.set_locationaccuracy2d_value)
			propierty_locationaccuracy2d_widget.textChanged.connect(self.set_locationaccuracy2d_value)
		elif isinstance(propierty_locationaccuracy2d_widget, QCheckBox):
			propierty_locationaccuracy2d_widget.stateChanged.connect(self.set_locationaccuracy2d_value)
		self.__widget_by_propierty['locationaccuracy2d'] = propierty_locationaccuracy2d_widget
		propierty_locationaccuracyheight_widget = self.__widget.get_widget('locationaccuracyheight')
		if isinstance(propierty_locationaccuracyheight_widget, QSpinBox):
			propierty_locationaccuracyheight_widget.valueChanged.connect(self.set_locationaccuracyheight_value)
		elif isinstance(propierty_locationaccuracyheight_widget, QDoubleSpinBox):
			propierty_locationaccuracyheight_widget.valueChanged.connect(self.set_locationaccuracyheight_value)
		elif isinstance(propierty_locationaccuracyheight_widget, QComboBox):
			propierty_locationaccuracyheight_widget.currentIndexChanged.connect(self.set_locationaccuracyheight_value)
		elif isinstance(propierty_locationaccuracyheight_widget, QLineEdit):
			propierty_locationaccuracyheight_widget.editingFinished.connect(self.set_locationaccuracyheight_value)
			propierty_locationaccuracyheight_widget.textChanged.connect(self.set_locationaccuracyheight_value)
		elif isinstance(propierty_locationaccuracyheight_widget, QCheckBox):
			propierty_locationaccuracyheight_widget.stateChanged.connect(self.set_locationaccuracyheight_value)
		self.__widget_by_propierty['locationaccuracyheight'] = propierty_locationaccuracyheight_widget
		propierty_method_widget = self.__widget.get_widget('method')
		if isinstance(propierty_method_widget, QSpinBox):
			propierty_method_widget.valueChanged.connect(self.set_method_value)
		elif isinstance(propierty_method_widget, QDoubleSpinBox):
			propierty_method_widget.valueChanged.connect(self.set_method_value)
		elif isinstance(propierty_method_widget, QComboBox):
			propierty_method_widget.currentIndexChanged.connect(self.set_method_value)
		elif isinstance(propierty_method_widget, QLineEdit):
			propierty_method_widget.editingFinished.connect(self.set_method_value)
			propierty_method_widget.textChanged.connect(self.set_method_value)
		elif isinstance(propierty_method_widget, QCheckBox):
			propierty_method_widget.stateChanged.connect(self.set_method_value)
		self.__widget_by_propierty['method'] = propierty_method_widget
		propierty_epsg_widget = self.__widget.get_widget('epsg')
		if isinstance(propierty_epsg_widget, QSpinBox):
			propierty_epsg_widget.valueChanged.connect(self.set_epsg_value)
		elif isinstance(propierty_epsg_widget, QDoubleSpinBox):
			propierty_epsg_widget.valueChanged.connect(self.set_epsg_value)
		elif isinstance(propierty_epsg_widget, QComboBox):
			propierty_epsg_widget.currentIndexChanged.connect(self.set_epsg_value)
		elif isinstance(propierty_epsg_widget, QLineEdit):
			propierty_epsg_widget.editingFinished.connect(self.set_epsg_value)
			propierty_epsg_widget.textChanged.connect(self.set_epsg_value)
		elif isinstance(propierty_epsg_widget, QCheckBox):
			propierty_epsg_widget.stateChanged.connect(self.set_epsg_value)
		self.__widget_by_propierty['epsg'] = propierty_epsg_widget
		propierty_eopath_widget = self.__widget.get_widget('eopath')
		if isinstance(propierty_eopath_widget, QSpinBox):
			propierty_eopath_widget.valueChanged.connect(self.set_eopath_value)
		elif isinstance(propierty_eopath_widget, QDoubleSpinBox):
			propierty_eopath_widget.valueChanged.connect(self.set_eopath_value)
		elif isinstance(propierty_eopath_widget, QComboBox):
			propierty_eopath_widget.currentIndexChanged.connect(self.set_eopath_value)
		elif isinstance(propierty_eopath_widget, QLineEdit):
			propierty_eopath_widget.editingFinished.connect(self.set_eopath_value)
			propierty_eopath_widget.textChanged.connect(self.set_eopath_value)
		elif isinstance(propierty_eopath_widget, QCheckBox):
			propierty_eopath_widget.stateChanged.connect(self.set_eopath_value)
		self.__widget_by_propierty['eopath'] = propierty_eopath_widget
