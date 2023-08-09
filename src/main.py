import json
from models.workbook import WorkbookGenerator
from models.cells import Cells


record_table = []
line = 2

header = ['Day', 'Plate', 'Vehicle', 'Day Period', 'Weight']
header_generator = WorkbookGenerator(header)


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
    status =  data_vehicle.check_records(record_table)

    record_table.append(data_vehicle)
    print(status)