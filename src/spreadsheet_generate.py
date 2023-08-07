import json
from openpyxl import Workbook

def cells(vehicle):
    ...


file_excel = Workbook() 
spreadsheet = file_excel.active 
spreadsheet.title = 'REPORT.X'


with open('data.json', 'r') as file:
    object = json.load(file)


line = 1


spreadsheet.cell(row = line, column = 1, value = 'Daty')
spreadsheet.cell(row = line, column = 2, value = 'Plate')
spreadsheet.cell(row = line, column = 3, value = 'Description Vehicle')
spreadsheet.cell(row = line, column = 4, value = 'Day Period')
spreadsheet.cell(row = line, column = 4, value = 'Weight')


for vehicle in object['rows']:    
    cells(vehicle) 


print(file_excel.sheetnames)
file_excel.save("relatorio.xlsx")