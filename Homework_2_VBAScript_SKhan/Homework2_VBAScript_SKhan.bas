Attribute VB_Name = "Module2"
Sub stock()

    Dim ticker As String
    Dim stock_volume As Double
    Dim row As Integer
    Dim WS_Count As Integer
    Dim x As Integer
    stock_volume = 0
    row = 2
   
    WS_Count = ActiveWorkbook.Worksheets.Count
   
    Dim lastrow As Long
    Dim sht As Worksheet
    
    For x = 1 To WS_Count
        
        Set sht = ActiveWorkbook.Worksheets(x)
        lastrow = sht.Cells(sht.Rows.Count, "A").End(xlUp).row
        sht.Range("J1").Value = "Ticker"
        sht.Range("K1").Value = "Total Stock Volume"
        For I = 2 To lastrow
    
         If sht.Cells(I + 1, 1).Value <> sht.Cells(I, 1).Value Then
            
            ticker = sht.Cells(I, 1).Value
            sht.Range("J" & row).Value = ticker
            
            stock_volume = stock_volume + sht.Cells(I, 7).Value
            sht.Range("k" & row).Value = stock_volume
            
            row = row + 1
            stock_volume = 0
            
         Else
         
            stock_volume = stock_volume + sht.Cells(I, 7).Value
        
        End If
    Next I
    
    row = 2
    
   Next x

End Sub



