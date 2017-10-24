# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/data/output"

# Identify your local variables
inPointFeatures = "fishnet_label.shp"
inRaster = "raster.asc"
outPointFeatures = "C:/Users/User1/Desktop/fishnet_coordinated.shp"

# Ensure that the Spatial Analyst License is activated
arcpy.CheckOutExtension("Spatial")

# Execute ExtractValuesToPoints
ExtractValuesToPoints(inPointFeatures, inRaster, outPointFeatures,
                      "INTERPOLATE", "VALUE_ONLY")
