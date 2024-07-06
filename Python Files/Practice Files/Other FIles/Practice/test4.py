import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword123",
    database="airline"
)

mycursor=mydb.cursor()
mycursor.execute("create database if not exists school")
mycursor.execute("show databases")
for x in mycursor:
    print(x)