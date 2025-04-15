productos = [{"id": 1, "precio": 2000, "año": 2019, "vendidos": 30},
             {"id": 2, "precio": 2000, "año": 2019, "vendidos": 15},
             {"id": 3, "precio": 2000, "año": 2019, "vendidos": 20},
             {"id": 1, "precio": 2000, "año": 2020, "vendidos": 50},
             {"id": 2, "precio": 2000, "año": 2021, "vendidos": 100}]


def suma(y):
    suma = productos[y]['vendidos']
    for i in range(0, len(productos)):
        if productos[y]['id'] == productos[i]['id'] and productos[y]['vendidos'] != productos[i]['vendidos']:
            suma = productos[y]['vendidos'] + productos[i]['vendidos']
    return suma


lista_id = []

for i in range(len(productos)):
    if productos[i]['id'] not in lista_id:
        lista_id.append(productos[i]['id'])
    
print(lista_id)

for i in range(0, len(lista_id)):
    print("El id: " + str(lista_id[i]) + " en total vendio: " + str(suma(i)))