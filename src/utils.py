import csv
from pathlib import Path
from constants import Data

def genero_to_string (lista_de_datos):
    """Funcion que agrega culumna de Masculino o Femenino"""
    if dic['CH04'] == 1:
        dic['CH04_str'] = 'Masculino'
    elif dic['CH04_str'] == 2:
        dic['CH04_str'] = 'Femenino'            

def nivel_to_string(lista_de_datos):
    """Función que agrega columna de nivel educativo"""
    lista_de_datos[0].append('NIVEL_ED_str')
    for linea in lista_de_datos[1:]:
        match int(linea[26]):
            case 1:
                linea.append('Primario incompleto')
            case 2:
                linea.append('Primario completo')
            case 3:
                linea.append('Secundario incompleto')
            case 4:
                linea.append('Secundario completo')
            case 5 | 6:
                linea.append('Superior o universitario')
            case 7 | 9:
                linea.append('Sin información')



def condicion_laboral_to_string (diccionario): #HAY QUE CAMBIAR NIVEL ED POR ESTADO Y ESTADO POR CAT_OCUP
    """Funcion que agrega culumna de condicion laboral"""
    for linea in diccionario:
        if (int(diccionario["NIVEL_ED"]) == 1) and (int(diccionario["ESTADO"])== 1 or 2):
            diccionario["CONDICION_LABORAL"]=('Ocupado autónomo')
        if (int(diccionario["NIVEL_ED"]) == 1) and (int(linea["ESTADO"])== 3 or 4 or 9):
            diccionario["CONDICION_LABORAL"]=('Ocupado dependiente')
        if (int(diccionario["NIVEL_ED"]) == 2):
            diccionario["CONDICION_LABORAL"]=('Desocupado')
        if (int(diccionario["NIVEL_ED"]) == 3):
            diccionario["CONDICION_LABORAL"]=('Inactivo')
        if (int(diccionario["NIVEL_ED"]) == 4):
            diccionario["CONDICION_LABORAL"]=('Fuera de categoria')  

def universitario (diccionario):     
    """Funcion que agrega culumna de universitario"""
<<<<<<< HEAD
    for linea in lista_de_datos:
        if ("aca hay q poner si es mayor d edad"):
            if (int(linea[26]) == 5 or 6):
                linea['UNIVERSITARIO']=1
=======
    for linea in diccionario:
        if (int(diccionario["CH06"])>=18):
            if (int(diccionario["NIVEL_ED"]) == 5 or 6):
                diccionario[universitario] = 1
>>>>>>> 33646b9b1ef243356d3feee13a604453b980dac2
            else:
                diccionario[universitario] = 0
        else:
            diccionario[universitario] = 2



        
    