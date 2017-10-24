# DEMtoDTM
Convert high resolution DEMs to DTM elevation points using ArcGIS, Microsoft Excel, and the Python module. However, it can be done all together by executing Python and Visual Basic files individually.

## Files must be run in this order:
### ArcGIS
fishnet.py --> ExtractZValues.py --> ExtractXYValues.py --> TableToExcel.py -->
### Excel/Visual Basic Application
AdjustColsRows.vb --> FilterRows.vb --> SaveCSV.vb -->
### Python
csvTopts.py

