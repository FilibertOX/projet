
#Question 3
def lecture(fichier_bin):
	res=""
	f=open(fichier_bin, "rb")
	while True:
		tmp=""
		contenu = f.read(1)
		if not contenu:
			break
		
		byte = contenu[0]
		i=8
		while i	> 0:
			i-=1
			if byte&1:
				tmp += '1'
			else:
				tmp += '0'
			byte = byte >> 1
		res += tmp[::-1] # inverser chaque octet
	#print(res)
	f.close()
	return res

#Question 4
def ecriture(fichier_text,fichier_bin):
	text=open(fichier_text,"r")
	bin=open(fichier_bin,"wb")
	while True:
		car=text.read(8)
		if not car:
			break
		if len(car)<8:
			car+='0'*(8-len(car))
		i=0
		byte=0
		while i<8:
			if car[i] == '1':
				byte += 1 << 7-i
			i+=1
		bin.write(byte.to_bytes())


	text.close()
	bin.close() 

		
#ecriture("fichier.txt","fichier.bin")