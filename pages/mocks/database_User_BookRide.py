import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS User
             (id INTEGER NOT NULL PRIMARY KEY, 
             email TEXT NOT NULL, 
             first_name TEXT NOT NULL, 
             last_name TEXT NOT NULL, 
             password TEXT NOT NULL, 
             discount_points INTEGER(10))''')

new_users = [
    ('jnowak@example.com', 'Jan', 'Nowak', 'password1', 5),
    ('akowalska@example.com', 'Anna', 'Kowalska', 'password2', 0),
    ('molszewski@example.com', 'Marek', 'Olszewski', 'password3', 15),
    ('kadamczyk@example.com', 'Katarzyna', 'Adamczyk', 'password4', 20),
    ('ppawlowski@example.com', 'Piotr', 'Pawlowski', 'password5', 0),
    ('mmichalski@example.com', 'Michal', 'Michalski', 'password6', 10),
    ('bwozniak@example.com', 'Barbara', 'Wozniak', 'password7', 5),
    ('pkrakowski@example.com', 'Pawel', 'Krakowski', 'password8', 5),
    ('tadamska@example.com', 'Teresa', 'Adamska', 'password9', 0),
    ('tmarkowski@example.com', 'Tomasz', 'Markowski', 'password10', 10)
]
c.executemany("INSERT INTO User (email, first_name, last_name, password, discount_points) VALUES (?, ?, ?, ?, ?)", new_users)

c.execute('''CREATE TABLE IF NOT EXISTS BookRide
             (user_id INTEGER  FOREIGN KEY REFERENCES User(id), 
             type TEXT NOT NULL, 
             departure_address TEXT NOT NULL, 
             destination_address TEXT NOT NULL,
              travel_distance INTEGER(10) NOT NULL, 
              travel_time INTEGER(10) NOT NULL, 
              departure_date DATE NOT NULL, 
              departure_time INTEGER(10) NOT NULL, 
              price INTEGER(10) NOT NULL, 
              payment_date DATE NOT NULL, 
              rate INTEGER(5), 
              is_favourite INTEGER(1), 
              is_delayed INTEGER(1),
               car TEXT NOT NULL, 
               is_route_of_the_day INTEGER(1))''')

conn.commit()

# cursor = conn.cursor()
#
# cursor.execute("SELECT * FROM User")
#
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
#
# cursor.close()
conn.close()
