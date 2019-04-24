#!/usr/bin/python3
"""Definition of DataBase Storage class"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorage class for database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """__init__ method for DBStorage class"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All method for DBStorage class"""
        obj_list = []
        classList = ["State", "City"]
        if cls:
            classList = [cls]
        for cls in classList:
            if type(cls) == str:
                objs = self.__session.query(eval(cls)).all()
            else:
                objs = self.__session.query(cls).all()
            obj_list.extend(objs)
        retdict = {}
        for obj in obj_list:
            retdict["{}.{}".format(cls, obj.id)] = obj
        return retdict

    def new(self, obj):
        """Add obj to session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create tables in database and create database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes session"""
        self.__session.close()
