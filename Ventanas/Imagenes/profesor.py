import pymysql
from tkinter import *
from  tkinter import ttk
import turtle
import tkinter as tk
import os



try:
	conn = pymysql.connect(host='127.0.0.1',
	                             user='root',
	                             password='',
	                             db='basedatos',
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)

	cur=conn.cursor()
	#cur.execute("DROP TABLE IF EXISTS profesor")

	#sql="CREATE TABLE profesor ( nombre VARCHAR(30) NOT NULL , cedula VARCHAR(30) NOT NULL )"
	sql="SELECT *  FROM profesores "
	#sql="SELECT *  FROM profesores "
	#mostrar en un label de tkinter concatenando con un +
	#ingresar las notas
	#con insert


	cur.execute(sql)
	result= cur.fetchone()
	print (result)

	cur.close()
	conn.close
	#print ("conectada")

except:

		messagebox.showwarning("¡ATENCION!","NO EXISTE EL USUARIO")
finally:
	conn.close





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
	#vartxtUsuario.set("USUARIO: "+ )
	print ("")
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