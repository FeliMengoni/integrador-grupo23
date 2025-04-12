def tipo_hogar (diccionario_de_datos):
    """Funcion que agrega culumna de tipo de hogar"""
    for linea in diccionario_de_datos:
        match int(linea("IX_TOT")):
            case 1:
                linea['TIPO_HOGAR']= 'unipersonal'
            case 2|3|4:
                linea['TIPO_HOGAR']='Nuclear'
        if int(linea('IX_TOT')) >= 5:
            linea['TIPO_HOGAR']= 'Extensa'


def material_techumbre (diccionario_de_datos):
    """Funcion que agrega culumna de material de techumbre"""
    for linea in diccionario_de_datos:
        match int(linea['V4']):
            case 1|2|3|4:
                linea['MATERIAL_TECHUMBRE']='Material durable'
            case 5|6|7:
                linea['MATERIAL_TECHUMBRE']= 'Material precario'
            case 9:
                linea['MATERIAL_TECHUMBRE']= ' No aplica'

"""def densidad_hogar (lista_de_datos):
    #Funcion que agrega culumna de densidad de hogar
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
            linea.append('Alto')"""

def densidad_hogar(diccionario_de_datos):
    for linea in diccionario_de_datos.items():
        personas_por_habitacion = int(linea["IX_TOT"]) / int(linea["II1"])
        if personas_por_habitacion < 1:
            linea["DENSIDAD_HOGAR"] = "Bajo"
        elif personas_por_habitacion <= 2:
            linea["DENSIDAD_HOGAR"] = "Medio"
        else:
            linea["DENSIDAD_HOGAR"] = "Alto"


def condicion_de_habitabilidad (lista_de_datos):  #NO ESTA TERMINADA (hay q hablarlo)
    """Funcion que agrega culumna de condicion de habitabilidad"""
    

    
            
