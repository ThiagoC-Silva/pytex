import json, os
from openpyxl import Workbook


def reportFolder():
    report = 'report/'
    if not os.path.exists(report):
        os.mkdir(report)

    file_name = 'report.xlsx'
    report_path = report + file_name
    file_excel.save(report_path) 


def cells(vehicle):
    status = False
    match_line = 1
    global line
    
    for record in registered_vehicles:
        match_line += 1
        if(
            vehicle['Day'] == record['Day'] and
            vehicle['Plate'] == record['Plate'] and
            vehicle['Day Period'] == record['Day Period']
        ):
            
            status = True
            weight_column = len(record) + 1
            spreadsheet.cell(row = 1, column = weight_column, value = 'Weight' )
            spreadsheet.cell(row = match_line, column = weight_column, value = vehicle['Weight'] )
            line -= 1
            break
        
    if status == False:
        spreadsheet.cell(row  = line, column = 1, value = vehicle['Day'])
        spreadsheet.cell(row  = line, column = 2, value = vehicle['Plate'])
        spreadsheet.cell(row  = line, column = 3, value = vehicle['Description Vehicle'])
        spreadsheet.cell(row  = line, column = 4, value = vehicle['Day Period'])
        spreadsheet.cell(row  = line, column = 5, value = vehicle['Weight'])
        

    registered_vehicles.append(vehicle)

file_excel = Workbook() 
spreadsheet = file_excel.active 
spreadsheet.title = 'REPORT.X'


with open('src/data.json', 'r') as file:
    object = json.load(file)


line = 1
registered_vehicles = []

spreadsheet.cell(row = line, column = 1, value = 'Day')
spreadsheet.cell(row = line, column = 2, value = 'Plate')
spreadsheet.cell(row = line, column = 3, value = 'Description Vehicle')
spreadsheet.cell(row = line, column = 4, value = 'Day Period')
spreadsheet.cell(row = line, column = 5, value = 'Weight')


for vehicle in object['rows']:    
    line += 1
    cells(vehicle)


print(file_excel.sheetnames)
reportFolder()