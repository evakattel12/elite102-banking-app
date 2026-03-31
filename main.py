import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("DROP TABLE test")
