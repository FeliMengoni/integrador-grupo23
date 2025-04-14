def porcentaje_de_leer(diccionario): #Falta terminar
    resultados={}
    categorias={
        1:"capaces",
        2:"no_capaces",
        3:"menores",
    }
    for linea in diccionario:
        anio=diccionario["ANO4"]
        trimestre=diccionario["TRIMESTRE"]
        capacidad=diccionario["CHO9"]
        if anio not in resultados:
            resultados[anio]={'capaces':0,'no_capaces':0}
        if trimestre==4:
            if capacidad==1:
                resultados[anio]['capaces']+=1
            elif capacidad==2:
                resultados[anio]['no_capaces']+=1
    for anio, conteos in resultados.items():
        total=conteos['capaces']+conteos['no_capaces']
        if total > 0:
            conteos["Porcentaje Capaces"]=(conteos['capaces']/total)*100
            conteos["Porcentaje No Capaces"]=(conteos['no_capaces']/total)*100
    return resultados

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