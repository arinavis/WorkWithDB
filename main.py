import SecretData
import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3317,
    user='root',
    password=SecretData.mySQLpass,
    database='employees_data'
)

c = conn.cursor()
c.execute('select * from employees')
conn.commit()


