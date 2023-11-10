#!/usr/bin/python3
"""
Unittest for models/place.py
"""
import models
import unittest
import time
from datetime import datetime
from models.place import Place


class TestPlaceConstructor(unittest.TestCase):
    """
    Unittests for testing the constructor
    """
    def test_type_object(self):
        self.assertEqual(Place, type(Place()))

    def test_city_id_default(self):
        obj = Place()
        self.assertEqual(obj.city_id, "")

    def test_user_id_default(self):
        obj = Place()
        self.assertEqual(obj.user_id, "")

    def test_name_default(self):
        obj = Place()
        self.assertEqual(obj.name, "")

    def test_description_default(self):
        obj = Place()
        self.assertEqual(obj.description, "")

    def test_number_rooms_default(self):
        obj = Place()
        self.assertEqual(obj.number_rooms, 0)

    def test_number_bathrooms_default(self):
        obj = Place()
        self.assertEqual(obj.number_bathrooms, 0)

    def test_max_guest_default(self):
        obj = Place()
        self.assertEqual(obj.max_guest, 0)

    def test_price_by_night_default(self):
        obj = Place()
        self.assertEqual(obj.price_by_night, 0)

    def test_latitude_default(self):
        obj = Place()
        self.assertEqual(obj.latitude, 0.0)

    def test_longitude_default(self):
        obj = Place()
        self.assertEqual(obj.longitude, 0.0)

    def test_amenity_ids_default(self):
        obj = Place()
        self.assertEqual(obj.amenity_ids, [])

    def test_initiation_with_args(self):
        obj = Place(id="1234", created_at="2023-07-06T13:15:32.4534")
        self.assertIn("1234", obj.__str__())

    def test_type_id(self):
        self.assertEqual(type(Place().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(Place().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(Place().updated_at), datetime)

    def test_unicity_id(self):
        obj1 = Place()
        obj2 = Place()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_two_models_different_created_at(self):
        obj1 = Place()
        time.sleep(1)
        obj2 = Place()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_invalid_created_at(self):
        with self.assertRaises(ValueError):
            Place(created_at="invalid_datetime_format")

    def test_invalid_updated_at(self):
        with self.assertRaises(ValueError):
            Place(updated_at="invalid_datetime_format")


class TestPlaceStr(unittest.TestCase):
    """
    Unittests for testing __str__
    """
    def test_str_with_arguments(self):
        obj = Place()
        with self.assertRaises(TypeError):
            obj.__str__("arg1", "arg2")


class TestPlaceSave(unittest.TestCase):
    """
    Unittests for testing save method
    """
    def test_save_with_arguments(self):
        obj = Place()
        with self.assertRaises(TypeError):
            obj.save("arg1", "arg2")

    def test_save_method_updates_updated_at(self):
        obj = Place()
        initial_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_save_not_update(self):
        obj = Place()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertEqual(initial_updated_at, obj.updated_at)


class TestPlaceToDict(unittest.TestCase):
    """
    Unittests for testing to_dict
    """
    def test_to_dict_with_arguments(self):
        obj = Place()
        with self.assertRaises(TypeError):
            obj.to_dict("arg1", "arg2")

    def test_to_dict_type(self):
        obj = Place()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_to_dict_keys(self):
        obj = Place()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_initiation_with_args(self):
        obj = Place(name="example_name", id="1234")
        self.assertIn("id", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_to_dict_values(self):
        obj = Place(ex_name="example_name", id="1234")
        place_dict = obj.to_dict()
        self.assertEqual(place_dict["ex_name"], "example_name")
        self.assertEqual(place_dict["id"], "1234")

    def test_to_dict_output(self):
        obj = Place()
        obj.id = "1234"
        created_time = obj.created_at
        update_time = obj.updated_at
        obj.city_id = "5678"
        obj.user_id = "abcd"
        obj.name = "Sample Place"
        obj.description = "A sample description"
        obj.number_rooms = 2
        obj.number_bathrooms = 1
        obj.max_guest = 4
        obj.price_by_night = 100
        obj.latitude = 40.0
        obj.longitude = -74.0
        obj.amenity_ids = ["a1", "a2"]

        my_dictionary = {
            'id': '1234',
            '__class__': 'Place',
            'created_at': created_time.isoformat(),
            'updated_at': update_time.isoformat(),
            'city_id': '5678',
            'user_id': 'abcd',
            'name': 'Sample Place',
            'description': 'A sample description',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 40.0,
            'longitude': -74.0,
            'amenity_ids': ['a1', 'a2']
        }

        self.assertDictEqual(obj.to_dict(), my_dictionary)


if __name__ == "__main__":
    unittest.main()
