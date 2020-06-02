# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:51:52 2020

tratar de generar un raster virtual a partir de los archivos ascii de lidar

@author: fneir
"""

from osgeo import gdal
import glob
import os

# VARIABLES DE ENTORNO
# directorio de trabajo
os.chdir("D:/WORK/CIREN/CAPAS/05 DEM LIDAR/TILESET/")
os.getcwd()  ## directorio actual

# producto modis a procesar, solo por referencia de nombre
#imgMOD = "MOD11A2"
# periocidad temporal del producto MO13A2 16días, MOD13Q1 8 días
#step = 1  ## eventualmente se puede dejar en periodo que se desee


#EPSG:32718 - WGS 84 / UTM zone 18S - Projected
# sistema de coordenadas del proceso, son constantes.
coordASC = '+proj=utm +zone=18 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs'
# coordENT = "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +a=6371007.181 +b=6371007.181 +units=m +no_defs"
# coordSAL = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"
# limites = (-76.5, -68.0, -56.0, -16.8)  ## en sistema salida

mosaico_lista = ['736_6090.asc',
'736_6092.asc', '736_6094.asc', '736_6096.asc', '736_6098.asc', '738_6090.asc', '738_6092.asc', '738_6094.asc', '738_6096.asc', '738_6098.asc', '738_6100.asc', '740_6088.asc', '740_6090.asc', '740_6092.asc', '740_6094.asc', '740_6096.asc', '740_6098.asc', '740_6100.asc', '740_6102.asc', '742_6088.asc', '742_6090.asc', '742_6092.asc', '742_6094.asc', '742_6096.asc', '742_6098.asc', '742_6100.asc', '742_6102.asc', '744_6088.asc', '744_6090.asc', '744_6092.asc', '744_6094.asc', '744_6096.asc', '744_6098.asc', '744_6100.asc', '744_6102.asc', '744_6104.asc', '746_6088.asc', '746_6090.asc', '746_6092.asc', '746_6094.asc', '746_6096.asc', '746_6098.asc', '746_6100.asc', '746_6102.asc', '746_6104.asc', '746_6106.asc', '748_6088.asc', '748_6090.asc', '748_6092.asc', '748_6094.asc', '748_6096.asc', '748_6098.asc', '748_6100.asc', '748_6102.asc', '748_6104.asc', '748_6106.asc', '750_6088.asc', '750_6090.asc', '750_6092.asc', '750_6094.asc', '750_6096.asc', '750_6098.asc', '750_6100.asc', '750_6102.asc', '750_6104.asc', '750_6106.asc', '750_6108.asc', '752_6084.asc', '752_6086.asc', '752_6088.asc', '752_6090.asc', '752_6092.asc', '752_6094.asc', '752_6096.asc', '752_6098.asc', '752_6100.asc', '752_6102.asc', '752_6104.asc', '752_6106.asc', '752_6108.asc', '754_6084.asc', '754_6086.asc', '754_6088.asc', '754_6090.asc', '754_6092.asc', '754_6094.asc', '754_6096.asc', '754_6098.asc', '754_6100.asc', '754_6102.asc', '754_6104.asc', '754_6106.asc', '754_6108.asc', '756_6084.asc', '756_6086.asc', '756_6088.asc', '756_6090.asc', '756_6092.asc', '756_6094.asc', '756_6096.asc', '756_6098.asc', '756_6100.asc', '756_6102.asc', '756_6104.asc', '758_6084.asc', '758_6086.asc', '758_6088.asc', '758_6090.asc', '758_6092.asc', '758_6094.asc', '758_6096.asc']

# mosaico_lista = glob.glob(("*.asc"))
ls=gdal.BuildVRT('mosaico_VRT.VRT', mosaico_lista, outputSRS = coordASC)
print(ls)

ls = None

# %% creacion mosaico virtual

# # Ciclo de lectura de imagenes / escritura del mosaico en geotif
# for year in range(2001, 2018):
#     year = str(year)
#     #print(year)
#     for day in range(1, 366, step):
#         day = str("%0.3d" % day)  ## genera dia con pad de 0, ej; 001, 017, etc.
#         # nombre archivo de salida, corregir acorde idea, sistema de nombre.
#         outfile = (imgMOD + ".A" + year + day + ".mosaic.SPLINE.").upper()
#         # lista de archivos a generar en mosaico
#         mosaico_lista = glob.glob((os.getcwd()+'/'+year +"/"+ imgMOD + ".A" + year + day + "*.tif"))
#         if not mosaico_lista:
#             print(("").join(["empty ", day]))
#         elif mosaico_lista:
#             # genera mosaico formato virtual gdal, liviano, no mas de 4 mb
#             ls = gdal.BuildVRT(year + "/" + outfile + "VRT", mosaico_lista)
#             print(ls)
#             ls = None # libera memoria en el garbage collection.
#             #ls.Destroy()
#             #ls.ReadAsArray()
#             #ls.FlushCache()


# del mosaico_lista, outfile, year, day
