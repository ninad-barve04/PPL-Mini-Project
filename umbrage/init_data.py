import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

cur.execute("INSERT INTO location (name, description, lat, lng, zoom) VALUES (?, ?, ?, ?, ?)",
            ('Panshet', 'Panshet is an important eco-sensetive zone in western ghat', '18.3839','73.6036', '12')
            )

cur.execute("INSERT INTO history (loc_id, date, mapimage, greyimage, greencover) VALUES (?,?,?,?,?)",
            (1,'2009-12-1'  ,'map.png', 'grey.png',63.4)
            )
cur.execute("INSERT INTO history (loc_id, date, mapimage, greyimage, greencover) VALUES (?,?,?,?,?)",
            (1,'2009-12-1'  ,'map.png', 'grey.png',62.4)
            )   
cur.execute("INSERT INTO history (loc_id, date, mapimage, greyimage, greencover) VALUES (?,?,?,?,?)",
            (1,'2009-12-1'  ,'map.png', 'grey.png',61.4)
            ) 
connection.commit()
connection.close()
