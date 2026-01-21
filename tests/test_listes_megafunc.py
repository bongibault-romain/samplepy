import pytest
from src.listes import megafunc

def test_megafunc_vide():
    assert megafunc([]) == []

def test_megafunc_negatifs():
    assert megafunc([-1, -5, -100]) == []

def test_megafunc_petit():
    assert megafunc([1, 2, 5, 10]) == [1, 2, 5, 10]

def test_megafunc_grand():
    assert megafunc([20]) == [40]

def test_megafunc_tres_grand():
    assert megafunc([200]) == [100.0]

def test_megafunc_mix():
    assert megafunc([-5, 0, 5, 15, 150]) == [5, 30, 75.0]
