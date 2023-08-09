import json
from models.workbook import WorkbookGenerator
from models.cells import Cells


record_table = []
line = 2

header = ['Day', 'Plate', 'Vehicle', 'Day Period', 'Weight']
workbook = WorkbookGenerator(header)


with open('src/data.json', 'r') as file:
    data =  json.load(file)


for data_row in data['rows']:
    data_vehicle = Cells(
        data_row['Day'], 
        data_row['Plate'], 
        data_row['Description Vehicle'], 
        data_row['Day Period'], 
        data_row['Weight']
    )
    status, line = data_vehicle.check_records(record_table, line)
    if status == False:
        record_table.append(data_row)

    workbook.insertion_cells(data_row, status, line)
    line += 1

    
    
