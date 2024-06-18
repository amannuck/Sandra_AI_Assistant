import sqlite3

con = sqlite3.connect("sandra.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'discord','C://Users//amann//AppData//Local//Discord//app-1.0.9149//Discord.exe')"
# cursor.execute(query)
# con.commit()


# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'spotify', 'https://www.spotify.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'chatgpt', 'https://www.chatgpt.com/')"
# cursor.execute(query)
# con.commit()

# query = "DELETE FROM web_command WHERE name='spotify'"
# cursor.execute(query)
# con.commit()
