import pymysql
from tkinter import *
from  tkinter import ttk
import tkinter as tk
import os
from sys import exit


def conexion():
	global con,cur
	conn = pymysql.connect(host='127.0.0.1',
	                             user='root',
	                             password='',
	                             db='basedatos',
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)

	cur=conn.cursor()



ventana=tk.Tk()
ventana.title("Calificaciones")
ventana.geometry('500x500')
ventana.configure(background='white')

image=tk.PhotoImage(file="esfotEpn.gif")
image=image.subsample(1	,1)
label=tk.Label(image=image)
label.pack()

image1=tk.PhotoImage(file="logo-epn.gif")
image1=image1.subsample(2,2)
label=tk.Label(image=image1)
label.pack()


var_IdP=StringVar()
var_pwsP=StringVar()
#Usuario
usuario=tk.Label(ventana, text="USUARIO: ", bg="blue",fg="white").place(x=150,y=225)

txtUsuario=Entry(ventana,textvariable=var_IdP).place(x=250,y=225)

#contraseña
contraseña=tk.Label(ventana, text="CONTRASEÑA: ", bg="blue",fg="white").place(x=150,y=275)

txtContraseña=Entry(ventana,textvariable=var_pwsP).place(x=250,y=275)



btProf=Button(ventana,text="ESTUDIANTE",padx=42,pady=5,background="#91F467", command=lambda:os.system("usuario.py")).place(x=160,y=325)
btEst=Button(ventana,text="PRFESOR",padx=42,pady=5,background="#91F467", command=lambda:os.system("profesor.py")).place(x=160,y=375)

ventana.mainloop()

def query(script,variable):
    #global conn,cur
    conexion()
    cur.execute(script,(variable))
    conn.commit()
    tabla=cur.fetchall()
    cur.close()
    conn.close
    return tabla


def extraer_celda(tabla,columna):
    try:
        fila=tabla[0]
        celda=fila[columna]
        return celda
    except:
        print('Datos incorrectos')

#LIMPIA  LABEL
def limpiar_label():
    global txtUsuario,txtContraseña
    txtUsuario.delete(0, END)
    txtContraseña.delete(0, END)

#CREAMOS VENTANA PARA LOGIN PROFESOR.

def loginProf():
    global var_IdP,var_pwsP
    usuario_ingresado=var_IdP.get()
    clave_ingresada=var_pwsP.get()
    limpiar_label()
    extraer_id_bd="SELECT IdProfesor FROM profesores WHERE IdProfesor=%s"
    extraer_psw_bd="SELECT pswProfesor FROM profesores WHERE pswProfesor =%s"
    print(extraer_psw_bd)
    tabla=query(extraer_id_bd,extraer_psw_bd)
    
    id_bd=extraer_celda(tabla,'IdProfesor')


    tabla=query(extraer_psw_bd,usuario_ingresado)
    psw_bd=extraer_celda(tabla,'nombre_estudiante')
    
    if id_bd == clave_ingresada and psw_bd == usuario_ingresado :

        print("Bienvenido!!")
        os.system('usuario.py')
    else:
        conexion_fallida()
        print('Usuario o clave incorrectos')

"""
def verifica_loginP():
    global verifica_usuario
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
    lista_idProfe=[]
    lista_pswProfe=[]

    buscar_profe=cur.fetchall()
    cur.execute("SELECT lidProfesor FROM profesores")

    lista_profe = cur.fetchall() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    for row in lista_profe:
        lista_idProfe.append(str(row[0]))       
       
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_idProfe:
        
        cur.execute("SELECT pswProfesor FROM profesores")
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        clave1=cur.fetchall()
        for row in clave1:
            lista_pswProfe.append(row[0])
            if clave1 in lista_pswProfe:
                print("conexion ok")
    else:
        print("conexion fallo")  




verifica_loginP()

def verifica_loginE():
    global verifica_usuario
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
    lista_idProfe=[]
    lista_pswProfe=[]

    buscar_profe=cur.fetchall()
    cur.execute("SELECT lidProfesor FROM profesores")

    lista_profe = cur.fetchall() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    for row in lista_profe:
        lista_idProfe.append(str(row[0]))       
       
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_idProfe:
        
        cur.execute("SELECT pswProfesor FROM profesores")
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        clave1=cur.fetchall()
        for row in clave1:
            lista_pswProfe.append(row[0])
            if clave1 in lista_pswProfe:
                print("conexion ok")
    else:
        print("conexion fallo")  

 
verifica_loginE()     

"""