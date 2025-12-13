class Arbre:
	def __init__(self, valeur,pere,poids):
		self.valeur = valeur
		self.gauche = None
		self.droite = None
		self.pere = pere
		self.poids=poids


	
	


class Sdd:
	def __init__(self):
		self.racine = Arbre ("special",None,0)
		self.chemainSpecial = self.racine
		self.valeurs={"special":''}