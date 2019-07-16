#import pymysql
from tkinter import *
from  tkinter import ttk
import turtle
import tkinter as tk


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
def contraseña():
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

#perfil
perfil=tk.Label(ventana, text="PERFIL: ", bg="blue",fg="white").place(x=150,y=190)
#comboBox para seleccionar el estudiante o el profesor
vartxtPerfil=StringVar()
combo=ttk.Combobox(ventana)
combo.place(x=250,y=190)
combo ['values']=('ESTUDIANTE','PROFESOR')
combo.current(0)

#boton de ingreso
bIngresar=Button(ventana,command=Ingresar,text="INGRESAR",padx=42,pady=5,background="#91F467").place(x=200,y=225)

#image1=tk.PhotoImage(file="epn.gif")
#image1=image1.subsample(1,1)
#label1=tk.Label(image1=image1)
#label1.place(x=25,y=400,relwidth=1.0,relheight=1.0)

ventana.mainloop()
