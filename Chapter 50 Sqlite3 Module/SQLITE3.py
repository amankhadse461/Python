import sqlite3
#Create a Table
conn = sqlite3.connect('test.db')


conn.execute('''CREATE TABLE STUDENT
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         NUMBER         INT     NOT NULL);''')


conn.close()

#Insert Operation

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,NUMBER) \
      VALUES (1, 'Aman', 32, 'Wardha', 7457484569 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,NUMBER) \
      VALUES (2, 'Ram', 25, 'Nagpur', 7458456235 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,NUMBER) \
      VALUES (3, 'Trupti', 23, 'Pune', 8352236547 )");

conn.close()

cursor = conn.execute("SELECT id, name, address, number from STUDENT")
for row in cursor:
   print ("ID = "), row[0]
   print ("NAME = "), row[1]
   print ("ADDRESS = "), row[2]
   print ("NUMBER = "), row[3], "\n"


conn.close()