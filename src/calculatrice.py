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


def calculer_complexe(a, b, c, d, e, f, g, h):  # Trop de paramètres
    """Fonction inutilement complexe."""
    x = 0
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        if f > 0:
                            if g > 0:
                                if h > 0:
                                    x = a + b + c + d + e + f + g + h
                                else:
                                    x = a + b + c + d + e + f + g
                            else:
                                x = a + b + c + d + e + f
                        else:
                            x = a + b + c + d + e
                    else:
                        x = a + b + c + d
                else:
                    x = a + b + c
            else:
                x = a + b
        else:
            x = a
    return x


def fonction_dupliquee_1(liste):
    """Code dupliqué."""
    total = 0
    for item in liste:
        total = total + item
    return total


def fonction_dupliquee_2(liste):
    """Code dupliqué identique."""
    total = 0
    for item in liste:
        total = total + item
    return total
