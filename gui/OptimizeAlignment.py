from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class OptimizeAlignment:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'Orientación'
		self.__text_by_propierty['method'] = 'Método de medida en las imágenes de los puntos de apoyo'
		self.__widget_by_propierty['method'] = None
		self.__method = ['Medidas en la interfaz gráfica de Metashape' ,' Medidas importadas de fichero markers XML de Metashape']
		self.__method_value = 'Medidas en la interfaz gráfica de Metashape'
		self.__text_by_propierty['epsg'] = 'Código EPSG'
		self.__widget_by_propierty['epsg'] = None
		self.__epsg = "25830+5782"
		self.__epsg_value = "25830+5782"
		self.__text_by_propierty['path'] = 'Fichero de puntos de apoyo'
		self.__widget_by_propierty['path'] = None
		self.__path = ""
		self.__path_value = ""
		self.__text_by_propierty['accuracy'] = 'Precisión'
		self.__widget_by_propierty['accuracy'] = None
		self.__accuracy = ['Mayor posible' ,' Alto' ,' Medio' ,' Bajo' ,' Menor posible']
		self.__accuracy_value = 'Mayor posible'
		self.__text_by_propierty['referencepreselection'] = 'Preselección'
		self.__widget_by_propierty['referencepreselection'] = None
		self.__referencepreselection = ['Con localización de origen (importada desde EXIF o CSV)' ,' Sin localización' ,' Con localización estimada' ,' Con imágenes consecutivas']
		self.__referencepreselection_value = 'Con localización de origen (importada desde EXIF o CSV)'
		self.__text_by_propierty['tiepointlimit'] = 'Límite'
		self.__widget_by_propierty['tiepointlimit'] = None
		self.__tiepointlimit = 4000
		self.__tiepointlimit_value = 4000
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['Method'] = self.__method_value
		values['EPSG'] = self.__epsg_value
		values['Path'] = self.__path_value
		values['Accuracy'] = self.__accuracy_value
		values['ReferencePreselection'] = self.__referencepreselection_value
		values['TiePointLimit'] = self.__tiepointlimit_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def method(self):
		return self.__method

	@method.setter
	def method(self, value: 'widget:QComboBox, toolTip:Método de medida de los puntos de apoyo en las imágenes'):
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
	def epsg(self, value: 'widget:QLineEdit, toolTip:Código EPSG de las coordenadas terreno de los puntos de apoyo'):
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
	def path(self, value: 'widget:file, toolTip:Archivo de puntos de apoyo, filters: *.txt *.csv'):
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
	def accuracy(self):
		return self.__accuracy

	@accuracy.setter
	def accuracy(self, value: 'widget:QComboBox, toolTip:Precisión establecida para el alineamiento'):
		self.__accuracy = value

	def set_accuracy_value(self):
		propierty_accuracy_widget = self.__widget_by_propierty['accuracy'] 
		if isinstance(propierty_accuracy_widget, QSpinBox):
			self.__accuracy_value = propierty_accuracy_widget.value()
		elif isinstance(propierty_accuracy_widget, QDoubleSpinBox):
			self.__accuracy_value = propierty_accuracy_widget.value()
		elif isinstance(propierty_accuracy_widget, QComboBox):
			self.__accuracy_value = propierty_accuracy_widget.currentText()
		elif isinstance(propierty_accuracy_widget, QLineEdit):
			self.__accuracy_value = propierty_accuracy_widget.text()
		elif isinstance(propierty_accuracy_widget, QCheckBox):
			self.__accuracy_value = propierty_accuracy_widget.isChecked()

	@property
	def referencepreselection(self):
		return self.__referencepreselection

	@referencepreselection.setter
	def referencepreselection(self, value: 'widget:QComboBox, toolTip:Método de preselección de imágenes según su localización'):
		self.__referencepreselection = value

	def set_referencepreselection_value(self):
		propierty_referencepreselection_widget = self.__widget_by_propierty['referencepreselection'] 
		if isinstance(propierty_referencepreselection_widget, QSpinBox):
			self.__referencepreselection_value = propierty_referencepreselection_widget.value()
		elif isinstance(propierty_referencepreselection_widget, QDoubleSpinBox):
			self.__referencepreselection_value = propierty_referencepreselection_widget.value()
		elif isinstance(propierty_referencepreselection_widget, QComboBox):
			self.__referencepreselection_value = propierty_referencepreselection_widget.currentText()
		elif isinstance(propierty_referencepreselection_widget, QLineEdit):
			self.__referencepreselection_value = propierty_referencepreselection_widget.text()
		elif isinstance(propierty_referencepreselection_widget, QCheckBox):
			self.__referencepreselection_value = propierty_referencepreselection_widget.isChecked()

	@property
	def tiepointlimit(self):
		return self.__tiepointlimit

	@tiepointlimit.setter
	def tiepointlimit(self, value: 'widget:QSpinBox, minimum:1000, maximum:100000, singleStep:1000, toolTip:Límite de puntos de enlace'):
		self.__tiepointlimit = value

	def set_tiepointlimit_value(self):
		propierty_tiepointlimit_widget = self.__widget_by_propierty['tiepointlimit'] 
		if isinstance(propierty_tiepointlimit_widget, QSpinBox):
			self.__tiepointlimit_value = propierty_tiepointlimit_widget.value()
		elif isinstance(propierty_tiepointlimit_widget, QDoubleSpinBox):
			self.__tiepointlimit_value = propierty_tiepointlimit_widget.value()
		elif isinstance(propierty_tiepointlimit_widget, QComboBox):
			self.__tiepointlimit_value = propierty_tiepointlimit_widget.currentText()
		elif isinstance(propierty_tiepointlimit_widget, QLineEdit):
			self.__tiepointlimit_value = propierty_tiepointlimit_widget.text()
		elif isinstance(propierty_tiepointlimit_widget, QCheckBox):
			self.__tiepointlimit_value = propierty_tiepointlimit_widget.isChecked()

	def set_widget(self, widget):
		self.__widget = widget
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
		propierty_accuracy_widget = self.__widget.get_widget('accuracy')
		if isinstance(propierty_accuracy_widget, QSpinBox):
			propierty_accuracy_widget.valueChanged.connect(self.set_accuracy_value)
		elif isinstance(propierty_accuracy_widget, QDoubleSpinBox):
			propierty_accuracy_widget.valueChanged.connect(self.set_accuracy_value)
		elif isinstance(propierty_accuracy_widget, QComboBox):
			propierty_accuracy_widget.currentIndexChanged.connect(self.set_accuracy_value)
		elif isinstance(propierty_accuracy_widget, QLineEdit):
			propierty_accuracy_widget.editingFinished.connect(self.set_accuracy_value)
			propierty_accuracy_widget.textChanged.connect(self.set_accuracy_value)
		elif isinstance(propierty_accuracy_widget, QCheckBox):
			propierty_accuracy_widget.stateChanged.connect(self.set_accuracy_value)
		self.__widget_by_propierty['accuracy'] = propierty_accuracy_widget
		propierty_referencepreselection_widget = self.__widget.get_widget('referencepreselection')
		if isinstance(propierty_referencepreselection_widget, QSpinBox):
			propierty_referencepreselection_widget.valueChanged.connect(self.set_referencepreselection_value)
		elif isinstance(propierty_referencepreselection_widget, QDoubleSpinBox):
			propierty_referencepreselection_widget.valueChanged.connect(self.set_referencepreselection_value)
		elif isinstance(propierty_referencepreselection_widget, QComboBox):
			propierty_referencepreselection_widget.currentIndexChanged.connect(self.set_referencepreselection_value)
		elif isinstance(propierty_referencepreselection_widget, QLineEdit):
			propierty_referencepreselection_widget.editingFinished.connect(self.set_referencepreselection_value)
			propierty_referencepreselection_widget.textChanged.connect(self.set_referencepreselection_value)
		elif isinstance(propierty_referencepreselection_widget, QCheckBox):
			propierty_referencepreselection_widget.stateChanged.connect(self.set_referencepreselection_value)
		self.__widget_by_propierty['referencepreselection'] = propierty_referencepreselection_widget
		propierty_tiepointlimit_widget = self.__widget.get_widget('tiepointlimit')
		if isinstance(propierty_tiepointlimit_widget, QSpinBox):
			propierty_tiepointlimit_widget.valueChanged.connect(self.set_tiepointlimit_value)
		elif isinstance(propierty_tiepointlimit_widget, QDoubleSpinBox):
			propierty_tiepointlimit_widget.valueChanged.connect(self.set_tiepointlimit_value)
		elif isinstance(propierty_tiepointlimit_widget, QComboBox):
			propierty_tiepointlimit_widget.currentIndexChanged.connect(self.set_tiepointlimit_value)
		elif isinstance(propierty_tiepointlimit_widget, QLineEdit):
			propierty_tiepointlimit_widget.editingFinished.connect(self.set_tiepointlimit_value)
			propierty_tiepointlimit_widget.textChanged.connect(self.set_tiepointlimit_value)
		elif isinstance(propierty_tiepointlimit_widget, QCheckBox):
			propierty_tiepointlimit_widget.stateChanged.connect(self.set_tiepointlimit_value)
		self.__widget_by_propierty['tiepointlimit'] = propierty_tiepointlimit_widget
