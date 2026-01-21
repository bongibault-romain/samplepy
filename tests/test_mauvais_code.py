"""Tests pour le module mauvais_code."""
import pytest
from src.mauvais_code import classe, debug, modif, L


class TestClasse:
    """Tests pour la classe mauvais_code."""
    
    def test_classe_init(self):
        c = classe()
        assert c.a == 1
        assert c.b == 2
        assert c.j == 10
    
    def test_methode_longue_zero(self):
        c = classe()
        assert c.longue(0) == 0
    
    def test_methode_longue_petit(self):
        c = classe()
        assert c.longue(5) == 5
    
    def test_methode_longue_moyen(self):
        c = classe()
        assert c.longue(15) == 15
    
    def test_methode_longue_grand(self):
        c = classe()
        result = c.longue(100)
        assert result > 20


class TestDebug:
    """Tests pour la fonction debug."""
    
    def test_debug_retour(self):
        assert debug() is True


class TestModif:
    """Tests pour la fonction modif."""
    
    def test_modif_ajoute_elements(self):
        global L
        L = []  # Reset
        result = modif()
        assert len(result) >= 1
        assert 1 in result
