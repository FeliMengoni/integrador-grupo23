import pandas as pd
import os

def cleaner(bd):
    """
    Función para limpiar los datos de un DataFrame.
    
    Args:
        bd (DataFrame): DataFrame a limpiar.
        
    Returns:
        DataFrame: DataFrame limpio.
    """
    
    # Eliminar columnas innecesarias
    bd.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
    
    # Renombrar columnas
    bd.rename(columns={"CODIGO": "codigo", "NOMBRE": "nombre"}, inplace=True)

    #rellena valores nulos con None
    bd.fillna(0)

    #crea nueva columna con
    
    return bd

