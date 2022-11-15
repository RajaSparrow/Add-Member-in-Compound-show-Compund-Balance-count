# Imports
import sqlite3


# Db class
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
         CREATE TABLE IF NOT EXISTS password (
              name text ,
              dob text ,
              username text , 
              password text,
              solt text
              ) 
         """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, dob, username, password, slot):
        self.cur.execute("insert into password values (?,?,?,?,?)", (name, dob, username, password, slot))
        self.con.commit()
