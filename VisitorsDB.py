import sqlite3  
  
con = sqlite3.connect("visitor.db")  
print("Database opened successfully")  
con.execute("create table Visitors (Id INTEGER PRIMARY KEY AUTOINCREMENT, Number VARCHAR NOT NULL, Visited_at DATETIME DEFAULT CURRENT_TIMESTAMP)")  
  
print("Table created successfully")  
  
con.close()  