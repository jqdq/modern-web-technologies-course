import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies (
    title TEXT,
    cat_death INTEGER,
    violence INTEGER,
    loud_noises INTEGER,
    jump_scares INTEGER
);

DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);
                     
INSERT INTO Movies (title, cat_death, violence, loud_noises, jump_scares)
VALUES ('Shrek 2', 0, 1, 1, 1)
""")

cursor.execute("SELECT * FROM Movies")
for i in cursor.fetchall():
    print(i)

db.commit()
db.close()