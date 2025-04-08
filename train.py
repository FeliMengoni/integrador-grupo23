import os
from src import cleandata


ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_individual_T324.txt")

with open (ruta_archivo, 'r') as contenido:
    lista_datos = contenido.read()

spliteado = lista_datos.splitlines()
del spliteado[0]

contaH = 0
contaM = 0
for l in spliteado:
    linea = l.split(';')
    if int(linea[11]) == 1:
        contaH = contaH + int(linea[9])
    if int(linea[11]) == 2:
        contaM = contaM + int(linea[9])

print(contaM)
print(contaH)