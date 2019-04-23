#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
