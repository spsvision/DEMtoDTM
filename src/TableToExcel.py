import arcpy
arcpy.env.workspace = "c:/data/output"

# Convert directly to an Excel workbook. ArcMap can only export 65535 rows though.
arcpy.TableToExcel_conversion("100x", "C:/Users/User1/Desktop/table.xlx")

# Convert to a 
arcpy.TableToDBASE_conversion(["TABLE"], "C:/output")
