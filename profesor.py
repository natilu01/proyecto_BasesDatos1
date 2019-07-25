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


ventana.mainloop()