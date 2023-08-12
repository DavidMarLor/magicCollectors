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
            print(elemento[1])
            imagen = cv2.imread(elemento[1])

            check = elemento[2]
            if nombreSeleccionado == nombre:
                print("Encontrada")
                cv2.imshow('Bill el poni', imagen)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("No encontrada")



#Obtener Imagen, sobre en el que se obtiene y precio
nombreCarta = "Bill el poni"
obtenerInfo(nombreCarta)