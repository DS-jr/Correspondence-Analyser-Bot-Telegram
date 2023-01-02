import os

DATABASE_STRING = os.getenv("DATABASE_STRING", "sqlite:///my_db.sqlite")




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

