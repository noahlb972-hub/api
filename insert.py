import mysql.connector


mydb = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "",
  database = "ciel2027",
)

cursor = mydb.cursor()
request = "SELECT * FROM etudiant"
cursor.execute(request)
result = cursor.fetchall()


nom = "boug"
prenom = "an mwen"
request = f"INSERT INTO etudiant (nom,prenom) VALUES ('{nom}','{prenom}')"
print(request)
cursor.execute(request)
mydb.commit()

for record in result:
    print(record)

