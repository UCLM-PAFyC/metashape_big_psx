from . import gui_defines

class Photo:
	def __init__(self):
		self.__path = ""
		self.__locationaccuracy2d = 0.08
		self.__locationaccuracyheight = 0.12
		self.__method = ['Metadatos de las fotos' ,' Fichero CSV']
		self.__epsg = "4326"
		self.__eopath = ""

	@property
	def path(self):
		return self.__path

	@path.setter
	def path(self, value: 'widget:file, type:folder, toolTip:Ruta del directorio donde se localizan las imágenes'):
		self.__path = value

	@property
	def locationaccuracy2d(self):
		return self.__locationaccuracy2d

	@locationaccuracy2d.setter
	def locationaccuracy2d(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:5.0, singleStep:0.01, toolTip:Precisión horizontal de la orientación externa de las imágenes en metros'):
		self.__locationaccuracy2d = value

	@property
	def locationaccuracyheight(self):
		return self.__locationaccuracyheight

	@locationaccuracyheight.setter
	def locationaccuracyheight(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:5.0, singleStep:0.01, toolTip:Precisión vertical de la orientación externa de las imágenes en metros'):
		self.__locationaccuracyheight = value

	@property
	def method(self):
		return self.__method

	@method.setter
	def method(self, value: 'widget:QComboBox, toolTip:Fuente de la que se importarán las orientaciones externas de las imágenes'):
		self.__method = value

	@property
	def epsg(self):
		return self.__epsg

	@epsg.setter
	def epsg(self, value: 'widget:QLineEdit, toolTip:Código EPSG con el que se importarán las imágenes'):
		self.__epsg = value

	@property
	def eopath(self):
		return self.__eopath

	@eopath.setter
	def eopath(self, value: 'widget:file, toolTip:Ruta del archivo CSV con las orientaciones externas'):
		self.__eopath = value
