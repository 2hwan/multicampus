import sqlite3

conn  = sqlite3.connect('database_new.db')

c = conn.cursor()

c.execute('UPDATE users SET username = ? WHERE id = ?', ('niceman',11))
conn.commit()

c.execute('UPDATE users SET username = :name WHERE id = :id', {'name': 'goodman', 'id': 12})
conn.commit()

c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badman','13'))
conn.commit()

c.execute("DELETE FROM users WHERE id = ?",(14,))
conn.commit()

conn.close()