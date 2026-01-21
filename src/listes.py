"""Module de manipulation de listes."""


def trouver_maximum(liste: list) -> float:
    """Trouve le maximum dans une liste.
    
    Args:
        liste: Liste de nombres
        
    Returns:
        Le plus grand nombre
        
    Raises:
        ValueError: Si la liste est vide
    """
    if not liste:
        raise ValueError("La liste ne peut pas être vide")
    return max(liste)


def trouver_minimum(liste: list) -> float:
    """Trouve le minimum dans une liste.
    
    Args:
        liste: Liste de nombres
        
    Returns:
        Le plus petit nombre
        
    Raises:
        ValueError: Si la liste est vide
    """
    if not liste:
        raise ValueError("La liste ne peut pas être vide")
    return min(liste)


def calculer_moyenne(liste: list) -> float:
    """Calcule la moyenne d'une liste de nombres.
    
    Args:
        liste: Liste de nombres
        
    Returns:
        La moyenne
        
    Raises:
        ValueError: Si la liste est vide
    """
    if not liste:
        raise ValueError("La liste ne peut pas être vide")
    return sum(liste) / len(liste)


def filtrer_pairs(liste: list) -> list:
    """Filtre les nombres pairs d'une liste.
    
    Args:
        liste: Liste de nombres
        
    Returns:
        Liste contenant uniquement les nombres pairs
    """
    return [x for x in liste if x % 2 == 0]


def filtrer_impairs(liste: list) -> list:
    """Filtre les nombres impairs d'une liste.
    
    Args:
        liste: Liste de nombres
        
    Returns:
        Liste contenant uniquement les nombres impairs
    """
    return [x for x in liste if x % 2 != 0]


def supprimer_doublons(liste: list) -> list:
    """Supprime les doublons d'une liste en préservant l'ordre.
    
    Args:
        liste: Liste avec potentiellement des doublons
        
    Returns:
        Liste sans doublons
    """
    resultat = []
    for element in liste:
        if element not in resultat:
            resultat.append(element)
    return resultat


def fusionner_listes(liste1: list, liste2: list) -> list:
    """Fusionne deux listes.
    
    Args:
        liste1: Première liste
        liste2: Deuxième liste
        
    Returns:
        Liste fusionnée
    """
    return liste1 + liste2
