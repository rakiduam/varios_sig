# -*- coding: utf-8 -*-
"""
cargar capas de forma/datos especifica en qgis

sería util si hay que generar multiples replicas de un archivo/estilo base

fuente: QGIS Python Programming Cookbook - Second Edition

@author: fanr
"""


import os
# cargar capas
from qgis.core import (
    QgsVectorLayer
    )

# operaciones union, merge, etc
from qgis.core import (
    QgsGeometry
    )


os.chdir('D:/WORK/CIREN/CAPAS/05 DEM LIDAR/TILESET/')
print(os.getcwd())

# carpeta = 'CAPAS/14 CUERPOS DE AGUA E INFRA RIEGO/Productos Hidrofor/'
# path_to_drenfor = (carpeta + "drenaje_bosque_área_1_VaVII.shp")

LIDAR = ['736_6090.asc', '736_6092.asc', '736_6094.asc', '736_6096.asc', '736_6098.asc', '738_6090.asc', '738_6092.asc', '738_6094.asc', '738_6096.asc', '738_6098.asc', '738_6100.asc', '740_6088.asc', '740_6090.asc', '740_6092.asc', '740_6094.asc', '740_6096.asc', '740_6098.asc', '740_6100.asc', '740_6102.asc', '742_6088.asc', '742_6090.asc', '742_6092.asc', '742_6094.asc', '742_6096.asc', '742_6098.asc', '742_6100.asc', '742_6102.asc', '744_6088.asc', '744_6090.asc', '744_6092.asc', '744_6094.asc', '744_6096.asc', '744_6098.asc', '744_6100.asc', '744_6102.asc', '744_6104.asc', '746_6088.asc', '746_6090.asc', '746_6092.asc', '746_6094.asc', '746_6096.asc', '746_6098.asc', '746_6100.asc', '746_6102.asc', '746_6104.asc', '746_6106.asc', '748_6088.asc', '748_6090.asc', '748_6092.asc', '748_6094.asc', '748_6096.asc', '748_6098.asc', '748_6100.asc', '748_6102.asc', '748_6104.asc', '748_6106.asc', '750_6088.asc', '750_6090.asc', '750_6092.asc', '750_6094.asc', '750_6096.asc', '750_6098.asc', '750_6100.asc', '750_6102.asc', '750_6104.asc', '750_6106.asc', '750_6108.asc', '752_6084.asc', '752_6086.asc', '752_6088.asc', '752_6090.asc', '752_6092.asc', '752_6094.asc', '752_6096.asc', '752_6098.asc', '752_6100.asc', '752_6102.asc', '752_6104.asc', '752_6106.asc', '752_6108.asc', '754_6084.asc', '754_6086.asc', '754_6088.asc', '754_6090.asc', '754_6092.asc', '754_6094.asc', '754_6096.asc', '754_6098.asc', '754_6100.asc', '754_6102.asc', '754_6104.asc', '754_6106.asc', '754_6108.asc', '756_6084.asc', '756_6086.asc', '756_6088.asc', '756_6090.asc', '756_6092.asc', '756_6094.asc', '756_6096.asc', '756_6098.asc', '756_6100.asc', '756_6102.asc', '756_6104.asc', '758_6084.asc', '758_6086.asc', '758_6088.asc', '758_6090.asc', '758_6092.asc', '758_6094.asc', '758_6096.asc']

# lee las capas como una variable
# drenfor_VaVII = QgsVectorLayer((carpeta + "drenaje_bosque_área_1_VaVII.shp"),
#                                 "drenfor_VaVII", "ogr")

for asc in LIDAR:
    asc = str(asc)
    rasterLyr = QgsRasterLayer(asc, asc[:-4])
    if not rasterLyr.isValid(): print("Layer failed to load!")
    QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])
