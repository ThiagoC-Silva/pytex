import json
from openpyxl import Workbook

def cells(vehicle):
    status = False
    match_line = 1
    for record in registered_vehicles:
        match_line += 1
        if(
            vehicle['Day'] == record['Day'] and
            vehicle['Plate'] == record['Plate'] and
            vehicle['Day Period'] == record['Day Period']
        ):
            weight_column = len(registered_vehicles)
            spreadsheet.cell(row = 1, column = weight_column, value = 'Weight' )
            spreadsheet.cell(row = match_line, column = weight_column, value = vehicle['Weight'] )
            status = True
            line -= 1
        
        if not status:
            spreadsheet.cell(row  = line, column = 1, value = vehicle['Day'])
            spreadsheet.cell(row  = line, column = 2, value = vehicle['Plate'])
            spreadsheet.cell(row  = line, column = 3, value = vehicle['Description Vehicle'])
            spreadsheet.cell(row  = line, column = 4, value = vehicle['Day Period'])
            spreadsheet.cell(row  = line, column = 5, value = vehicle['Weight'])
            

file_excel = Workbook() 
spreadsheet = file_excel.active 
spreadsheet.title = 'REPORT.X'


with open('data.json', 'r') as file:
    object = json.load(file)


line = 1
registered_vehicles = []

spreadsheet.cell(row = line, column = 1, value = 'Daty')
spreadsheet.cell(row = line, column = 2, value = 'Plate')
spreadsheet.cell(row = line, column = 3, value = 'Description Vehicle')
spreadsheet.cell(row = line, column = 4, value = 'Day Period')
spreadsheet.cell(row = line, column = 4, value = 'Weight')


for vehicle in object['rows']:    
    cells(vehicle) 


print(file_excel.sheetnames)
file_excel.save("relatorio.xlsx")