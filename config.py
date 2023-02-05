import os

DATABASE_STRING = os.getenv(
    "DATABASE_STRING", "postgresql://DS@localhost:5432/v1_tg_data_export"
)
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]

# HOST = "localhost"
# PORT = 5432
# DATABASE = "v1_tg_data_export"
# USER = "DS"

# DATABASE_STRING = os.getenv("DATABASE_STRING", "sqlite:///my_db.sqlite")   # This solution worked fine


# "DATABASE_STRING" is an ‘environment variable’ here, right?
# Why is “os.getenv” used?
# Where is "DATABASE_STRING" defined & taken from?
# What does "DATABASE_STRING" contain?
# ***NOT connected to .env, so NO changes / additions in .env, correct?

# (from documentation)
# def getenv(key: str,
#            default: _T) -> str | _T
# Get an environment variable, return None if it doesn't exist. The optional second argument can specify an alternate default. key, default and the result are str.
# `getenv(key, default)`
