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
	sql= 'SELECT nombreEstudiante,apellidoEstudiante FROM estudiantes'
	
	cur.execute(sql)
	result= cur.fetchall()

	#imprime en consola
	for row in result:
		print ("Nombre y Apellido: %s, %s " % (row['nombreEstudiante'],row['apellidoEstudiante']))
		
		print("------------------------------------")
		
	cur.close()
	conn.close

	#print ("conectada")
except Exception as e:
	raise
finally:
	conn.close
 
ventana=tk.Tk()
ventana.title("Estudiantes")
ventana.geometry('550x550')
ventana.configure(background='white')

image=tk.PhotoImage(file="epn.gif")
image=image.subsample(1	,1)
label=tk.Label(image=image)
label.pack()

#funcion para determinar que hace el boton
def usuario():
	usuario.set("Nombre: %s" % nombreEstudiante)
	#varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def contraseña():
	print("")
	#varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def Ingresar():
	print("")
	#varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))
def Nuevo():
	print("")
	#varresult.set("suma="+str(float(vartxt1.get())+float(vartxt2.get())))


btEst=Button(ventana,text="ATRAS",padx=42,pady=5,background="#91F465", command=lambda:os.system("calificaciones.py")).place(x=100,y=275)



ventana.mainloop()