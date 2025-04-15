def porcentaje_de_leer(dic): # Recibe la lista de diccionarios 
    """Porcentaje de personas capaces de leer"""
    """Recibe la lista de diccionarios y devuelve el porcentaje de personas capaces de leer y de no leer"""
    resultados={} # almacena los resultados por año
    categorias={    # diccionario para clasificar las categorias
        1:"capaces",
        2:"no_capaces",
        3:"menores", }
    for linea in dic:   #recorre la lista de diccionarios
        #obtengo los datos necesarios
        anio=(linea['ANO4'])
        trimestre=(linea["TRIMESTRE"])
        capacidad_de_leer=int(linea['CH09'])
        cantidad=(linea["PONDERA"])
        categoria=categorias.get(capacidad_de_leer)
        if categoria is not None and categoria!="menores": #si no es menor de edad y categoria no esta vacia
            if anio not in resultados: # Si no existe el año en resultados, lo inicializo
                resultados[anio]={categoria: 0 for categoria in categorias.values()}
            if trimestre==4:    # Si es el trimestre 4
                if categoria!=3: # Si no es menor de edad contabilizo
                    resultados[anio][categoria]+=cantidad
    for anio, conteos in resultados.items():#calcular los promedios
        total=sum(conteos.values()) # Total de personas
        if total > 0:
            conteos["Porcentaje Capaces"]=round((conteos['capaces']/total)*100, 2)
            conteos["Porcentaje No Capaces"]=round((conteos['no_capaces']/total)*100, 2)
            print(f"Porcentaje de personas capaces de leer: {conteos['Porcentaje Capaces']}%")
            print(f"Porcentaje de personas no capaces de leer: {conteos['Porcentaje No Capaces']}%")
    

def no_nacidas (lista): # Recibe la lista de diccionarios / CH15: donde nacio
    """Porcentaje de personas no nacidas en ARG que hayan cursado nivel universitario o mayor"""
    anio = int(input('Inserte el año: '))
    trim = int(input('Inserte el trimestre: '))
    cant_personas = 0
    aprobados = 0
    for dic in lista:
        if (anio < dic['ANO4']) or (dic['ANO4'] == anio and trim < dic['TRIMESTRE']):
            continue
        elif anio == dic['ANO4'] and trim == dic['TRIMESTRE']:
            if dic['CH15'] == 4 or dic['CH15'] == 5:
                cant_personas = dic['PONDERA'] + cant_personas
                if (dic['CH12'] == 7) or dic['CH12'] == 8:
                    aprobados = aprobados + dic['PONDERA']
        else:
            break
    print(round(aprobados/cant_personas*100, 2))

"""def menor_desocupacion (lista_dic):
    anio,trim=None,None
    desempleo= 0
    lista_dic_orden = sorted(lista_dic, key=lambda x: (x['ANO4'],x['TRIMESTRE']))
    for dic in lista_dic:
        if dic:"""

def ranking_aglomerados (lista_dic_I):#creanear
    """Definir que hace la funcion"""  
    new_dic = {}  
    for dicI in lista_dic_I:
        if dicI['NIVEL_ED_str'] == 'Superior o universitario':
            #if new_dic[dicI['AGLOMERADO']]['Cant'] == None:
            new_dic[dicI['AGLOMERADO']]['Cant'] = 0
            new_dic[dicI['AGLOMERADO']]['Cant'] = new_dic[dicI['AGLOMERADO']]['Cant'] + dicI['PONDERA']
    print(new_dic)
            