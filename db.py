import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db) #connection to data base
        self.cur = self.conn.cursor()  #used to execute queries
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY, guest text, country text, num_guests integer, email text, apartment integer, checkin text, checkout text, price integer)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM reservations")
        rows = self.cur.fetchall()
        return rows

    def insert(self, guest, country, num_guests, email, apartment, checkin, checkout, price):
        self.cur.execute("INSERT INTO reservations VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                         ( guest, country, num_guests, email, apartment, checkin, checkout, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM reservations WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, guest, country, num_guests, email, apartment, checkin, checkout, price):
        self.cur.execute("UPDATE reservations SET guest = ?, country = ?, num_guests = ?, email= ?, apartment = ?, checkin = ?, checkout = ?, price = ? WHERE id = ?",
                         (guest, country, num_guests, email, apartment, checkin, checkout, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

'''
db = Database('reservacijeinfo.db')
db.insert("Daria Zelenskaia", "Russia", 2, "daria@gmail.com" ,1, "26.12.2021.", "28.12.2021." , 84)
db.insert("Jan Carsten Schroeder", "Germany", 1, "jan@gmail.com" , 1, "25.12.2021.", "27.12.2021." , 62)
db.insert("Lindy Lely", "New Zealand", 2, "lindylen@gmail.com" , 1, "21.07.2022.", "23.07.2022." , 64)
db.insert("Baeva Aleksandrova", "Russia", 2,"baeva@gmail.com" , 2, "25.07.2022.", "31.07.2022." , 192)
db.insert("Fabian Eva", "Slovakia", 2,"fabian@gmail.com" , 2, "31.07.2022.", "05.08.2022." , 160)
db.insert("Krisztina Lakatos", "Slovakia", 3, "krisztina@gmail.com" , 2, "31.07.2022.", "05.08.2022." , 190)
db.insert("Alfred Maisone", "Germany", 2,"maisone@gmail.com" , 2, "18.09.2022.", "21.09.2022." , 96)
'''

#SQL Lite database #35 min