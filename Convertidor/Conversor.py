import MySQLdb.cursors
import time
import tkinter as tk
from tkinter import Tk
from tkinter import CENTER
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import filedialog
from docx2pdf import convert
from pdf2docx import parse
import Menu_Eleccion
from tkinter import Label
from tkinter.filedialog import askdirectory
import win32com.client as win32
from win32com.client import constants
import os
import re
import ctypes

direc = os.path.dirname(__file__)
principal = os.path.join(direc, 'imagenes/ElegirArchivo.png')
sii = os.path.join(direc, 'imagenes/si.png')
no = os.path.join(direc, 'imagenes/no.png')
icono = os.path.join(direc, 'imagenes/icono.png')
imagenn = os.path.join(direc, 'imagenes/Background_ElegirConversion.png')

class Conversor:


    def __init__(self):
        #Creo la ventana
        self.ruta = None
        self.ventana = tk.Tk()
        ancho_ventana = 500
        alto_ventana = 550
        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana.geometry(posicion)

        #IMAGENES

        #Icono de ventana
        self.ventana.configure(bg='#FFFFFF')
        self.ventana.title("Conversor")
        self.icono = PhotoImage(file= icono)
        self.ventana.resizable(False, False)
        self.ventana.iconphoto(False, self.icono)

        #otras imagenes
        self.imagen = PhotoImage(file = principal)
        self.si = PhotoImage(file = sii)
        self.no = PhotoImage(file = no)
        self.labelEspera = tk.Label(self.ventana,text="Espere por favor, su conversion esta siendo llevada a cabo")

        #Fondo principal de ventana
        self.imagenn = PhotoImage(file = imagenn)
        self.boton = Label(self.ventana, text = "Elegir archivo",image=self.imagenn)
        self.boton.pack()
        self.boton["border"] = "0"
        self.boton["bg"] = "white"

        #BOTONES

        #Boton elegir archivo
        self.boton = tk.Button(self.ventana, text = "Elegir archivo",image=self.imagen,command=self.guardar_en_carpeta)
        self.boton.place(relx=0.5, rely=0.75, anchor=CENTER)
        self.boton["border"] = "0"
        self.boton["bg"] = "white"

        #Boton volver
        self.boton_ventana= tk.Button(self.ventana, text="Volver",command = self.volver, bg = '#18191e', fg= '#FFFFFF')
        self.boton_ventana.place(relx=0.13, rely=0.8, anchor=CENTER)

        #Slider desplegable
        self.lista = ttk.Combobox(self.ventana, values=[
                                    "PDF a Word",
                                    "Word a PDF"
                                    ])
        self.lista.set('PDF a Word')
        self.lista.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.ventana.mainloop()

    #METODOS
    def guardar_en_carpeta(self):

        self.labelEspera.place(relx=0.5, rely=0.6, anchor=CENTER)
        ventana = tk.Toplevel()
        ventana.geometry("530x120")
        ventana.title("Conversor")
        ventana.configure(bg='#18191e')
        ventana.resizable(False, False)

        ventana.iconphoto(False, self.icono)

        titulo = tk.Label(ventana, text = "¿Desea guardar el nuevo archivo en su carpeta de orígen?",
        font=("Arial Black", 12), bg='#18191e', fg='#FFFFFF')
        titulo.place(relx=0.5, rely=0.15, anchor=CENTER)

        #si = PhotoImage(master = ventana, file = sii)

        boton_si = tk.Button(ventana, text = "Sí", height=50, width=70,image=self.si,command=lambda:self.elegir_archivo(True, ventana))
        boton_si["border"] = "0"

        boton_si.place(relx=0.3, rely=0.7, anchor=CENTER)

        boton_no = tk.Button(ventana, text = "No", height=50, width=70,image=self.no,command=lambda:self.elegir_archivo(False, ventana))
        boton_no["border"] = "0"

        boton_no.place(relx=0.7, rely=0.7, anchor=CENTER)


    def elegir_archivo(self, decision, ventana):


        ventana.destroy()

        root = Tk()
        root.withdraw()

        if self.lista.get() == "PDF a Word":
            root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Elegir archivo",
            filetypes = [("PDF","*.PDF")])
        elif self.lista.get() == "Word a PDF":
            root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Elegir archivo",
            filetypes = [("Word","*.docx"),("Word","*.doc")])
        ruta = root.filename


        self.convertir_archivo(ruta, decision)
        self.labelEspera['text'] = "Su conversion ha finalizado con exito"
        time.sleep(3)

        self.ventana.destroy()

    def convertir_archivo(self, ruta, decision):

        if decision == True:
            if ruta.endswith('pdf'):
                lista = ruta.split("\"")
                nombre_aux = lista[len(lista)-1]
                nombre_archivo = nombre_aux.replace('pdf','docx')
                parse(ruta, nombre_archivo, start=0, end=9999)

                ctypes.windll.user32.MessageBoxW(0, "Archivo convertido con éxito", "Convertido", 0)

            elif ruta.endswith('docx'):
                convert(ruta)
                ctypes.windll.user32.MessageBoxW(0, "Archivo convertido con éxito", "Convertido", 0)

            elif ruta.endswith('doc'):
                ruta_doc = ruta.replace("/", "\\\\""")
                self.doc_a_docx(ruta_doc)
                ruta_final = ruta_doc + 'x'
                convert(ruta_final)
                os.remove(ruta_final)
                ctypes.windll.user32.MessageBoxW(0, "Archivo convertido con éxito", "Convertido", 0)

            else:
                Exception('El archivo seleccionado no es doc, docx o pdf')

        else:
            root = Tk()
            root.withdraw()
            path = askdirectory(title='Elegir carpeta')
            os.chdir(path)

            if ruta.endswith('pdf'):
                lista = ruta.split("/")
                nombre_aux = lista[len(lista)-1]
                nombre_archivo = nombre_aux.replace('pdf','docx')
                ruta_nueva = path + "/" + nombre_archivo
                parse(ruta, ruta_nueva, start=0, end=9999)
                ctypes.windll.user32.MessageBoxW(0, "Archivo convertido con éxito", "Convertido", 0)
            elif ruta.endswith('docx'):
                convert(ruta, path)
                ctypes.windll.user32.MessageBoxW(0, "Archivo convertido con éxito", "Convertido", 0)
            elif ruta.endswith('doc'):
                ruta_doc = ruta.replace("/", "\\\\""")
                self.doc_a_docx(ruta_doc)
                ruta_final = ruta_doc + 'x'
                convert(ruta_final)
                os.remove(ruta_final)
                ctypes.windll.user32.MessageBoxW(0, "Archivo convertido con éxito", "Convertido", 0)
            else:
                Exception('El archivo seleccionado no es doc, docx o pdf')

    def doc_a_docx(self, ruta):

        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(ruta)
        doc.Activate ()

        new_file_abs = os.path.abspath(ruta)
        new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatXMLDocument
        )
        doc.Close(False)

    def volver(self):

        self.ventana.destroy()
        Menu_Eleccion.Menu()
