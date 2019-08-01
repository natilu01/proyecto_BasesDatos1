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
	sql="SELECT nombreProfesor,apellidoProfesor  FROM profesores "
	
	cur.execute(sql)
	result= cur.fetchall()
	
	for row in result:
		print ("Nombre y Apellido: %s, %s " % (row['nombreProfesor'],row['apellidoProfesor']))
		
		print("------------------------------------")
		

	cur.close()
	conn.close
	#print ("conectada")

except Exception as e:
	raise
finally:
	conn.close


ventana=tk.Tk()
ventana.title("Profesores")
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
	print ("")
def Ingresar():
	print ("")

#boton de ingreso y regreso
btEst=Button(ventana,text="ATRAS",padx=42,pady=5,background="#91F465", command=lambda:os.system("calificaciones.py")).place(x=100,y=275)




ventana.mainloop()