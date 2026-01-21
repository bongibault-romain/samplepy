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
        
    # Tests manquants pour négatifs, mixte, etc.


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
    
    # Test de division par zéro manquant !


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
