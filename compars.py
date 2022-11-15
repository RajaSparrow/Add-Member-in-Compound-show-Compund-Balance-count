# Imports
import sqlite3


# Db class
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
         CREATE TABLE IF NOT EXISTS compars(
              Id text , 
              Name text,
              Age INTEGER,
              Gender text,
              Contact text,
              Address text,
              Solt text
              ) 
         """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, id, name, age, gender, contact, address, slot):
        self.cur.execute("insert into compars values (?,?,?,?,?,?,?)", (id, name, age, gender, contact, address, slot))
        self.con.commit()

    def select(self):
        self.cur.execute("SELECT * from  compars")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("delete from compars where id=? ", (id,))
        self.con.commit()

    def update(self, id, name, age, gender, contact, address, slot):
        self.cur.execute("update compars set name=?,age=?,gender=?,contact=?,address=?,solt=?  where id=?",
                         (name, age, gender, contact, address, slot, id))
        self.con.commit()

    # lion dear wolf counts
    def sqlcountl(self):
        rows = self.cur.execute('SELECT COUNT(solt)FROM compars WHERE solt="Solt-1 (LOIN)"')
        my = rows.fetchone()
        a = (''.join(map(str, my)))
        row = 50 - int(a)
        return row

    def sqlcountd(self):
        rows = self.cur.execute('SELECT COUNT(solt)FROM compars WHERE solt="Solt-2 (DEAR)"')
        my = rows.fetchone()
        a = (''.join(map(str, my)))
        row = 90 - int(a)
        return row

    def sqlcountw(self):
        rows = self.cur.execute('SELECT COUNT(solt)FROM compars WHERE solt="Solt-3 (WOLF)"')
        my = rows.fetchone()
        a = (''.join(map(str, my)))
        row = 30 - int(a)
        return row
