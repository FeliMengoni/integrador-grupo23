import os

# Obtener la ruta del archivo dentro de "datasets"
ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_hogar_T324.txt")

# Leer el archivo y convertirlo en una lista
with open(ruta_archivo, "r", encoding="utf-8") as file:
    lista_datos = file.read().splitlines()  # Divide el contenido por líneas

print(lista_datos)  # Ver la lista resultante

print ("hola prueba")