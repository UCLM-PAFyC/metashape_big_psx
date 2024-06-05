from . import gui_defines
class Project:
    def __init__(self,
                 label=gui_defines.PROJECT_LABEL_DEFAULT,
                 epsg=gui_defines.PROJECT_EPSG_DEFAULT,
                 path=None,
                 dem_gsd=gui_defines.PROJECT_DEM_GSD_DEFAULT,
                 ortho_gsd=gui_defines.PROJECT_DEM_GSD_DEFAULT):
        self.__label = label
        self.__epsg = epsg
        self.__path = path
        self.__dem_gsd = dem_gsd
        self.__ortho_gsd = ortho_gsd

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
    # def path(self, value: 'widget:file'):
    # def path(self, value: 'widget:file, type:save'):
    def path(self, value: 'widget:file, type:folder'):
        self.__path = value

    @property
    def dem_gsd(self):
        return self.__dem_gsd

    @dem_gsd.setter
    def dem_gsd(self, value: 'widget:QDoubleSpinBox, decimals:2,minimum:0.01, maximum:2.00, singleStep:0.01'):
        self.__dem_gsd = value

    @property
    def ortho_gsd(self):
        return self.__ortho_gsd

    @ortho_gsd.setter
    def ortho_gsd(self, value: 'widget:QDoubleSpinBox, decimals:2,minimum:0.01, maximum:2.00, singleStep:0.01'):
        self.__ortho_gsd = value
