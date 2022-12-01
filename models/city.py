#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String

HBHB_TYPE_STORAGE = os.environ['HBHB_TYPE_STORAGE']


class City(BaseModel, Base if HBHB_TYPE_STORAGE == 'db' else object):
    """ The city class, contains state ID and name """
    if HBHB_TYPE_STORAGE == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
