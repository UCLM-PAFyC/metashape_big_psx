from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class OptimizeAlignment:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Orientación', 'english': 'Optimize alignment'}
		self.__text = 'Orientación'
		self.__json_content_by_propierty['Method'] = {'text': {'spanish': 'Método de medida en las imágenes de los puntos de apoyo', 'english': 'Method for GCPs measurements in images'}, 'definition': {'spanish': 'Método de medida de los puntos de apoyo en las imágenes', 'english': 'Method for GCPs measurements in images'}, 'type': 'values', 'values': {'PSX': {'spanish': 'Medidas en la interfaz gráfica de Metashape', 'english': 'Measurements in Metashape GUI'}, 'XML': {'spanish': 'Medidas importadas de fichero markers XML de Metashape', 'english': 'Measurements imported from Metashape Markers XML file'}}, 'default': 'Medidas en la interfaz gráfica de Metashape'}
		self.__text_by_propierty['Method'] = 'Método de medida en las imágenes de los puntos de apoyo'
		self.__widget_by_propierty['Method'] = None
		self.__Method = ['Medidas en la interfaz gráfica de Metashape' ,'Medidas importadas de fichero markers XML de Metashape']
		self.__Method_value = 'Medidas en la interfaz gráfica de Metashape'
		self.__json_content_by_propierty['EPSG'] = {'text': {'spanish': 'Código EPSG', 'english': 'EPSG code'}, 'definition': {'spanish': 'Código EPSG de las coordenadas terreno de los puntos de apoyo', 'english': 'EPSG code for GCPs terrain coordinates'}, 'type': 'string', 'len': 11, 'default': '25830+5782'}
		self.__text_by_propierty['EPSG'] = 'Código EPSG'
		self.__widget_by_propierty['EPSG'] = None
		self.__EPSG = "25830+5782"
		self.__EPSG_value = "25830+5782"
		self.__json_content_by_propierty['Path'] = {'text': {'spanish': 'Fichero de puntos de apoyo', 'english': 'GCPs file'}, 'definition': {'spanish': 'Archivo de puntos de apoyo', 'english': 'GCPs file'}, 'type': 'file open', 'formats': '*.txt *.csv', 'default': ''}
		self.__text_by_propierty['Path'] = 'Fichero de puntos de apoyo'
		self.__widget_by_propierty['Path'] = None
		self.__Path = ""
		self.__Path_value = ""
		self.__json_content_by_propierty['Accuracy'] = {'text': {'spanish': 'Precisión', 'english': 'Accuracy'}, 'definition': {'spanish': 'Precisión establecida para el alineamiento', 'english': 'Accuracy for aligment'}, 'type': 'values', 'values': {'Highest': {'spanish': 'Mayor posible', 'english': 'Highest'}, 'High': {'spanish': 'Alto', 'english': 'High'}, 'Medium': {'spanish': 'Medio', 'english': 'Medium'}, 'Low': {'spanish': 'Bajo', 'english': 'Low'}, 'Lowest': {'spanish': 'Menor posible', 'english': 'Lowest'}}, 'default': 'Mayor posible'}
		self.__text_by_propierty['Accuracy'] = 'Precisión'
		self.__widget_by_propierty['Accuracy'] = None
		self.__Accuracy = ['Mayor posible' ,'Alto' ,'Medio' ,'Bajo' ,'Menor posible']
		self.__Accuracy_value = 'Mayor posible'
		self.__json_content_by_propierty['ReferencePreselection'] = {'text': {'spanish': 'Preselección', 'english': 'Preselection'}, 'definition': {'spanish': 'Método de preselección de imágenes según su localización', 'english': 'Method for preselection of images based in their positions'}, 'type': 'values', 'values': {'False': {'spanish': 'Sin localización', 'english': 'Generic without position'}, 'Source': {'spanish': 'Con localización de origen (importada desde EXIF o CSV)', 'english': 'From imported position (CSV or EXIF)'}, 'Estimated': {'spanish': 'Con localización estimada', 'english': 'From estimated position'}, 'Sequential': {'spanish': 'Con imágenes consecutivas', 'english': 'From consecutive images'}}, 'default': 'Con localización de origen (importada desde EXIF o CSV)'}
		self.__text_by_propierty['ReferencePreselection'] = 'Preselección'
		self.__widget_by_propierty['ReferencePreselection'] = None
		self.__ReferencePreselection = ['Con localización de origen (importada desde EXIF o CSV)' ,'Sin localización' ,'Con localización estimada' ,'Con imágenes consecutivas']
		self.__ReferencePreselection_value = 'Con localización de origen (importada desde EXIF o CSV)'
		self.__json_content_by_propierty['TiePointLimit'] = {'text': {'spanish': 'Límite', 'english': 'Limit'}, 'definition': {'spanish': 'Límite de puntos de enlace', 'english': 'Tie points limit'}, 'type': 'integer', 'minimum': 1000, 'maximum': 100000, 'singleStep': 1000, 'default': 4000}
		self.__text_by_propierty['TiePointLimit'] = 'Límite'
		self.__widget_by_propierty['TiePointLimit'] = None
		self.__TiePointLimit = 4000
		self.__TiePointLimit_value = 4000
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['Method'] = self.__Method_value
		values['EPSG'] = self.__EPSG_value
		values['Path'] = self.__Path_value
		values['Accuracy'] = self.__Accuracy_value
		values['ReferencePreselection'] = self.__ReferencePreselection_value
		values['TiePointLimit'] = self.__TiePointLimit_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def Method(self):
		return self.__Method

	@Method.setter
	def Method(self, value: 'widget:QComboBox, toolTip:Método de medida de los puntos de apoyo en las imágenes'):
		self.__Method = value

	def set_Method_value(self):
		propierty_Method_widget = self.__widget_by_propierty['Method'] 
		if isinstance(propierty_Method_widget, QSpinBox):
			self.__Method_value = propierty_Method_widget.value()
		elif isinstance(propierty_Method_widget, QDoubleSpinBox):
			self.__Method_value = propierty_Method_widget.value()
		elif isinstance(propierty_Method_widget, QComboBox):
			self.__Method_value = propierty_Method_widget.currentText()
		elif isinstance(propierty_Method_widget, QLineEdit):
			self.__Method_value = propierty_Method_widget.text()
		elif isinstance(propierty_Method_widget, QCheckBox):
			self.__Method_value = propierty_Method_widget.isChecked()

	@property
	def EPSG(self):
		return self.__EPSG

	@EPSG.setter
	def EPSG(self, value: 'widget:QLineEdit, toolTip:Código EPSG de las coordenadas terreno de los puntos de apoyo'):
		self.__EPSG = value

	def set_EPSG_value(self):
		propierty_EPSG_widget = self.__widget_by_propierty['EPSG'] 
		if isinstance(propierty_EPSG_widget, QSpinBox):
			self.__EPSG_value = propierty_EPSG_widget.value()
		elif isinstance(propierty_EPSG_widget, QDoubleSpinBox):
			self.__EPSG_value = propierty_EPSG_widget.value()
		elif isinstance(propierty_EPSG_widget, QComboBox):
			self.__EPSG_value = propierty_EPSG_widget.currentText()
		elif isinstance(propierty_EPSG_widget, QLineEdit):
			self.__EPSG_value = propierty_EPSG_widget.text()
		elif isinstance(propierty_EPSG_widget, QCheckBox):
			self.__EPSG_value = propierty_EPSG_widget.isChecked()

	@property
	def Path(self):
		return self.__Path

	@Path.setter
	def Path(self, value: 'widget:file, toolTip:Archivo de puntos de apoyo, filters: *.txt *.csv'):
		self.__Path = value

	def set_Path_value(self):
		propierty_Path_widget = self.__widget_by_propierty['Path'] 
		if isinstance(propierty_Path_widget, QSpinBox):
			self.__Path_value = propierty_Path_widget.value()
		elif isinstance(propierty_Path_widget, QDoubleSpinBox):
			self.__Path_value = propierty_Path_widget.value()
		elif isinstance(propierty_Path_widget, QComboBox):
			self.__Path_value = propierty_Path_widget.currentText()
		elif isinstance(propierty_Path_widget, QLineEdit):
			self.__Path_value = propierty_Path_widget.text()
		elif isinstance(propierty_Path_widget, QCheckBox):
			self.__Path_value = propierty_Path_widget.isChecked()

	@property
	def Accuracy(self):
		return self.__Accuracy

	@Accuracy.setter
	def Accuracy(self, value: 'widget:QComboBox, toolTip:Precisión establecida para el alineamiento'):
		self.__Accuracy = value

	def set_Accuracy_value(self):
		propierty_Accuracy_widget = self.__widget_by_propierty['Accuracy'] 
		if isinstance(propierty_Accuracy_widget, QSpinBox):
			self.__Accuracy_value = propierty_Accuracy_widget.value()
		elif isinstance(propierty_Accuracy_widget, QDoubleSpinBox):
			self.__Accuracy_value = propierty_Accuracy_widget.value()
		elif isinstance(propierty_Accuracy_widget, QComboBox):
			self.__Accuracy_value = propierty_Accuracy_widget.currentText()
		elif isinstance(propierty_Accuracy_widget, QLineEdit):
			self.__Accuracy_value = propierty_Accuracy_widget.text()
		elif isinstance(propierty_Accuracy_widget, QCheckBox):
			self.__Accuracy_value = propierty_Accuracy_widget.isChecked()

	@property
	def ReferencePreselection(self):
		return self.__ReferencePreselection

	@ReferencePreselection.setter
	def ReferencePreselection(self, value: 'widget:QComboBox, toolTip:Método de preselección de imágenes según su localización'):
		self.__ReferencePreselection = value

	def set_ReferencePreselection_value(self):
		propierty_ReferencePreselection_widget = self.__widget_by_propierty['ReferencePreselection'] 
		if isinstance(propierty_ReferencePreselection_widget, QSpinBox):
			self.__ReferencePreselection_value = propierty_ReferencePreselection_widget.value()
		elif isinstance(propierty_ReferencePreselection_widget, QDoubleSpinBox):
			self.__ReferencePreselection_value = propierty_ReferencePreselection_widget.value()
		elif isinstance(propierty_ReferencePreselection_widget, QComboBox):
			self.__ReferencePreselection_value = propierty_ReferencePreselection_widget.currentText()
		elif isinstance(propierty_ReferencePreselection_widget, QLineEdit):
			self.__ReferencePreselection_value = propierty_ReferencePreselection_widget.text()
		elif isinstance(propierty_ReferencePreselection_widget, QCheckBox):
			self.__ReferencePreselection_value = propierty_ReferencePreselection_widget.isChecked()

	@property
	def TiePointLimit(self):
		return self.__TiePointLimit

	@TiePointLimit.setter
	def TiePointLimit(self, value: 'widget:QSpinBox, minimum:1000, maximum:100000, singleStep:1000, toolTip:Límite de puntos de enlace'):
		self.__TiePointLimit = value

	def set_TiePointLimit_value(self):
		propierty_TiePointLimit_widget = self.__widget_by_propierty['TiePointLimit'] 
		if isinstance(propierty_TiePointLimit_widget, QSpinBox):
			self.__TiePointLimit_value = propierty_TiePointLimit_widget.value()
		elif isinstance(propierty_TiePointLimit_widget, QDoubleSpinBox):
			self.__TiePointLimit_value = propierty_TiePointLimit_widget.value()
		elif isinstance(propierty_TiePointLimit_widget, QComboBox):
			self.__TiePointLimit_value = propierty_TiePointLimit_widget.currentText()
		elif isinstance(propierty_TiePointLimit_widget, QLineEdit):
			self.__TiePointLimit_value = propierty_TiePointLimit_widget.text()
		elif isinstance(propierty_TiePointLimit_widget, QCheckBox):
			self.__TiePointLimit_value = propierty_TiePointLimit_widget.isChecked()

	def set_values_from_dictionary(self, values):
		for value in values:
			propierty_widget = self.__widget_by_propierty[value]
			if isinstance(propierty_widget, QComboBox):
				json_values = self.__json_content_by_propierty[value][gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG]
				if values[value] in json_values:
					for language in json_values[values[value]]:
						value_language = json_values[values[value]][language]
						pos = propierty_widget.findText(value_language)
						if pos != -1:
							propierty_widget.setCurrentIndex(pos)
							break
				#pos = propierty_widget.findText(values[value])
				#if pos != -1:
					#propierty_widget.setCurrentIndex(pos)
				#else:
					#json_values = self.__json_content_by_propierty[value][gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG]
					#for json_value in json_values:
						#find_value = False
						#for language in json_values[json_value]:
							#value_language = json_values[json_value][language]
							#if pos == -1:
								#pos = propierty_widget.findText(value_language)
							#if value_language == values[value]:
								#find_value = True
						#if find_value and pos != -1:
							#propierty_widget.setCurrentIndex(pos)
							#break
		self.__Method_value = values['Method']
		self.__EPSG_value = values['EPSG']
		self.__EPSG = values['EPSG']
		self.__Path_value = values['Path']
		self.__Path = values['Path']
		self.__Accuracy_value = values['Accuracy']
		self.__ReferencePreselection_value = values['ReferencePreselection']
		self.__TiePointLimit_value = values['TiePointLimit']
		self.__TiePointLimit = values['TiePointLimit']
		return

	def set_widget(self, widget):
		self.__widget = widget
		propierty_Method_widget = self.__widget.get_widget('Method')
		if isinstance(propierty_Method_widget, QSpinBox):
			propierty_Method_widget.valueChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QDoubleSpinBox):
			propierty_Method_widget.valueChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QComboBox):
			propierty_Method_widget.currentIndexChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QLineEdit):
			propierty_Method_widget.editingFinished.connect(self.set_Method_value)
			propierty_Method_widget.textChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QCheckBox):
			propierty_Method_widget.stateChanged.connect(self.set_Method_value)
		self.__widget_by_propierty['Method'] = propierty_Method_widget
		propierty_EPSG_widget = self.__widget.get_widget('EPSG')
		if isinstance(propierty_EPSG_widget, QSpinBox):
			propierty_EPSG_widget.valueChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QDoubleSpinBox):
			propierty_EPSG_widget.valueChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QComboBox):
			propierty_EPSG_widget.currentIndexChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QLineEdit):
			propierty_EPSG_widget.editingFinished.connect(self.set_EPSG_value)
			propierty_EPSG_widget.textChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QCheckBox):
			propierty_EPSG_widget.stateChanged.connect(self.set_EPSG_value)
		self.__widget_by_propierty['EPSG'] = propierty_EPSG_widget
		propierty_Path_widget = self.__widget.get_widget('Path')
		if isinstance(propierty_Path_widget, QSpinBox):
			propierty_Path_widget.valueChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QDoubleSpinBox):
			propierty_Path_widget.valueChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QComboBox):
			propierty_Path_widget.currentIndexChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QLineEdit):
			propierty_Path_widget.editingFinished.connect(self.set_Path_value)
			propierty_Path_widget.textChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QCheckBox):
			propierty_Path_widget.stateChanged.connect(self.set_Path_value)
		self.__widget_by_propierty['Path'] = propierty_Path_widget
		propierty_Accuracy_widget = self.__widget.get_widget('Accuracy')
		if isinstance(propierty_Accuracy_widget, QSpinBox):
			propierty_Accuracy_widget.valueChanged.connect(self.set_Accuracy_value)
		elif isinstance(propierty_Accuracy_widget, QDoubleSpinBox):
			propierty_Accuracy_widget.valueChanged.connect(self.set_Accuracy_value)
		elif isinstance(propierty_Accuracy_widget, QComboBox):
			propierty_Accuracy_widget.currentIndexChanged.connect(self.set_Accuracy_value)
		elif isinstance(propierty_Accuracy_widget, QLineEdit):
			propierty_Accuracy_widget.editingFinished.connect(self.set_Accuracy_value)
			propierty_Accuracy_widget.textChanged.connect(self.set_Accuracy_value)
		elif isinstance(propierty_Accuracy_widget, QCheckBox):
			propierty_Accuracy_widget.stateChanged.connect(self.set_Accuracy_value)
		self.__widget_by_propierty['Accuracy'] = propierty_Accuracy_widget
		propierty_ReferencePreselection_widget = self.__widget.get_widget('ReferencePreselection')
		if isinstance(propierty_ReferencePreselection_widget, QSpinBox):
			propierty_ReferencePreselection_widget.valueChanged.connect(self.set_ReferencePreselection_value)
		elif isinstance(propierty_ReferencePreselection_widget, QDoubleSpinBox):
			propierty_ReferencePreselection_widget.valueChanged.connect(self.set_ReferencePreselection_value)
		elif isinstance(propierty_ReferencePreselection_widget, QComboBox):
			propierty_ReferencePreselection_widget.currentIndexChanged.connect(self.set_ReferencePreselection_value)
		elif isinstance(propierty_ReferencePreselection_widget, QLineEdit):
			propierty_ReferencePreselection_widget.editingFinished.connect(self.set_ReferencePreselection_value)
			propierty_ReferencePreselection_widget.textChanged.connect(self.set_ReferencePreselection_value)
		elif isinstance(propierty_ReferencePreselection_widget, QCheckBox):
			propierty_ReferencePreselection_widget.stateChanged.connect(self.set_ReferencePreselection_value)
		self.__widget_by_propierty['ReferencePreselection'] = propierty_ReferencePreselection_widget
		propierty_TiePointLimit_widget = self.__widget.get_widget('TiePointLimit')
		if isinstance(propierty_TiePointLimit_widget, QSpinBox):
			propierty_TiePointLimit_widget.valueChanged.connect(self.set_TiePointLimit_value)
		elif isinstance(propierty_TiePointLimit_widget, QDoubleSpinBox):
			propierty_TiePointLimit_widget.valueChanged.connect(self.set_TiePointLimit_value)
		elif isinstance(propierty_TiePointLimit_widget, QComboBox):
			propierty_TiePointLimit_widget.currentIndexChanged.connect(self.set_TiePointLimit_value)
		elif isinstance(propierty_TiePointLimit_widget, QLineEdit):
			propierty_TiePointLimit_widget.editingFinished.connect(self.set_TiePointLimit_value)
			propierty_TiePointLimit_widget.textChanged.connect(self.set_TiePointLimit_value)
		elif isinstance(propierty_TiePointLimit_widget, QCheckBox):
			propierty_TiePointLimit_widget.stateChanged.connect(self.set_TiePointLimit_value)
		self.__widget_by_propierty['TiePointLimit'] = propierty_TiePointLimit_widget
