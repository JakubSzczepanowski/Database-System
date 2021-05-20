import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
# c.execute(f"CREATE TABLE {'elosz'} (elo text, siema real)")
# c.execute(f"INSERT INTO elosz VALUES ('a',1)")
# c.execute(f"INSERT INTO elosz VALUES ('a',2)")
#c.execute("PRAGMA table_info('produkty')")
#c.execute("select name from sqlite_master where type = 'table'")
c.execute("SELECT * FROM Products")
#c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produkty'")
print(c.fetchall())
conn.close()
