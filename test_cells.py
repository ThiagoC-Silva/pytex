from pytest import fixture
from src.models.cells import Cells


@fixture
def test_cell_instance():
    return Cells(1, 'ABC123', 'CAR-XPTO', 'DIURNO', 2.49)


def test_check_records_false(test_cell_instance):
    test_cell = test_cell_instance
    test_record_list = [{'Day': 2, 'Plate': 'ABC321', 'Day Period': 'NOTURNO'}]
    status, line = test_cell.check_records(test_record_list, 3)
    assert status == False
    assert line == 3


def test_check_records_true(test_cell_instance):
    test_cell = test_cell_instance
    test_record_list = [{'Day': 1, 'Plate': 'ABC123', 'Day Period': 'DIURNO'}]
    status, line = test_cell.check_records(test_record_list, 3)
    assert status == True
    assert line < 3