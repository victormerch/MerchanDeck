from tkinter import*
from tkinter import messagebox

from accesos import*
from carpetas import*

class main:
    def __init__(self):
        # --- Obejeto accesos para almacenar la funcion de cada accesso a las paginas ---
        acces = accessos()
        carps = carpetas()

        # --- Configuracion de la interfaz ---

        ventana = Tk()
        ventana.geometry("543x420")
        ventana.title("Merchan Deck")
        ventana.resizable(0, 0)
        ventana.config(bg='black')
        ventana.iconbitmap('iconoVictorDeck.ico')

        # --- Imagen de los iconos ---

        imagen1 = PhotoImage(file="371907120_YOUTUBE_ICON_400px.gif")
        imagen2 = PhotoImage(file="netflix.png")
        imagen3 = PhotoImage(file="twitch.png")
        imagen4 = PhotoImage(file="79828727383839.56364425d6616.gif")
        imagen5 = PhotoImage(file="tenor.gif")
        imagen6 = PhotoImage(file="images.png")
        imagen7 = PhotoImage(file="images - copia.png")
        imagen8 = PhotoImage(file="unnamed.png")
        imagen9 = PhotoImage(file="videogamee.png")
        imagen10 = PhotoImage(file="Discord512512-1.gif")
        imagen11 = PhotoImage(file="1014286.png")
        imagen12 = PhotoImage(file="0efaec704981b4653bc5459f309eca57.gif")
        imagSalir = PhotoImage(file="unnamed.gif")


        #--- Funciones de esta ventana ---

        def Salir():
            valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
            if valor == "yes":
                ventana.destroy()

        def aviso():
            messagebox.showwarning(title="Opcion no disponible", message="Esta opcion esta en desarrollo")

        # --- Botones ---

        #Fila 1
        Youtube = Button(ventana, command=acces.youtube,
                         image=imagen1,
                         width=100, height=100,bg="black").place(x=30, y=40)
        Netlfix = Button(ventana, command=acces.netflix,
                         image=imagen2,
                         width=100, height=100,bg="black").place(x=160, y=40)
        Twitch = Button(ventana, command=acces.twitch,
                        image=imagen3,
                        width=100, height=100,bg="black").place(x=290, y=40)
        Google = Button(ventana, command=acces.google,
                        image=imagen8,
                        width=100, height=100,bg="black").place(x=410, y=40)

        #Fila2
        Whatsapp = Button(ventana, command=acces.whatsapp,
                          image=imagen4,
                          width=100, height=100,bg="black").place(x=160, y=160)
        Instagram = Button(ventana, command=acces.instagram,
                           image=imagen5,
                           width=100, height=100,bg="black").place(x=30, y=160)
        Gmail = Button(ventana, command=acces.gmail,
                       image=imagen6,
                       width=100, height=100).place(x=290, y=160)
        Pc = Button(ventana, command=carps.PC,
                       image=imagen12,
                       width=100, height=100,bg="black").place(x=410, y=160)

        #Fila 3
        Dicord = Button(ventana, command=acces.discord,
                       image=imagen10,
                       width=100, height=100,bg="black").place(x=30, y=280)
        Games = Button(ventana, command=carps.games,
                       image=imagen9,
                       width=100, height=100,bg="black").place(x=160, y=280)
        Editores = Button(ventana, command=carps.Editores,
                       image=imagen11,
                       width=100, height=100,bg="black").place(x=290, y=280)
        Apagar = Button(ventana, command=Salir,
                       image=imagSalir,
                       width=100, height=100,bg="black").place(x=410, y=280)


        # --- Etiquetas ---

        Texto = Label(ventana, text='Merchan Deck', font=("Sectar",17), fg="grey", bg="black").place(x=190, y=6)

        # --- Bucle para que la interfaz siga funcionando ---
        ventana.mainloop()

App = main()