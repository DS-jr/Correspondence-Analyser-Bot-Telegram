import os

# DATABASE_STRING = os.getenv("DATABASE_STRING", "sqlite:///my_db.sqlite")
DATABASE_STRING = os.getenv("DATABASE_STRING", "postgresql://postgres:postgres@localhost/postgres")
