def tipo_hogar (diccionario_de_datos):
    """Funcion que agrega culumna de tipo de hogar"""
    for linea in diccionario_de_datos:
        match int(linea["IX_TOT"]):
            case 1:
                linea['TIPO_HOGAR']= 'unipersonal'
            case 2|3|4:
                linea['TIPO_HOGAR']='Nuclear'
        if int(linea['IX_TOT']) >= 5:
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
                linea['MATERIAL_TECHUMBRE']= 'No aplica'


def densidad_hogar(diccionario_de_datos):
    for linea in diccionario_de_datos:
        if int(linea["II1"])!=0:
            personas_por_habitacion = (int(linea["IX_TOT"])/int(linea["II1"]))
        else:
            personas_por_habitacion = 5
        if personas_por_habitacion < 1:
            linea["DENSIDAD_HOGAR"] = "Bajo"
        elif personas_por_habitacion <= 2:
            linea["DENSIDAD_HOGAR"] = "Medio"
        else:
            linea["DENSIDAD_HOGAR"] = "Alto"


def condicion_de_habitabilidad (diccionario_de_datos): 
    """Funcion que agrega culumna de condicion de habitabilidad"""
    for linea in diccionario_de_datos:
        puntos=(3-int(linea['IV9']))+ (2-int(linea['IV8'])) + (3-int(linea['IV6']))
        puntos+= (3-int(linea['IV7'])) + (3-int(linea['IV10']))
        match puntos:
            case 14:
             linea['condicion_de_habitabilidad']= 'bueno'
            case 13|12|11|10:
                linea['condicion_de_habitabilidad']= 'saludable'
            case 9|8|7|6|5:
                linea['condicion_de_habitabilidad']= 'regular'
            case 4|3|2|1|0:
                linea['condicion_de_habitabilidad']= 'insuficiente'
        

    
            
