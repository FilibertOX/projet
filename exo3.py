from sdd import Arbre, Sdd
from exo2 import lecture, ecriture


def code_utf8(s):
    # éviter d'appeler le paramètre `str`
    b = s.encode('utf-8')   # bytes
    bits = []
    for byte in b:          # byte est un entier 0..255
        bits.append(format(byte, '08b'))  # 8 bits, avec zéros initiaux
    return ''.join(bits)

def compresion(text):
	H=Sdd()
	#print(H.valeurs)
	i=0
	res=""
	while i < len(text): 
		#afficherArbre(H.racine)
		#print (i)
		#print("lecture de la lettre ",text[i])
		
		
		s=text[i]
		if s in H.valeurs:
			res+=H.valeurs[s]
		else:
			res+=H.valeurs["special"]+code_utf8(s)
		#print(res)
		
		H=modification(H,s)
		i+=1
	#afficherArbre(H.racine)
	return res


def decompression(textC):
	H=Sdd()
	i=0

	if textC[0] == '0':
		lettre=textC[0:8]
		i+=7
	elif textC[0:3] == "110":
		lettre=textC[0:16]
		i+=15
	elif textC[0:4] == "1110":
		lettre=textC[0:24]
		i+=23
	else:
		lettre=textC[0:32]
		i+=31

	# découpe `lettre` en paquets de 8 bits, convertit en octets puis décode en UTF-8
	octets = [lettre[i:i+8] for i in range(0, len(lettre), 8)]
	data = bytes(int(b, 2) for b in octets)
	try:
		s = data.decode("utf-8")
	except UnicodeDecodeError:
		# tentative de récupération: remplace les octets invalides
		s = data.decode("utf-8", errors='replace')
	res = s


	H=modification(H,s)

	
	i+=1
	arbre=H.racine
	while i < len(textC):
		#print("p",i)
		code=''
		if textC[i]=='0':
			arbre=arbre.gauche
		elif textC[i]=='1':
			arbre=arbre.droite
		if arbre.valeur is not None:
			if arbre.valeur=="special":
				i+=1
				"""print("n",i)
				print("nouvelle lettre")""" 

				if textC[i] == '0':
					lettre=textC[i:i+8]
					i+=7
				elif textC[i:i+3] == "110":
					lettre=textC[i:i+16]
					i+=15
				elif textC[i:i+4] == "1110":
					lettre=textC[i:i+24]
					i+=23
				else:
					lettre=textC[i:i+32]
					i+=31
				"""print("lettre lue :",lettre)"""
				# découpe `lettre` en paquets de 8 bits, convertit en octets puis décode en UTF-8
				octets = [lettre[i:i+8] for i in range(0, len(lettre), 8)]
				data = bytes(int(b, 2) for b in octets)
				try:
					s = data.decode("utf-8")
				except UnicodeDecodeError:
					s = data.decode("utf-8", errors='replace')
				#print("lettre lue :",s)
				res += s
				#print(textC[i::])
			else:
				"""print("on connait la lettre lue :",arbre.valeur)
				print("code :",H.valeurs[arbre.valeur])
				print(textC[i::])"""
				s=arbre.valeur
				#print("lettre lue :",s)
				res+=s
				#print(textC[i::])

			#print (res)
			H=modification(H,s)
			arbre=H.racine
		
		i+=1
	return res
		


def finBloc(noeud,suivants):
	H=noeud
	
	if H==suivants[-1]:
		return H
	Hsuivant=suivants[suivants.index(H)+1]
	while H.poids==Hsuivant.poids:
		if Hsuivant==suivants[-1]:
			return H
		H=Hsuivant
		Hsuivant=suivants[suivants.index(H)+1]
		
	#print("fin",H.valeur)
	return H



def modification(sdd,s):
	H=sdd.racine
	#print(sdd.valeurs)
	if H.valeur=="special":
		H.valeur=None
		H.poids=1
		H.droite=Arbre(s,H,1)
		H.gauche=Arbre("special",H,0)
		sdd.valeurs["special"]='0'
		sdd.valeurs[s]='1'
		sdd.cheminSpecial=H.gauche
		
		#afficherArbre(H)
		return sdd
	elif s not in sdd.valeurs:
		q=sdd.cheminSpecial.pere
		newNoeud=Arbre(None,q,1)
		newNoeud.gauche=sdd.cheminSpecial
		sdd.cheminSpecial.pere=newNoeud
		newNoeud.droite=Arbre(s,newNoeud,1)
		q.gauche=newNoeud


		sdd.valeurs[s]=sdd.valeurs["special"]+'1'
		sdd.valeurs["special"]+='0'
	
		
	else:
		q=feuille(sdd,s)
		suivants=suivantsList(suivantsTab(sdd.racine,[],0))
		#afficherSuiv(suivants)
		if q.pere.gauche==sdd.cheminSpecial and q.pere == finBloc(q,suivants):
			"""print("ici")
			print("feuille",q,q,q.valeur)"""
			q.poids+=1
			#print(q.poids)
			q=q.pere
	return traitement(sdd,q)
			

def feuille(sdd,s):
	H=sdd.racine
	chemin=sdd.valeurs[s]
	i=0
	while i < len(chemin):
		if chemin[i]=='0':
			H=H.gauche
		else:
			H=H.droite
		i+=1
	return H

