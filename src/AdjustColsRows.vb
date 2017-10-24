Option Explicit

Sub MoveColumns()

With ActiveSheet
    .Columns("B:B").Cut
    .Columns("E:E").Insert Shift:=xlToRight
End With
Application.CutCopyMode = False
Columns("A").Delete
Rows("1").Delete
End Sub
