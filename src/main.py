import json
from models.workbook import WorkbookGenerator

header = ['Day', 'Plate', 'Vehicle', 'Day Period', 'Weight']
header_generator = WorkbookGenerator(header)


# with open('data.json', 'r') as file:
#     data =  json.load(file)


# for register in data['rows']:
