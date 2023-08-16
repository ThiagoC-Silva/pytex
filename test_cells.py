from pytest import fixture
from src.models.cells import Cells


@fixture
def test_cell():
    return Cells(1, 'ABC123', 'CAR-XPTO', 'DIURNO', 2.49)


def test_check_records_false(test_cell):
    test_record_list = [{'Day': 2, 'Plate': 'ABC321', 'Day Period': 'NOTURNO'}]
    status = test_cell.check_records(test_record_list)
    assert status[0] == False


def test_check_records_true(test_cell):
    test_record_list = [{'Day': 1, 'Plate': 'ABC123', 'Day Period': 'DIURNO'}]
    status = test_cell.check_records(test_record_list)
    assert status[0] == True
    