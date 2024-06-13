from . import gui_defines

class Project:
	def __init__(self):
		self.__label = "Example project"
		self.__epsg = "25830+5782"
		self.__path = ""
		self.__demgsd = 0.05
		self.__orthogsd = 0.05

	@property
	def label(self):
		return self.__label

	@label.setter
	def label(self, value: 'widget:QLineEdit'):
		self.__label = value

	@property
	def epsg(self):
		return self.__epsg

	@epsg.setter
	def epsg(self, value: 'widget:QLineEdit'):
		self.__epsg = value

	@property
	def path(self):
		return self.__path

	@path.setter
	def path(self, value: 'widget:file, type:folder'):
		self.__path = value

	@property
	def demgsd(self):
		return self.__demgsd

	@demgsd.setter
	def demgsd(self, value: 'widget:QDoubleSpinBox, decimals:2, minimum:0.0, maximum:2.0, singleStep:0.01'):
		self.__demgsd = value

	@property
	def orthogsd(self):
		return self.__orthogsd

	@orthogsd.setter
	def orthogsd(self, value: 'widget:QDoubleSpinBox, decimals:2, minimum:0.0, maximum:2.0, singleStep:0.01'):
		self.__orthogsd = value
