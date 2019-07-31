import pymysql
from tkinter import *
from  tkinter import ttk
import turtle
import tkinter as tk
import os
from tkinter import messagebox




ventana=tk.Tk()
ventana.title("Calificaciones")
ventana.geometry('550x550')
ventana.configure(background='white')

image=tk.PhotoImage(file="esfotEpn.gif")
image=image.subsample(1	,1)
label=tk.Label(image=image)
label.pack()

#funcion para determinar que hace el boton
def usuario():
	print ("")

def profesor():
	varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def contraseña():
	varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def Ingresar():
	if  (combo.get())=="PROFESOR":
	    command=lambda:os.system("python usuario.py")


#Usuario
usuario=tk.Label(ventana, text="USUARIO: ", bg="blue",fg="white").place(x=150,y=120)
vartxtUsuario=StringVar()
txtUsuario=Entry(ventana,textvariable=vartxtUsuario).place(x=250,y=120)

#contraseña
contraseña=tk.Label(ventana, text="CONTRASEÑA: ", bg="blue",fg="white").place(x=150,y=155)
vartxtContraseña=StringVar()
txtContraseña=Entry(ventana,textvariable=vartxtContraseña).place(x=250,y=155)

#perfil
#perfil=tk.Label(ventana, text="PERFIL: ", bg="blue",fg="white").place(x=150,y=190)
#comboBox para seleccionar el estudiante o el profesor
#vartxtPerfil=StringVar()
btProf=Button(ventana,text="ESTUDIANTE",padx=42,pady=5,background="#91F467", command=lambda:os.system("usuario.py")).place(x=100,y=225)
btEst=Button(ventana,text="PRFESOR",padx=42,pady=5,background="#91F467", command=lambda:os.system("profesor.py")).place(x=100,y=275)


#boton de ingreso
#bIngresar=Button(ventana,command=Ingresar,text="INGRESAR",padx=42,pady=5,background="#91F467").place(x=200,y=225)

#image1=tk.PhotoImage(file="epn.gif")
#image1=image1.subsample(1,1)
#label1=tk.Label(image1=image1)
#label1.place(x=25,y=400,relwidth=1.0,relheight=1.0)

ventana.mainloop()
