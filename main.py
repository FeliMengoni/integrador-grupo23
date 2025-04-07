import os
from src import cleandata


ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_hogar_T324.txt")
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    data_base = [linea.strip().split(";") for linea in archivo]



#lista_datos.dropna(inplace=True)  # Eliminar filas con valores nulos
#data_base = cleandata.cleaner(data_base)  # Limpiar los datos
print(data_base[])
