import processing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qgis.core import *
from qgis.utils import iface

miasta = QgsVectorLayer(r"C:/Users/ola/Documents/pw/PROGRAMOWANIE_W_SIP/zajęcia_nr_7/DANE/dane/miasta.shp","miasta","ogr")
if miasta.isValid():
    QgsProject.instance().addMapLayer(miasta)

c=miasta.crs()
e=miasta.extent()
miny=e.yMinimum()
maxy=e.yMaximum()
minx=e.xMinimum()
maxx=e.xMaximum()

print("rozciaglosc poludnikowa to ", maxx-minx)
print("rozciaglosc rownoleznikowa to ", maxy-miny)
print("EPSG to ", c)
print("nazwa układu to ", c.description())
print("typ ukladu to ", c.CrsType())
print("jednostka miary wsp to ", c.mapUnits())

#project_crs
#project_crs_description
#project_units