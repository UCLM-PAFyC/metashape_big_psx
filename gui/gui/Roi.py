from . import gui_defines

class Roi:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__text = 'Región de interés'
		self.__text_by_propierty['path'] = 'Ruta ROI'
		self.__path = ""
		self.__text_by_propierty['method'] = 'Fuente ROI'
		self.__method = ['Región total con recubrimiento' ,' Importada de shapefile']

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

	@property
	def method(self):
		return self.__method

	@method.setter
	def method(self, value: 'widget:QComboBox, toolTip:Método de definición de la ROI'):
		self.__method = value
