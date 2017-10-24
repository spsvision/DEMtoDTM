Sub test()

Application.DisplayAlerts = False

ThisWorkbook.Sheets(strSourceSheet).Copy
ActiveWorkbook.SaveAs Filename:=strFullname, FileFormat:=xlCSV, CreateBackup:=True
ActiveWorkbook.Close

Application.DisplayAlerts = True

End Sub
