#!/usr/bin/python3
"""
Unittest for models/review.py
"""
import models
import unittest
import time
from datetime import datetime
from models.review import Review

class TestReviewConstructor(unittest.TestCase):
    """
    Unittests for testing the constructor
    """
    def test_type_object(self):
        self.assertEqual(Review, type(Review()))

    def test_place_id_default(self):
        obj = Review()
        self.assertEqual(obj.place_id, "")

    def test_user_id_default(self):
        obj = Review()
        self.assertEqual(obj.user_id, "")

    def test_text_default(self):
        obj = Review()
        self.assertEqual(obj.text, "")

    def test_initiation_with_args(self):
        obj = Review(id="1234", created_at="2023-07-06T13:15:32.4534")
        self.assertIn("1234", obj.__str__())

    def test_type_id(self):
        self.assertEqual(type(Review().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(Review().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(Review().updated_at), datetime)

    def test_unicity_id(self):
        obj1 = Review()
        obj2 = Review()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_two_models_different_created_at(self):
        obj1 = Review()
        time.sleep(1)
        obj2 = Review()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_invalid_created_at(self):
        with self.assertRaises(ValueError):
            Review(created_at="invalid_datetime_format")

    def test_invalid_updated_at(self):
        with self.assertRaises(ValueError):
            Review(updated_at="invalid_datetime_format")

    def test_place_id_default(self):
        obj = Review()
        self.assertEqual(obj.place_id, "")

    def test_user_id_default(self):
        obj = Review()
        self.assertEqual(obj.user_id, "")

    def test_text_default(self):
        obj = Review()
        self.assertEqual(obj.text, "")

class TestReviewStr(unittest.TestCase):
    """
    Unittests for testing __str__
    """
    def test_str_with_arguments(self):
        obj = Review()
        with self.assertRaises(TypeError):
            obj.__str__("arg1", "arg2")

class TestReviewSave(unittest.TestCase):
    """
    Unittests for testing save method
    """
    def test_save_with_arguments(self):
        obj = Review()
        with self.assertRaises(TypeError):
            obj.save("arg1", "arg2")

    def test_save_method_updates_updated_at(self):
        obj = Review()
        initial_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_save_not_update(self):
        obj = Review()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertEqual(initial_updated_at, obj.updated_at)

class TestReviewToDict(unittest.TestCase):
    """
    Unittests for testing to_dict
    """
    def test_to_dict_with_arguments(self):
        obj = Review()
        with self.assertRaises(TypeError):
            obj.to_dict("arg1", "arg2")

    def test_to_dict_type(self):
        obj = Review()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_to_dict_keys(self):
        obj = Review()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())
        self.assertIn("place_id", obj.to_dict())
        self.assertIn("user_id", obj.to_dict())
        self.assertIn("text", obj.to_dict())

    def test_initiation_with_args(self):
        obj = Review(text="example_text", id="1234")
        self.assertIn("id", obj.to_dict())
        self.assertIn("text", obj.to_dict())

    def test_to_dict_values(self):
        obj = Review(ex_text="example_text", id="1234")
        review_dict = obj.to_dict()
        self.assertEqual(review_dict["ex_text"], "example_text")
        self.assertEqual(review_dict["id"], "1234")

    def test_to_dict_output(self):
        obj = Review()
        obj.id = "1234"
        created_time = obj.created_at
        update_time = obj.updated_at
        obj.place_id = "5678"
        obj.user_id = "abcd"
        obj.text = "Sample Review Text"

        my_dictionary = {
            'id': '1234',
            '__class__': 'Review',
            'created_at': created_time.isoformat(),
            'updated_at': update_time.isoformat(),
            'place_id': '5678',
            'user_id': 'abcd',
            'text': 'Sample Review Text'
        }

        self.assertDictEqual(obj.to_dict(), my_dictionary)

if __name__ == "__main__":
    unittest.main()
