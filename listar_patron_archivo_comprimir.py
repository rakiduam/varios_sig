# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:31:06 2020

Comprime todos los archivos que cumplan con un patron de nombre.
Por ej. archivos compuestos como: shapefiles, geotif, raster, etc.

Python posee por defecto un modulo de compresión zip.

Queda evaluar algun otro metodo de mejor compresión.

@author: fanr
"""
# carga de modulos
import zipfile, os, glob

# directorio entrada, comprimira todo lo que hay dentro de dicho directorio
entDIR = 'D:/rugosidad/5x5'

# vecinos = str(n) +'x' + str(n)
os.chdir(entDIR)
print(os.getcwd())

# obtener el listado unico{} de los archivos, independiente de extension
lista = set([str(i).split('.')[0] for i in glob.glob('**/*.*', recursive=True)])

# obtener todas las extensiones{} de los archivos
# existe la opcion del endswith, pero implica saber largo del texto
tipos = set([str(i).split('.')[-1] for i in glob.glob('*.*')])

# es muy probable que pandas tenga una funcion que haga un mix entre ambas variables
# en este instante estan seteadas como diccionarios{} y no listas[]
print(lista, tipos)

# comprimir en archivos zip, separados.
for imagen in lista:
    # script para compresión, sin tener que abrir / cerrar archivo.
    with zipfile.ZipFile(imagen+'.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        for ext in tipos:
            # chequea archivo existe, sino lo salta.
            archivo = ('').join(glob.glob(imagen + '*' + ext))
            print(archivo)
            if os.path.exists(archivo):
                my_zip.write(archivo)