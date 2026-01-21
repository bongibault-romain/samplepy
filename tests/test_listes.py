"""Tests pour le module listes."""
import pytest
from src.listes import (
    max, min, moy,
    pairs, impairs, nodup,
    fusion
)


class TestTrouverMaximum:
    """Tests pour la fonction trouver_maximum."""
    
    def test_maximum_positifs(self):
        assert max([1, 5, 3, 9, 2]) == 9
        
    def test_maximum_negatifs(self):
        assert max([-5, -1, -10, -3]) == -1
        
    def test_maximum_un_element(self):
        assert max([42]) == 42
        
    def test_maximum_liste_vide(self):
        with pytest.raises(ValueError):
            max([])


class TestTrouverMinimum:
    """Tests pour la fonction trouver_minimum."""
    
    def test_minimum_positifs(self):
        assert min([1, 5, 3, 9, 2]) == 1
        
    def test_minimum_negatifs(self):
        assert min([-5, -1, -10, -3]) == -10
        
    def test_minimum_un_element(self):
        assert min([42]) == 42
        
    def test_minimum_liste_vide(self):
        with pytest.raises(ValueError):
            min([])


class TestCalculerMoyenne:
    """Tests pour la fonction calculer_moyenne."""
    
    def test_moyenne_entiers(self):
        assert moy([1, 2, 3, 4, 5]) == 3.0
        
    def test_moyenne_avec_bug(self):
        # Ce test va échouer à cause du bug introduit
        try:
            moy([])
            assert False, "Devrait lever une exception"
        except ValueError:
            pass


class TestFiltrerPairs:
    """Tests pour la fonction filtrer_pairs."""
    
    def test_filtrer_pairs_mixte(self):
        assert pairs([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        
    def test_filtrer_pairs_tous_pairs(self):
        assert pairs([2, 4, 6, 8]) == [2, 4, 6, 8]
        
    def test_filtrer_pairs_aucun_pair(self):
        assert pairs([1, 3, 5, 7]) == []
        
    def test_filtrer_pairs_vide(self):
        assert pairs([]) == []


class TestFiltrerImpairs:
    """Tests pour la fonction filtrer_impairs."""
    
    def test_filtrer_impairs_mixte(self):
        assert impairs([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    
    def test_filtrer_impairs_tous_impairs(self):
        assert impairs([1, 3, 5, 7]) == [1, 3, 5, 7]
    
    def test_filtrer_impairs_aucun_impair(self):
        assert impairs([2, 4, 6, 8]) == []
    
    def test_filtrer_impairs_vide(self):
        assert impairs([]) == []
    def test_filtrer_impairs_tous_impairs(self):
        assert impairs([1, 3, 5, 7]) == [1, 3, 5, 7]
        
    def test_filtrer_impairs_aucun_impair(self):
        assert impairs([2, 4, 6, 8]) == []
        
    def test_filtrer_impairs_vide(self):
        assert impairs([]) == []


class TestSupprimerDoublons:
    """Tests pour la fonction supprimer_doublons."""
    
    def test_supprimer_doublons_simple(self):
        assert nodup([1, 2, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
        
    def test_supprimer_doublons_aucun(self):
        assert nodup([1, 2, 3, 4]) == [1, 2, 3, 4]
        
    def test_supprimer_doublons_tous_identiques(self):
        assert nodup([5, 5, 5, 5]) == [5]
        
    def test_supprimer_doublons_vide(self):
        assert nodup([]) == []


class TestFusionnerListes:
    """Tests pour la fonction fusionner_listes."""
    
    def test_fusionner_deux_listes(self):
        assert fusion([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
        
    def test_fusionner_liste_vide_premiere(self):
        assert fusion([], [1, 2, 3]) == [1, 2, 3]
        
    def test_fusionner_liste_vide_deuxieme(self):
        assert fusion([1, 2, 3], []) == [1, 2, 3]
        
    def test_fusionner_deux_listes_vides(self):
        assert fusion([], []) == []
