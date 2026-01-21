"""Tests pour le module texte."""
import pytest
from src.texte import (
    inv, voy, palin,
    nbmots, cap, supprespace
)


class TestInverserChaine:
    """Tests pour la fonction inverser_chaine."""
    
    def test_inverser_simple(self):
        assert inv("hello") == "olleh"
        
    def test_inverser_vide(self):
        assert inv("") == ""
        
    def test_inverser_un_caractere(self):
        assert inv("a") == "a"
        
    def test_inverser_avec_espaces(self):
        assert inv("hello world") == "dlrow olleh"


class TestCompterVoyelles:
    """Tests pour la fonction compter_voyelles."""
    
    def test_compter_voyelles_simple(self):
        assert voy("hello") == 2
    
    # Beaucoup de tests manquants


class TestCompterMots:
    """Tests pour la fonction compter_mots."""
    
    def test_compter_mots_simple(self):
        assert nbmots("hello world") == 2
        
    def test_compter_mots_espaces_multiples(self):
        assert nbmots("hello   world") == 2
        
    def test_compter_mots_vide(self):
        assert nbmots("") == 0
        
    def test_compter_mots_un_mot(self):
        assert nbmots("hello") == 1
        
    def test_compter_mots_espaces_uniquement(self):
        assert nbmots("   ") == 0


class TestCapitaliserMots:
    """Tests pour la fonction capitaliser_mots."""
    
    def test_capitaliser_simple(self):
        assert cap("hello world") == "Hello World"
        
    def test_capitaliser_deja_capitalise(self):
        assert cap("Hello World") == "Hello World"
        
    def test_capitaliser_majuscules(self):
        assert cap("HELLO WORLD") == "Hello World"
        
    def test_capitaliser_vide(self):
        assert cap("") == ""


class TestSupprimerEspacesMultiples:
    """Tests pour la fonction supprimer_espaces_multiples."""
    
    def test_supprimer_espaces_doubles(self):
        assert supprespace("hello  world") == "hello world"
        
    def test_supprimer_espaces_multiples(self):
        assert supprespace("hello     world") == "hello world"
        
    def test_supprimer_espaces_debut_fin(self):
        assert supprespace("  hello world  ") == "hello world"
        
    def test_aucun_espace_multiple(self):
        assert supprespace("hello world") == "hello world"
