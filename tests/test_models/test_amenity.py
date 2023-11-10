#!/usr/bin/python3
"""
Unittest for models/amenity.py
"""
import models
import unittest
import time
from datetime import datetime
from models.amenity import Amenity

class TestAmenityConstructor(unittest.TestCase):
    """
    Unittests for testing the constructor
    """
    def test_type_object(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_default(self):
        obj = Amenity()
        self.assertEqual(obj.name, "")

    def test_initiation_with_args(self):
        obj = Amenity(id="1234", created_at="2023-07-06T13:15:32.4534")
        self.assertIn("1234", obj.__str__())

    def test_type_id(self):
        self.assertEqual(type(Amenity().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(Amenity().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(Amenity().updated_at), datetime)

    def test_unicity_id(self):
        obj1 = Amenity()
        obj2 = Amenity()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_two_models_different_created_at(self):
        obj1 = Amenity()
        time.sleep(1)
        obj2 = Amenity()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_invalid_created_at(self):
        with self.assertRaises(ValueError):
            Amenity(created_at="invalid_datetime_format")

    def test_invalid_updated_at(self):
        with self.assertRaises(ValueError):
            Amenity(updated_at="invalid_datetime_format")

class TestAmenityStr(unittest.TestCase):
    """
    Unittests for testing __str__
    """
    def test_str_with_arguments(self):
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.__str__("arg1", "arg2")

class TestAmenitySave(unittest.TestCase):
    """
    Unittests for testing save method
    """
    def test_save_with_arguments(self):
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.save("arg1", "arg2")

    def test_save_method_updates_updated_at(self):
        obj = Amenity()
        initial_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_save_not_update(self):
        obj = Amenity()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertEqual(initial_updated_at, obj.updated_at)

class TestAmenityToDict(unittest.TestCase):
    """
    Unittests for testing to_dict
    """
    def test_to_dict_with_arguments(self):
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.to_dict("arg1", "arg2")

    def test_to_dict_type(self):
        obj = Amenity()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_to_dict_keys(self):
        obj = Amenity()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_initiation_with_args(self):
        obj = Amenity(name="example_name", id="1234")
        self.assertIn("id", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_to_dict_values(self):
        obj = Amenity(ex_name="example_name", id="1234")
        amenity_dict = obj.to_dict()
        self.assertEqual(amenity_dict["ex_name"], "example_name")
        self.assertEqual(amenity_dict["id"], "1234")

    def test_to_dict_output(self):
        obj = Amenity()
        obj.id = "1234"
        created_time = obj.created_at
        update_time = obj.updated_at
        obj.name = "Sample Amenity Name"

        my_dictionary = {
            'id': '1234',
            '__class__': 'Amenity',
            'created_at': created_time.isoformat(),
            'updated_at': update_time.isoformat(),
            'name': 'Sample Amenity Name'
        }

        self.assertDictEqual(obj.to_dict(), my_dictionary)

if __name__ == "__main__":
    unittest.main()
