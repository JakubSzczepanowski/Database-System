import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
# c.execute(f"CREATE TABLE {'elosz'} (elo text, siema real)")
# c.execute(f"INSERT INTO elosz VALUES ('a',1)")
# c.execute(f"INSERT INTO elosz VALUES ('a',2)")
#c.execute("PRAGMA table_info('produkty')")
#c.execute("select name from sqlite_master where type = 'table'")
c.execute("SELECT amount,quantity_price FROM Data")
#c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produkty'")
result = 0
for elem in c.fetchall():
    result += elem[0] if elem[1] is not None else -elem[0]
if result >= 0:
    print(True)
print(result)
conn.close()
