#!/usr/bin/python3
"""
Unittest for models/city.py
"""
import models
import unittest
import time
from datetime import datetime
from models.city import City

class TestCityConstructor(unittest.TestCase):
    """
    Unittests for testing the constructor
    """
    def test_type_object(self):
        self.assertEqual(City, type(City()))

    def test_state_id_default(self):
        obj = City()
        self.assertEqual(obj.state_id, "")

    def test_name_default(self):
        obj = City()
        self.assertEqual(obj.name, "")

    def test_initiation_with_args(self):
        obj = City(id="1234", created_at="2023-07-06T13:15:32.4534")
        self.assertIn("1234", obj.__str__())

    def test_type_id(self):
        self.assertEqual(type(City().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(City().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(City().updated_at), datetime)

    def test_unicity_id(self):
        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_two_models_different_created_at(self):
        obj1 = City()
        time.sleep(1)
        obj2 = City()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_invalid_created_at(self):
        with self.assertRaises(ValueError):
            City(created_at="invalid_datetime_format")

    def test_invalid_updated_at(self):
        with self.assertRaises(ValueError):
            City(updated_at="invalid_datetime_format")

class TestCityStr(unittest.TestCase):
    """
    Unittests for testing __str__
    """
    def test_str_with_arguments(self):
        obj = City()
        with self.assertRaises(TypeError):
            obj.__str__("arg1", "arg2")

class TestCitySave(unittest.TestCase):
    """
    Unittests for testing save method
    """
    def test_save_with_arguments(self):
        obj = City()
        with self.assertRaises(TypeError):
            obj.save("arg1", "arg2")

    def test_save_method_updates_updated_at(self):
        obj = City()
        initial_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_save_not_update(self):
        obj = City()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertEqual(initial_updated_at, obj.updated_at)

class TestCityToDict(unittest.TestCase):
    """
    Unittests for testing to_dict
    """
    def test_to_dict_with_arguments(self):
        obj = City()
        with self.assertRaises(TypeError):
            obj.to_dict("arg1", "arg2")

    def test_to_dict_type(self):
        obj = City()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_to_dict_keys(self):
        obj = City()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())
        self.assertIn("state_id", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_initiation_with_args(self):
        obj = City(name="example_name", id="1234")
        self.assertIn("id", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_to_dict_values(self):
        obj = City(ex_name="example_name", id="1234")
        city_dict = obj.to_dict()
        self.assertEqual(city_dict["ex_name"], "example_name")
        self.assertEqual(city_dict["id"], "1234")

    def test_to_dict_output(self):
        obj = City()
        obj.id = "1234"
        created_time = obj.created_at
        update_time = obj.updated_at
        obj.state_id = "5678"
        obj.name = "Sample City Name"

        my_dictionary = {
            'id': '1234',
            '__class__': 'City',
            'created_at': created_time.isoformat(),
            'updated_at': update_time.isoformat(),
            'state_id': '5678',
            'name': 'Sample City Name'
        }

        self.assertDictEqual(obj.to_dict(), my_dictionary)

if __name__ == "__main__":
    unittest.main()
