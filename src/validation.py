"""Module de validation de données."""
import re


def valider_email(email: str) -> bool:
    """Valide une adresse email.
    
    Args:
        email: Adresse email à valider
        
    Returns:
        True si l'email est valide, False sinon
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def valider_telephone_fr(telephone: str) -> bool:
    """Valide un numéro de téléphone français.
    
    Args:
        telephone: Numéro de téléphone à valider
        
    Returns:
        True si le téléphone est valide, False sinon
    """
    # Format: 0X XX XX XX XX ou 0XXXXXXXXX
    pattern = r'^0[1-9](?:\s?\d{2}){4}$'
    return bool(re.match(pattern, telephone.replace('.', ' ')))


def valider_code_postal_fr(code_postal: str) -> bool:
    """Valide un code postal français.
    
    Args:
        code_postal: Code postal à valider
        
    Returns:
        True si le code postal est valide, False sinon
    """
    pattern = r'^[0-9]{5}$'
    return bool(re.match(pattern, code_postal))


def est_majeur(age: int) -> bool:
    """Vérifie si une personne est majeure.
    
    Args:
        age: Âge de la personne
        
    Returns:
        True si majeur (>= 18 ans), False sinon
        
    Raises:
        ValueError: Si l'âge est négatif
    """
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")
    return age >= 18


def valider_mot_de_passe(mot_de_passe: str) -> bool:
    """Valide un mot de passe (min 8 caractères, une majuscule, un chiffre).
    
    Args:
        mot_de_passe: Mot de passe à valider
        
    Returns:
        True si le mot de passe est valide, False sinon
    """
    if len(mot_de_passe) < 8:
        return False
    if not any(c.isupper() for c in mot_de_passe):
        return False
    if not any(c.isdigit() for c in mot_de_passe):
        return False
    return True
