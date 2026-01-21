"""Tests pour le module validation."""
import pytest
from src.validation import (
    valider_email, valider_telephone_fr, valider_code_postal_fr,
    est_majeur, valider_mot_de_passe
)


class TestValiderEmail:
    """Tests pour la fonction valider_email."""
    
    def test_email_valide_simple(self):
        assert valider_email("test@example.com") is True
    
    # Manque tous les tests de cas invalides !


class TestValiderTelephoneFr:
    """Tests pour la fonction valider_telephone_fr."""
    
    def test_telephone_valide_espaces(self):
        assert valider_telephone_fr("01 23 45 67 89") is True
        
    def test_telephone_valide_sans_espaces(self):
        assert valider_telephone_fr("0123456789") is True
        
    def test_telephone_valide_mobile(self):
        assert valider_telephone_fr("06 12 34 56 78") is True
        
    def test_telephone_invalide_trop_court(self):
        assert valider_telephone_fr("0123456") is False
        
    def test_telephone_invalide_commence_par_1(self):
        assert valider_telephone_fr("00 23 45 67 89") is False


class TestValiderCodePostalFr:
    """Tests pour la fonction valider_code_postal_fr."""
    
    def test_code_postal_valide(self):
        assert valider_code_postal_fr("75001") is True
        
    def test_code_postal_valide_corse(self):
        assert valider_code_postal_fr("20000") is True
        
    def test_code_postal_invalide_trop_court(self):
        assert valider_code_postal_fr("7500") is False
        
    def test_code_postal_invalide_trop_long(self):
        assert valider_code_postal_fr("750001") is False
        
    def test_code_postal_invalide_lettres(self):
        assert valider_code_postal_fr("7500A") is False


class TestEstMajeur:
    """Tests pour la fonction est_majeur."""
    
    def test_majeur_18_ans(self):
        assert est_majeur(18) is True
        
    def test_majeur_plus_de_18(self):
        assert est_majeur(25) is True
        
    def test_mineur_17_ans(self):
        assert est_majeur(17) is False
        
    def test_mineur_0_an(self):
        assert est_majeur(0) is False
        
    def test_age_negatif(self):
        with pytest.raises(ValueError, match="L'âge ne peut pas être négatif"):
            est_majeur(-5)


class TestValiderMotDePasse:
    """Tests pour la fonction valider_mot_de_passe."""
    
    def test_mot_de_passe_valide(self):
        assert valider_mot_de_passe("Password123") is True
        
    def test_mot_de_passe_valide_complexe(self):
        assert valider_mot_de_passe("MyP@ssw0rd") is True
        
    def test_mot_de_passe_trop_court(self):
        assert valider_mot_de_passe("Pass1") is False
        
    def test_mot_de_passe_sans_majuscule(self):
        assert valider_mot_de_passe("password123") is False
        
    def test_mot_de_passe_sans_chiffre(self):
        assert valider_mot_de_passe("Password") is False
        
    def test_mot_de_passe_vide(self):
        assert valider_mot_de_passe("") is False
