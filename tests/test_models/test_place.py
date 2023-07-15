#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Tests instances and methods from place class"""

    pla = Place()

    def test_class_exists(self):
        """tests if Place class is present"""
        self.assertEqual(str(type(self.pla)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if class Place is a subclass of BaseModel"""
        self.assertIsInstance(self.pla, Place)

    def testHasAttributes(self):
        """verify if attr exist"""
        self.assertTrue(hasattr(self.pla, 'city_id'))
        self.assertTrue(hasattr(self.pla, 'user_id'))
        self.assertTrue(hasattr(self.pla, 'name'))
        self.assertTrue(hasattr(self.pla, 'description'))
        self.assertTrue(hasattr(self.pla, 'number_rooms'))
        self.assertTrue(hasattr(self.pla, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pla, 'max_guest'))
        self.assertTrue(hasattr(self.pla, 'price_by_night'))
        self.assertTrue(hasattr(self.pla, 'latitude'))
        self.assertTrue(hasattr(self.pla, 'longitude'))
        self.assertTrue(hasattr(self.pla, 'amenity_ids'))
        self.assertTrue(hasattr(self.pla, 'id'))
        self.assertTrue(hasattr(self.pla, 'created_at'))
        self.assertTrue(hasattr(self.pla, 'updated_at'))

    def test_types(self):
        """tests if the type of the attr is the correct one"""
        self.assertIsInstance(self.pla.city_id, str)
        self.assertIsInstance(self.pla.user_id, str)
        self.assertIsInstance(self.pla.name, str)
        self.assertIsInstance(self.pla.description, str)
        self.assertIsInstance(self.pla.number_rooms, int)
        self.assertIsInstance(self.pla.number_bathrooms, int)
        self.assertIsInstance(self.pla.max_guest, int)
        self.assertIsInstance(self.pla.price_by_night, int)
        self.assertIsInstance(self.pla.latitude, float)
        self.assertIsInstance(self.pla.longitude, float)
        self.assertIsInstance(self.pla.amenity_ids, list)
        self.assertIsInstance(self.pla.id, str)
        self.assertIsInstance(self.pla.created_at, datetime.datetime)
        self.assertIsInstance(self.pla.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
