# -*- coding: utf-8 -*-
"""
idea general, ejecutar calculo de pendiente en porcentajes a partir de un dem
proceso automatico de renombre de archivos, solo necesita que existan carpeta
de entrada y salida.
"""
import subprocess, glob

# directorios
entDIR = 'E:/ORIGINALES/DEM_5m/'
outDIR = 'E:/ORIGINALES/SLOPE_5m/'

# listado archivos entrada - salida
input_dem = glob.glob(entDIR + 'R07_*.tif')
#output_slope = [('').join([ outDIR,'slope_', str(i).split('\\')[-1]]) for i in dem]
#[print(i) for i in input_dem]
#[print(i) for i in output_slope]

# version complicada, genera todo de inmediato
cmd =[("").join(['gdaldem slope ', i, ' ', (lambda x: ('').join([ outDIR,'slope_', str(x).split('\\')[-1]])) (i),' -of GTiff -b 1 -s 1.0']) for i in input_dem]
# cmd = ('').join(['gdaldem slope ', input_tif, ' ',output_tif, ' -of GTiff -b 1 -s 1.0 -p'])
#print(cmd)
# [print(i) for i in cmd]

## ejecuta subproceso en gdal
## subprocess.run ([x for x in cmd.split(" ") if x != ""])
for i in cmd:
    # print(i)
    subprocess.run(str(i))
    print(('').join([str(i), '\t...listo']))


cmd2 = [('').join(['gdaladdo ', str(i), ' -r nearest -ro 2 4 8 16']) for i in glob.glob(outDIR + '*.tif')]
for i in cmd2:
    subprocess.run(str(i))
    print(('').join([str(i), '\t...listo']))
