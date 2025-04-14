import os
import pathlib
import csv
from src import utils
from src import datacleaner

#unimos las bases de datos de hogar e individuo

#ruta_individuos = Path('datasets') / 'individual' / 'usu_individual_T423.txt'

#with open(ruta_individuos, 'r', encoding='utf-8') as archivo_individuos:
   #datosU = list(csv.DictReader(archivo_individuos, delimiter=';'))

print(datosU[0])
for line in datosU[:5]:
   datacleaner.cleaner(line)
   utils.genero_to_string(line)
   utils.nivel_to_string(line)
   utils.condicion_laboral_to_string(line)
   utils.universitario(line)
   
   print(line)




  