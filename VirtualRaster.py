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
os.chdir("E:/CIREN_guardar_aqui/R07/DTM_r07/DTM")
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



mosaico_lista = glob.glob(("*.asc"))
ls=gdal.BuildVRT('E:/mosaico_VRT.VRT', mosaico_lista, outputSRS = coordASC)
print(ls) ; ls = None

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
