import os
from src import cleandata


ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_hogar_T324.txt")

#lista_datos.dropna(inplace=True)  # Eliminar filas con valores nulos
lista_datos = cleandata.cleaner(lista_datos)  # Limpiar los datos
print(lista_datos)
