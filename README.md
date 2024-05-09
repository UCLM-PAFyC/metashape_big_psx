# Requisitos instalación

* Entorno conda con QGis + módulo python de Metashape Pro (2.1.1)
  * `conda search -c conda-forge qgis` Comprobar última versión estable de QGis
  * `conda create -n metashape2.1.1_qgis3.34.6 -c conda-forge qgis=3.34.6 python=3.11` Crear entorno
  * `conda activate metashape2.1.1_qgis3.34.6` Activar entorno
  * `pip install D:\Aicedrone\metashape_big_psx\Metashape-2.1.1-cp37.cp38.cp39.cp310.cp311-none-win_amd64.whl` Instalar módulo python de Metashape
  * `conda search -c conda-forge laspy` Comprobar última versión de laspy
  * `conda install -c conda-forge laspy=2.5.3` Instalar laspy
* Agisoft Metashape 2.1.1 [link](https://s3-eu-west-1.amazonaws.com/download.agisoft.com/metashape-pro_2_1_1_x64.msi) + activar licencia en GUI.
* Módulo python de Metashape Pro 2.1.1 [link](https://s3-eu-west-1.amazonaws.com/download.agisoft.com/Metashape-2.1.1-cp37.cp38.cp39.cp310.cp311-none-win_amd64.whl)
* Modelos del geoide para descargar [link](https://www.agisoft.com/downloads/geoids/)

# Requisitos de uso

## Advertencias generales

* EPSG permitidos: 25830, 25830+5782, 4326, 4326+3855, 4258+5782.
* No se permiten parámetros sin dato. Si no procede, debe completarse con el valor `"0"`.
* La carpeta de resultados será borrada en cada ejecución.
* No se permiten caracteres especiales en la definición de los parámetros de entrada.
* Las rutas a directorios o ficheros deben ser absolutas.
* Los parámetros de orientación interna que no se calibren se mantendrán fijos tras la importación.

## Importación de orientaciones externas

Para importar **orientaciones externas** desde archivo CSV, éste debe tener la siquiente estructura:
* Separador de campos `;`
* Separador decimal `.`
* Sin cabecera
* Sin primera fila de títulos o encabezados
* Para coordendas geodésicas:
  * Campos: `label,longitude,latitude,altitude`
  * Unidades: deg
* Para coordenadas proyectadas:
  * Campos: `label,east,north,altitude`
  * Unidades: según EPSG
  
## Importación de puntos de apoyo

Para importar **GCP** desde archivo CSV, éste debe tener la siquiente estructura:
* Separador de campos `;`
* Separador decimal `.`
* Sin cabecera
* Sin primera fila de títulos o encabezados
* Para coordendas geodésicas:
  * Campos: `label,longitude,latitude,altitude`
  * Unidades: deg
* Para coordenadas proyectadas:
  * Campos: `label,east,north,altitude`
  * Unidades: según EPSG

## Fotointerpretación de los puntos de apoyo

* No deben quedar puntos de apoyo desmarcados = check points.
* Cada punto debe estar fotointerpretado en al menos 3 imágenes.
* Para mejorar la visualización de imágenes térmicas, ir a Tools / Set Brightness... / Estimate.
* No se debe modificar ningún otro parámetro o configuración del proyecto.

## Importación de región de interés

Para utilizar una **región de interés**, debe:
* Estar previamente definida en un archivo SHP
* Tipo: `Polygon`
* Contener una sola entidad
* CRS: EPSG:4326

## Importación de malla de tileado

Para utilizar **una malla vectorial en archivo GPKG** el archivo debe haber sido creado previamente por este script.

# Instrucciones de ejecucción

1. Revisar y editar parámetros de entrada en el archivo `params.json`:

* `Project.Label` Etiqueta con la que se nombrarán los productos resultantes.
* `Project.EPSG` Código EPSG con el que se exportarán los productos resultantes.
* `Project.Path` Ruta del directorio de resultados.
* `Project.DemGSD` Resolución en metros con la que se exportarán el modelo digital de superficie y del terreno.
  * `0` Para seleccionar resolución mínima.
* `Project.OrthoGSD` Resolución en metros con la que se exportará la ortoimagen:
  * `0` Para seleccionar resolución mínima.

* `Workflow.CleanPrevious` Ejecuta la limpieza del trabajo anterior.
  * `True` | `False`
* `Workflow.Initialize` Ejecuta la creacción del proyecto e importación de los datos de entrada.
  * `True` | `False`
* `Workflow.Preprocess` Ejecuta el cosido y alineamiento inicial.
  * `True` | `False`
* `Workflow.Optimize` Ejecuta la optimización del alineamiento inicial con puntos de apoyo.
  * `True` | `False`
* `Workflow.Split` Ejecuta la partición del trabajo en tiles.
  * `True` | `False`
* `Workflow.PointCloud` Ejecuta la creacción y exportación de la nube de puntos densa.
  * `True` | `False`
* `Workflow.DEMs` Ejecuta la creacción y exportación de los modelos digitales de elevaciones.
  * `True` | `False`
* `Workflow.Orthomosaic` Ejecuta la creacción y exportación del orthomosaico.
  * `True` | `False`
* `Workflow.Report` Ejecuta la exportación del informe de resultados.
  * `True` | `False`

* `Photo.Path` Ruta del directorio donde se localizan las imágenes.
* `Photo.LocationAccuracy2D` Precisión en posición horizontal de la orientación externa de las imágenes en metros.
* `Photo.LocationAccuracyHeight` Precisión en posición vertical de la orientación externa de las imágenes en metros.
* `Photo.Method` Fuente de la que se importarán las orientaciones externas de las imágenes:
  * `CSV` Fichero CSV.
  * `EXIF` Metadatos de las fotos.
* `Photo.EPSG` Código EPSG con el que se importarán las imágenes.
* `Photo.EoPath` Ruta del archivo CSV con las orientaciones externas. [(Ver requisitos)](#importación-de-orientaciones-externas)

* `ROI.Method` Método de definición de la región de interés. [(Ver requisitos)](#importación-de-región-de-interés)
  * `0` Para utilizar el espacio máximo que abarquen los productos geométicos generados.
  * `1` Para definir con las herramienta de dibujo en el GUI de Metashape. #TODO
  * `SHP` Para importar un archivo SHP.
* `ROI.Path` Ruta del archivo en el que se delimita la región de interés.

* `CameraCalibration.f` Selección si calibra y no se fija el parámetro de orientación interna: focal length coefficient:
  * `True` | `False`
* `CameraCalibration.cx` Selección si calibra y no se fija el parámetro de orientación interna: X principal point coordinates.
  * `True` | `False`
* `CameraCalibration.cy` Selección si calibra y no se fija el parámetro de orientación interna: Y principal point coordinates.
  * `True` | `False`
* `CameraCalibration.k1` Selección si calibra y no se fija el parámetro de orientación interna: k1 radial distortion coefficient.
  * `True` | `False`
* `CameraCalibration.k2` Selección si calibra y no se fija el parámetro de orientación interna: k2 radial distortion coefficient.
  * `True` | `False`
* `CameraCalibration.k3` Selección si calibra y no se fija el parámetro de orientación interna: k3 radial distortion coefficient.
  * `True` | `False`
* `CameraCalibration.k4` Selección si calibra y no se fija el parámetro de orientación interna: k4 radial distortion coefficient.
  * `True` | `False`
* `CameraCalibration.b1` Selección si calibra y no se fija el parámetro de orientación interna: aspect ratio.
  * `True` | `False`
* `CameraCalibration.b2` Selección si calibra y no se fija el parámetro de orientación interna: skew coefficient.
  * `True` | `False`
* `CameraCalibration.p1` Selección si calibra y no se fija el parámetro de orientación interna: p1 tangential distortion coefficient.
  * `True` | `False`
* `CameraCalibration.p2` Selección si calibra y no se fija el parámetro de orientación interna: p2 tangential distortion coefficient.
  * `True` | `False`
  
* `OptimizeAlignment.Method` Selección si se calibra el alineamiento inicial:
  * `PSX` Para optimizar alineamiento inicial con puntos de apoyo fotointerpretados en la GUI de Metashape [(Ver requisitos)](#fotointerpretación-de-los-puntos-de-apoyo).
  * `XML` Para optimizar alineamiento inicial con puntos de apoyo importados de archivo XML con formato de markers de Metashape. OPCIÓN EN PRUEBAS.
* `OptimizeAlignment.EPSG` Código EPSG con el que se importarán los puntos de apoyo.
* `OptimizeAlignment.Path` Ruta del archivo de puntos de apoyo [(Ver requisitos)](#importación-de-puntos-de-apoyo) o markers .
* `OptimizeAlignment.Accuracy` Precisión establecida para el alineamiento:
  * `Highest` | `High` | `Medium` | `Low` | `Lowest`
* `OptimizeAlignment.ReferencePreselection` Método de preselección de imágenes según su localización:
  * `False` Selección del método genérico sin localización.
  * `Source` Selección del método según la localización de origen.
  * `Estimated` Selección del método según la localización estimada.
  * `Sequential` Selección del método secuencial.
* `OptimizeAlignment.TiePointLimit` Selección del límite de tie points.

* `SplitTile.TileSize` Dimensiones de tileado del bloque de vuelo para proyectos grandes en metros y unidades enteras.
* `SplitTile.TileSizeBuffer` Porcentage de ampliación del perímetro de los tiles. Valores enteros comprendidos entre 5 y 100.
* `SplitTile.Path` Opción de utilizar malla vectorial completa o editada por el usuario.
  * `0` Crea de forma automática la malla vestorial que cubre todo el trabajo o la ROI aplicada.
  * Ruta al archivo que contiene la malla vectorial editada por el usuario [(Ver requisitos)](#importación-de-malla-de-tileado). Si no encuentra el archivo, será creado y el proceso interrumpido. 
* `SplitTile.MergeMethod` Selección de opciones para unión de los productos resultantes:
  * `Metashape` Utilizando la API de Metashape.
  * `OsgeoLaspy` Utilizando las librerías `osgeo` (ráster) y `laspy` (nubes de puntos). #TODO
* `SplitTile.MergePointClouds` Selección si une la nube de puntos:
  * `True` | `False`
* `SplitTile.MergeElevations` Selección si une los modelos digitales de elevaciones (DSM y DTM):
  * `True` | `False`
* `SplitTile.MergeOrthomosaics` Selección si une el ortomosaico:
  * `True` | `False`
* `SplitTile.MergedDEM` Selección si une DSM o DTM como modelo de elevación predeterminado (Recomendado `DSM`):
  * `DSM` | `DTM`

* `PointCloud.Quality` Selección de la calidad:
  * `Ultrahigh` | `High` | `Medium` | `Low` | `Lowest`
* `PointCloud.FilterMode` Selección del filtro:
  * `False` | `Mild` | `Moderate` | `Aggressive`

* `InstallRequirement.Env` Ruta del entorno de instalación.
* `InstallRequirement.Geoid` Ruta del directorio donde se encuentras los modelos del geoide.

2. Ejecutar el archivo `BigPsx.bat`.
