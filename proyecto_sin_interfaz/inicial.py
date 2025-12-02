import json

from funciones_libros.gestor_libros import Libro

def agregar_libro():


    lib = Libro()

    inventario = lib.inventario_actual()

    

    libro= lib.cargar_libro(inventario)

    inventario.append(libro)

    lib.agregar_libro_archivo(inventario)


def lista_ordenada():

    lib=Libro()

    inventario = lib.inventario_actual()

    

    n=len(inventario)

    inventario_ascendente=[]

    for e in range(len(inventario)):

        for i in range(0,len(inventario)-1-e):

            if  inventario[i]["ISBN"]>inventario[i+1]["ISBN"]:

                temp= inventario[i]
                inventario[i]= inventario[i+1]
                inventario[i+1]=temp

    return inventario           


inventario_ascendente= lista_ordenada()
print(inventario_ascendente)