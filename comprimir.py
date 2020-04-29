# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:31:06 2020

@author: fneir
"""

import zipfile, os, glob


n=3
vecinos = str(n) +'x' + str(n)
os.chdir('D:/rugosidad/'+vecinos)
print(os.getcwd())

lista = glob.glob('**/*.tif', recursive=True)

lista = [i.split('.')[0] for i in lista]

imagen = lista[0]

for imagen in lista:
    # [my_zip.write(archivo) for archivo in glob.glob(imagen + '.*')]
    print(imagen)
    with zipfile.ZipFile(imagen+'.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write(imagen + '.tif')
        my_zip.write(imagen + '.tfw')
        my_zip.write(imagen + '.tif.aux.xml')
        my_zip.write(imagen + '.tif.ovr')
        # my_zip.close()
