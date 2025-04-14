def porcentaje_de_leer(dic): #Falta terminar
    resultados={}
    categorias={
        1:"capaces",
        2:"no_capaces",
        3:"menores",
    }
    for linea in dic:
        anio=(linea['ANO4'])
        trimestre=(linea["TRIMESTRE"])
        capacidad_de_leer=int(linea['CH09'])
        cantidad=(linea["PONDERA"])
        if anio not in resultados:
            resultados[anio]={'capaces':0,'no_capaces':0}
        if trimestre==4:
            categoria=categorias.get(capacidad_de_leer)
            if categoria!=3:
                resultados[anio][categoria]+=cantidad
    for anio, conteos in resultados.items():
        total=sum(conteos.values()) # Total de personas
        print(total)
        if total > 0:
            conteos["Porcentaje Capaces"]=(conteos['capaces']/total)*100
            conteos["Porcentaje No Capaces"]=(conteos['no_capaces']/total)*100
            print(f"año: {anio} trimestre: {trimestre}")
            print(f"Porcentaje de personas capaces de leer: {conteos['Porcentaje Capaces']}%")
            print(f"Porcentaje de personas no capaces de leer: {conteos['Porcentaje No Capaces']}%")


#def no_nacidas (lista): # Recibe la lista de diccionarios
 #   """Porcentaje de personas no nacidas en ARG que hayan cursado nivel universitario o mayor"""
  #  anio = int(input('Inserte el año: '))
   # trim = int(input('Inserte el trimestre: '))
    #for dic in lista:
     #   if (anio < dic['ANO4']) or (dic['ANO4'] == anio and trim < dic['TRIMESTRE']):
      #      continue
       # elif anio == dic['ANO4'] and trim == dic['TRIMESTRE']:
        #else:
         #   break