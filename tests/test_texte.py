"""Tests pour le module texte."""
import pytest
from src.texte import (
    inverser_chaine, compter_voyelles, est_palindrome,
    compter_mots, capitaliser_mots, supprimer_espaces_multiples
)


class TestInverserChaine:
    """Tests pour la fonction inverser_chaine."""
    
    def test_inverser_simple(self):
        assert inverser_chaine("hello") == "olleh"
        
    def test_inverser_vide(self):
        assert inverser_chaine("") == ""
        
    def test_inverser_un_caractere(self):
        assert inverser_chaine("a") == "a"
        
    def test_inverser_avec_espaces(self):
        assert inverser_chaine("hello world") == "dlrow olleh"


class TestCompterVoyelles:
    """Tests pour la fonction compter_voyelles."""
    
    def test_compter_voyelles_simple(self):
        assert compter_voyelles("hello") == 2
        
    def test_compter_voyelles_aucune(self):
        assert compter_voyelles("bcdfg") == 0
        
    def test_compter_voyelles_toutes(self):
        assert compter_voyelles("aeiou") == 5
        
    def test_compter_voyelles_majuscules(self):
        assert compter_voyelles("HELLO") == 2
        
    def test_compter_voyelles_accents(self):
        assert compter_voyelles("éèêë") == 4


class TestEstPalindrome:
    """Tests pour la fonction est_palindrome."""
    
    def test_palindrome_simple(self):
        assert est_palindrome("radar") is True
        
    def test_palindrome_phrase(self):
        assert est_palindrome("A man a plan a canal Panama") is True
        
    def test_non_palindrome(self):
        assert est_palindrome("hello") is False
        
    def test_palindrome_vide(self):
        assert est_palindrome("") is True
        
    def test_palindrome_un_caractere(self):
        assert est_palindrome("a") is True


class TestCompterMots:
    """Tests pour la fonction compter_mots."""
    
    def test_compter_mots_simple(self):
        assert compter_mots("hello world") == 2
        
    def test_compter_mots_espaces_multiples(self):
        assert compter_mots("hello   world") == 2
        
    def test_compter_mots_vide(self):
        assert compter_mots("") == 0
        
    def test_compter_mots_un_mot(self):
        assert compter_mots("hello") == 1
        
    def test_compter_mots_espaces_uniquement(self):
        assert compter_mots("   ") == 0


class TestCapitaliserMots:
    """Tests pour la fonction capitaliser_mots."""
    
    def test_capitaliser_simple(self):
        assert capitaliser_mots("hello world") == "Hello World"
        
    def test_capitaliser_deja_capitalise(self):
        assert capitaliser_mots("Hello World") == "Hello World"
        
    def test_capitaliser_majuscules(self):
        assert capitaliser_mots("HELLO WORLD") == "Hello World"
        
    def test_capitaliser_vide(self):
        assert capitaliser_mots("") == ""


class TestSupprimerEspacesMultiples:
    """Tests pour la fonction supprimer_espaces_multiples."""
    
    def test_supprimer_espaces_doubles(self):
        assert supprimer_espaces_multiples("hello  world") == "hello world"
        
    def test_supprimer_espaces_multiples(self):
        assert supprimer_espaces_multiples("hello     world") == "hello world"
        
    def test_supprimer_espaces_debut_fin(self):
        assert supprimer_espaces_multiples("  hello world  ") == "hello world"
        
    def test_aucun_espace_multiple(self):
        assert supprimer_espaces_multiples("hello world") == "hello world"
