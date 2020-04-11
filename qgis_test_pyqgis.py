import os
# cargar capas
from qgis.core import ( 
    QgsVectorLayer
    )

# operaciones union, merge, etc
from qgis.core import ( 
    QgsGeometry
    )


os.chdir('D:/WORK/CIREN/')
print(os.getcwd())

carpeta = 'CAPAS/14 CUERPOS DE AGUA E INFRA RIEGO/Productos Hidrofor/'
path_to_drenfor = (carpeta + "drenaje_bosque_área_1_VaVII.shp")

# lee las capas como una variable
drenfor_VaVII = QgsVectorLayer((carpeta + "drenaje_bosque_área_1_VaVII.shp"), 
                                "drenfor_VaVII", "ogr")
if not drenfor_VaVII.isValid():
    print("Layer failed to load!")

drenfor_VIIIaX = QgsVectorLayer((carpeta + "drenaje_bosque_área_2_VIIIaX_S_Chiloé.shp"), 
                                "drenfor_VIIIaX", "ogr")
if not drenfor_VIIIaX.isValid():
    print("Layer failed to load!")


# merge de las capas

drenfor = QgsGeometry.merge(drenfor_VaVII, drenfor_VIIIaX)

# carga la capa como layer activo en qgis
drenfor_VaVII = iface.addVectorLayer((carpeta + "drenaje_bosque_área_1_VaVII.shp"), 
                                "drenfor_VaVII", "ogr")

drenfor_VIIIaX = iface.addVectorLayer((carpeta + "drenaje_bosque_área_2_VIIIaX_S_Chiloé.shp"), 
                                "drenfor_VIIIaX", "ogr")