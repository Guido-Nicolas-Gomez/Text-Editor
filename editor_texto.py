#   Crear un Editor de texto basico

from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox

#   ____ DEFINICIONES ____

# Funciones

ruta = ""

def elegir_ruta_abrir():
    ruta = FileDialog.askopenfilename(title="Archivo de texto",
                                      initialdir=".",
                                      filetypes=(("Archivo de texto","*.txt"),),
    )
    return ruta

def elegir_ruta_guardar():
    ruta = FileDialog.asksaveasfilename(title="Guardar Fichero",
                                        initialdir=".",
                                        filetypes=(("Archivo de taxto","*.txt"),),
                                        defaultextension=".txt"
        )
    return ruta

def nuevo():
    global ruta
    ruta = ""
    # Titulo
    root.title("Nuevo archivo - Editor de Nico")
    # Cuerpo
    texto.delete(1.0,"end")
    #Pie
    mensaje_pie.set("Nuevo Archivo")

def abrir():
    global ruta
    ruta = elegir_ruta_abrir()
    #Titulo
    root.title(ruta + "- Editor de Nico")
    # Cuerpos
    with open(ruta, "r") as f: # Cargando el contenido del archivo en el editor
        texto.delete(1.0,"end")
        texto.insert("insert", f.read())
    # Pie
    mensaje_pie.set("El archivo de Abrio correctamente")

def guardar():
    global ruta

    if ruta != "":
        with open(ruta, "w") as f:
            contenido = texto.get(1.0,"end-1c")
            f.write(contenido)
        mensaje_pie.set("El archivo fue guardado")
    else:
        guardar_como()

def guardar_como():
    global ruta
    ruta = elegir_ruta_guardar()

    if ruta != "":
        guardar()
    else:
        mensaje_pie.set("Guardado cancelado")

def salir():
    root.quit()

def acerca_de():
    MessageBox.showinfo(
        title="Detalle:",
        message="""
        Creado por: Guido Nicolás Gómez
        Fecha: 08/04/2022
        Version: 1.0
        """)


# Ventana
root = Tk()
root.title("Editor de nico")
root.iconbitmap("icono.ico")
root.geometry('324x525')

# menus
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=salir)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Acerca de", command=acerca_de)

# Cuerpo
texto = Text(root, font="Console", bg="beige")

# Pie
mensaje_pie = StringVar(value="Bienvenido a tu editor")
monitor = Label(root)
monitor.config(textvariable=mensaje_pie)

#   ____ INSTANCIAS ____

# Menus
root.config(menu=menubar)
menubar.add_cascade(menu=filemenu, label="Archivos")
menubar.add_cascade(menu=editmenu, label="Ayuda")

# Cuerpo
texto.pack(fill="both", expand=1)

# Pie
monitor.pack(side="left")

# Raíz
root.mainloop()
