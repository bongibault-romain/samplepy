"""Tests pour le module calculatrice."""
import pytest
from src.calculatrice import (
    addition, soustraction, multiplication, division,
    puissance, factorielle
)


class TestAddition:
    """Tests pour la fonction addition."""
    
    def test_addition_positifs(self):
        assert addition(2, 3) == 5
        
    def test_addition_negatifs(self):
        assert addition(-2, -3) == -5
        
    def test_addition_mixte(self):
        assert addition(-2, 3) == 1
        
    def test_addition_zero(self):
        assert addition(0, 5) == 5
        
    def test_addition_decimaux(self):
        assert addition(2.5, 3.7) == pytest.approx(6.2)


class TestSoustraction:
    """Tests pour la fonction soustraction."""
    
    def test_soustraction_positifs(self):
        assert soustraction(5, 3) == 2
        
    def test_soustraction_negatifs(self):
        assert soustraction(-5, -3) == -2
        
    def test_soustraction_resultat_negatif(self):
        assert soustraction(3, 5) == -2
        
    def test_soustraction_zero(self):
        assert soustraction(5, 0) == 5


class TestMultiplication:
    """Tests pour la fonction multiplication."""
    
    def test_multiplication_positifs(self):
        assert multiplication(4, 5) == 20
        
    def test_multiplication_negatifs(self):
        assert multiplication(-4, -5) == 20
        
    def test_multiplication_mixte(self):
        assert multiplication(-4, 5) == -20
        
    def test_multiplication_par_zero(self):
        assert multiplication(5, 0) == 0
        
    def test_multiplication_decimaux(self):
        assert multiplication(2.5, 4) == 10.0


class TestDivision:
    """Tests pour la fonction division."""
    
    def test_division_normale(self):
        assert division(10, 2) == 5
        
    def test_division_decimale(self):
        assert division(7, 2) == 3.5
        
    def test_division_par_zero(self):
        with pytest.raises(ValueError, match="Division par zéro impossible"):
            division(5, 0)
            
    def test_division_negatifs(self):
        assert division(-10, 2) == -5


class TestPuissance:
    """Tests pour la fonction puissance."""
    
    def test_puissance_positive(self):
        assert puissance(2, 3) == 8
        
    def test_puissance_zero(self):
        assert puissance(5, 0) == 1
        
    def test_puissance_un(self):
        assert puissance(5, 1) == 5
        
    def test_puissance_negative(self):
        assert puissance(2, -2) == 0.25


class TestFactorielle:
    """Tests pour la fonction factorielle."""
    
    def test_factorielle_zero(self):
        assert factorielle(0) == 1
        
    def test_factorielle_un(self):
        assert factorielle(1) == 1
        
    def test_factorielle_cinq(self):
        assert factorielle(5) == 120
        
    def test_factorielle_dix(self):
        assert factorielle(10) == 3628800
        
    def test_factorielle_negative(self):
        with pytest.raises(ValueError, match="La factorielle n'est pas définie"):
            factorielle(-5)
