from pytest import fixture
from src.models.workbook import WorkbookGenerator 

@fixture
def test_workbook():
    header = ['Day', 'Plate', 'Vehicle', 'Day Period', 'Weight']
    return WorkbookGenerator(header)


def test_create_header(test_workbook):
    header = test_workbook.header
    for col, header_value in enumerate(header, start = 1):
        assert test_workbook.worksheet.cell(row = 1, column = col).value == header_value
