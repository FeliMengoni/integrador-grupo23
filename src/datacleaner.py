from src import utils
from src import utilsH

def cleanerU (lista_dic):

    for dic in lista_dic:
        for dato in dic:
            if dic[dato].isnumeric():
                dic[dato] = int(dic[dato])
            elif not dic[dato]:
                dic[dato] = None
            elif isinstance(dic[dato], str):
                dic[dato] = dic[dato].strip()
            else:
                dic[dato] = None
        utils.genero_to_string(dic)
        utils.nivel_to_string(dic)
        utils.condicion_laboral_to_string(dic)
        utils.universitario(dic)

def cleanerH (lista_dic):
    for dic in lista_dic:
        for dato in dic:
            if dic[dato].isnumeric():
                dic[dato] = int(dic[dato])
            elif not dic[dato]:
                dic[dato] = None
            elif isinstance(dic[dato], str):
                dic[dato] = dic[dato].strip()
            else:
                dic[dato] = None
    #utilsH.condicion_de_habitabilidad(lista_dic)
    utilsH.densidad_hogar(lista_dic)
    utilsH.material_techumbre(lista_dic)
    utilsH.tipo_hogar(lista_dic)
