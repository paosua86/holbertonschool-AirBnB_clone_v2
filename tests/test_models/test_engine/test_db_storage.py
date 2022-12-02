#!/usr/bin/python3
""" Module for testing DB storage"""
import os
import unittest
from models.engine.db_storage import DBStorage, Base
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker
from models import storage


class TestDBStorage(unittest.TestCase):
    def setUp(self) -> None:
        if type(storage) == DBStorage:
            self.storage = DBStorage()
            Base.metadata.create_all(self.storage._DBStorage__engine)
            Session = sessionmaker(bind=self.storage._DBStorage__engine)
            self.storage._DBStorage__session = Session()
            self.user = User(email='none@gmail.com', password='password')
            self.storage._DBStorage__session.add(self.user)
            self.state = State(name='California')
            self.storage._DBStorage__session.add(self.state)
            self.city = City(name='San Francisco', state_id=self.state.id)
            self.storage._DBStorage__session.add(self.city)
            self.place = Place(user_id=self.user.id,
                               city_id=self.city.id, name='Church')
            self.storage._DBStorage__session.add(self.place)
            self.review = Review(user_id=self.user.id,
                                 palce_id=self.place.id, text='Very good')
            self.storage._DBStorage__session.add(self.review)
            self.amenity = Amenity(name='TV')
            self.storage._DBStorage__session.add(self.amenity)
            self.storage._DBStorage__session.commit()

    def tearDown(self) -> None:
        if type(storage) == DBStorage:
            self.storage._DBStorage__session.delete(self.user)
            self.storage._DBStorage__session.delete(self.state)
            self.storage._DBStorage__session.delete(self.city)
            self.storage._DBStorage__session.delete(self.place)
            self.storage._DBStorage__session.delete(self.review)
            self.storage._DBStorage__session.delete(self.amenity)
            self.storage._DBStorage__session.commit()

    @unittest.skipIf(type(storage) == FileStorage, "File Storage ignore")
    def test_instance_creation(self):
        self.assertEqual(type(self.storage), DBStorage)

    @unittest.skipIf(type(storage) == FileStorage, "File Storage ignore")
    def test_all(self):
        states = self.storage.all(State)
        self.assertEqual(self.state, states['State'+'.'+self.state.id])
