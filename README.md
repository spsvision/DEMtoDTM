# DEMtoDTM
Convert high resolution Digital Elevation Models (DEM) to Digital Terrain Model (DTM) elevation points using ArcGIS, Microsoft Excel, and the Python module. However, it can be done all together by executing Python and Visual Basic files individually.

## Files must be run in this order:
### Python Compiler
fishnet.py --> ExtractZValues.py --> ExtractXYValues.py --> TableToExcel.py -->
### Excel/Visual Basic Application
AdjustColsRows.vb --> FilterRows.vb --> SaveCSV.vb -->
### Python (Optional)
csvTopts.py
The Alternative would be to open the file in notepad or another text editor and save it as a .PTS file.
