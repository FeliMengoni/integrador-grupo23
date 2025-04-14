import os
from pathlib import Path
import csv
from src import utils
from src import datacleaner

#unimos las bases de datos de hogar e individuo

ruta_individuos = Path('datasets') / 'usu_individual_T423.txt'
ruta_hogares = Path("datasets") / 'usu_hogar_T423.txt'

with open(ruta_individuos, 'r', encoding='utf-8') as archivo_individuos:
   datosU = list(csv.DictReader(archivo_individuos, delimiter=';'))
with open(ruta_hogares, 'r', encoding='utf-8') as archivo_hogares:
   datosH = list(csv.DictReader(archivo_hogares, delimiter=';'))

datacleaner.cleanerU(datosU)
datacleaner.cleanerH(datosH)
   
print(datosU[:5])
print('='*50)
print(datosH[:5])



  
