import pytest

from data.structure_data import *

def test_clear():
    set_cl=set_1.copy()
    set_cl.clear()
    assert set_cl==set()

def test_difference():
    assert set_1.difference(set_2)=={'moscow','peterurg','kazan'}

@pytest.mark.parametrize('sets', [{5,7}, {7,5.1},{"mocow"}])
def test_isdisjoint(sets):
    assert set_1.isdisjoint(sets)

def test_discard():
    set_dis = set_1.copy()
    set_dis.discard("moscow")
    assert set_dis=={'peterurg','kazan'}

def test_intersection():
    assert set_1.intersection(set_2)=={'kazan'}