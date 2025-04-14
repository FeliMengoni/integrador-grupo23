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

def menor_desocupacion (lista_dic):
    anio,trim=None,None
    desempleo= 0
    lista_dic_orden = sorted(lista_dic, key=lambda x: (x['ANO4'],x['TRIMESTRE']))
    for dic in lista_dic:
        if dic
