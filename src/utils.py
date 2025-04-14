import csv
from pathlib import Path
#from constants import Data

def genero_to_string (dic):
    """Funcion que agrega culumna de Masculino o Femenino"""
    if dic['CH04'] == 1:
        dic['CH04_str'] = 'Masculino'
    elif dic['CH04'] == 2:
        dic['CH04_str'] = 'Femenino'            
    else:
        dic['CH04_str'] = None     

def nivel_to_string(dic):
    """Función que agrega columna de nivel educativo"""
    match dic['NIVEL_ED']:
        case 1:
            dic["NIVEL_ED_str"]=('Primario incompleto')
        case 2:
            dic["NIVEL_ED_str"]=('Primario completo')
        case 3:
            dic["NIVEL_ED_str"]=('Secundario incompleto')
        case 4:
            dic["NIVEL_ED_str"]=('Secundario completo')
        case 5 | 6:
            dic["NIVEL_ED_str"]=('Superior o universitario')
        case 7 | 9:
            dic["NIVEL_ED_str"]=('Sin información')

def condicion_laboral_to_string (dic): 
    """Funcion que agrega culumna de condicion laboral"""
    if (int(dic["ESTADO"]) == 1) and (int(dic["CAT_OCUP"])== 1 or 2):
        dic["CONDICION_LABORAL"]=('Ocupado autónomo')
    if (int(dic["ESTADO"]) == 1) and (int(dic["CAT_OCUP"])== 3 or 4 or 9):
        dic["CONDICION_LABORAL"]=('Ocupado dependiente')
    if (int(dic["ESTADO"]) == 2):
        dic["CONDICION_LABORAL"]=('Desocupado')
    if (int(dic["ESTADO"]) == 3):
        dic["CONDICION_LABORAL"]=('Inactivo')
    if (int(dic["ESTADO"]) == 4):
        dic["CONDICION_LABORAL"]=('Fuera de categoria')  

def universitario (diccionario):     
    """Funcion que agrega culumna de universitario"""
    if (int(diccionario["CH06"])>=18):
        if (int(diccionario["NIVEL_ED"]) == 5 or 6):
            diccionario['Universitario'] = 1
        else:
            diccionario['Universitario'] = 0
    else:
        diccionario['Universitario'] = 2

        
    