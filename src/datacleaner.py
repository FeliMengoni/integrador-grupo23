"""def clean_int (dato): 
    if dato.isnumeric() :
        return int(dato)
    
def clean_None(dato): 
   #si es una lista
        for i in range(len(dato)):
            if not dato[i]:
                dato[i] = None
        return dato
   
    #si es un diccionario
        for i in dato:
            if not dato[i]:
                dato[i] = None
        return dato 

def clean_espacios(dato):
      #si es una lista
        for i in range(len(dato)):
            if isinstance(dato[i], str): #me dice si es un string
                dato[i] = dato[i].strip()
        return dato
    #si es un diccionario
        for i in dato:
            if isinstance(dato[i], str):
                dato[i] = dato[i].strip()
        return dato"""

def cleaner (dic):
    for dato in dic:
        if dic[dato].isnumeric():
            dic[dato] = int(dic[dato])
        elif not dic[dato]:
            dic[dato] = None
        elif isinstance(dic[dato], str):
            dic[dato] = dic[dato].strip()
        else:
            dic[dato] = None
                