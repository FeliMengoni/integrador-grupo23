def genero_to_string (lista_de_datos):
    """Funcion que agrega culumna de Masculino o Femenino"""
    lista_de_datos[0].append('CH04_str')
    for linea in lista_de_datos[1:]:
        if int(linea[11]) == 1:
            linea.append('Masculino')
        if int(linea[11]) == 2:
            linea.append('Femenino')
            

