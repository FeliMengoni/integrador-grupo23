import os
from pathlib import Path
import csv

#unimos las bases de datos de hogar e individuo

ruta_individuos = Path('datasets') / 'individual' / 'usu_individual_T423.txt'

with open(ruta_individuos, 'r', encoding='utf-8') as archivo_individuos:
   datosU = list(csv.DictReader(archivo_individuos, delimiter=';'))


print(datosU[0:2])





