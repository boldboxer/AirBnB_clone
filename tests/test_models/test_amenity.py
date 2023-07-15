#!/usr/bin/python3
"""
Unittest for the Amenity class
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    aty = Amenity()

    def test_class_exists(self):
        """tests if the amenity class exists"""
        response = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.aty)), response)

    def test_user_inheritance(self):
        """test if the Amenity Class is a subclass of BaseModel"""
        self.assertIsInstance(self.aty, Amenity)

    def testHasAttributes(self):
        """verify if attributes exist in the class"""
        self.assertTrue(hasattr(self.aty, 'name'))
        self.assertTrue(hasattr(self.aty, 'id'))
        self.assertTrue(hasattr(self.aty, 'created_at'))
        self.assertTrue(hasattr(self.aty, 'updated_at'))

    def test_types(self):
        """tests if the type of the attr is correct"""
        self.assertIsInstance(self.aty.name, str)
        self.assertIsInstance(self.aty.id, str)
        self.assertIsInstance(self.aty.created_at, datetime.datetime)
        self.assertIsInstance(self.aty.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
