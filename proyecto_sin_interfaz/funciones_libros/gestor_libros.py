import json








class Libro:
    
    def __init__(self):
        pass
    

    def cargar_libro(self):

        print("Ingrese los datos de cada libro")

        isbn = input("Ingrese ISBN: ")
        titulo = input("Ingrese título: ")
        autor = input("Ingrese autor: ")
        peso = float(input("Ingrese peso (Kg): "))
        valor = int(input("Ingrese valor ($ COP): "))
        cantidad = int(input("Ingrese la cantidad "))

        libro = {
            "ISBN": isbn,
            "Título": titulo,
            "Autor": autor,
            "Peso": peso,
            "Valor": valor,
            "Cantidad": cantidad,
            "Cantidad_presente": 0
        }
    
        return libro
    
    def inventario_actual(self):

        with open("libros.json","r")as archivo_json:

            lista_actual = json.load(archivo_json)
    
            archivo_json.close()

        return lista_actual
    
    
    def agregar_libro_archivo(self,inventario):


        with open("libros.json","w") as archivo:

            json.dump(inventario,archivo,indent=4)

            archivo.close()

        print("libro cargado correctamente")