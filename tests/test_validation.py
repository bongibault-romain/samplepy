"""Tests pour le module validation."""
import pytest
from src.validation import (
    mail, tel, cp,
    majeur, mdp
)


class TestValiderEmail:
    """Tests pour la fonction valider_email."""
    
    def test_email_valide_simple(self):
        assert mail("test@example.com") is True
    
    # Manque tous les tests de cas invalides !


class TestValiderTelephoneFr:
    """Tests pour la fonction valider_telephone_fr."""
    
    def test_telephone_valide_espaces(self):
        assert tel("01 23 45 67 89") is True
        
    def test_telephone_valide_sans_espaces(self):
        assert tel("0123456789") is True
        
    def test_telephone_valide_mobile(self):
        assert tel("06 12 34 56 78") is True
        
    def test_telephone_invalide_trop_court(self):
        assert tel("0123456") is False
        
    def test_telephone_invalide_commence_par_1(self):
        assert tel("00 23 45 67 89") is False


class TestValiderCodePostalFr:
    """Tests pour la fonction valider_code_postal_fr."""
    
    def test_code_postal_valide(self):
        assert cp("75001") is True
        
    def test_code_postal_valide_corse(self):
        assert cp("20000") is True
        
    def test_code_postal_invalide_trop_court(self):
        assert cp("7500") is False
        
    def test_code_postal_invalide_trop_long(self):
        assert cp("750001") is False
        
    def test_code_postal_invalide_lettres(self):
        assert cp("7500A") is False


class TestEstMajeur:
    """Tests pour la fonction est_majeur."""
    
    def test_majeur_18_ans(self):
        assert majeur(18) is True
        
    def test_majeur_plus_de_18(self):
        assert majeur(25) is True
        
    def test_mineur_17_ans(self):
        assert majeur(17) is False
        
    def test_mineur_0_an(self):
        assert majeur(0) is False
        
    def test_age_negatif(self):
        with pytest.raises(ValueError):
            majeur(-5)


class TestValiderMotDePasse:
    """Tests pour la fonction valider_mot_de_passe."""
    
    def test_mot_de_passe_valide(self):
        assert mdp("Password123") is True
        
    def test_mot_de_passe_valide_complexe(self):
        assert mdp("MyP@ssw0rd") is True
        
    def test_mot_de_passe_trop_court(self):
        assert mdp("Pass1") is False
        
    def test_mot_de_passe_sans_majuscule(self):
        assert mdp("password123") is False
        
    def test_mot_de_passe_sans_chiffre(self):
        assert mdp("Password") is False
        
    def test_mot_de_passe_vide(self):
        assert mdp("") is False
