import csv
from pathlib import Path
from constants import Data

def genero_to_string (dic):
    """Funcion que agrega culumna de Masculino o Femenino"""
    if dic['CH04'] == 1:
        dic['CH04_str'] = 'Masculino'
    elif dic['CH04_str'] == 2:
        dic['CH04_str'] = 'Femenino'            
    else:
        dic['CH04_str'] = None

def genero_to_string (diccionario):
    """Funcion que agrega culumna de Masculino o Femenino"""
    if diccionario['CH04'] == 1:
        diccionario['CH04_str'] = 'Masculino'
    elif diccionario['CH04_str'] == 2:
        diccionario['CH04_str'] = 'Femenino'            

def nivel_to_string(diccionario):
    """Función que agrega columna de nivel educativo"""
    for linea in diccionario:
        match int(linea[26]):
            case 1:
                diccionario["NIVEL_ED_str"]=('Primario incompleto')
            case 2:
                diccionario["NIVEL_ED_str"]=('Primario completo')
            case 3:
                diccionario["NIVEL_ED_str"]=('Secundario incompleto')
            case 4:
                diccionario["NIVEL_ED_str"]=('Secundario completo')
            case 5 | 6:
                diccionario["NIVEL_ED_str"]=('Superior o universitario')
            case 7 | 9:
                diccionario["NIVEL_ED_str"]=('Sin información')



def condicion_laboral_to_string (diccionario): 
    """Funcion que agrega culumna de condicion laboral"""
    for linea in diccionario:
        if (int(diccionario["ESTADO"]) == 1) and (int(diccionario["ESTADO"])== 1 or 2):
            diccionario["CONDICION_LABORAL"]=('Ocupado autónomo')
        if (int(diccionario["ESTADO"]) == 1) and (int(linea["ESTADO"])== 3 or 4 or 9):
            diccionario["CONDICION_LABORAL"]=('Ocupado dependiente')
        if (int(diccionario["ESTADO"]) == 2):
            diccionario["CONDICION_LABORAL"]=('Desocupado')
        if (int(diccionario["ESTADO"]) == 3):
            diccionario["CONDICION_LABORAL"]=('Inactivo')
        if (int(diccionario["ESTADO"]) == 4):
            diccionario["CONDICION_LABORAL"]=('Fuera de categoria')  

def universitario (diccionario):     
    """Funcion que agrega culumna de universitario"""
    for linea in diccionario:
        if (int(diccionario["CH06"])>=18):
            if (int(diccionario["NIVEL_ED"]) == 5 or 6):
                diccionario[universitario] = 1
            else:
                diccionario[universitario] = 0
        else:
            diccionario[universitario] = 2

        
    