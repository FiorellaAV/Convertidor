from MySQLdb import *
import MySQLdb
from tkinter import CENTER, Entry, Tk, Button
from Menu_Eleccion import Menu
from tkinter import PhotoImage
from tkinter import Label
import os
import ctypes


direc = os.path.dirname(__file__)
icono = os.path.join(direc, 'imagenes/icono.png')
fondo = os.path.join(direc, 'imagenes/Backgroundd.png')


class Vent:

    def __init__(self):

        self.login = Tk()
        ancho_ventana = 500
        alto_ventana = 550
        x_ventana = self.login.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.login.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.login.geometry(posicion)
        self.login.configure(bg='#FFFFFF')
        self.login.title("Inicie Sesión")
        self.icono = PhotoImage(file= icono)
        self.login.iconphoto(False, self.icono)
        self.login.resizable(False, False)
        self.inicioSesion= False

        #Boton elegir archivo

        self.imagenn = PhotoImage(file = fondo)
        self.boton = Label(self.login, text = "Elegir archivo",image=self.imagenn)
        self.boton.pack()
        self.boton["border"] = "0"
        self.boton["bg"] = "white"

        #Label de Usuario
        self.user = Label(self.login, text = "Usuario", font=("Minion Pro", 12), fg = '#FFFFFF',
        bg='#18191e')
        self.user.place(relx=0.225, rely=0.35, anchor=CENTER)

        self.usuario= Entry(self.login)
        self.usuario.place(relx=0.30, rely=0.40, anchor=CENTER)

        #Label de Contraseña
        self.pw = Label(self.login, text = "Contraseña", font=("Minion Pro", 12), fg = '#FFFFFF',
        bg='#18191e')
        self.pw.place(relx=0.250, rely=0.48, anchor=CENTER)

        self.password = Entry(self.login, show="*")
        self.password.place(relx=0.30, rely=0.53, anchor=CENTER)

        self.DB_HOST = '31.170.167.13'
        self.DB_USER = 'u886019393_pablejkz_bd'
        self.DB_PASS = 'Pablitobasededatos73'
        self.DB_NAME = 'u886019393_pythonlogin'

        #Boton salir 
        button_salir = Button(self.login, text = "        Salir        ", command = self.salir, font=("Minion Pro", 10, 'bold'), bg = '#18191e', fg = '#FFFFFF')
        button_salir.config(highlightbackground= '#FFFFFF')
        button_salir.place(relx=0.65, rely=0.68, anchor=CENTER)

        #Boton iniciar sesion
    def buscar(self):
        boton_buscar = Button(self.login, text = " Iniciar Sesión ", command = self.iniciarSesion, font=("Minion Pro", 10, 'bold'), bg = '#18191e', fg = '#FFFFFF')
        boton_buscar.config(highlightbackground= '#FFFFFF')
        boton_buscar.place(relx=0.38, rely=0.68, anchor=CENTER)
        self.login.mainloop()


    def salir(self):
        self.login.destroy()


    def run_query(self,query=''):

        datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]

        conn = MySQLdb.connect(*datos) # Conectar a la base de datos
        cursor = conn.cursor()         # Crear un cursor
        cursor.execute(query)          # Ejecutar una consulta

        if query.upper().startswith('SELECT'):
            data = cursor.fetchall()   # Traer los resultados de un select
        else:
            conn.commit()              # Hacer efectiva la escritura de datos
            data = None

        cursor.close()                 # Cerrar el cursor
        conn.close()                   # Cerrar la conexión

        return data


    def iniciarSesion(self):

        usuario=self.usuario.get()

        #query2 = "SELECT pc_name FROM accounts WHERE username = '%s'" % usuario

        usuario=self.usuario.get()
        criterio = usuario
        query = "SELECT username FROM accounts WHERE username = '%s'" % criterio

        try:
            usuario_encontrado= self.run_query(query)
            usuario_encontrado=usuario_encontrado[0]
            usuario_encontrado=usuario_encontrado[0]

            if(usuario_encontrado != None):
                password = self.password.get()
                clave="SELECT username FROM accounts WHERE password = '%s'" % password
                contrasena=self.run_query(clave)
                contrasena=contrasena[0]
                contrasena=contrasena[0]
                if(usuario_encontrado == contrasena):

                    ver_nombrepc_en_base= "SELECT pc_name FROM accounts WHERE username= '%s'" % usuario_encontrado
                    pc_en_base=self.run_query(ver_nombrepc_en_base)
                    pc_en_base=pc_en_base[0]
                    pc_en_base=pc_en_base[0]
                    print(pc_en_base)

                    if (pc_en_base != None):
                        nombre_de_la_pc=os.getenv('COMPUTERNAME')

                        if(nombre_de_la_pc == pc_en_base):
                            self.inicioSesion = True
                        else:
                            ctypes.windll.user32.MessageBoxW(0, "La cuenta con la que esta queriendo ingresar no corresponden a esta computadora", "Ingresando", 0)

                    if(pc_en_base == None):
                        nombre_de_la_pc=os.getenv('COMPUTERNAME')
                        query3 = "update accounts set pc_name = '%s' where username = '%s'" % (nombre_de_la_pc, usuario_encontrado)
                        self.run_query(query3)
                        self.inicioSesion=True

            if (self.inicioSesion == True):
                self.login.destroy()
                Menu()

        except IndexError:
            ctypes.windll.user32.MessageBoxW(0, "Usuario o contraseña incorrectos", "Ingresando", 0)



xd = Vent()
xd.buscar()