from models import *
from db import engine, Base

try:
    Base.metadata.create_all(engine)
except:
    print("Error creating tables, make sure the config is correct and the database exists")
