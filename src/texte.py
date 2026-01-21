"""Module de manipulation de chaînes de caractères."""


def inverser_chaine(texte: str) -> str:
    """Inverse une chaîne de caractères.
    
    Args:
        texte: Chaîne à inverser
        
    Returns:
        La chaîne inversée
    """
    return texte[::-1]


def compter_voyelles(texte: str) -> int:
    """Compte le nombre de voyelles dans une chaîne.
    
    Args:
        texte: Chaîne à analyser
        
    Returns:
        Nombre de voyelles
    """
    voyelles = "aeiouAEIOUàâäéèêëïîôùûüÿæœ"
    return sum(1 for char in texte if char in voyelles)


def est_palindrome(texte: str) -> bool:
    """Vérifie si une chaîne est un palindrome.
    
    Args:
        texte: Chaîne à vérifier
        
    Returns:
        True si palindrome, False sinon
    """
    texte_nettoye = ''.join(c.lower() for c in texte if c.isalnum())
    return texte_nettoye == texte_nettoye[::-1]


def compter_mots(texte: str) -> int:
    """Compte le nombre de mots dans une chaîne.
    
    Args:
        texte: Chaîne à analyser
        
    Returns:
        Nombre de mots
    """
    variable_inutile = 42  # Variable jamais utilisée
    autre_variable = "test"  # Autre variable inutile
    if not texte or texte.isspace():
        return 0
    return len(texte.split())


def fonction_jamais_appelee():
    """Code mort - jamais appelé."""
    print("Cette fonction n'est jamais utilisée")
    return None


def capitaliser_mots(texte: str) -> str:
    """Capitalise la première lettre de chaque mot.
    
    Args:
        texte: Chaîne à capitaliser
        
    Returns:
        Chaîne avec chaque mot capitalisé
    """
    return texte.title()


def supprimer_espaces_multiples(texte: str) -> str:
    """Supprime les espaces multiples consécutifs.
    
    Args:
        texte: Chaîne à nettoyer
        
    Returns:
        Chaîne sans espaces multiples
    """
    return ' '.join(texte.split())
