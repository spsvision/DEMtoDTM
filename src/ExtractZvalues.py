# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/data/output"

# Set local variables
inPointFeatures = "fishnet_label.shp"
inRaster = "raster.asc"
outPointFeatures = "C:/Users/User1/Desktop/fishnet_coordinated.shp"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ExtractValuesToPoints
ExtractValuesToPoints(inPointFeatures, inRaster, outPointFeatures,
                      "INTERPOLATE", "VALUE_ONLY")
