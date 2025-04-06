import os

# Obtener la ruta del archivo dentro de "datasets"
ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_hogar_T324.txt")

# Leer el archivo y convertirlo en una lista
with open(ruta_archivo, "r", encoding="utf-8") as file: #convierto los datos a un diccionario y lo separo por punto y coma
    lista_datos = [linea.strip().split(";") for linea in file.readlines()]
    


