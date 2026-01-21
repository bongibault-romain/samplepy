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
    # Bug: pas de vérification de liste vide
    try:
        return sum(liste) / len(liste)
    except:
        # Mauvaise pratique: catch general exception
        pass


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


def mega_fonction(data):
    """Fonction qui fait trop de choses."""
    # Pas de type hints
    result = []
    temp = 0
    x = 1
    y = 2
    z = 3
    
    for item in data:
        if item > 0:
            temp = item
            if temp > 10:
                if temp < 100:
                    result.append(temp * 2)
                else:
                    result.append(temp / 2)
            else:
                result.append(temp)
        else:
            continue
    
    # Code mort
    if False:
        print("jamais exécuté")
    
    return result
