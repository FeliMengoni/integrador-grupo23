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

def merge_diccionarios_por_clave(lista1, lista2, clave_fusion):
    """
    Mergea dos listas de diccionarios por un valor común.
    """

    mergeado = {}

    # Crear el diccionario de mapeo con la primera lista
    for diccionario in lista1:
        valor_clave = diccionario['CODUSU']
        if valor_clave is not None:
            mergeado[valor_clave] = diccionario.copy() # Usar .copy() para evitar modificaciones

    # Combinar con la segunda lista
    for diccionario in lista2:
        valor_clave = diccionario['CODUSU']
        if valor_clave is not None:
            if valor_clave in mergeado:
                mergeado[valor_clave].update(diccionario)
            else:
                mergeado[valor_clave] = diccionario.copy()

    # Convertir a lista de diccionarios (opcional)
    resultado = list(mergeado.values())
    return resultado

def ranking_aglomerados (lista_dic_I, lista_dic_H): # TERMINAR TEMA DE LOS ULTIMOS 2 REPORTES
    """Ranking 5 aglomerados mayor porcentaje con dos o mas ocupantes con estudios universitarios"""  
    
    # Ordeno las listas de diccionarios por CODUSU y AGLOMERADO
    lista_ordenada_I = sorted(lista_dic_I, key=lambda x: x["CODUSU"])
    lista_ordenada_H = sorted(lista_dic_H, key=lambda x: x["AGLOMERADO"])
    
    # Inicializo las variables necesarias para el programa
    new_list = []
    dic = {}
    cont_hogares = 0
    linea_anterior = ''

    # Obtengo las variables necesarias de Individuo y las agrego a una nueva lista de diccionarios (ACOMODAR BIEN, dar vuelta la condicion de si es distinto)
    for line in lista_ordenada_I:
        codusu = line['CODUSU']
        if codusu != linea_anterior:
            if line['NIVEL_ED_str'] == 'Superior o universitario':
                personas_educadas = line['PONDERA']
            else:
                personas_educadas = 0
            dic = {'CODUSU': codusu, 'aglo': line['AGLOMERADO'], 'cant_personas': line['PONDERA'], 'sup_univer': personas_educadas}
            new_list.append(dic)
        else:
            dic['cant_personas'] = dic['cant_personas'] + line['PONDERA']
            if line['NIVEL_ED_str'] == 'Superior o universitario':
                dic['sup_univer'] = line['PONDERA'] + dic['sup_univer']
        linea_anterior = codusu
    
    # Ordenando la lista nueva para luego mergearla con la lista de hogares agrupandola por CODUSU
    new_list = sorted(new_list, key=lambda x: x["aglo"])
    mergeado = merge_diccionarios_por_clave(new_list, lista_dic_H, 'CODUSU')

    # Vaciamos la lista que ya no nos sirve y solo insertamos la informacion necesaria
    new_list = []

    # Inicializamos variables necesarias
    linea_anterior = ''
    new_dic = {}
    personas = 0
    universitarios = 0

    # Lleno la nueva lista en la que guardo el porcentaje y el aglomerado
    for line in mergeado:

        aglo = line['aglo']

        # Si es distinto agrega el diccionario anterior y resetea los contadores
        if aglo != linea_anterior and line != mergeado[0]: # La segunda condicion es para que no se ejecute una vez pasa al siguiente aglomerado
            new_dic = {'AGLOMERADO': linea_anterior, 'PORCENTAJE': round(universitarios/personas*100, 2)}
            new_list.append(new_dic)
            personas = 0
            universitarios = 0
        
        # Aumento los contadores, en caso de que haya mas de una persona en el hogar, aumenta la cantidad de universitarios
        personas += line['cant_personas']
        if line['IX_TOT'] > 1:
            universitarios += line['sup_univer']
        
        linea_anterior = aglo

        # En caso de que sea la ultima linea, agrega el ultimo diccionario a la lista
        if line == mergeado[-1]:
            new_dic = {'AGLOMERADO': linea_anterior, 'PORCENTAJE': round(universitarios/personas*100, 2)}
            new_list.append(new_dic)
    
    # Codigo que ordena a la nueva lista por el porcentaje (de mayor a menor)
    new_list = sorted(new_list, key=lambda x: x["PORCENTAJE"], reverse=True)
    
    # Hago el print ordenado del RANKING
    pos = 0
    print()
    print('----------------------------------------------------------------------------')
    print('TOP 5 AGLOMERADOS: DOS O MAS PERSONAS CON ESTUDIOS UNIVERSITARIOS O SUPERIOR')
    print('----------------------------------------------------------------------------')
    for top in new_list[:5]:
        pos += 1
        print(pos, '- Aglomerado: ',top['AGLOMERADO'], ' '*(2-len(str(top['AGLOMERADO']))),top['PORCENTAJE'], '%')

def porcentaje_universitario (dic):
    """Informar para cada aglomerado el porcentaje de personas que hayan cursado al 
    menos en nivel universitario o superior"""
    dicO = sorted(dic, key = lambda x:x['AGLOMERADO'])
    total_personas = 1
    total_universitario = 1
    anterior = ''
    porcentaje = 0
    #recorro y sumo las personas en total y las q estudiaron
    for linea in dicO:
        if linea["AGLOMERADO"] != anterior:
            print(anterior, " ", round(porcentaje, 2),"%")
            print(total_personas)
            print(total_universitario)
            porcentaje = total_universitario/total_personas*100
            total_personas=(linea["PONDERA"])
            total_universitario = 0
            if linea["NIVEL_ED"] == 5 or linea['NIVEL_ED'] == 6:
                total_universitario = total_personas
        else: 
            total_personas += linea['PONDERA']
            if linea["NIVEL_ED"] == 5 or linea['NIVEL_ED'] == 6:
                total_universitario += linea['PONDERA']
            porcentaje = total_universitario/total_personas*100
            
    
        anterior = linea['AGLOMERADO']