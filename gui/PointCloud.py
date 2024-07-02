from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class PointCloud:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'Nube de puntos'
		self.__text_by_propierty['quality'] = 'Densidad '
		self.__widget_by_propierty['quality'] = None
		self.__quality = ['Mayor posible' ,' Alto' ,' Medio' ,' Bajo' ,' Menor posible']
		self.__quality_value = 'Mayor posible'
		self.__text_by_propierty['filtermode'] = 'Tipo de filtrado'
		self.__widget_by_propierty['filtermode'] = None
		self.__filtermode = ['Agresivo' ,' Falso' ,' Medio' ,' Moderado']
		self.__filtermode_value = 'Agresivo'
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['Quality'] = self.__quality_value
		values['FilterMode'] = self.__filtermode_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def quality(self):
		return self.__quality

	@quality.setter
	def quality(self, value: 'widget:QComboBox, toolTip:Calidad final de la nube de puntos densa'):
		self.__quality = value

	def set_quality_value(self):
		propierty_quality_widget = self.__widget_by_propierty['quality'] 
		if isinstance(propierty_quality_widget, QSpinBox):
			self.__quality_value = propierty_quality_widget.value()
		elif isinstance(propierty_quality_widget, QDoubleSpinBox):
			self.__quality_value = propierty_quality_widget.value()
		elif isinstance(propierty_quality_widget, QComboBox):
			self.__quality_value = propierty_quality_widget.currentText()
		elif isinstance(propierty_quality_widget, QLineEdit):
			self.__quality_value = propierty_quality_widget.text()
		elif isinstance(propierty_quality_widget, QCheckBox):
			self.__quality_value = propierty_quality_widget.isChecked()

	@property
	def filtermode(self):
		return self.__filtermode

	@filtermode.setter
	def filtermode(self, value: 'widget:QComboBox, toolTip:Tipo de filtrado'):
		self.__filtermode = value

	def set_filtermode_value(self):
		propierty_filtermode_widget = self.__widget_by_propierty['filtermode'] 
		if isinstance(propierty_filtermode_widget, QSpinBox):
			self.__filtermode_value = propierty_filtermode_widget.value()
		elif isinstance(propierty_filtermode_widget, QDoubleSpinBox):
			self.__filtermode_value = propierty_filtermode_widget.value()
		elif isinstance(propierty_filtermode_widget, QComboBox):
			self.__filtermode_value = propierty_filtermode_widget.currentText()
		elif isinstance(propierty_filtermode_widget, QLineEdit):
			self.__filtermode_value = propierty_filtermode_widget.text()
		elif isinstance(propierty_filtermode_widget, QCheckBox):
			self.__filtermode_value = propierty_filtermode_widget.isChecked()

	def set_widget(self, widget):
		self.__widget = widget
		propierty_quality_widget = self.__widget.get_widget('quality')
		if isinstance(propierty_quality_widget, QSpinBox):
			propierty_quality_widget.valueChanged.connect(self.set_quality_value)
		elif isinstance(propierty_quality_widget, QDoubleSpinBox):
			propierty_quality_widget.valueChanged.connect(self.set_quality_value)
		elif isinstance(propierty_quality_widget, QComboBox):
			propierty_quality_widget.currentIndexChanged.connect(self.set_quality_value)
		elif isinstance(propierty_quality_widget, QLineEdit):
			propierty_quality_widget.editingFinished.connect(self.set_quality_value)
			propierty_quality_widget.textChanged.connect(self.set_quality_value)
		elif isinstance(propierty_quality_widget, QCheckBox):
			propierty_quality_widget.stateChanged.connect(self.set_quality_value)
		self.__widget_by_propierty['quality'] = propierty_quality_widget
		propierty_filtermode_widget = self.__widget.get_widget('filtermode')
		if isinstance(propierty_filtermode_widget, QSpinBox):
			propierty_filtermode_widget.valueChanged.connect(self.set_filtermode_value)
		elif isinstance(propierty_filtermode_widget, QDoubleSpinBox):
			propierty_filtermode_widget.valueChanged.connect(self.set_filtermode_value)
		elif isinstance(propierty_filtermode_widget, QComboBox):
			propierty_filtermode_widget.currentIndexChanged.connect(self.set_filtermode_value)
		elif isinstance(propierty_filtermode_widget, QLineEdit):
			propierty_filtermode_widget.editingFinished.connect(self.set_filtermode_value)
			propierty_filtermode_widget.textChanged.connect(self.set_filtermode_value)
		elif isinstance(propierty_filtermode_widget, QCheckBox):
			propierty_filtermode_widget.stateChanged.connect(self.set_filtermode_value)
		self.__widget_by_propierty['filtermode'] = propierty_filtermode_widget
