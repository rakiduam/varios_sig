# -*- coding: utf-8 -*-
"""
idea general:
piramidal nearesr neighbord

@author: fanr
"""

import subprocess, glob

# directorios
entDIR = 'E:\\CAPAS\\05 DEM LIDAR\\MOSAICO\\'
# outDIR = 'E:/ORIGINALES/SLOPE_5m/'

# listado archivos entrada - salida
input_dem = glob.glob(entDIR + '*.tif')
#output_slope = [('').join([ outDIR,'slope_', str(i).split('\\')[-1]]) for i in dem]
#[print(i) for i in input_dem]
#[print(i) for i in output_slope]


cmd2 = [('').join(['gdaladdo ', str(i), ' -r nearest -ro -clean 2 4 8 16']) for i in glob.glob(entDIR + '*.tif')]
for i in cmd2:
    subprocess.run(str(i))
    # print(('').join([str(i), '\t...listo']))
