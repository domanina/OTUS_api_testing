import pytest


@pytest.fixture
def powers():
    new_dict = {}

    for i in range(11):
        new_dict.update({i: pow(i, 2)})
    return new_dict


@pytest.fixture
def reverse(powers):
    list_for_sort = list(powers.keys())
    list_for_sort.sort(reverse=True)
    reverse_dict = {}

    for i in list_for_sort:
        reverse_dict.update({i: powers[i]})

    return reverse_dict





