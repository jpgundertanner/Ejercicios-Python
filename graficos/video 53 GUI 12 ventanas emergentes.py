from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
	messagebox.showinfo("Procesador de Jesús", "Procesador de textos 2020")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")#devuelve yes o no
	if valor == "yes":
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askokcancel("Reintentar", "No es posible cerrar, documento bloqueado")
	if valor == False:
		root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0) #con tearoff desaparece el separador ----
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardad")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de ...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()