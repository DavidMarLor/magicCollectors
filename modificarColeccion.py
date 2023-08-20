import cv2

import os
import shutil

#image_dir = os.path.join('path', 'to', 'image')
#image_filename = 'image.jpg'
#full_image_path = os.path.join(image_dir, image_filename)

#image = cv2.imread(full_image_path)
#Archivo que controla la logica de la coleccion

#Leer fichero
def leerFichero():
    with open('list.txt', 'r') as fichero:
        for linea in fichero:
            print(linea)

#Escribir solo los checks

#Obtener Imagen y check
def obtenerInfo(nombreSeleccionado):
    with open('list.txt', 'r') as fichero:
        for linea in fichero:
            elemento = linea.split(',')
            nombre = elemento[0]
            imagen = cv2.imread(elemento[1])

            if nombreSeleccionado == nombre:
                print("Encontrada")
                cv2.imshow('Bill el poni', imagen)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("No encontrada")

def numeroCartas():
    contador = 0
    contadorTotal = 0
    contadorRestantes = 0
    with open('list.txt', 'r') as fichero:
        for linea in fichero:
            elemento = linea.split(',')
            check = elemento[2].strip()
            if check == "True":
                contador += 1
            if check == "False":
                contadorRestantes += 1
            contadorTotal += 1
    print("El numero de cartas total es: ", contadorTotal, " y el numero de cartas que tengo es: ", contador,
          " y me quedan: ", contadorRestantes)

#Obtener Imagen, sobre en el que se obtiene y precio
nombreCarta = "Bill el poni"
contador = 0
contadorTotal = 0
contadorRestantes = 0
#obtenerInfo(nombreCarta)
numeroCartas()
