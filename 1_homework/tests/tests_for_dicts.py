import pytest
import math

from data.structure_data import *


def test_update():
    dict_upd = dic_1.copy()
    dict_upd.update({7: 49, 8: 64})
    expected_dict={0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    assert dict_upd == expected_dict


def test_get():
    assert dic_2.get('name') == 'John'


def test_pop():
    dict_pop = dic_1.copy()
    dict_pop.pop(5)
    assert dict_pop == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 6: 36}


def test_join():
    # используем ярлык
    dic_join = {**dic_1, **dic_2}
    assert dic_join == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 'name': 'John', 'surname': 'Malkovic', 'age': 65}


def test_sort_reverse(reverse):
    assert reverse == {10: 100, 9: 81, 8: 64, 7: 49, 6: 36, 5: 25, 4: 16, 3: 9, 2: 4, 1: 1, 0: 0}
