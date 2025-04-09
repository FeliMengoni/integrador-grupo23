import os


ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets","individual", "usu_individual_T423.txt")

with open (ruta_archivo, 'r') as contenido:
    lista_datos = contenido.read()

spliteado = lista_datos.splitlines()

contaH = 0
contaM = 0
for l in spliteado[1:]:
    linea = l.split(';')
    if int(linea[11]) == 1:
        contaH = contaH + int(linea[9])
    if int(linea[11]) == 2:
        contaM = contaM + int(linea[9])

print(contaM)
print(contaH)