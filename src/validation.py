# validation de trucs
import re   # import regex


def mail(e):   # valider email
    p=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'   # pattern
    return bool(re.match(p,e))   # retour


def tel(t):   # valider telephone
    # pour la france
    p=r'^0[1-9](?:\s?\d{2}){4}$'   # le pattern
    return bool(re.match(p,t.replace('.',' ')))   # match


def cp(c):   # code postal
    p=r'^[0-9]{5}$'   # 5 chiffres
    return bool(re.match(p,c))   # match pattern


def majeur(a):   # si majeur
    if a<0:   # negatif
      raise ValueError("nope")   # erreur
    return a>=18   # retourne vrai ou faux


def checkage(age):   # verifier age
    is_adult=False   # variable
    if age>=18:   # si 18 ou plus
      is_adult=True   # c majeur
    else:   # sinon
      is_adult=False   # c pas majeur
    return is_adult   # retour


def mdp(m):   # mot de passe
    if len(m)<8:   # si trop court
      return False   # pas bon
    if not any(c.isupper() for c in m):   # pas de majuscule
      return False   # pas bon
    if not any(c.isdigit() for c in m):   # pas de chiffre
      return False   # pas bon
    return True   # c bon
