import sqlite3
import os

class DatabaseManager:

    _instance = None
    #Singleton pattern implementation, controls object creation, to ensure a single
    #database connection throughout the application
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_db()
        return cls._instance
    
    def __init__(self):
        self.connection = sqlite3.connect("data/school_data.db")
    
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
        self.connection.commit()
        self.connection.close()
    
    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchall()
    
    def execute_write(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        return cursor.lastrowid, cursor.rowcount
    