def es_numero(caracter:str)->bool:
    retorno = False
    if ord(caracter) >= 48 and ord(caracter) <= 57:
        retorno = True

    return retorno

# def cadena_es_numero(caracter:str)->bool:
#    retorno = False
#    for i in range(len(caracter)): 
#      if ord(i) >= 48 and ord(i) <=57:
#         retorno = True
        
#         return retorno


# def cadena_es_numero(cadena:str)->bool:                 <---------- Revisar y corregir
#     retorno = False
#     for caracter in cadena:
#         if ord(caracter) >= 48 or ord(caracter) <= 57:
#             retorno = 

#         return retorno

def es_numerico(cadena:str)->bool:
    retorno = True
    for caracter in cadena:
        valor = es_numero(caracter)
        if(valor == False):
            retorno = False
            break
        
    return retorno
