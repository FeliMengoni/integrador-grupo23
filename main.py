import os
import pathlib
import csv

#unimos las bases de datos de hogar e individuo

#ruta_individuos = Path('datasets') / 'individual' / 'usu_individual_T423.txt'

#with open(ruta_individuos, 'r', encoding='utf-8') as archivo_individuos:
   #datosU = list(csv.DictReader(archivo_individuos, delimiter=';'))


for archivo in (pathlib.Path.cwd() / "datasets").iterdir():
   individuos = next(archivo.glob("usu_individual_*"))   
   hogares = next(archivo.glob("usu_hogar_*"))
print(individuos)


