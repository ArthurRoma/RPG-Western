import os
from peewee import PostgresqlDatabase

from dotenv import load_dotenv

load_dotenv()
DATABASE_db = os.getenv("DATABASE_db")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PSW = os.getenv("DATABASE_PSW")
DATABASE_host = os.getenv("DATABASE_host")
DATABASE_PORT = 5432


db = PostgresqlDatabase(DATABASE_db, user=DATABASE_USER, password=DATABASE_PSW, host=DATABASE_host, port=DATABASE_PORT)


