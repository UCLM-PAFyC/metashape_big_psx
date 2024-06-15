from . import gui_defines

class Project:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__text = 'Proyecto'
		self.__text_by_propierty['label'] = 'Etiqueta'
		self.__label = "Example project"
		self.__text_by_propierty['epsg'] = 'Código EPSG'
		self.__epsg = "25830+5782"
		self.__text_by_propierty['path'] = 'Directorio de resultados'
		self.__path = ""
		self.__text_by_propierty['demgsd'] = 'GSD para MDT y MDS'
		self.__demgsd = 0.05
		self.__text_by_propierty['orthogsd'] = 'GSD para ortomosaico'
		self.__orthogsd = 0.05

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

	@property
	def epsg(self):
		return self.__epsg

	@epsg.setter
	def epsg(self, value: 'widget:QLineEdit, toolTip:Código EPSG con el que se exportarán los productos resultantes'):
		self.__epsg = value

	@property
	def path(self):
		return self.__path

	@path.setter
	def path(self, value: 'widget:file, type:folder, toolTip:Ruta del directorio de resultados'):
		self.__path = value

	@property
	def demgsd(self):
		return self.__demgsd

	@demgsd.setter
	def demgsd(self, value: 'widget:QDoubleSpinBox, decimals:2, minimum:0.0, maximum:2.0, singleStep:0.01, toolTip:Resolución en metros con la que se exportarán el modelo digital de superficies y del terreno (0 para máxima posible)'):
		self.__demgsd = value

	@property
	def orthogsd(self):
		return self.__orthogsd

	@orthogsd.setter
	def orthogsd(self, value: 'widget:QDoubleSpinBox, decimals:2, minimum:0.0, maximum:2.0, singleStep:0.01, toolTip:Resolución en metros con la que se exportará el ortomosaico (0 para máxima posible)'):
		self.__orthogsd = value
