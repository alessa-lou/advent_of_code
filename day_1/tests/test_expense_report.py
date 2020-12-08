import pytest
from expense_report import ExpenseReport

def test_add_nums():
    er = ExpenseReport()
    sum = er.add_nums()
    assert type(sum) is int