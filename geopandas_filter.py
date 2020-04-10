# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:06:09 2020

@author: fneir
"""


import os
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

os.chdir('D:/WORK/CIREN/')
print(os.getcwd())

suelo = gpd.read_file('TEMPORALES/clip_suelo.shp')
propiedad = gpd.read_file('TEMPORALES/clip_propiedades.shp')

suelo.boundary.plot()
propiedad.plot()

# obtener listado de columnas
list(suelo)
# obtener listado de valores unicos en la columna de interes
print((suelo.descvari).unique())
# filtrar por la columna de interes
suelo.loc[(suelo.descvari=='CAJA DE ESTERO') | (suelo.descvari=='CAJA DE RIO')].plot()


 ['CAJA DE ESTERO', 'CAJA DE RIO', 'MISCELANEO RIO',
                         'MISCELANEO RIO (1)']]


