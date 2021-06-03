import tkinter as tk
from tkinter import CENTER
from tkinter import W
from Conversor import Conversor
from Descargar import Download
from tkinter import Label
from tkinter import PhotoImage
import os

direc = os.path.dirname(__file__)
icono = os.path.join(direc, 'imagenes/icono.png')
fondo_menu = os.path.join(direc, 'imagenes/background_SeleccioneSuOperacion.png')

class Menu:

    def __init__(self):
        #Creo la ventana
        self.menu_eleccion = tk.Tk()
        ancho_ventana = 500
        alto_ventana = 550
        x_ventana = self.menu_eleccion.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.menu_eleccion.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.menu_eleccion.geometry(posicion)

        #IMAGENES

        #Icono de ventana
        self.menu_eleccion.configure(bg='#FFFFFF')
        self.menu_eleccion.title("MENU")
        self.menu_eleccion.resizable(False, False)
        self.icono = PhotoImage(file= icono)
        self.menu_eleccion.iconphoto(False, self.icono)

        #Fondo principal de ventana
        self.imagenn = PhotoImage(file = fondo_menu)
        self.boton = Label(self.menu_eleccion, text = "Elegir archivo",image=self.imagenn)
        self.boton.pack()
        self.boton["border"] = "0"
        self.boton["bg"] = "white"

        #TEXTOS

        #textos 1 del menu
        self.boton_convertidor = tk.Button(self.menu_eleccion, text = "Asistente de conversión",command=self.conversor, font=("Minion Pro", 20),fg = '#FFFFFF',
        bg='#18191e')
        self.boton_convertidor.place(relx=0.5, rely=0.47, anchor=CENTER)

        #textos 2 del menu
        self.boton_descargar = tk.Button(self.menu_eleccion, text = "  Asistente de descarga  ",command=self.descargar, font=("Minion Pro", 20),fg = '#FFFFFF',
        bg='#18191e')
        self.boton_descargar.place(relx=0.5, rely=0.62, anchor=CENTER)

        #self.user = tk.Label(self.menu_eleccion, text = " Seleccione su operacion ", font=("Arial Black", 16),
        #bg='#FFFFFF')
        #self.user.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.menu_eleccion.mainloop()

    #Metodos
    def conversor(self):
        self.menu_eleccion.destroy()
        Conversor()
    def descargar(self):
        self.menu_eleccion.destroy()
        Download()

