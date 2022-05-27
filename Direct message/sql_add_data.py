import sqlite3
# my_list=[("chess.design.co",0), ("pawful.designs_", 0), ("johnny", 0)]
file_data = [i.strip('\n').split(',') for i in open('filename.txt')]
new_data = [a for a in file_data]  # convert string id to integer

con = sqlite3.connect("dog.db")

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS usernames
                    (user TEXT PRIMARY KEY, bolean INTEGER DEFAULT 0 ) ''')

cur.executemany("INSERT OR IGNORE INTO usernames (user) VALUES (?)", new_data)
# cur.execute("""ALTER TABLE usernames ADD bolean INTEGER DEFAULT 0""")


# cur.execute("SELECT user, bolean FROM usernames where bolean = 0")
# usern =cur.fetchone()[0]
# print(usern)
# cur.execute('SELECT bolean FROM usernames WHERE user= ?', (usern,))

# cur.execute('UPDATE usernames SET bolean=? WHERE user=?', (1, usern))
# print("%s" %usern +" "+ "updated")


cur.execute("UPDATE usernames set bolean ='0'")
for row in cur.execute(''' SELECT * FROM usernames'''):
    print(row)


con.commit()
con.close()
