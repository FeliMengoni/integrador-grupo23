import os
import pandas as pd
from src import cleandata


ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_hogar_T324.txt")
lista_datos = pd.read_csv(ruta_archivo, encoding="utf-8", delimiter=";")  # Separar por punto y coma

print(lista_datos.head())  # Verifica las primeras filas del DataFrame


#lista_datos.dropna(inplace=True)  # Eliminar filas con valores nulos
lista_datos = cleandata.cleaner(lista_datos)  # Limpiar los datos
print(lista_datos)