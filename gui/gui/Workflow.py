from . import gui_defines

class Workflow:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__text = 'Flujo de trabajo'
		self.__text_by_propierty['cleanprevious'] = 'Reseteo directorio previo'
		self.__cleanprevious = True
		self.__text_by_propierty['initialize'] = 'Project inicialización'
		self.__initialize = True
		self.__text_by_propierty['preprocess'] = 'Project preproceso'
		self.__preprocess = True
		self.__text_by_propierty['optimize'] = 'Optimización de OI'
		self.__optimize = True
		self.__text_by_propierty['split'] = 'Partición del proyecto'
		self.__split = True
		self.__text_by_propierty['pointcloud'] = 'Construcción de nube de puntos'
		self.__pointcloud = True
		self.__text_by_propierty['dems'] = 'Construcción de los modelos digitales de elevaciones'
		self.__dems = True
		self.__text_by_propierty['orthomosaic'] = 'Construcción del ortomosaico'
		self.__orthomosaic = True
		self.__text_by_propierty['report'] = 'Construcción del informe'
		self.__report = True

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

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
