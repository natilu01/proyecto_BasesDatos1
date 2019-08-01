from tkinter import *
import os
import pymysql
import turtle
import tkinter as tk
from  tkinter import ttk
from tkinter import messagebox

try:
    conn = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',
                                 db='basedatos',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    cur=conn.cursor()
    sql= 'SELECT IdProfesor,pswProfesor FROM profesores'
    
    cur.execute(sql)
    result= cur.fetchall()

    #imprime en consola
    for row in result:
        print ("Nombre y Apellido: %s, %s " % (row['IdProfesor'],row['pswProfesor']))
        
        print("------------------------------------")
        
    cur.close()
    conn.close

    #print ("conectada")
except Exception as e:
    raise
finally:
    conn.close

