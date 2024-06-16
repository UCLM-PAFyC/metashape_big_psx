from . import gui_defines

class CameraCalibration:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__text = 'Calibración de cámara'
		self.__text_by_propierty['f'] = 'Focal'
		self.__f = True
		self.__text_by_propierty['cx'] = 'X PPA'
		self.__cx = True
		self.__text_by_propierty['cy'] = 'Y PPA'
		self.__cy = True
		self.__text_by_propierty['k1'] = 'k1'
		self.__k1 = True
		self.__text_by_propierty['k2'] = 'k2'
		self.__k2 = True
		self.__text_by_propierty['k3'] = 'k3'
		self.__k3 = True
		self.__text_by_propierty['k4'] = 'k4'
		self.__k4 = False
		self.__text_by_propierty['b1'] = 'Afinidad'
		self.__b1 = False
		self.__text_by_propierty['b2'] = 'Asimetría'
		self.__b2 = False
		self.__text_by_propierty['p1'] = 'p1'
		self.__p1 = True
		self.__text_by_propierty['p2'] = 'p2'
		self.__p2 = True

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	@property
	def f(self):
		return self.__f

	@f.setter
	def f(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la focal'):
		self.__f = value

	@property
	def cx(self):
		return self.__cx

	@cx.setter
	def cx(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la coordenada X del PPA'):
		self.__cx = value

	@property
	def cy(self):
		return self.__cy

	@cy.setter
	def cy(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la coordenada Y del PPA'):
		self.__cy = value

	@property
	def k1(self):
		return self.__k1

	@k1.setter
	def k1(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k1 de distorsión radial'):
		self.__k1 = value

	@property
	def k2(self):
		return self.__k2

	@k2.setter
	def k2(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k2 de distorsión radial'):
		self.__k2 = value

	@property
	def k3(self):
		return self.__k3

	@k3.setter
	def k3(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k3 de distorsión radial'):
		self.__k3 = value

	@property
	def k4(self):
		return self.__k4

	@k4.setter
	def k4(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k4 de distorsión radial'):
		self.__k4 = value

	@property
	def b1(self):
		return self.__b1

	@b1.setter
	def b1(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la relación de aspecto'):
		self.__b1 = value

	@property
	def b2(self):
		return self.__b2

	@b2.setter
	def b2(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la asimetría'):
		self.__b2 = value

	@property
	def p1(self):
		return self.__p1

	@p1.setter
	def p1(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra p1 de distorsión tangencial'):
		self.__p1 = value

	@property
	def p2(self):
		return self.__p2

	@p2.setter
	def p2(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra p2 de distorsión tangencial'):
		self.__p2 = value
