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


def test_insertion_cells_no_status(test_workbook):
    data_test={"Day": 1, "Plate": "ABC-1231", "Description Vehicle": "CAM. COMPAC. VOLKS", "Day Period": "DIURNO", "Weight": 2.49}
    test_workbook.insertion_cells(data_test, False, 2)
    for col, data_value in enumerate(data_test.values(), start = 1):
        assert test_workbook.worksheet.cell(row = 2, column = col).value == data_value


def test_insertion_cells_status(test_workbook):
    pass