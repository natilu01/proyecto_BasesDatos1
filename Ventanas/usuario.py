#import pymysql
from tkinter import *
from  tkinter import ttk
import turtle
import tkinter as tk
import os

ventana=tk.Tk()
ventana.title("Calificaciones")
ventana.geometry('550x550')
ventana.configure(background='white')

image=tk.PhotoImage(file="epn.gif")
image=image.subsample(1	,1)
label=tk.Label(image=image)
label.pack()

#funcion para determinar que hace el boton
def usuario():
	varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def contraseña():
	varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def Ingresar():
	varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def Nuevo():
	varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))


#Usuario
usuario=tk.Label(ventana, text="USUARIO: ", bg="blue",fg="white").place(x=150,y=120)
vartxtUsuario=StringVar()
txtUsuario=Entry(ventana,textvariable=vartxtUsuario).place(x=250,y=120)

#contraseña
contraseña=tk.Label(ventana, text="CONTRASEÑA: ", bg="blue",fg="white").place(x=150,y=155)
vartxtContraseña=StringVar()
txtContraseña=Entry(ventana,textvariable=vartxtContraseña).place(x=250,y=155)

#boton de ingreso
bIngresar=Button(ventana,command=Ingresar,text="INGRESAR",padx=42,pady=5,background="#91F467").place(x=200,y=190)

#nuevo registro
registro=tk.Label(ventana, text="REGISTRATE",fg="red").place(x=200,y=225)

#ingresar nuevo usuario nombres
nombres=tk.Label(ventana, text="NOMBRES: ", bg="blue",fg="white").place(x=90,y=260)
vartxtNombres=StringVar()
txtNombres=Entry(ventana,textvariable=vartxtNombres).place(x=250,y=260)

#apellidos
apellidos=tk.Label(ventana, text="APELLIDOS: ", bg="blue",fg="white").place(x=90,y=295)
vartxtApellidos=StringVar()
txtApellidos=Entry(ventana,textvariable=vartxtApellidos).place(x=250,y=295)

#crear contraseña

login=tk.Label(ventana, text="CONTRASEÑA: ", bg="blue",fg="white").place(x=90,y=330)
vartxtLogin=StringVar()
txtLogin=Entry(ventana,textvariable=vartxtLogin).place(x=250,y=330)

#confirmar contraseña
login2=tk.Label(ventana, text="CONFIRMAR CONTRASEÑA: ", bg="blue",fg="white").place(x=90,y=365)
vartxtLogin2=StringVar()
txtLogin2=Entry(ventana,textvariable=vartxtLogin2).place(x=250,y=365)

#email
email=tk.Label(ventana, text="E-MAIL: ", bg="blue",fg="white").place(x=90,y=400)
vartxtEmail=StringVar()
txtEmail=Entry(ventana,textvariable=vartxtEmail).place(x=250,y=400)

#fecha nacimiento 
fechaNac=tk.Label(ventana, text="FECHA NACIMIENTO: ", bg="blue",fg="white").place(x=90,y=435)
vartxtFechaNac=StringVar()
txtFechaNac=Entry(ventana,textvariable=vartxtFechaNac).place(x=250,y=435)

#boton de crear nuevo usuario
bNuevo=Button(ventana,command=Nuevo,text="CREAR CUENTA",padx=42,pady=5,background="#91F467").place(x=200,y=480)

#image1=tk.PhotoImage(file="epn.gif")
#image1=image1.subsample(1,1)
#label1=tk.Label(image1=image1)
#label1.place(x=25,y=400,relwidth=1.0,relheight=1.0)

ventana.mainloop()