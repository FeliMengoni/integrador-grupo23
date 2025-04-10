def limpiador (datos):
    """Funcion que limpia los datos de la base de datos"""
    for linea in datos:
        for i in linea:
            i.strip()


  