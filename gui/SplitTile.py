from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class SplitTile:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__text = 'División en celdas'
		self.__text_by_propierty['tilesize'] = 'Tamaño de la celda'
		self.__widget_by_propierty['tilesize'] = None
		self.__tilesize = 50
		self.__tilesize_value = 50
		self.__text_by_propierty['tilesizebuffer'] = 'Ampliación'
		self.__widget_by_propierty['tilesizebuffer'] = None
		self.__tilesizebuffer = 5
		self.__tilesizebuffer_value = 5
		self.__text_by_propierty['method'] = 'Definición de la malla de celdas a procesar'
		self.__widget_by_propierty['method'] = None
		self.__method = ['Malla editada por el usuario' ,' Automático para toda la ROI o zona estereoscópica']
		self.__method_value = 'Malla editada por el usuario'
		self.__text_by_propierty['path'] = 'Fichero de la malla'
		self.__widget_by_propierty['path'] = None
		self.__path = ""
		self.__path_value = ""
		self.__text_by_propierty['mergemethod'] = 'Método de unión'
		self.__widget_by_propierty['mergemethod'] = None
		self.__mergemethod = ['OSGeo (ráster) y laspy (nubes de puntos)' ,' Metashape']
		self.__mergemethod_value = 'OSGeo (ráster) y laspy (nubes de puntos)'
		self.__text_by_propierty['mergepointclouds'] = 'Unir nubes de puntos'
		self.__widget_by_propierty['mergepointclouds'] = None
		self.__mergepointclouds = True
		self.__mergepointclouds_value = True
		self.__text_by_propierty['mergeelevations'] = 'Unir MDEs'
		self.__widget_by_propierty['mergeelevations'] = None
		self.__mergeelevations = True
		self.__mergeelevations_value = True
		self.__text_by_propierty['mergeorthomosaics'] = 'Unir ortomosaicos'
		self.__widget_by_propierty['mergeorthomosaics'] = None
		self.__mergeorthomosaics = True
		self.__mergeorthomosaics_value = True
		self.__text_by_propierty['mergeddem'] = 'Tipo de MDE a unir'
		self.__widget_by_propierty['mergeddem'] = None
		self.__mergeddem = ['Modelo Digital de Superficies (MDS)' ,' Modelo Digital del Terreno (MDT)']
		self.__mergeddem_value = 'Modelo Digital de Superficies (MDS)'
		self.__widget = None

	def get_values_as_dictionary(self):
		values = {}
		values['TileSize'] = self.__tilesize_value
		values['TileSizeBuffer'] = self.__tilesizebuffer_value
		values['Method'] = self.__method_value
		values['Path'] = self.__path_value
		values['MergeMethod'] = self.__mergemethod_value
		values['MergePointClouds'] = self.__mergepointclouds_value
		values['MergeElevations'] = self.__mergeelevations_value
		values['MergeOrthomosaics'] = self.__mergeorthomosaics_value
		values['MergedDEM'] = self.__mergeddem_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def tilesize(self):
		return self.__tilesize

	@tilesize.setter
	def tilesize(self, value: 'widget:QSpinBox, minimum:10, maximum:1000, singleStep:10, toolTip:Tamaño de las celdas en metros (ej. 50)'):
		self.__tilesize = value

	def set_tilesize_value(self):
		propierty_tilesize_widget = self.__widget_by_propierty['tilesize'] 
		if isinstance(propierty_tilesize_widget, QSpinBox):
			self.__tilesize_value = propierty_tilesize_widget.value()
		elif isinstance(propierty_tilesize_widget, QDoubleSpinBox):
			self.__tilesize_value = propierty_tilesize_widget.value()
		elif isinstance(propierty_tilesize_widget, QComboBox):
			self.__tilesize_value = propierty_tilesize_widget.currentText()
		elif isinstance(propierty_tilesize_widget, QLineEdit):
			self.__tilesize_value = propierty_tilesize_widget.text()
		elif isinstance(propierty_tilesize_widget, QCheckBox):
			self.__tilesize_value = propierty_tilesize_widget.isChecked()

	@property
	def tilesizebuffer(self):
		return self.__tilesizebuffer

	@tilesizebuffer.setter
	def tilesizebuffer(self, value: 'widget:QSpinBox, minimum:1, maximum:100, singleStep:1, toolTip:Porcentaje de solape entre celdas (ej. 5)'):
		self.__tilesizebuffer = value

	def set_tilesizebuffer_value(self):
		propierty_tilesizebuffer_widget = self.__widget_by_propierty['tilesizebuffer'] 
		if isinstance(propierty_tilesizebuffer_widget, QSpinBox):
			self.__tilesizebuffer_value = propierty_tilesizebuffer_widget.value()
		elif isinstance(propierty_tilesizebuffer_widget, QDoubleSpinBox):
			self.__tilesizebuffer_value = propierty_tilesizebuffer_widget.value()
		elif isinstance(propierty_tilesizebuffer_widget, QComboBox):
			self.__tilesizebuffer_value = propierty_tilesizebuffer_widget.currentText()
		elif isinstance(propierty_tilesizebuffer_widget, QLineEdit):
			self.__tilesizebuffer_value = propierty_tilesizebuffer_widget.text()
		elif isinstance(propierty_tilesizebuffer_widget, QCheckBox):
			self.__tilesizebuffer_value = propierty_tilesizebuffer_widget.isChecked()

	@property
	def method(self):
		return self.__method

	@method.setter
	def method(self, value: 'widget:QComboBox, toolTip:Definición de la malla de celdas a procesar'):
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
	def path(self):
		return self.__path

	@path.setter
	def path(self, value: 'widget:file, toolTip:Fichero de la malla editado por el usario, filters: *.gpkg'):
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
	def mergemethod(self):
		return self.__mergemethod

	@mergemethod.setter
	def mergemethod(self, value: 'widget:QComboBox, toolTip:Estrategia de unión de los productos resultantes'):
		self.__mergemethod = value

	def set_mergemethod_value(self):
		propierty_mergemethod_widget = self.__widget_by_propierty['mergemethod'] 
		if isinstance(propierty_mergemethod_widget, QSpinBox):
			self.__mergemethod_value = propierty_mergemethod_widget.value()
		elif isinstance(propierty_mergemethod_widget, QDoubleSpinBox):
			self.__mergemethod_value = propierty_mergemethod_widget.value()
		elif isinstance(propierty_mergemethod_widget, QComboBox):
			self.__mergemethod_value = propierty_mergemethod_widget.currentText()
		elif isinstance(propierty_mergemethod_widget, QLineEdit):
			self.__mergemethod_value = propierty_mergemethod_widget.text()
		elif isinstance(propierty_mergemethod_widget, QCheckBox):
			self.__mergemethod_value = propierty_mergemethod_widget.isChecked()

	@property
	def mergepointclouds(self):
		return self.__mergepointclouds

	@mergepointclouds.setter
	def mergepointclouds(self, value: 'widget:QCheckBox, toolTip:Unir nubes de puntos'):
		self.__mergepointclouds = value

	def set_mergepointclouds_value(self):
		propierty_mergepointclouds_widget = self.__widget_by_propierty['mergepointclouds'] 
		if isinstance(propierty_mergepointclouds_widget, QSpinBox):
			self.__mergepointclouds_value = propierty_mergepointclouds_widget.value()
		elif isinstance(propierty_mergepointclouds_widget, QDoubleSpinBox):
			self.__mergepointclouds_value = propierty_mergepointclouds_widget.value()
		elif isinstance(propierty_mergepointclouds_widget, QComboBox):
			self.__mergepointclouds_value = propierty_mergepointclouds_widget.currentText()
		elif isinstance(propierty_mergepointclouds_widget, QLineEdit):
			self.__mergepointclouds_value = propierty_mergepointclouds_widget.text()
		elif isinstance(propierty_mergepointclouds_widget, QCheckBox):
			self.__mergepointclouds_value = propierty_mergepointclouds_widget.isChecked()

	@property
	def mergeelevations(self):
		return self.__mergeelevations

	@mergeelevations.setter
	def mergeelevations(self, value: 'widget:QCheckBox, toolTip:Unir MDEs'):
		self.__mergeelevations = value

	def set_mergeelevations_value(self):
		propierty_mergeelevations_widget = self.__widget_by_propierty['mergeelevations'] 
		if isinstance(propierty_mergeelevations_widget, QSpinBox):
			self.__mergeelevations_value = propierty_mergeelevations_widget.value()
		elif isinstance(propierty_mergeelevations_widget, QDoubleSpinBox):
			self.__mergeelevations_value = propierty_mergeelevations_widget.value()
		elif isinstance(propierty_mergeelevations_widget, QComboBox):
			self.__mergeelevations_value = propierty_mergeelevations_widget.currentText()
		elif isinstance(propierty_mergeelevations_widget, QLineEdit):
			self.__mergeelevations_value = propierty_mergeelevations_widget.text()
		elif isinstance(propierty_mergeelevations_widget, QCheckBox):
			self.__mergeelevations_value = propierty_mergeelevations_widget.isChecked()

	@property
	def mergeorthomosaics(self):
		return self.__mergeorthomosaics

	@mergeorthomosaics.setter
	def mergeorthomosaics(self, value: 'widget:QCheckBox, toolTip:Unir ortomosaicos'):
		self.__mergeorthomosaics = value

	def set_mergeorthomosaics_value(self):
		propierty_mergeorthomosaics_widget = self.__widget_by_propierty['mergeorthomosaics'] 
		if isinstance(propierty_mergeorthomosaics_widget, QSpinBox):
			self.__mergeorthomosaics_value = propierty_mergeorthomosaics_widget.value()
		elif isinstance(propierty_mergeorthomosaics_widget, QDoubleSpinBox):
			self.__mergeorthomosaics_value = propierty_mergeorthomosaics_widget.value()
		elif isinstance(propierty_mergeorthomosaics_widget, QComboBox):
			self.__mergeorthomosaics_value = propierty_mergeorthomosaics_widget.currentText()
		elif isinstance(propierty_mergeorthomosaics_widget, QLineEdit):
			self.__mergeorthomosaics_value = propierty_mergeorthomosaics_widget.text()
		elif isinstance(propierty_mergeorthomosaics_widget, QCheckBox):
			self.__mergeorthomosaics_value = propierty_mergeorthomosaics_widget.isChecked()

	@property
	def mergeddem(self):
		return self.__mergeddem

	@mergeddem.setter
	def mergeddem(self, value: 'widget:QComboBox, toolTip:Tipo de MDE a unir'):
		self.__mergeddem = value

	def set_mergeddem_value(self):
		propierty_mergeddem_widget = self.__widget_by_propierty['mergeddem'] 
		if isinstance(propierty_mergeddem_widget, QSpinBox):
			self.__mergeddem_value = propierty_mergeddem_widget.value()
		elif isinstance(propierty_mergeddem_widget, QDoubleSpinBox):
			self.__mergeddem_value = propierty_mergeddem_widget.value()
		elif isinstance(propierty_mergeddem_widget, QComboBox):
			self.__mergeddem_value = propierty_mergeddem_widget.currentText()
		elif isinstance(propierty_mergeddem_widget, QLineEdit):
			self.__mergeddem_value = propierty_mergeddem_widget.text()
		elif isinstance(propierty_mergeddem_widget, QCheckBox):
			self.__mergeddem_value = propierty_mergeddem_widget.isChecked()

	def set_values_from_dictionary(self, values):
		self.__tilesize_value = values['TileSize']
		self.__tilesize = values['TileSize']
		self.__tilesizebuffer_value = values['TileSizeBuffer']
		self.__tilesizebuffer = values['TileSizeBuffer']
		self.__method_value = values['Method']
		self.__method = values['Method']
		self.__path_value = values['Path']
		self.__path = values['Path']
		self.__mergemethod_value = values['MergeMethod']
		self.__mergemethod = values['MergeMethod']
		self.__mergepointclouds_value = values['MergePointClouds']
		self.__mergepointclouds = values['MergePointClouds']
		self.__mergeelevations_value = values['MergeElevations']
		self.__mergeelevations = values['MergeElevations']
		self.__mergeorthomosaics_value = values['MergeOrthomosaics']
		self.__mergeorthomosaics = values['MergeOrthomosaics']
		self.__mergeddem_value = values['MergedDEM']
		self.__mergeddem = values['MergedDEM']
		return

	def set_widget(self, widget):
		self.__widget = widget
		propierty_tilesize_widget = self.__widget.get_widget('tilesize')
		if isinstance(propierty_tilesize_widget, QSpinBox):
			propierty_tilesize_widget.valueChanged.connect(self.set_tilesize_value)
		elif isinstance(propierty_tilesize_widget, QDoubleSpinBox):
			propierty_tilesize_widget.valueChanged.connect(self.set_tilesize_value)
		elif isinstance(propierty_tilesize_widget, QComboBox):
			propierty_tilesize_widget.currentIndexChanged.connect(self.set_tilesize_value)
		elif isinstance(propierty_tilesize_widget, QLineEdit):
			propierty_tilesize_widget.editingFinished.connect(self.set_tilesize_value)
			propierty_tilesize_widget.textChanged.connect(self.set_tilesize_value)
		elif isinstance(propierty_tilesize_widget, QCheckBox):
			propierty_tilesize_widget.stateChanged.connect(self.set_tilesize_value)
		self.__widget_by_propierty['tilesize'] = propierty_tilesize_widget
		propierty_tilesizebuffer_widget = self.__widget.get_widget('tilesizebuffer')
		if isinstance(propierty_tilesizebuffer_widget, QSpinBox):
			propierty_tilesizebuffer_widget.valueChanged.connect(self.set_tilesizebuffer_value)
		elif isinstance(propierty_tilesizebuffer_widget, QDoubleSpinBox):
			propierty_tilesizebuffer_widget.valueChanged.connect(self.set_tilesizebuffer_value)
		elif isinstance(propierty_tilesizebuffer_widget, QComboBox):
			propierty_tilesizebuffer_widget.currentIndexChanged.connect(self.set_tilesizebuffer_value)
		elif isinstance(propierty_tilesizebuffer_widget, QLineEdit):
			propierty_tilesizebuffer_widget.editingFinished.connect(self.set_tilesizebuffer_value)
			propierty_tilesizebuffer_widget.textChanged.connect(self.set_tilesizebuffer_value)
		elif isinstance(propierty_tilesizebuffer_widget, QCheckBox):
			propierty_tilesizebuffer_widget.stateChanged.connect(self.set_tilesizebuffer_value)
		self.__widget_by_propierty['tilesizebuffer'] = propierty_tilesizebuffer_widget
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
		propierty_mergemethod_widget = self.__widget.get_widget('mergemethod')
		if isinstance(propierty_mergemethod_widget, QSpinBox):
			propierty_mergemethod_widget.valueChanged.connect(self.set_mergemethod_value)
		elif isinstance(propierty_mergemethod_widget, QDoubleSpinBox):
			propierty_mergemethod_widget.valueChanged.connect(self.set_mergemethod_value)
		elif isinstance(propierty_mergemethod_widget, QComboBox):
			propierty_mergemethod_widget.currentIndexChanged.connect(self.set_mergemethod_value)
		elif isinstance(propierty_mergemethod_widget, QLineEdit):
			propierty_mergemethod_widget.editingFinished.connect(self.set_mergemethod_value)
			propierty_mergemethod_widget.textChanged.connect(self.set_mergemethod_value)
		elif isinstance(propierty_mergemethod_widget, QCheckBox):
			propierty_mergemethod_widget.stateChanged.connect(self.set_mergemethod_value)
		self.__widget_by_propierty['mergemethod'] = propierty_mergemethod_widget
		propierty_mergepointclouds_widget = self.__widget.get_widget('mergepointclouds')
		if isinstance(propierty_mergepointclouds_widget, QSpinBox):
			propierty_mergepointclouds_widget.valueChanged.connect(self.set_mergepointclouds_value)
		elif isinstance(propierty_mergepointclouds_widget, QDoubleSpinBox):
			propierty_mergepointclouds_widget.valueChanged.connect(self.set_mergepointclouds_value)
		elif isinstance(propierty_mergepointclouds_widget, QComboBox):
			propierty_mergepointclouds_widget.currentIndexChanged.connect(self.set_mergepointclouds_value)
		elif isinstance(propierty_mergepointclouds_widget, QLineEdit):
			propierty_mergepointclouds_widget.editingFinished.connect(self.set_mergepointclouds_value)
			propierty_mergepointclouds_widget.textChanged.connect(self.set_mergepointclouds_value)
		elif isinstance(propierty_mergepointclouds_widget, QCheckBox):
			propierty_mergepointclouds_widget.stateChanged.connect(self.set_mergepointclouds_value)
		self.__widget_by_propierty['mergepointclouds'] = propierty_mergepointclouds_widget
		propierty_mergeelevations_widget = self.__widget.get_widget('mergeelevations')
		if isinstance(propierty_mergeelevations_widget, QSpinBox):
			propierty_mergeelevations_widget.valueChanged.connect(self.set_mergeelevations_value)
		elif isinstance(propierty_mergeelevations_widget, QDoubleSpinBox):
			propierty_mergeelevations_widget.valueChanged.connect(self.set_mergeelevations_value)
		elif isinstance(propierty_mergeelevations_widget, QComboBox):
			propierty_mergeelevations_widget.currentIndexChanged.connect(self.set_mergeelevations_value)
		elif isinstance(propierty_mergeelevations_widget, QLineEdit):
			propierty_mergeelevations_widget.editingFinished.connect(self.set_mergeelevations_value)
			propierty_mergeelevations_widget.textChanged.connect(self.set_mergeelevations_value)
		elif isinstance(propierty_mergeelevations_widget, QCheckBox):
			propierty_mergeelevations_widget.stateChanged.connect(self.set_mergeelevations_value)
		self.__widget_by_propierty['mergeelevations'] = propierty_mergeelevations_widget
		propierty_mergeorthomosaics_widget = self.__widget.get_widget('mergeorthomosaics')
		if isinstance(propierty_mergeorthomosaics_widget, QSpinBox):
			propierty_mergeorthomosaics_widget.valueChanged.connect(self.set_mergeorthomosaics_value)
		elif isinstance(propierty_mergeorthomosaics_widget, QDoubleSpinBox):
			propierty_mergeorthomosaics_widget.valueChanged.connect(self.set_mergeorthomosaics_value)
		elif isinstance(propierty_mergeorthomosaics_widget, QComboBox):
			propierty_mergeorthomosaics_widget.currentIndexChanged.connect(self.set_mergeorthomosaics_value)
		elif isinstance(propierty_mergeorthomosaics_widget, QLineEdit):
			propierty_mergeorthomosaics_widget.editingFinished.connect(self.set_mergeorthomosaics_value)
			propierty_mergeorthomosaics_widget.textChanged.connect(self.set_mergeorthomosaics_value)
		elif isinstance(propierty_mergeorthomosaics_widget, QCheckBox):
			propierty_mergeorthomosaics_widget.stateChanged.connect(self.set_mergeorthomosaics_value)
		self.__widget_by_propierty['mergeorthomosaics'] = propierty_mergeorthomosaics_widget
		propierty_mergeddem_widget = self.__widget.get_widget('mergeddem')
		if isinstance(propierty_mergeddem_widget, QSpinBox):
			propierty_mergeddem_widget.valueChanged.connect(self.set_mergeddem_value)
		elif isinstance(propierty_mergeddem_widget, QDoubleSpinBox):
			propierty_mergeddem_widget.valueChanged.connect(self.set_mergeddem_value)
		elif isinstance(propierty_mergeddem_widget, QComboBox):
			propierty_mergeddem_widget.currentIndexChanged.connect(self.set_mergeddem_value)
		elif isinstance(propierty_mergeddem_widget, QLineEdit):
			propierty_mergeddem_widget.editingFinished.connect(self.set_mergeddem_value)
			propierty_mergeddem_widget.textChanged.connect(self.set_mergeddem_value)
		elif isinstance(propierty_mergeddem_widget, QCheckBox):
			propierty_mergeddem_widget.stateChanged.connect(self.set_mergeddem_value)
		self.__widget_by_propierty['mergeddem'] = propierty_mergeddem_widget
