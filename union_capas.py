# -*- coding: utf-8 -*-
"""
Script para cortar informacion base para proyecto erosion region maule
tambien para aprender a usar geopandas / rasterio en terminos simples.
@fanr
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

#definicion de carpeta de trabajo
os.chdir("D:/WORK/CIREN/")
print(os.getcwd())

# lectura archivo de area of interes, aoi
aoi = gpd.read_file("TEMPORALES/Delimitacion_perimetro_cuencas_comunas.shp")


### SUELOS
# directorio donde se albergan las capas de interes
file = os.listdir("D:/WORK/CIREN/CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/")
# listado de todos los shapefiles dentro del directorio
path = [os.path.join("D:/WORK/CIREN/CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/", i) for i in file if ".shp" in i[-4:]]

# seleccion de los elementos que interesan en este caso son solo 3
path = list([path[1],path[2],path[-1]])
# generar geodataframe, mediante lectura y union archivos interes.
suelos = gpd.GeoDataFrame(pd.concat([gpd.read_file(i) for i in path],
                        ignore_index=True), crs=gpd.read_file(path[0]).crs)
# chequeo de la forma visual union
suelos.plot()
# chequeo de las columnas totales de la union
suelos.head()
# guardar el archivo
suelos.to_file('TEMPORALES/merge_suelos6716.shp')

# "clip" del geodataframe acorde al area de interes.
suelos_aoi = gpd.overlay(suelos, aoi, how='intersection' )
suelos_aoi.plot()
# guardar el archivo
suelos_aoi.to_file('TEMPORALES/clip_suelo.shp')
# None a varibles temporales
file, path, suelos, suelo_aoi = None, None, None, None

### PROPIEDADES RURALES
file = os.listdir("D:/WORK/CIREN/CAPAS/09 PROPIEDADES RURALES/")
path = [os.path.join("D:/WORK/CIREN/CAPAS/09 PROPIEDADES RURALES/", i) for i in file if ".shp" in i[-4:]]
path = list([path[5],path[6],path[-1]])
propiedades = gpd.GeoDataFrame(pd.concat([gpd.read_file(i) for i in path],
                        ignore_index=True), crs=gpd.read_file(path[0]).crs)
# propiedades.to_file('TEMPORALES/merge_propiedades6716.shp')
propiedades_aoi = gpd.overlay(propiedades, aoi, how='intersection' )
propiedades_aoi.to_file('TEMPORALES/clip_propiedades.shp')
file, path, propiedades, propiedades_aoi = None, None, None, None


### CATASTRO DE BOSQUE NATIVO - NO SUELOS
# cbn no suelom que es principalmente zonas urbanas que identifico
# en su momento el catastro de bosque nativo, esta bastante desactualizado
file = os.listdir('D:/WORK/CIREN/CAPAS/01 CATASTRO CBN NO SUELOS/')
path = [os.path.join('D:/WORK/CIREN/CAPAS/01 CATASTRO CBN NO SUELOS/', i) for i in file if ".shp" in i[-4:]]
path = list([path[0],path[1],path[-1]])
cbn_ns = gpd.GeoDataFrame(pd.concat([gpd.read_file(i) for i in path],
                        ignore_index=True), crs=gpd.read_file(path[0]).crs)
cbn_ns.to_file('TEMPORALES/merge_cbns.shp')
cbn_ns_aoi = gpd.overlay(cbn_ns, aoi, how='intersection' )
cbn_ns_aoi.to_file('TEMPORALES/clip_cbn_ns.shp')
file, path, cbn_ns, cbn_ns_aoi = None, None, None, None


### CATASTRO DE BOSQUE NATIVO
file = os.listdir('D:/WORK/CIREN/CAPAS/01 CATASTRO CBN/')
path = [os.path.join('D:/WORK/CIREN/CAPAS/01 CATASTRO CBN/', i) for i in file if ".shp" in i[-4:]]
path = list([path[-1],path[0],path[1]])
cbn_ns = gpd.GeoDataFrame(pd.concat([gpd.read_file(i) for i in path],
                        ignore_index=True), crs=gpd.read_file(path[0]).crs)
cbn_ns.to_file('TEMPORALES/merge_cbn.shp')
cbn_ns_aoi = gpd.overlay(cbn_ns, aoi, how='intersection' )
cbn_ns_aoi.to_file('TEMPORALES/clip_cbn.shp')
file, path, cbn_ns, cbn_ns_aoi = None, None, None, None






# hidrofor
hidrofor = gpd.read_file("CAPAS/14 CUERPOS DE AGUA E INFRA RIEGO/CAJAS_RIOS_HIDROFOR/CR_V_X.shp")
hidro_aoi = gpd.overlay(hidrofor, aoi, how="intersection")
hidro_aoi.to_file('TEMPORALES/clip_CR_V_X.shp')
hidrofor, hidro_aoi = None, None

# hidrofor drenaje
carpeta = "CAPAS/14 CUERPOS DE AGUA E INFRA RIEGO/Productos Hidrofor/"
drenafor = gpd.read_file(carpeta + "drenaje_bosque_área_1_VaVII.shp")
drena_aoi = gpd.overlay(drenafor, aoi, how="intersection")
drena_aoi.to_file('TEMPORALES/clip_drenafor.shp')
drenafor, drena_aoi = None, None





cbn_ns = gpd.read_file("CAPAS/1.shp")
cbn_ns_aoi = gpd.overlay(drenafor, aoi, how="intersection")
cbn_ns_aoi.to_file('TEMPORALES/clip_drenafor.shp')
cbn_ns, cbn_ns_aoi = None, None



# %% otras pruebas que resultaron en errores
# # zona de estudio, limite de recorte.

# # cargar capas de suelos para generar un merge
# suelo6 = gpd.read_file("CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/suelos10mil_06.shp")
# suelo7 = gpd.read_file("CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/suelos10mil_07.shp")
# suelo16 = gpd.read_file("CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/suelos10mil_16.shp")

# # # ploteo de las capas para saber el contenido y como se ve visualmente
# # suelo6.plot()
# # suelo7.plot()
# # suelo16.plot()

# suelo6.head()

# # merge data... a diferencia del union, deberia unir o concatenas las bases de datos
# # en este caso, creo que este metodo no funciona por usar la funcion union.
# suel1 = gpd.overlay(suelo6, suelo7, how="union")
# suel2 = gpd.overlay(suelo16, suel1, how="union")

# suel1 = suelo6.merge(suelo6, suelo7)
# suel1.plot()



suel2.plot()

suel1  = None
# suel1, suelo6, suelo7, suelo16  = None, None, None, None





# cargar capas de propiedades para generar merge
propiedades6 = gpd.read_file("CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/suelos10mil_06.shp")
propiedades7 = gpd.read_file("CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/suelos10mil_07.shp")
propiedades8 = gpd.read_file("CAPAS/02 SUELOS/suelos_ptorres BBDD_Completa/suelos10mil_16.shp")

prop_aoi = gpd.overlay(prop2, aoi, how='intersection' )

suel1.plot()
suel2.plot()

suel1.head()
suel1.tail()




