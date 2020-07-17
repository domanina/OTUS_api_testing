import pytest

from data.structure_data import *


@pytest.mark.parametrize('params', ['param1', 'param2'])
def test_append(params):
    list_app = list_1.copy()
    list_app.append(params)
    assert list_app == [1, 3, 3, 4, 6, 2, params]


def test_extend():
    list_ex = list_1.copy()
    list_ex.extend(['ex'])
    assert list_ex == [1, 3, 3, 4, 6, 2, 'ex']


def test_insert():
    list_ins = list_1.copy()
    list_ins.insert(0, 'ins')
    assert list_ins == ['ins', 1, 3, 3, 4, 6, 2]


def test_remove():
    list_rem = list_1.copy()
    list_rem.remove(1)
    assert list_rem == [3, 3, 4, 6, 2]


def test_reverse():
    list_rev = list_1.copy()
    list_rev.reverse()
    assert list_rev == [2, 6, 4, 3, 3, 1]
