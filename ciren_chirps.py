# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:55:17 2020

@author: fanr

idea general: leer una bbdd de TS de puntos con coordenadas espaciales.

https://towardsdatascience.com/nearest-neighbour-analysis-with-geospatial-data-7bcd95f34c0e

"""

import pandas as pd, numpy as np, os, geopandas as gpd

chirps = gpd.read_file('E:/ESTACIONES_CORRECCION/BBDD/chile_puntos.shp')
