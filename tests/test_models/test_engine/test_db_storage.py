#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from models import storage
import unittest
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
import MySQLdb
import pep8
import json
from models.engine.db_storage import DBStorage
from models import storage
import os
import MySQLdb

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "only testing db")
class test_DBStorage(unittest.TestCase):

    def test_State(self):
        """ Check if loads name"""
        state = State(name="Carl")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Carl")

    def test_City(self):
        """ Check if loads name """
        city = City(name="Bogota")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Bogota")

    def test_Place(self):
        """ Checks if leads name and numer """
        place = Place(name="Hotel", number_rooms=4)
        if place.id in models.storage.all():
            self.assertTrue(place.number_rooms, 4)
            self.assertTrue(place.name, "Hotel")

    def test_User(self):
        """ Check if loads name """
        user = User(name="926")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "926")

    def test_Amenity(self):
        """ Check if loads name """
        amenity = Amenity(name="Wifi")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Wifi")

    def test_Review(self):
        """ Tests if leads text """
        review = Review(text="Very_good_place")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "Very_good_place")

    def teardown(self):
        self.session.close()
        self.session.rollback()

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.all().keys():
            del_list.append(key)
        for key in del_list:
            storage._DBStorage__session.delete(storage.all()[key])
            storage._DBStorage__session.commit()

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_store(self):
        """ Test if an object is store in the database """
        new = State(name="Florida")
        new.save()
        _id = new.to_dict()['id']
        self.assertIn(new.__class__.__name__ + '.' + _id,
                        storage.all(type(new)).keys())

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def setUp(self):
        """Initialize the setup connection"""
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            self.db = MySQLdb.connect(os.getenv("HBNB_MYSQL_HOST"),
                                      os.getenv("HBNB_MYSQL_USER"),
                                      os.getenv("HBNB_MYSQL_PWD"),
                                      os.getenv("HBNB_MYSQL_DB"))
            self.cursor = self.db.cursor()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def tearDown(self):
        """Close db"""
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            self.db.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def test_attributes_DBStorage(self):
        """Check if has the attributes"""
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def test_pep8_DBStorage(self):
        """Check PEP8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
