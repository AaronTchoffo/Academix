import sqlite3
import os
import bcrypt

class DatabaseManager:

    _instance = None
    #Singleton pattern implementation, controls object creation, to ensure a single
    #database connection throughout the application
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if hasattr(self, "connection"):
            return
        self.connection = sqlite3.connect("data/school_data.db")
        self._init_db()
    
    def _init_db(self):
        #verify and create data/
        if not os.path.exists("data"):
            os.makedirs("data")
        #reads schema.sql and executes the CREATE TABLE and CREATE INDEX
        cursor = self.connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON") #Enable foreign key constraints for SQlite
        with open("database/schema.sql", "r", encoding="utf-8") as file:
            schema = file.read()
        cursor.executescript(schema)

        #verify if admin exist:
        cursor.execute("SELECT id FROM users WHERE username = ?", ("admin",))
        admin = cursor.fetchone()
        if not admin:
            #create admin user with default password "admin123"
            hashed_password = bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt())
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                            ("admin", hashed_password.decode('utf-8')))

        self.connection.commit()
    
    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchall()
    
    def execute_write(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        return cursor.lastrowid, cursor.rowcount
    