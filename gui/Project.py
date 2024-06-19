from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class Project:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'Proyecto'
		self.__text_by_propierty['label'] = 'Etiqueta'
		self.__widget_by_propierty['label'] = None
		self.__label = "Example project"
		self.__label_value = "Example project"
		self.__text_by_propierty['epsg'] = 'Código EPSG'
		self.__widget_by_propierty['epsg'] = None
		self.__epsg = "25830+5782"
		self.__epsg_value = "25830+5782"
		self.__text_by_propierty['path'] = 'Directorio de resultados'
		self.__widget_by_propierty['path'] = None
		self.__path = ""
		self.__path_value = ""
		self.__text_by_propierty['demgsd'] = 'GSD para MDT y MDS'
		self.__widget_by_propierty['demgsd'] = None
		self.__demgsd = 0.05
		self.__demgsd_value = 0.05
		self.__text_by_propierty['orthogsd'] = 'GSD para ortomosaico'
		self.__widget_by_propierty['orthogsd'] = None
		self.__orthogsd = 0.05
		self.__orthogsd_value = 0.05
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['Label'] = self.__label_value
		values['EPSG'] = self.__epsg_value
		values['Path'] = self.__path_value
		values['DemGSD'] = self.__demgsd_value
		values['OrthoGSD'] = self.__orthogsd_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def label(self):
		return self.__label

	@label.setter
	def label(self, value: 'widget:QLineEdit, toolTip:Etiqueta con la que se nombrarán los productos resultantes'):
		self.__label = value

	def set_label_value(self):
		propierty_label_widget = self.__widget_by_propierty['label'] 
		if isinstance(propierty_label_widget, QSpinBox):
			self.__label_value = propierty_label_widget.value()
		elif isinstance(propierty_label_widget, QDoubleSpinBox):
			self.__label_value = propierty_label_widget.value()
		elif isinstance(propierty_label_widget, QComboBox):
			self.__label_value = propierty_label_widget.currentText()
		elif isinstance(propierty_label_widget, QLineEdit):
			self.__label_value = propierty_label_widget.text()
		elif isinstance(propierty_label_widget, QCheckBox):
			self.__label_value = propierty_label_widget.isChecked()

	@property
	def epsg(self):
		return self.__epsg

	@epsg.setter
	def epsg(self, value: 'widget:QLineEdit, toolTip:Código EPSG con el que se exportarán los productos resultantes'):
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
	def path(self):
		return self.__path

	@path.setter
	def path(self, value: 'widget:file, type:folder, toolTip:Ruta del directorio de resultados'):
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
	def demgsd(self):
		return self.__demgsd

	@demgsd.setter
	def demgsd(self, value: 'widget:QDoubleSpinBox, decimals:2, minimum:0.0, maximum:2.0, singleStep:0.01, toolTip:Resolución en metros con la que se exportarán el modelo digital de superficies y del terreno (0 para máxima posible)'):
		self.__demgsd = value

	def set_demgsd_value(self):
		propierty_demgsd_widget = self.__widget_by_propierty['demgsd'] 
		if isinstance(propierty_demgsd_widget, QSpinBox):
			self.__demgsd_value = propierty_demgsd_widget.value()
		elif isinstance(propierty_demgsd_widget, QDoubleSpinBox):
			self.__demgsd_value = propierty_demgsd_widget.value()
		elif isinstance(propierty_demgsd_widget, QComboBox):
			self.__demgsd_value = propierty_demgsd_widget.currentText()
		elif isinstance(propierty_demgsd_widget, QLineEdit):
			self.__demgsd_value = propierty_demgsd_widget.text()
		elif isinstance(propierty_demgsd_widget, QCheckBox):
			self.__demgsd_value = propierty_demgsd_widget.isChecked()

	@property
	def orthogsd(self):
		return self.__orthogsd

	@orthogsd.setter
	def orthogsd(self, value: 'widget:QDoubleSpinBox, decimals:2, minimum:0.0, maximum:2.0, singleStep:0.01, toolTip:Resolución en metros con la que se exportará el ortomosaico (0 para máxima posible)'):
		self.__orthogsd = value

	def set_orthogsd_value(self):
		propierty_orthogsd_widget = self.__widget_by_propierty['orthogsd'] 
		if isinstance(propierty_orthogsd_widget, QSpinBox):
			self.__orthogsd_value = propierty_orthogsd_widget.value()
		elif isinstance(propierty_orthogsd_widget, QDoubleSpinBox):
			self.__orthogsd_value = propierty_orthogsd_widget.value()
		elif isinstance(propierty_orthogsd_widget, QComboBox):
			self.__orthogsd_value = propierty_orthogsd_widget.currentText()
		elif isinstance(propierty_orthogsd_widget, QLineEdit):
			self.__orthogsd_value = propierty_orthogsd_widget.text()
		elif isinstance(propierty_orthogsd_widget, QCheckBox):
			self.__orthogsd_value = propierty_orthogsd_widget.isChecked()

	def set_widget(self, widget):
		self.__widget = widget
		propierty_label_widget = self.__widget.get_widget('label')
		if isinstance(propierty_label_widget, QSpinBox):
			propierty_label_widget.valueChanged.connect(self.set_label_value)
		elif isinstance(propierty_label_widget, QDoubleSpinBox):
			propierty_label_widget.valueChanged.connect(self.set_label_value)
		elif isinstance(propierty_label_widget, QComboBox):
			propierty_label_widget.currentIndexChanged.connect(self.set_label_value)
		elif isinstance(propierty_label_widget, QLineEdit):
			propierty_label_widget.editingFinished.connect(self.set_label_value)
			propierty_label_widget.textChanged.connect(self.set_label_value)
		elif isinstance(propierty_label_widget, QCheckBox):
			propierty_label_widget.stateChanged.connect(self.set_label_value)
		self.__widget_by_propierty['label'] = propierty_label_widget
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
		propierty_demgsd_widget = self.__widget.get_widget('demgsd')
		if isinstance(propierty_demgsd_widget, QSpinBox):
			propierty_demgsd_widget.valueChanged.connect(self.set_demgsd_value)
		elif isinstance(propierty_demgsd_widget, QDoubleSpinBox):
			propierty_demgsd_widget.valueChanged.connect(self.set_demgsd_value)
		elif isinstance(propierty_demgsd_widget, QComboBox):
			propierty_demgsd_widget.currentIndexChanged.connect(self.set_demgsd_value)
		elif isinstance(propierty_demgsd_widget, QLineEdit):
			propierty_demgsd_widget.editingFinished.connect(self.set_demgsd_value)
			propierty_demgsd_widget.textChanged.connect(self.set_demgsd_value)
		elif isinstance(propierty_demgsd_widget, QCheckBox):
			propierty_demgsd_widget.stateChanged.connect(self.set_demgsd_value)
		self.__widget_by_propierty['demgsd'] = propierty_demgsd_widget
		propierty_orthogsd_widget = self.__widget.get_widget('orthogsd')
		if isinstance(propierty_orthogsd_widget, QSpinBox):
			propierty_orthogsd_widget.valueChanged.connect(self.set_orthogsd_value)
		elif isinstance(propierty_orthogsd_widget, QDoubleSpinBox):
			propierty_orthogsd_widget.valueChanged.connect(self.set_orthogsd_value)
		elif isinstance(propierty_orthogsd_widget, QComboBox):
			propierty_orthogsd_widget.currentIndexChanged.connect(self.set_orthogsd_value)
		elif isinstance(propierty_orthogsd_widget, QLineEdit):
			propierty_orthogsd_widget.editingFinished.connect(self.set_orthogsd_value)
			propierty_orthogsd_widget.textChanged.connect(self.set_orthogsd_value)
		elif isinstance(propierty_orthogsd_widget, QCheckBox):
			propierty_orthogsd_widget.stateChanged.connect(self.set_orthogsd_value)
		self.__widget_by_propierty['orthogsd'] = propierty_orthogsd_widget
