from . import gui_defines

class Workflow:
	def __init__(self):
		self.__cleanprevious = True
		self.__initialize = True
		self.__preprocess = True
		self.__optimize = True
		self.__split = True
		self.__pointcloud = True
		self.__dems = True
		self.__orthomosaic = True
		self.__report = True

	@property
	def cleanprevious(self):
		return self.__cleanprevious

	@cleanprevious.setter
	def cleanprevious(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la limpieza del trabajo anterior'):
		self.__cleanprevious = value

	@property
	def initialize(self):
		return self.__initialize

	@initialize.setter
	def initialize(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación del proyecto e importación de los datos de entrada'):
		self.__initialize = value

	@property
	def preprocess(self):
		return self.__preprocess

	@preprocess.setter
	def preprocess(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta el cosido y alineamiento inicial'):
		self.__preprocess = value

	@property
	def optimize(self):
		return self.__optimize

	@optimize.setter
	def optimize(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la optimización del alineamiento inicial con puntos de apoyo'):
		self.__optimize = value

	@property
	def split(self):
		return self.__split

	@split.setter
	def split(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la partición del trabajo en tiles'):
		self.__split = value

	@property
	def pointcloud(self):
		return self.__pointcloud

	@pointcloud.setter
	def pointcloud(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación y exportación de la nube de puntos densa'):
		self.__pointcloud = value

	@property
	def dems(self):
		return self.__dems

	@dems.setter
	def dems(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación y exportación de los modelos digitales de elevaciones'):
		self.__dems = value

	@property
	def orthomosaic(self):
		return self.__orthomosaic

	@orthomosaic.setter
	def orthomosaic(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creación y exportación del orthomosaico'):
		self.__orthomosaic = value

	@property
	def report(self):
		return self.__report

	@report.setter
	def report(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la exportación del informe de resultados'):
		self.__report = value
