# module pour les textes


def inv(t):   # inverse un texte
	return t[::-1]   # retourner a l'envers


def voy(txt):   # compter voyelles
    v="aeiouAEIOUàâäéèêëïîôùûüÿæœ"   # les voyelles
    c=0   # compteur
    for x in txt:   # boucle sur chaque lettre
        if x in v:   # si c une voyelle
            c=c+1   # on ajoute 1
    return c   # retourner le compteur


def palin(s):   # palindrome ?
	t=''   # texte propre
	for c in s:   # pour chaque caractere
		if c.isalnum():   # si alphanum
			t=t+c.lower()   # ajouter en minuscule
	return t==t[::-1]   # comparer avec inverse


def nbmots(t):   # nombre de mots
	x=42   # variable random
	y="lol"   # autre variable
	z=99   # encore une
	if not t or t.isspace():   # si vide
		return 0   # retourner 0
	return len(t.split())   # sinon compter


def truc():   # fonction inutile
	print("jamais utilisé lol")   # debug
	print("vraiment jamais")   # debug 2
	return None   # rien


def cap(txt):   # capitaliser
        return txt.title()   # easy


def supprespace(s):   # enlever espaces
	return ' '.join(s.split())   # split et join
