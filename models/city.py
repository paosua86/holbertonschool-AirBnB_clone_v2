#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

env = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base if (env == "db") else object):
    """ The city class, contains state ID and name """
    if env == "db":
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")
    else:
        name = ""
        state_id = ""
