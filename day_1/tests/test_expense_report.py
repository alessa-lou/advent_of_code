import pytest
from expense_report import ExpenseReport

@pytest.fixture
def er():
    er = ExpenseReport()
    return er

def test_read_input(er):
    file_content = er.read_input()
    assert type(file_content) is list

def test_add_nums(er):
    sum = er.add_nums()
    assert type(sum) is int
    assert sum == 878724
    assert er.res == [2020]

def test_add_three_nums(er):
    sum = er.add_three_nums()
    assert type(sum) is list
    assert er.res_two == [2020]