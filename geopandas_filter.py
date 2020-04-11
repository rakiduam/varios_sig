# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:06:09 2020

@author: fneir

documentacion pandas:
   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains

regular expressions en python:
    https://www.dataquest.io/wp-content/uploads/2019/03/python-regular-expressions-cheat-sheet.pdf
"""


import os
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

os.chdir('D:/WORK/CIREN/')
print(os.getcwd())

suel = gpd.read_file('TEMPORALES/clip_suelo.shp')
prop = gpd.read_file('TEMPORALES/clip_propiedades.shp')

suel.boundary.plot(color='blue')
prop.plot(color='red')

# obtener listado de columnas
list(suel)
# obtener listado de valores unicos en la columna de interes
print((suel.descvari).unique())
# filtrar por la columna de interes
# suel.loc[(suel.descvari=='CAJA DE ESTERO') |
#           (suel.descvari=='CAJA DE RIO') |
#           (suel.descvari=='MISCELANEO RIO') |
#           (suel.descvari=='MISCELANEO RIO (1)')].plot(color='blue')

suel2=suel.loc[suel.descvari.str.contains('\ACAJA*|\AMISCELANEO.RIO|\AMISCELANEO?RIO?(1)', case=False, regex=True)==True]

# obtener listado de columnas
list(prop)
# obtener listado de valores unicos en la columna de interes
([print(i) for i in (prop.rol).unique()])
# no resulto demasiados valores unicos

# filtrar por la columna de interes
pro2 = prop.loc[prop.rol.str.contains('\ACAJA*|\ARIO*|\AESTERO*', case=False,regex=True)]

pro2.rol.unique()

