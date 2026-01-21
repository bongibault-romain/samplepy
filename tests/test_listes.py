"""Tests pour le module listes."""
import pytest
from src.listes import (
    trouver_maximum, trouver_minimum, calculer_moyenne,
    filtrer_pairs, filtrer_impairs, supprimer_doublons,
    fusionner_listes
)


class TestTrouverMaximum:
    """Tests pour la fonction trouver_maximum."""
    
    def test_maximum_positifs(self):
        assert trouver_maximum([1, 5, 3, 9, 2]) == 9
        
    def test_maximum_negatifs(self):
        assert trouver_maximum([-5, -1, -10, -3]) == -1
        
    def test_maximum_un_element(self):
        assert trouver_maximum([42]) == 42
        
    def test_maximum_liste_vide(self):
        with pytest.raises(ValueError, match="La liste ne peut pas être vide"):
            trouver_maximum([])


class TestTrouverMinimum:
    """Tests pour la fonction trouver_minimum."""
    
    def test_minimum_positifs(self):
        assert trouver_minimum([1, 5, 3, 9, 2]) == 1
        
    def test_minimum_negatifs(self):
        assert trouver_minimum([-5, -1, -10, -3]) == -10
        
    def test_minimum_un_element(self):
        assert trouver_minimum([42]) == 42
        
    def test_minimum_liste_vide(self):
        with pytest.raises(ValueError, match="La liste ne peut pas être vide"):
            trouver_minimum([])


class TestCalculerMoyenne:
    """Tests pour la fonction calculer_moyenne."""
    
    def test_moyenne_entiers(self):
        assert calculer_moyenne([1, 2, 3, 4, 5]) == 3.0
        
    def test_moyenne_decimaux(self):
        assert calculer_moyenne([1.5, 2.5, 3.5]) == pytest.approx(2.5)
        
    def test_moyenne_un_element(self):
        assert calculer_moyenne([42]) == 42.0
        
    def test_moyenne_liste_vide(self):
        with pytest.raises(ValueError, match="La liste ne peut pas être vide"):
            calculer_moyenne([])


class TestFiltrerPairs:
    """Tests pour la fonction filtrer_pairs."""
    
    def test_filtrer_pairs_mixte(self):
        assert filtrer_pairs([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        
    def test_filtrer_pairs_tous_pairs(self):
        assert filtrer_pairs([2, 4, 6, 8]) == [2, 4, 6, 8]
        
    def test_filtrer_pairs_aucun_pair(self):
        assert filtrer_pairs([1, 3, 5, 7]) == []
        
    def test_filtrer_pairs_vide(self):
        assert filtrer_pairs([]) == []


class TestFiltrerImpairs:
    """Tests pour la fonction filtrer_impairs."""
    
    def test_filtrer_impairs_mixte(self):
        assert filtrer_impairs([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
        
    def test_filtrer_impairs_tous_impairs(self):
        assert filtrer_impairs([1, 3, 5, 7]) == [1, 3, 5, 7]
        
    def test_filtrer_impairs_aucun_impair(self):
        assert filtrer_impairs([2, 4, 6, 8]) == []
        
    def test_filtrer_impairs_vide(self):
        assert filtrer_impairs([]) == []


class TestSupprimerDoublons:
    """Tests pour la fonction supprimer_doublons."""
    
    def test_supprimer_doublons_simple(self):
        assert supprimer_doublons([1, 2, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
        
    def test_supprimer_doublons_aucun(self):
        assert supprimer_doublons([1, 2, 3, 4]) == [1, 2, 3, 4]
        
    def test_supprimer_doublons_tous_identiques(self):
        assert supprimer_doublons([5, 5, 5, 5]) == [5]
        
    def test_supprimer_doublons_vide(self):
        assert supprimer_doublons([]) == []


class TestFusionnerListes:
    """Tests pour la fonction fusionner_listes."""
    
    def test_fusionner_deux_listes(self):
        assert fusionner_listes([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
        
    def test_fusionner_liste_vide_premiere(self):
        assert fusionner_listes([], [1, 2, 3]) == [1, 2, 3]
        
    def test_fusionner_liste_vide_deuxieme(self):
        assert fusionner_listes([1, 2, 3], []) == [1, 2, 3]
        
    def test_fusionner_deux_listes_vides(self):
        assert fusionner_listes([], []) == []
