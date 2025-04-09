def tipo_hogar (lista_de_datos):
    """Funcion que agrega culumna de tipo de hogar"""
    lista_de_datos[0].append('TIPO_HOGAR')
    indice_de_IX_TOT = lista_de_datos[0].index('IX_TOT')

    for linea in lista_de_datos[1:]:
        match int(indice_de_IX_TOT):
            case 1:
                linea.append('Unipersonal')
            case 2|3|4:
                linea.append('Nuclear')
        if int('IX_TOT') >= 5:
            linea.append('Extensa')


def material_techumbre (lista_de_datos):
    """Funcion que agrega culumna de material de techumbre"""
    lista_de_datos[0].append('MATERIAL_TECHUMBRE')
    indice_de_MATERIAL_TECHUMBRE = lista_de_datos[0].index('MATERIAL_TECHUMBRE')
    for linea in lista_de_datos[1:]:
        match int(linea[indice_de_MATERIAL_TECHUMBRE]):
            case 1|2|3|4:
                linea.append('Material durable')
            case 5|6|7:
                linea.append('Material precario')

def densidad_hogar (lista_de_datos):
    """Funcion que agrega culumna de densidad de hogar"""
    lista_de_datos[0].append('DENSIDAD_HOGAR')
    indice_de_IX_TOT = lista_de_datos[0].index('IX_TOT')
    indice_de_II1 = lista_de_datos[0].index('II1')
    for linea in lista_de_datos[1:]:
        personas_por_habitacion = int(linea[indice_de_IX_TOT])/int(linea[indice_de_II1])
        if personas_por_habitacion <1:
            linea.append('Bajo')
        elif personas_por_habitacion <= 2:
            linea.append('Medio')
        else:
            linea.append('Alto')

def condicion_de_habitabilidad (lista_de_datos):  #NO ESTA TERMINADA (hay q hablarlo)
    """Funcion que agrega culumna de condicion de habitabilidad"""
    

    
            
