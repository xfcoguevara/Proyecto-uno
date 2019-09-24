"""Modulo que contiene las funciones para encriptar y desencriptar un texto
encriptar() 
desencriptar()"""
diccionario = {" ":".","a":"!", "b":'"', "c":"#", "d":"$", "e":"%", "f":"^", "g":"&", "h":"*", "i":"(",
    "j":"[", "k":")", "l":"]", "m":"{", "n":":", "o":"}", "p":"?", "q":">", "r":"<", "s":"+",
    "t":";", "u":"_", "v":"/", "w":"÷", "x":"`", "y":"@", "z":"="}

def encriptar(mensaje,diccionario):   
    """Funcion para encriptar un mensaje
    mensaje = variable que contiene al mensaje o texto a encriptar
    diccionario = diccionario con el cual se va a encriptar el mensaje o texto """
    #global diccionario
    mensaje = mensaje.lower() #Convertir todas la letras del texto en minusculas 
    encrip = ""
    for r in mensaje: #Mover entre cada una de las letras del texto o mensaje
        if r in diccionario:#Buscar la letra en el diccionario y agregar la letra encriptada en una variable
            encrip += diccionario[r]
        else:
            encrip += r #Si el caracter no se encuentras en el diccionario se agrega directamente sin encriptar
    return encrip

def desencriptar(encriptado,diccionario):
    """Funcion para desencriptar mensaje o texto encriptado
    encriptado = Variable que contiene el mensaje o texto encriptado
    diccionario = Diccionario con el cual se encripto el mensaje """
    #global diccionario
    dic_invertido = dict([[v,k] for k,v in diccionario.items()]) # invertir el diccionario para desencriptar el mensaje
    #mensaje = mensaje.lower()
    encrip = ""
    for r in encriptado:
        if r in dic_invertido:
            encrip += dic_invertido[r]
        else:
            encrip += r
    return encrip
x = "Hola"
print(encriptar(x,diccionario))
print(desencriptar(encriptar(x,diccionario),diccionario))
