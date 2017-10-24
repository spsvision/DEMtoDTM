Sub Delete_Rows()
  Dim rng As Range, cell As Range, del As Range
  Set rng = Intersect(Range("C2:C10"), ActiveSheet.UsedRange)
  For Each cell In rng
' Enter -1 or whatever null value is returned for points on the grid not covered by the raster
    If (cell.Value) = "-1" 
    Then
      If del Is Nothing Then
        Set del = cell
      Else: Set del = Union(del, cell)
      End If
    End If
  Next cell
  On Error Resume Next
  del.EntireRow.Delete
End Sub
