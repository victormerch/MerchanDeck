from email.mime import image
from tkinter import*
from accesos import *
import os
'''
Solucionar problemas con las fotos 

'''
acces = accessos()
class carpetas:


    def PC(self):
        #--- Configuracion general---
        ventana2 = Tk()
        ventana2.geometry("350x300")
        ventana2.resizable(0,0)
        ventana2.title("PC")
        ventana2.config(bg='grey')
        ventana2.iconbitmap('pc-icon-13.ico')

        #putaima = PhotoImage(file="download.png")

        #--- Botones ---
        Volver = Button(ventana2, text='<-',
                        command=ventana2.destroy,bg="grey",
                        width=10, height=5).place(x=30, y=40)
        Cerra_sesion = Button(ventana2, text = 'Cerrar sesion',
                              command= acces.cerrarSesion,bg="grey",
                              width=10, height=5).place(x = 130, y = 40)
        Reiniciar = Button(ventana2, text = 'Reiniciar',
                           command=acces.reiniciar,bg="grey",
                           width=10, height=5).place(x = 230, y = 40)

        # --- Etiquetas ---
        etiqueta1 = Label(ventana2, text="Configuracion PC",
                          font=("retro", 20),
                          fg="black", bg="grey").place(x=100, y=6)

        # --- Bucle ---
        ventana2.mainloop()

    def Editores(self):
        # --- Configuracion general---
        ventana3 = Tk()
        ventana3.geometry("350x300")
        #ventana3.resizable(0, 0)
        ventana3.title("Editores de codigo")
        ventana3.config(bg='black')
        ventana3.iconbitmap("1014286.ico")


        # --- Botones ---
        Volver = Button(ventana3, text='<-',
                        command=ventana3.destroy
                        ,width=10, height=5,
                        fg="green", bg="black").place(x=30, y=40)
        Cmd  = Button(ventana3, text='Cmd',
                      command=acces.cmd,
                      width=10, height=5,
                      fg="green", bg="black").place(x = 130, y = 40)
        Python = Button(ventana3, text="m",
                        font=("openlogos",33),
                        command=acces.python,
                        width=2, height=1,
                        fg="green", bg="black").place(x = 225, y = 40)
        Java = Button(ventana3, text="Java",
                      command=acces.java,
                      width=10, height=5,
                      fg="green", bg="black").place(x = 230, y = 145)
        Mysql = Button(ventana3, text="d",
                      command=acces.mysql,
                      font=("openlogos", 33),
                      width=2, height=1,
                      fg="green", bg="black").place(x = 125, y = 145)
        Vb = Button(ventana3, text="Virtual Box",
                      command=acces.vb,
                      width=10, height=5,
                      fg="green", bg="black").place(x = 30, y = 145)


        #--- Etiquetas ---
        etiqueta2 = Label(ventana3, text="Editores de codigo",
                         font=("Paskowy",20),
                         fg="green", bg="black").place(x=115, y=6)


        #--- Bucle ---
        ventana3.mainloop()

    def games(self):
        # --- Configuracion general---
        ventana4 = Tk()
        ventana4.geometry("350x300")
        ventana4.resizable(0, 0)
        ventana4.title("Video Games")
        ventana4.config(bg='yellow')
        ventana4.iconbitmap("videogamee.ico")

        # --- Botones ---
        Volver = Button(ventana4, text='<-',
                        command=ventana4.destroy
                        , width=10, height=5,
                        fg="black", bg="yellow").place(x=30, y=40)

        Among_Us = Button(ventana4, text='Among Us',
                        command=acces.among
                        , width=10, height=5,
                        fg="black", bg="yellow").place(x=130, y=40)

        Minecraft = Button(ventana4, text="Minecraft",
                            command=acces.minecraft
                            , width = 10, height = 5,
                            fg = "black", bg = "yellow").place(x=230, y=40)

        # --- Etiquetas ---
        titulo = Label(ventana4, text="VideoGames",
                          font=("Paskowy", 23),
                          fg="black", bg="yellow").place(x=134, y=6)








        ventana4.mainloop()


