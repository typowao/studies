import gdal
from gdalconst import *

#import biblioteki ktora obsluguje matplotlib
import pylab as pl
import numpy as np
gdal.AllRegister()

fn=r'C:\Users\ola\Documents\pw\PROGRAMOWANIE_W_SIP\zajęcia_nr_8\dane\dem2.tif'
ds=gdal.Open(fn, GA_ReadOnly)
if ds is None:
    print ("Niewlasciwa definicja rastra")
    
z1=ds.RasterXSize
z2=ds.RasterYSize
z3=ds.RasterCount

#W miesjce "..." wstaw odpowiednia wlasciwisc warstwy rastrowej
print('Liczba kolumn wynosi: '+str(z1))
print('Liczba wierszy wynosi: '+str(z2))
print('Liczba pikseli wynosi: '+str(z3))

# GeoTransforms
geotransform=ds.GetGeoTransform()

z4=geotransform[0]
z5=geotransform[3]
z6=geotransform[1]
z7=geotransform[5]

#W miesjce "..." wstaw odpowiednia wlasciwisc warstwy rastrowej
print('i.e., horizontal '+str(z4))
print('i.e., vertical '+str(z5))
print('rozdzielczość pozioma '+str(z6))
print('rozdzielczość pionowa '+str(z7))

#zmienna odnoszaca sie do wybranego kanalu rastra
band=ds.GetRasterBand(1)
band.GetMetadata()
print("[ MAX ] =", band.GetMaximum())
print("[ MIN ] =", band.GetMinimum())

#zmienna bedaca tablica z wybranego kanalu rastra
rdata=band.ReadAsArray(0,0,z1,z2)
arr = np.array(rdata)
val = arr[[90], :][:, [20]]
print("[ 90;20 ] =", val)
#tworzenie histogramu z biblioteki pylab
pl.hist(rdata,10)

#wyswietlanie histogramu
pl.show()

#zerowanie zmiennej ds
ds=None
band=None
rdata=None