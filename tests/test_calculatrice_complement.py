import pytest
from src.calculatrice import calc, somme1, somme2

def test_calc_tout_positif():
    assert calc(1,1,1,1,1,1,1,1) == 8

def test_calc_sans_h():
    assert calc(1,1,1,1,1,1,1,0) == 7

def test_calc_sans_g():
    assert calc(1,1,1,1,1,1,0,0) == 6

def test_calc_sans_f():
    assert calc(1,1,1,1,1,0,0,0) == 5

def test_calc_sans_e():
    assert calc(1,1,1,1,0,0,0,0) == 4

def test_calc_sans_d():
    assert calc(1,1,1,0,0,0,0,0) == 3

def test_calc_sans_c():
    assert calc(1,1,0,0,0,0,0,0) == 2

def test_calc_sans_b():
    assert calc(1,0,0,0,0,0,0,0) == 1

def test_calc_negatif():
    assert calc(-1,1,1,1,1,1,1,1) == 0

def test_somme1():
    assert somme1([1,2,3]) == 6

def test_somme2():
    assert somme2([4,5,6]) == 15
