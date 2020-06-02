# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:38:42 2020

@author: fneir

fuentes:
- https://rasterio.readthedocs.io/en/latest/

"""


import rasterio
import os

os.chdir('E:\SENTINEL\UNZIP\S2A_MSIL2A_20190119T143751_N0211_R096_T18HYE_20190119T184849\S2A_MSIL2A_20190119T143751_N0211_R096_T18HYE_20190119T184849.SAFE\GRANULE\L2A_T18HYE_A018683_20190119T144606\IMG_DATA\R10m')

dataset1 = rasterio.open('example.tif')
dataset2 = rasterio.open('example.tif')