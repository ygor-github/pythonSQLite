import sqlite3
import pandas as pd

con = sqlite3.connect('test.db')
cur = con.cursor()

#cur.execute('insert into users(name, cpf) values ("Juan Quiñonez","369258147-88")')

con.commit()

cur.execute('select * from users')
print(cur.fetchall())

con.close()