"""
def traitement(H,Q):

	suivants=suivantsList(suivantsTab(H.racine,[],0))

	
	Qi=Q

	while Qi is not None:
		if Qi.pere
		Qi.poids+=1
		Qisuivant=suivants[suivants.index(Qi)+1]
		if Qi.poids >= Qisuivant.poids:
			
			m=Qi
			b=finBloc(m,suivants)
			print	("Echange entre ",m.valeur," et ",b.valeur)
			echanger(H,m,b)
			
			return traitement(H,m.pere)


		Qi=Qi.pere
	return H
"""


def traitement(H,Q):
	#print("heho")
	suivants=suivantsList(suivantsTab(H.racine,[],0))
	#afficherSuiv(suivants)
	Qi=Q
	Gamma_Q=[Qi]
	incrementable=True
	while Qi.pere is not None:
		Qisuivant=suivants[suivants.index(Qi)+1]
		if Qi.poids >= Qisuivant.poids and incrementable==True:
			incrementable=False
			m=Qi
		Qi=Qi.pere
		Gamma_Q.append(Qi)
	if incrementable:
		for noeud in Gamma_Q:
			noeud.poids+=1
		return H
	else: 
		b=finBloc(m,suivants)
		for noeud in Gamma_Q:
			if noeud==m:
				noeud.poids+=1
				break	
			
			noeud.poids+=1
		if m!=b:
			"""afficherArbre(H.racine)
			print	("Echange entre ",m," et ",b)"""
			echanger(H,m,b)
		return traitement(H,m.pere)
	

def echanger(H,m,b):

	tmpArbre=Arbre(None,None,0)
	tmpArbre.droite=b
	tmpArbre.gauche=m

	if m.pere==b.pere:
		if m.pere.gauche==m:
			m.pere.gauche=tmpArbre.droite
			m.pere.droite=tmpArbre.gauche
		else:
			m.pere.droite=tmpArbre.droite
			m.pere.gauche=tmpArbre.gauche
		#afficherArbre(H.racine)

	else:
		if m.pere.gauche==m:
			
			m.pere.gauche=b
			
			m.pere.gauche=tmpArbre.droite
		else:

			
			m.pere.droite=tmpArbre.droite

		if b.pere.gauche==b:
			
			b.pere.gauche=tmpArbre.gauche
			
		else:
			
			b.pere.droite=tmpArbre.gauche



	tmpP=m.pere
	m.pere=b.pere
	b.pere=tmpP

	cheminM=""
	cheminB=""

	tmpM=m
	tmpB=b

	while tmpM.pere != None :
		if tmpM.pere.gauche==tmpM:
			cheminM='0' + cheminM
			tmpM=tmpM.pere
		else:
			cheminM='1' + cheminM
			tmpM=tmpM.pere

	while tmpB.pere != None :
		if tmpB.pere.gauche==tmpB:
			cheminB='0' + cheminB
			tmpB=tmpB.pere
		else:
			cheminB='1' + cheminB
			tmpB=tmpB.pere

	#print("echange m: ",cheminM," et b:",cheminB)
	H=modif(H,m,cheminM)
	H=modif(H,b,cheminB)





def modif(H,m,cheminM):
	if m.valeur is not None:
		#print("nouveau chemin de ",m.valeur," :",cheminM)
		H.valeurs[m.valeur]=cheminM
	if m.gauche is not None:
		H=modif(H,m.gauche,cheminM+'0')	
	
	if m.droite is not None:
		H=modif(H,m.droite,cheminM+'1')

	return H

def suivantsTab(H,tab,etage):
	
	if H is not None:
		if etage >= len (tab):
			tab.append([])
			#print(H.valeur)
		tab[etage].append(H)
		suivantsTab(H.gauche,tab,etage+1)
		suivantsTab(H.droite,tab,etage+1)

	
	return tab[::-1]

test=Arbre('a',None,1)
test.gauche=Arbre('b',test,1)
test.droite=Arbre('c',test,1)
test.gauche.gauche=Arbre('d',test.gauche,1)



def suivantsList(tab):
	list=[]
	for niveau in tab:
		list.extend(niveau)
	return list


def afficherArbre(H):
	if H is not None:
		print("Noeud : ",H,H.valeur," Poids : ",H.poids)
		afficherArbre(H.gauche)
		afficherArbre(H.droite)

def afficherSuiv(tab):
	for i in tab:
		print(i.valeur,i.poids,"->")


"""
codeFix={'a':'01100001','b':'01100010','c':'01100011','r':'01110010','m':'01101101'}
text="carambarbcm"
tc=compresion(text)
print(tc)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
dtc=decompression(tc)

print("Texte original : ",text)
print("Texte compressé : ",tc)
print("Texte décompressé : ",dtc)
"""



# Exécution automatique sécurisée : si un fichier nommé 'Blaise_Pascal' existe dans le dossier
# on lance le pipeline demandé et on écrit 'Blaise_Pascal2.txt.huff' et 'Blaise_Pascal2'.

"""
textO = 'Blaise_Pascal.txt'
textC = 'Blaise_Pascal_binary.txt'
textCBin = 'Blaise_Pascal2.txt.huff'
textFinal = 'Blaise_Pascal2.txt'

with open(textO, 'r', encoding='utf-8') as f:
	text_in = f.read()

compressed = compresion(text_in)

with open(textC, 'w', encoding='utf-8') as f:
    f.write(compressed)

ecriture(textC, textCBin)

res=lecture(textCBin)

decompressed = decompression(res)

with open(textFinal, 'w', encoding='utf-8') as f:
	f.write(decompressed)
"""