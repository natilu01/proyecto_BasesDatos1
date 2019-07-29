import pymysql


# Connect to the database

conn = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='basedatos',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cur=conn.cursor()
#cur.execute("DROP TABLE IF EXISTS profesor")

#sql="CREATE TABLE profesor ( nombre VARCHAR(30) NOT NULL , cedula VARCHAR(30) NOT NULL )"
sql="SELECT *  FROM estudiantes "
#sql="SELECT *  FROM profesores "
#mostrar en un label de tkinter concatenando con un +
#ingresar las notas
#con insert


cur.execute(sql)
result= cur.fetchone()
print (result)

cur.close()
conn.close





