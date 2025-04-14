import os
from pathlib import Path
import csv
from src import utils
from src import datacleaner

#unimos las bases de datos de hogar e individuo

ruta_individuos = Path('datasets') / 'usu_individual_T423.txt'

with open(ruta_individuos, 'r', encoding='utf-8') as archivo_individuos:
   datosU = list(csv.DictReader(archivo_individuos, delimiter=';'))

datacleaner.cleaner(datosU)
   
print(datosU[:5])




  