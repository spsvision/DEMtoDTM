import arcpy
from arcpy import env
env.workspace = "C:/data/output"

arcpy.AddXY_management("C:/Users/User1/Desktop/fishnet.shp")
