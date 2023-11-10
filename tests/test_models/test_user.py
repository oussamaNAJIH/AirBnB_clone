#!/usr/bin/python3
"""
Unittest for models/user.py
"""
import models
import unittest
import uuid
from datetime import datetime
import time
from models.user import User


class TestUserConstructor(unittest.TestCase):
    """
    Unittests for testing the constructor of the User class
    """
    def test_type_object(self):
        self.assertEqual(User, type(User()))

    def test_initiation_with_args(self):
        obj = User(id="1234", created_at="2023-07-06T13:15:32.4534")
        self.assertIn("1234", obj.__str__())

    def test_type_id(self):
        self.assertEqual(type(User().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(User().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(User().updated_at), datetime)

    def test_unicity_id(self):
        obj1 = User()
        obj2 = User()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_two_users_different_created_at(self):
        obj1 = User()
        time.sleep(1)
        obj2 = User()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_invalid_created_at(self):
        with self.assertRaises(ValueError):
            User(created_at="invalid_datetime_format")

    def test_invalid_updated_at(self):
        with self.assertRaises(ValueError):
            User(updated_at="invalid_datetime_format")

    def test_email_attribute(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_password_attribute(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_attribute(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_attribute(self):
        user = User()
        self.assertEqual(user.last_name, "")


class TestUserStr(unittest.TestCase):
    """
    Unittests for testing __str__ of the User class
    """
    def test_str_with_arguments(self):
        obj = User()
        with self.assertRaises(TypeError):
            obj.__str__("arg1", "arg2")

    def test_str_method(self):
        obj = User()
        id = obj.id
        str_rep = obj.__str__()
        expected_str = f"[{type(obj).__name__}] ({id}) {obj.__dict__}"
        self.assertEqual(expected_str, str_rep)


class TestUserSave(unittest.TestCase):
    """
    Unittests for testing save method of the User class
    """
    def test_save_with_arguments(self):
        obj = User()
        with self.assertRaises(TypeError):
            obj.save("arg1", "arg2")

    def test_save_method_updates_updated_at(self):
        obj = User()
        initial_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_save_not_update(self):
        obj = User()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertEqual(initial_updated_at, obj.updated_at)


class TestUserToDict(unittest.TestCase):
    """
    Unittests for testing to_dict of the User class
    """
    def test_to_dict_with_arguments(self):
        obj = User()
        with self.assertRaises(TypeError):
            obj.to_dict("arg1", "arg2")

    def test_to_dict_type(self):
        obj = User()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_to_dict_keys(self):
        obj = User()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_initiation_with_args(self):
        obj = User(name="mike", id="1234")
        self.assertIn("id", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_to_dict_values(self):
        obj = User(name="mike", id="1234")
        user_dict = obj.to_dict()
        self.assertEqual(user_dict["name"], "mike")
        self.assertEqual(user_dict["id"], "1234")

    def test_to_dict_output(self):
        obj = User()
        created_time = obj.created_at
        update_time = obj.updated_at
        obj.id = "1234"

        user_dictionary = {
            'id': '1234',
            '__class__': 'User',
            'created_at': created_time.isoformat(),
            'updated_at': update_time.isoformat(),
            'email': '',
            'password': '',
            'first_name': '',
            'last_name': ''
        }

        self.assertDictEqual(obj.to_dict(), user_dictionary)


if __name__ == "__main__":
    unittest.main()
