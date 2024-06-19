from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class Roi:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'Región de interés'
		self.__text_by_propierty['path'] = 'Ruta ROI'
		self.__widget_by_propierty['path'] = None
		self.__path = ""
		self.__path_value = ""
		self.__text_by_propierty['method'] = 'Fuente ROI'
		self.__widget_by_propierty['method'] = None
		self.__method = ['Región total con recubrimiento' ,' Importada de shapefile']
		self.__method_value = 'Región total con recubrimiento'
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['Path'] = self.__path_value
		values['Method'] = self.__method_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def path(self):
		return self.__path

	@path.setter
	def path(self, value: 'widget:file, toolTip:Ruta del archivo de la ROI'):
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
	def method(self):
		return self.__method

	@method.setter
	def method(self, value: 'widget:QComboBox, toolTip:Método de definición de la ROI'):
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
