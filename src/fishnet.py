# import system module
import arcpy
from arcpy import env
env.workspace = "C:/data/output"

# Set coordinate system of the output fishnet
env.outputCoordinateSystem = arcpy.SpatialReference("_UTMZone_")

# Source for the output feature class
outFeatureClass = "C:/Users/User1/Desktop/fishnet.shp"

# Set the origin
originCoordinate = 'LeftCoordinate BottomCoordinate'

# Set the orientation
yAxisCoordinate = 'LeftCoordinate BottomCoordinate'

# Dimensions for each point (ie. distance between DTM points)
cellSizeWidth = '100'
cellSizeHeight = '100'

# Number of rows and columns together with origin and opposite corner can determine the size of each cell if entered
numRows =  '0'
numColumns = '0'

oppositeCoorner = 'RightCoordinate TopCoordinate'

# Create a point label feature class 
labels = 'LABELS'
templateExtent = '#'

# Output cell can either be a POLYGON or POLYLINE
geometryType = 'POLYGON'

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate, cellSizeWidth, cellSizeHeight, numRows, numColumns, oppositeCoorner, labels, templateExtent, geometryType)
