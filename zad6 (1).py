import processing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qgis.core import *
from qgis.utils import iface
import gdal
from gdalconst import *

import pylab as pl
import numpy as np
gdal.AllRegister()


#deklaracja zmiennych
a=r"C:\Users\ola\Documents\pw\PROGRAMOWANIE_W_SIP\zajęcia_nr_8\dane\dem2.tif"

spadki=r"C:\Users\ola\Documents\pw\PROGRAMOWANIE_W_SIP\zajęcia_nr_8\dane\dem2_spadki.tif"
recl=r"C:\Users\ola\Documents\pw\PROGRAMOWANIE_W_SIP\zajęcia_nr_8\dane\dem2_reclass.tif"
zonal_stat=r"C:\Users\ola\Documents\pw\PROGRAMOWANIE_W_SIP\zajęcia_nr_8\dane\dem2_filtr_recl_zs.csv"

#mapa spadkow
#processing.run("gdal:slope", {'INPUT': a, 'BAND': 1, 'COMPUTE_EDGES': True, 'ZEVENBERGEN': 0, 'AS_PERCENT': True, 'SCALE': 1.0, 'OUTPUT': spadki})
#iface.addRasterLayer(spadki)

#wskaz wartosc graniczna dla 2 stref na podstawie nmt
ds=gdal.Open(spadki, GA_ReadOnly)
band=ds.GetRasterBand(1)
band.GetMetadata()
war=band.GetMaximum()
wartosc = war/2
print("wartosc = ", band.GetMaximum())
print(wartosc )

#definicja formuly wyznaczenia stref dla kalkulatora rastrow
formula="ifelse(gt(g1,"+str(wartosc)+"),1,2)"

#reklasyfikacja rastra nmt - dwie strefy wg formuly
pr={ 'FORMULA': formula, 'GRIDS': a, 'RESAMPLING': 3, 'RESULT': recl, 'TYPE': 7, 'USE_NODATA': False, 'XGRIDS': None }
processing.run('saga:rastercalculator', pr)

#obliczenie statystyk spadkow w strefach zdefiniowanych na podstawie nmt
prs={'ZONES':recl, 'OUTTAB':zonal_stat}
processing.run('saga:zonalgridstatistics', prs)