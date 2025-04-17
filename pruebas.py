def merge_diccionarios_por_clave(lista1, lista2, clave_fusion):
    """
    Mergea dos listas de diccionarios por un valor común.

    Args:
        lista1: La primera lista de diccionarios.
        lista2: La segunda lista de diccionarios.
        clave_fusion: El campo común por el que se fusionan los diccionarios.

    Returns:
        Una nueva lista de diccionarios fusionados.
    """

    diccionario_mapeo = {}

    # Crear el diccionario de mapeo con la primera lista
    for diccionario in lista1:
        valor_clave = diccionario['id']
        if valor_clave is not None:
            diccionario_mapeo[valor_clave] = diccionario.copy() # Usar .copy() para evitar modificaciones

    # Combinar con la segunda lista
    for diccionario in lista2:
        valor_clave = diccionario['id']
        if valor_clave is not None:
            if valor_clave in diccionario_mapeo:
                diccionario_mapeo[valor_clave].update(diccionario)
            else:
                diccionario_mapeo[valor_clave] = diccionario.copy()

    # Convertir a lista de diccionarios (opcional)
    resultado = list(diccionario_mapeo.values())
    return resultado

# Ejemplo de uso:
lista1 = [
    {"id": 1, "nombre": "Juan", "ciudad": "La Plata"},
    {"id": 2, "nombre": "Maria", "ciudad": "Buenos Aires"}
]
lista2 = [
    {"id": 1, "edad": 30},
    {"id": 3, "nombre": "Pedro", "edad": 25, "ciudad": "Rosario"}
]

clave_fusion = "id"
lista_fusionada = merge_diccionarios_por_clave(lista1, lista2, clave_fusion)

for diccionario in lista_fusionada:
    print(diccionario)