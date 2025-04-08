import os
#conseguir las carpetas de los datasets
carpeta_hogar = os.path.join(os.path.dirname(__file__), "datasets","hogar")
carpeta_individuos = os.path.join(os.path.dirname(__file__), "datasets", "individual")
# Unir los archivos de las carpetas
archivos_hogar = [archivo for archivo in os.listdir(carpeta_hogar) if archivo.endswith(".txt")]
archivos_individuos = [archivo for archivo in os.listdir(carpeta_individuos) if archivo.endswith(".txt")]

#ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_hogar_T324.txt")
#with open(ruta_archivo, "r", encoding="utf-8") as archivo:
 ##   data_base = [linea.strip().split(";") for linea in archivo]



#lista_datos.dropna(inplace=True)  # Eliminar filas con valores nulos
#data_base = cleandata.cleaner(data_base)  # Limpiar los datos
#print(data_base)
print("Archivo 2 de la carpeta hogar")
print(archivos_hogar[0])
print("Archivo 2 de la carpeta individuos")
print(archivos_individuos[0])