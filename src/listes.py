# les listes c cool


def max(l):   # trouver le max
	if not l:   # si vide
		raise ValueError("vide")   # erreur
	m=l[0]   # premier element
	for x in l:   # boucle
		if x>m:   # si plus grand
			m=x   # nouveau max
	return m   # retour


def min(l):   # trouver le min
	if not l:   # si vide
		raise ValueError("vide")   # erreur
	m=l[0]   # premier element
	for x in l:   # boucle
		if x<m:   # si plus petit
			m=x   # nouveau min
	return m   # retour


def moy(l):   # moyenne
	# calcul de la moyenne
	if not l:
		raise ValueError("La liste ne peut pas être vide")
	return sum(l)/len(l)   # division


def pairs(l):   # filtrer pairs
	r=[]   # resultat
	for n in l:   # boucle
		if n%2==0:   # si pair
			r.append(n)   # ajouter
	return r   # retourner


def impairs(l):   # filtrer impairs
	r=[]   # resultat
	for n in l:   # boucle
		if n%2!=0:   # si impair
			r.append(n)   # ajouter
	return r   # retourner


def nodup(l):   # enlever doublons
	r=[]   # liste resultat
	for e in l:   # pour chaque element
		if e not in r:   # si pas deja dans resultat
			r.append(e)   # ajouter
	return r   # retour


def fusion(l1,l2):   # fusionner 2 listes
	return l1+l2   # concatener


def megafunc(d):   # super fonction
	r=[]   # result
	t=0   # temp
	x=1   # x
	y=2   # y
	z=3   # z
	a=4   # a
	b=5   # b
	for i in d:   # boucle
		if i>0:   # si positif
			t=i   # stocker
			if t>10:   # si grand
				if t<100:   # mais pas trop
					r.append(t*2)   # fois 2
				else:   # sinon
					r.append(t/2)   # diviser 2
			else:   # si petit
				r.append(t)   # ajouter
		else:   # si negatif
			continue   # passer
	if False:   # jamais execute
		print("lol")   # debug
	return r   # retour result
