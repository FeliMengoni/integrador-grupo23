import os
import requests
from src import functions
#urls de las bases de datos:
urls_hogar = ["https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/EPH_usu_hogar_4to_trim2020_txt.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/USU_hogar_t219.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/Usu_hogar_T319.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/Usu_hogar_T417.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T120.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T121.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T122.txt.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T123.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T124.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T216.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T220.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T221.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T222.txt.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T223.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T224.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T318.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T320.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T321.txt.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T322.txt.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T323.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T419.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T421.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T422.txt.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_T423.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t117.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t118.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t119.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t217txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t218.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t316.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t317.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t416.txt",
"https://github.com/FeliMengoni/integrador-grupo23/blob/main/datasets/hogar/usu_hogar_t418.txt",]
urls_individuales=[]
# Rutas de las carpetas locales y salidas
carpeta_hogar = "datasets_hogar"
carpeta_individuos = "datasets_individuos"
salida_hogar = "dataset_combinado_hogar.txt"
salida_individuales = "dataset_combinado_individuo.txt"

#unimos las bases de datos de hogar e individuo
functions.unir_individuales(salida_individuales)
print(salida_individuales)
#ruta_archivo = os.path.join(os.path.dirname(__file__), "datasets", "usu_hogar_T324.txt")
#with open(ruta_archivo, "r", encoding="utf-8") as archivo:
 ##   data_base = [linea.strip().split(";") for linea in archivo]



#lista_datos.dropna(inplace=True)  # Eliminar filas con valores nulos
#data_base = cleandata.cleaner(data_base)  # Limpiar los datos
#print(data_base)
