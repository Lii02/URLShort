import sqlite3

class Database:
    def __init__(self):
        self.handle = sqlite3.connect("urlshort.db")