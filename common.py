import sqlite3
import random
import string

DB_CREATE_TABLE = '''CREATE TABLE Links
                (id INTEGER PRIMARY KEY,
                src TEXT,
                dest TEXT)'''

class Database:
    def __init__(self, short_length):
        self.short_length = short_length
        self.handle = sqlite3.connect("urlshort.db")
        if not self.check_table():
            print("Table doesn't exist, creating one...")
            self.handle.execute(DB_CREATE_TABLE)
        else:
            print("Table already exists in database...")
        self.handle.commit()

    def check_table(self):
        c = self.handle.cursor()
        c.execute('''SELECT name FROM sqlite_master
             WHERE type='table' AND name='Links' ''')
        return c.fetchone()

    def close(self):
        self.handle.close()

    def lookup(self, link_id: str):
        pass

    def add(self, link: str):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for i in range(self.short_length))
        self.handle.execute("INSERT INTO Links (src, dest) VALUES (?, ?)", (link, random_string))
        self.handle.commit()
        print(f"Added link {link} with database address of {random_string}")