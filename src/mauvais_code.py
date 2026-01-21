"""Module avec du code de mauvaise qualité intentionnel."""


class MaClasse:
    """Classe avec des problèmes."""
    
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.i = 9
        self.j = 10  # Trop d'attributs
        
    def methode_trop_longue(self, x):
        """Méthode avec trop de lignes."""
        result = 0
        
        # Beaucoup de code répétitif
        if x > 0:
            result += 1
        if x > 1:
            result += 1
        if x > 2:
            result += 1
        if x > 3:
            result += 1
        if x > 4:
            result += 1
        if x > 5:
            result += 1
        if x > 6:
            result += 1
        if x > 7:
            result += 1
        if x > 8:
            result += 1
        if x > 9:
            result += 1
        if x > 10:
            result += 1
        if x > 11:
            result += 1
        if x > 12:
            result += 1
        if x > 13:
            result += 1
        if x > 14:
            result += 1
        if x > 15:
            result += 1
        if x > 16:
            result += 1
        if x > 17:
            result += 1
        if x > 18:
            result += 1
        if x > 19:
            result += 1
        if x > 20:
            result += 1
            
        return result


def fonction_avec_print():
    """Fonction qui utilise print au lieu de logging."""
    print("Debug message")  # Mauvaise pratique
    print("Another debug")
    return True


# Variable globale mutable (mauvaise pratique)
LISTE_GLOBALE = []


def modifier_global():
    """Modifie une variable globale."""
    global LISTE_GLOBALE
    LISTE_GLOBALE.append(1)
    return LISTE_GLOBALE
