## NO FUNCIONA para dichas capas

# We will locate all the .shp files in the data directory and hand them to the
# saga:mergeshapeslayers object in order to merge them.


# 1. Start QGIS.
# 2. From the Plugins menu, select Python Console.
# 3. Import the Python glob module for wildcard file matching:
import glob
# 4. Next, import the processing module for the merge algorithm:
import processing
# 5. Now, specify the path of our data directory:
pth = "D:/WORK/CIREN/CAPAS/14 CUERPOS DE AGUA E INFRA RIEGO/Productos Hidrofor/"
# 6. Locate all the .shp files:
files = glob.glob(pth + "drenaje_bosque_*.shp")
# 7. Then, specify the output name of the merged shapefile:
out = "D:/WORK/CIREN/TEMPORALES/" + "merge_drenaje.shp"
# 8. Finally, run the algorithm that will load the merged shapefile on to the map:
processing.runandload("saga:mergeshapeslayers",files.pop(0),";".join(files),out)
