def es_numero(caracter:str)->bool:
    retorno = False
    if ord(caracter) >= 48 and ord(caracter) <= 57:
        retorno = True
    return retorno

def es_numerico(cadena:str)->bool:
    retorno = True
    for caracter in cadena:
        valor = es_numero(caracter)
        if valor == False:
            retorno = False
            break
    return retorno

# def es_entero(cadena:str)->bool:
    retorno = True
    for i in cadena:
        valor = es_numero(i) # Llamo a l funcion es_numero pra coorrobar que el caracter sea numero
        if valor == False:
            retorno = False # Si no es numero la flg cambia a false y termina devolviedo 'False'
            break 
    return retorno

def es_entero(cadena:str)->bool:
    retorno = True
    
    if len(cadena) == 0: # If para corroborar que no sea una cadena vacia
        retorno = False
    else:
        for i in range(len(cadena)): # Itero sobre la cadena ingresada
            caracter = cadena[i]
            
            if caracter == "-" and i == 0 and len(cadena) > 1: # Corrobor que sea un signo '-' , que este en el indice '0' o sea que este primero para evitar la resta y que sea mayr a 1 para evitar que '-' sea True
                continue
            
            valor = es_numero(caracter) # HAce la ultima revision para ver si los caracteres restantes son numeros o letras volviendo a la primer def
            if valor == False:
                retorno = False
                break 

    return retorno



def es_flotante(cadena:str)->bool:
    retorno = True
    puntos = 0
    numeros = 0

    if len(cadena) == 0: #Este if es para corroborar que la cadena no sea vacia tipo '.'
        retorno = False

    for i in range(len(cadena)):
        caracter = cadena[i]

        if caracter == ".":
            puntos += 1
            if puntos > 1:
                retorno = False # La flga cambia a fales si detecta que hay más de 1 punto para evitar '9.8.8' y rimpe
                break
        elif caracter == "-":
            if i != 0: # Cororborra que el signo - este al inicio indicando que es un num negativo y no en el medio como una resta
                retorno = False
                break
        elif es_numero(caracter): # Corroboro que sea un digito valido usando es_numero y aumento el contador 'digitos' para que pase al final
            digitos += 1
        else:                   # El else para evitar que tomen vacios tipo ' ' o con letra tipo 'a'
            retorno = False
            break

    if numeros == 0: # Este if es para corroborar que la cadena no sea '-.' o '-'
        retorno = False

    return retorno



def carac_min(letra:str)->str:
    caracter = ord(letra)
    if caracter >= 65 and caracter <=90:
        caracter = chr(caracter + 32)
    return caracter

def carac_mayu(letra:str)->str:
    caracter = ord(letra)
    if caracter >= 97 and caracter <= 122:
        caracter = chr(caracter - 32)
    return caracter

def convertir_minus(letra:str)->str:
    minus = ''
    for caracter in letra:
        if ord(caracter) >= 65 and ord(caracter) <=90:
            modificado = carac_min(caracter)
            minus += modificado
        elif ord(caracter) >= 97 and ord(caracter) <=122:
            no_modificado = caracter
            minus += no_modificado
        elif ord(caracter) == 32:
            espacio = caracter
            minus += espacio
        else:
            continue
    return minus

def convertir_mayus(letra:str)->str:
    mayus = ''
    for caracter in letra:
        if ord(caracter) >= 97 and ord(caracter) <=122:
            modificado = carac_mayu(caracter)
            mayus += modificado
        elif ord(caracter) >= 65 and ord(caracter) <=90:
            no_modificado = caracter
            mayus += no_modificado
        elif ord(caracter) == 32:
            espacio = caracter
            mayus += espacio
        else:
            continue
    return mayus

def primer_mayus(letra:str)->str:
    convertido = ''
    indice = 0
    for caracter in letra:
        if indice == 0:
            modificado1 = carac_mayu(caracter)
            convertido += modificado1
        else:
            if ord(caracter) >= 65 and ord(caracter) <=90:
                modificado = carac_min(caracter)
                convertido += modificado
            elif ord(caracter) >= 97 and ord(caracter) <=122:
                no_modificado = caracter
                convertido += no_modificado
            elif ord(caracter) == 32:
                espacio = caracter
                convertido += espacio
        
        indice += 1

    return convertido


valor = carac_min('L')
print(valor)
valor1 = carac_mayu('l')
print(valor1)
valor2 = convertir_minus('HOLA MUNDO')
print(valor2)
valor3 = convertir_mayus('hola mundo')
print(valor3)
valor4 = primer_mayus('hOLa MuNDo')
print(valor4)