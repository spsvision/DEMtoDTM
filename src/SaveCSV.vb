Sub test()

Application.DisplayAlerts = False
  strFullname = "coordinates"
ThisWorkbook.Sheets(strSourceSheet).Copy
ActiveWorkbook.SaveAs Filename:=strFullname, FileFormat:=xlCSV, CreateBackup:=True
ActiveWorkbook.Close

Application.DisplayAlerts = True

End Sub
