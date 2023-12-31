#!/usr/bin/python3
"""
Unittest for the City class
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Tests instances and methods from city class"""

    city = City()

    def test_class_exists(self):
        """tests if the City class exists"""
        self.assertEqual(str(type(self.city)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """test if the class city is a subclass of BaseModel"""
        self.assertTrue(self.city, City)

    def testHasAttributes(self):
        """confirm if attributes exist in the class"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is correct"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
