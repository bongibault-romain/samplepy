# lol une calculatrice trop cool


def add(x,y):  # addition
	return x+y   # ça fait la somme lol


def sous(a,b):     # moins
		return a-b


def mult(num1,num2):   # multiplier des trucs
    res=num1*num2    # calcul
    return res     # on retourne


def div(a,b):
# diviser
	if b==0:    # oups
		raise ValueError("lol tu peux pas diviser par 0")
	return a/b


def puiss(a,n):  # la puissance
	# calcul de a**n
        return a**n    # retour


def fact(n):   # factoriel !!!!
	if n<0:    # si negatif
		raise ValueError("nope")
	if n==0 or n==1:  # cas de base
		return 1    # retourne 1
	r=1   # resultat
	for i in range(2,n+1):   # boucle
		r=r*i   # multiplier
	return r   # fin


def calc(a,b,c,d,e,f,g,h):   # super fonction
	x=0   # x c'est le resultat
	if a>0:   # test a
		if b>0:   # test b
			if c>0:   # test c
				if d>0:   # test d
					if e>0:   # test e
						if f>0:   # test f
							if g>0:   # test g
								if h>0:   # test h
									x=a+b+c+d+e+f+g+h   # tout
								else:
									x=a+b+c+d+e+f+g   # sans h
							else:
								x=a+b+c+d+e+f   # sans g
						else:
							x=a+b+c+d+e   # sans f
					else:
						x=a+b+c+d   # sans e
				else:
					x=a+b+c   # sans d
			else:
				x=a+b   # sans c
		else:
			x=a   # sans b
	return x   # retour de x


def somme1(l):   # somme
	t=0   # total
	for i in l:   # boucle
		t=t+i   # ajouter
	return t   # fin


def somme2(l):   # somme aussi
	t=0   # total
	for i in l:   # boucle
		t=t+i   # ajouter
	return t   # fin
