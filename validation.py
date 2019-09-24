"""Este modulo tiene las siguientes funciones de validacion de variables:
1-. valInt
2-. valFloat
3-. valComplex
4-. ValList """

def valInt(*args):
	"""Validacion datos de tipo entero.
	true:
	ValInt(Int,tuple/list) --> int debe pertenece al intervalo definido por list o tuple 
	list y tuple tienen que representar un intervalo ordenados de forma creciente
	list = [] intervalo cerrado
	tuple = () intervalo abierto
	 """
	if len(args) == 1: 
		val = print(type(args[0]) == int)		
	else:
		if type(args[1]) == list or type(args[1]) == tuple:
			if args[1][0] > args[1][1] or len(args[1]) > 2:
				val = print("ValueError")
			elif type(args[1]) == tuple:
				val = print(args[0] < args[1][1] and args[0] > args[1][0])
			else:
				val = print(args[0] <= args[1][1] and args[0] >= args[1][0])
		else:
			val = print("TypeError")
	return val				

def valFloat(*args):
	"""Validar datos de tipo float
	true:
	valFloat(float)
	valFloat(float,list/tuple) --> float debe pertenece al intervalo definido por list o tuple 
	List y tuple deben representar un intervalo ordenado de forma creciente
	list = [] intervalo cerrado
	tuple = () intervalo abierto"""
	if len(args) == 1:
		val = print(type(args[0]) == float)
	else:
		if type(args[1]) == list or type(args[1]) == tuple:
			if args[1][0] > args[1][1] or len(args[1]) > 2:
				val = print("ValueError")
			elif type(args[1]) == tuple:
				val = print(args[0] < args[1][1] and args[0] > args[1][0])
			else:
				val = print(args[0] <= args[1][1] and args[0] >= args[1][0])
		else:
			val = print("TypeError")
	return val

def valComplex(*args):
	"""Validar datos de tipo complex
	true:
	valComplex(complex)
	valComplez(Complex,list/tuple) --> la norma de complex debe pertenecer al intervalo definido por list o tuple
	List y tuple deben representar un intervalo ordenado de forma creciente
	list = [] intervalo cerrado
	tuple = () intervalo abierto
	"""
	if len(args) == 1:
		val = print(type(args[0]) == complex)
	else:
		if type(args[1]) == list or type(args[1]) == tuple:
				if args[1][0] > args[1][1] or len(args[1]) > 2:
					val = print("ValueError")
				elif type(args[1]) == tuple:
					val = print(abs(args[0]) < args[1][1] and abs(args[0]) > args[1][0])
				else:
					val = print(abs(args[0]) <= args[1][1] and abs(args[0]) >= args[1][0])
		else:
			val = print("TypeError")
	return val

def valList(*args):
	"""Validar datos de tipo list
	True;
	valList(list,int,"len") --> longitud(list) = int
	valList(lis1,list2,"value") --> list1 = list2
	valList(list)"""
	if len(args) == 3:
		if type(args[2]) == str and (type(args[1]) == int or type(args[1]) == list):
			if args[2] == "value":
				val = print(type(args[0]) == list and type(args[1]) == list and args[0] == args[1])
			elif args[2] == "len" :
				val = print(type(args[0]) == list and type(args[1]) == int and len(args[0]) == args[1])
			else:
				val = print("ValueError")
		else:
			val = print("TypeError")		
	elif len(args) == 1:
		val = print(type(args[0]) == list)
	return val
	
def valMultiplicacionMatricial(matriz_1,matriz_2):
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
