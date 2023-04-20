from mysql.connector import connect

# Connexion à la base de données MySQL
mydb = connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="mysokoban"
)

mycursor = mydb.cursor()
mycursor.execute("Show tables;")

tables = mycursor.fetchall()

if ("game",) not in tables:
    print("Table does not exist -> so create it")
    mycursor.execute(
        "CREATE TABLE game (id INT AUTO_INCREMENT PRIMARY KEY, player_name VARCHAR(255), score INT)")
else:
    print("Table already exists")