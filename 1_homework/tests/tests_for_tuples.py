import pytest

from data.structure_data import *


def test_item():
    assert tuple_1[0] == 1


def test_item_inside():
    assert tuple_3[1][2]==3.1415


def test_len():
    assert len(tuple_2) == 4


def test_concatenations():
    tuple_con=tuple_1+tuple_2
    expected_tuple=(1, 'apple', None, 1, 2, 4, 4)
    assert tuple_con==expected_tuple


@pytest.mark.parametrize('params', [tuple_1, tuple_2])
def test_type(params):
    assert type(params)==tuple



