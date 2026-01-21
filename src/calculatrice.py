"""Module de calculs mathématiques."""


def addition(a: float, b: float) -> float:
    """Additionne deux nombres.
    
    Args:
        a: Premier nombre
        b: Deuxième nombre
        
    Returns:
        La somme de a et b
    """
    return a + b


def soustraction(a: float, b: float) -> float:
    """Soustrait deux nombres.
    
    Args:
        a: Premier nombre
        b: Deuxième nombre
        
    Returns:
        La différence entre a et b
    """
    return a - b


def multiplication(a: float, b: float) -> float:
    """Multiplie deux nombres.
    
    Args:
        a: Premier nombre
        b: Deuxième nombre
        
    Returns:
        Le produit de a et b
    """
    return a * b


def division(a: float, b: float) -> float:
    """Divise deux nombres.
    
    Args:
        a: Numérateur
        b: Dénominateur
        
    Returns:
        Le quotient de a par b
        
    Raises:
        ValueError: Si b est égal à 0
    """
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def puissance(a: float, n: int) -> float:
    """Calcule a à la puissance n.
    
    Args:
        a: Base
        n: Exposant
        
    Returns:
        a^n
    """
    return a ** n


def factorielle(n: int) -> int:
    """Calcule la factorielle de n.
    
    Args:
        n: Nombre entier positif
        
    Returns:
        n!
        
    Raises:
        ValueError: Si n est négatif
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
