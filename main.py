# Fichero main con la estructura para la visualizacion de la aplicacion
# Necesito una ventana principal para seleccionar la coleccion que cambiara de ventana y nos mostrara en cuadricula
# todas las cartas con un check abajo si lo tenemos o no, esto sera leyendo de un fichero en local que tendra el si o no.

from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("Collector")
ventana.geometry("500x700")


def verColeccion():
    ventana_Colleccion = Toplevel()
    ventana_Colleccion.title("Coleccion")
    ventana_Colleccion.geometry("500x700")

    control = IntVar()

    opcion1 = Checkbutton(ventana_Colleccion, text="Obtenido", variable=control)
    opcion1.pack()
    #Cada carta de la coleccion es un boton con el fondo de la carta, al pulsar sobre esta enviamos el nombre y creamos
    #una ventana nueva con la imagen, nombre, precio, si la tenemos o no, y donde se consigue.

def exit():
    ventana.destroy()


image = Image.open('./background.jpg')
python_image = ImageTk.PhotoImage(image)
image_label = Label(ventana, image=python_image)
boton1 = Button(ventana, text="Colección", command=verColeccion)
boton1.pack(side=BOTTOM, pady=200)

boton2 = Button(ventana, text="Cerrar", command=exit)
boton2.pack(side=BOTTOM, pady=5)

ventana.mainloop()
