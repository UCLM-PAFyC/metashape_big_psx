from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class InstallRequirement:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'Requisitos de instalación'
		self.__text_by_propierty['env'] = 'Carpeta del entorno conda'
		self.__widget_by_propierty['env'] = None
		self.__env = ""
		self.__env_value = ""
		self.__text_by_propierty['geoid'] = 'Carpeta con los modelos del Geoide'
		self.__widget_by_propierty['geoid'] = None
		self.__geoid = ""
		self.__geoid_value = ""
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['Env'] = self.__env_value
		values['Geoid'] = self.__geoid_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def env(self):
		return self.__env

	@env.setter
	def env(self, value: 'widget:file, type:folder, toolTip:Carpeta del entorno conda'):
		self.__env = value

	def set_env_value(self):
		propierty_env_widget = self.__widget_by_propierty['env'] 
		if isinstance(propierty_env_widget, QSpinBox):
			self.__env_value = propierty_env_widget.value()
		elif isinstance(propierty_env_widget, QDoubleSpinBox):
			self.__env_value = propierty_env_widget.value()
		elif isinstance(propierty_env_widget, QComboBox):
			self.__env_value = propierty_env_widget.currentText()
		elif isinstance(propierty_env_widget, QLineEdit):
			self.__env_value = propierty_env_widget.text()
		elif isinstance(propierty_env_widget, QCheckBox):
			self.__env_value = propierty_env_widget.isChecked()

	@property
	def geoid(self):
		return self.__geoid

	@geoid.setter
	def geoid(self, value: 'widget:file, type:folder, toolTip:Carpeta con los modelos del Geoide'):
		self.__geoid = value

	def set_geoid_value(self):
		propierty_geoid_widget = self.__widget_by_propierty['geoid'] 
		if isinstance(propierty_geoid_widget, QSpinBox):
			self.__geoid_value = propierty_geoid_widget.value()
		elif isinstance(propierty_geoid_widget, QDoubleSpinBox):
			self.__geoid_value = propierty_geoid_widget.value()
		elif isinstance(propierty_geoid_widget, QComboBox):
			self.__geoid_value = propierty_geoid_widget.currentText()
		elif isinstance(propierty_geoid_widget, QLineEdit):
			self.__geoid_value = propierty_geoid_widget.text()
		elif isinstance(propierty_geoid_widget, QCheckBox):
			self.__geoid_value = propierty_geoid_widget.isChecked()

	def set_values_from_dictionary(self, values):
		self.__env_value = values['Env']
		self.__env = values['Env']
		self.__geoid_value = values['Geoid']
		self.__geoid = values['Geoid']
		return

	def set_widget(self, widget):
		self.__widget = widget
		propierty_env_widget = self.__widget.get_widget('env')
		if isinstance(propierty_env_widget, QSpinBox):
			propierty_env_widget.valueChanged.connect(self.set_env_value)
		elif isinstance(propierty_env_widget, QDoubleSpinBox):
			propierty_env_widget.valueChanged.connect(self.set_env_value)
		elif isinstance(propierty_env_widget, QComboBox):
			propierty_env_widget.currentIndexChanged.connect(self.set_env_value)
		elif isinstance(propierty_env_widget, QLineEdit):
			propierty_env_widget.editingFinished.connect(self.set_env_value)
			propierty_env_widget.textChanged.connect(self.set_env_value)
		elif isinstance(propierty_env_widget, QCheckBox):
			propierty_env_widget.stateChanged.connect(self.set_env_value)
		self.__widget_by_propierty['env'] = propierty_env_widget
		propierty_geoid_widget = self.__widget.get_widget('geoid')
		if isinstance(propierty_geoid_widget, QSpinBox):
			propierty_geoid_widget.valueChanged.connect(self.set_geoid_value)
		elif isinstance(propierty_geoid_widget, QDoubleSpinBox):
			propierty_geoid_widget.valueChanged.connect(self.set_geoid_value)
		elif isinstance(propierty_geoid_widget, QComboBox):
			propierty_geoid_widget.currentIndexChanged.connect(self.set_geoid_value)
		elif isinstance(propierty_geoid_widget, QLineEdit):
			propierty_geoid_widget.editingFinished.connect(self.set_geoid_value)
			propierty_geoid_widget.textChanged.connect(self.set_geoid_value)
		elif isinstance(propierty_geoid_widget, QCheckBox):
			propierty_geoid_widget.stateChanged.connect(self.set_geoid_value)
		self.__widget_by_propierty['geoid'] = propierty_geoid_widget
