import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "6648",
    database ="mydatabase"
  )

mycursor = mydb.cursor()
 
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()
sql = "SELECT * FROM customers ORDER BY name"

for x in myresult:
  print(x)
  sql = "SELECT * FROM customers WHERE address ='Highway 21'"


mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
