#!/usr/bin/python3
"""state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="delete, delete-orphan")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns the list of City instances with state_id equals
            to the current State.id"""
            list_city = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
