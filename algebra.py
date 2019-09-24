def valMultiplicacionMatricial(matriz_1,matriz_2):
	"""Validar que los argumentos son una lista de lista que pueden representar una matriz"""
	if type(matriz_1) and type(matriz_2) == list:
		for i in range(0,len(matriz_1)):
			if type(matriz_1[i]) != list:
				 return print("Error el primer argumento no representa una matriz")
		for i in range(0,len(matriz_2)):
			if type(matriz_2[i]) != list:
				return print("Error el segundo argumento no representa una matriz")
		if len(matriz_1) == len(matriz_2[0]):
			return True
		else:
			return False
	else:
		return print("TypeError: revise los datos de entrada, puede que alguno de ellos no represente una matriz")

def expmatriz(n,m,matriz):
	"""Imprime una lista de lista de forma cuadrada simulando la forma de una matriz"""
	for i in range(0,n):#Recorre todas las lista para convertir los elementos en string
		for j in range(0,m):
			matriz[i][j] = str(matriz[i][j]) 
	for n in range(0,n):
		var =  print(" ".join(matriz[n])) #imprime la lista de string
	return var

def multiplicacionmatricial(matriz_1,matriz_2):
	"""Multiplicacion de dos matrices nxm * mxn
	multiplicacionmatricial(matriz1,matriz2) --> matriz1 y matriz2 son listas de listas M= [[],[],[],...]
	"""
	if valMultiplicacionMatricial(matriz_1,matriz_2) == True: #validar que los argumentos son un lista de lista
		matriz_3 = []		
		ij = 0											# ij es un acumulador 
		for h in range(0,len(matriz_1)): 				#Crear la matriz donde se guardara el resultado de la multiplicacion matricial
			lista_3 = []								#la matriz esta formado por ceros y tiene la dimension correspondiente al resultado de la multiplicacion de dos matrices nxm y mxn
			while len(lista_3) < len(matriz_1):			#uso el mismo controlador de fila de la primera matriz para ir creado dicha matriz resultante
				lista_3.append(0)
			matriz_3.append(lista_3)		
			for k in range(0,len(matriz_1[0])):					
				for l in range(0,len(matriz_1)):						
					ij = matriz_1[h][k] * matriz_2[k][l]
					matriz_3[h][l] = matriz_3[h][l] + ij 
		return expmatriz(len(matriz_1),len(matriz_2[0]),matriz_3)
	else:
		return print("No es posible realizar esta multiplicacion")

def productoVectorial(v1,v2):
	"""Producto vectorial o producto cruz de dos vectores en tres dimensiones
	productoVectorial(v1,v2)
	v1 y v2 deben ser listas contengan las componentes i,j,k respectivamente de los vectores
	"""
	i = str(v1[1]*v2[2] - v1[2]*v2[1]) + "i"
	j = str(v1[2]*v2[0] - v1[0]*v2[2]) + "j"
	k = str(v1[0]*v2[1] - v1[1]*v2[0]) + "k"
	if j>=0:
		j = "+" + str(j) + "j"
	else:
		j = str(v1[2]*v2[0] - v1[0]*v2[2]) + "j"
	if k>=0:
		k = "+" + str(k) + "k"
	else:
		k = str(v1[0]*v2[1] - v1[1]*v2[0]) + "k"
	return print("{}{}{}".format(i,j,k))

def traspuesta(matriz):
	"""Traspuesta de una matriz"""
	matriztras = []
	for m in range(0,len(matriz[0])):
		lista = []
		matriztras.append(lista)
		for n in range(0,len(matriz)):		
			lista.append(matriz[n][m])	
	print("la matriz es: ")	
	expmatriz(len(matriz),len(matriz[0]),matriz)
	print("\n La matriz traspuesta es: ")
	expmatriz(len(matriztras),len(matriztras[0]),matriztras)	
	return 
			
def gaussjordan(matriz):
	import copy
	inversa = []		
	for h in range(0,len(matriz)):
		lis_inversa = []
		for k in range(0,len(matriz)):
			if h == k:
				lis_inversa.append(1)
			else:
				lis_inversa.append(0)
		inversa.append(lis_inversa)
	
	def sumafilas(fila1,fila2,escalar):
		for i in range(0,len(fila1)):
			fila2[i] = (escalar * fila1[i]) + fila2[i]
		return fila2

	def pivote(fil,fila,columna):
		pivote = copy.deepcopy(fila[columna])
		for i in range(0,len(fila)):
			fil[i] = fil[i] / pivote
		return fil

	def intercambiofila(matriz,fila1,fila2):
		fila3 = matriz[fila1]
		matriz[fila1] = matriz[fila2]
		matriz[fila2] = fila3
		return matriz

	for columna in range(0,len(matriz)):
		if matriz[columna][columna] != 0:			
			inversa[columna] = pivote(inversa[columna],matriz[columna],columna)
			matriz[columna] = pivote(matriz[columna],matriz[columna],columna)
		#else:
			#for i range(0,len(matriz)):

		for fila in range(0,len(matriz)):
			if matriz[fila][columna] != 0 and columna != fila:
				escalar = -1 * copy.deepcopy(matriz[fila][columna])				
				inversa[fila] = sumafilas(inversa[columna],inversa[fila],escalar)
				matriz[fila] = sumafilas(matriz[columna],matriz[fila],escalar)
	return inversa



