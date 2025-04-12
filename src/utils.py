def genero_to_string (dic):
    """Funcion que agrega culumna de Masculino o Femenino"""
    if dic['CH04'] == 1:
        dic['CH04_str'] = 'Masculino'
    elif dic['CH04_str'] == 2:
        dic['CH04_str'] = 'Femenino'            
    else:
        dic['CH04_str'] = None

def nivel_to_string(lista_de_datos):
    """Función que agrega columna de nivel educativo"""
    
    lista_de_datos[0].append('NIVEL_ED_str')
    for linea in lista_de_datos[1:]:
        match int(linea[26]):
            case 1:
                linea.append('Primario incompleto')
            case 2:
                linea.append('Primario completo')
            case 3:
                linea.append('Secundario incompleto')
            case 4:
                linea.append('Secundario completo')
            case 5 | 6:
                linea.append('Superior o universitario')
            case 7 | 9:
                linea.append('Sin información')



def condicion_laboral_to_string (lista_de_datos):
    """Funcion que agrega culumna de condicion laboral"""
    lista_de_datos[0].append('CONDICION_LABORAL')
    for linea in lista_de_datos[1:]:
        if (int(linea[27]) == 1) and (int(linea[28])== 1 or 2):
            linea.append('Ocupado autónomo')
        if (int(linea[27]) == 1) and (int(linea[28])== 3 or 4 or 9):
            linea.append('Ocupado dependiente')
        if (int(linea[27]) == 2):
            linea.append('Desocupado')
        if (int(linea[27]) == 3):
            linea.append('Inactivo')
        if (int(linea[27]) == 4):
            linea.append('Fuera de categoria')

def universitario (lista_de_datos):     #NO ESTA TERMINADA
    """Funcion que agrega culumna de universitario"""
    lista_de_datos[0].append('universitario')
    for linea in lista_de_datos[1:]:
        if ("aca hay q poner si es mayor d edad"):
            if (int(linea[26]) == 5 or 6):
                linea.append(1)
            else:
                linea.append(0)
        else:
            linea.append(2)


        
    