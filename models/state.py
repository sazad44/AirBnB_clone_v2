#!/usr/bin/python3
"""This is the state class"""
import json
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref=backref("State", cascade="delete"))

    if (getenv('HBNB_TYPE_STORAGE') != "db"):
        @property
        def cities(self):
            """returns list of city
            instances with
            matching state_id
            """
            cityObjs = models.storage.all('City').values()
            return [c for c in cityObjs if c.state_id == self.id]
