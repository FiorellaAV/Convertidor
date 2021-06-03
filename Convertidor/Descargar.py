import tkinter as tk
import pytube, os
from tkinter import CENTER
from tkinter import PhotoImage
from tkinter import Label
import Menu_Eleccion
from MP4toMP3 import mp4_a_mp3

direc = os.path.dirname(__file__)
icono = os.path.join(direc, 'imagenes/icono.png')
youtube = os.path.join(direc, 'imagenes/yt2.png')
fondo = os.path.join(direc, 'imagenes/fondopelado.png')
videos = os.path.join(direc, 'videos_descargados')

class Download:

    def __init__(self):
        
        #Creo la ventana
        self.ventana_descargar = tk.Tk()
        ancho_ventana = 500
        alto_ventana = 550
        x_ventana = self.ventana_descargar.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana_descargar.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana_descargar.geometry(posicion)

        #IMAGENES:

        #Icono de ventana
        self.ventana_descargar.configure(bg='#FFFFFF')
        self.ventana_descargar.title("Descargar")
        self.icono = PhotoImage(file= icono)
        self.ventana_descargar.iconphoto(False, self.icono)
        self.ventana_descargar.resizable(False, False)

        #Fondo principal de ventana
        self.imagenn = PhotoImage(file = fondo)
        self.boton = Label(self.ventana_descargar, text = "Elegir archivo",image=self.imagenn)
        self.boton.pack()
        self.boton["border"] = "0"
        self.boton["bg"] = "white"

        #imagen de youtube
        self.yt = PhotoImage(file = youtube)
        self.label_yt = tk.Label(self.ventana_descargar, height=100, width=392,image=self.yt)
        self.label_yt["border"] = "0"
        self.label_yt.place(relx=0.5, rely=0.2, anchor=CENTER)

        #TEXTOS:

        #texto link
        self.cadena_link =tk.Label(self.ventana_descargar, text = "Inserte el link del video ", font=("Minion Pro", 15, 'bold'), bg = '#18191e', fg = '#FFFFFF')
        self.cadena_link.place(relx=0.345, rely=0.445, anchor=CENTER)

        #BOTONES:

        #boton volver
        self.boton_ventana_anterior = tk.Button(self.ventana_descargar, text="   Volver   ",font=("Minion Pro", 13), bg = '#18191e', fg = '#FFFFFF',command = self.volver)
        self.boton_ventana_anterior.place(relx=0.33 , rely=0.635, anchor=CENTER)

        #boton descraga
        self.boton_descargar = tk.Button(self.ventana_descargar, text = "  Descargar  ",font=("Minion Pro", 13), bg = '#18191e', fg = '#FFFFFF',command=lambda:self.descargar(0))
        self.boton_descargar.place(relx=0.68, rely=0.635, anchor=CENTER)



        #boton ADICIONAL 
        self.boton_descargar = tk.Button(self.ventana_descargar, text = "  Descargar video y sonido aparte  ",font=("Minion Pro", 13), bg = '#18191e', fg = '#FFFFFF',command=lambda:self.descargar(1))
        self.boton_descargar.place(relx=0.68, rely=0.75, anchor=CENTER)



        #Caja de link
        self.link= tk.Entry(self.ventana_descargar)
        self.link.config(width=60)
        self.link.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.ventana_descargar.mainloop()
   
    #METODOS:

    def descargar(self, modo):        

        self.enlace=self.link.get()
        self.yt = pytube.YouTube(self.enlace)
        self.yt.streams.first().download(videos)

        if(modo == 1):
            video = pytube.YouTube(self.enlace)
            video_titulo = video.title
            ruta_mp3 = videos + '/'
            mp4_a_mp3(ruta_mp3, video_titulo)


    def volver(self):

        self.ventana_descargar.destroy()
        Menu_Eleccion.Menu()