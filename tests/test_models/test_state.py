#!/usr/bin/python3
"""
Unittest for models/state.py
"""
import models
import unittest
import time
from datetime import datetime
from models.state import State


class TestStateConstructor(unittest.TestCase):
    def test_type_object(self):
        self.assertEqual(State, type(State()))

    def test_initiation_with_args(self):
        obj = State(id="1234", created_at="2023-07-06T13:15:32.4534")
        self.assertIn("1234", obj.__str__())

    def test_type_id(self):
        self.assertEqual(type(State().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(State().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(State().updated_at), datetime)

    def test_name_attribute(self):
        state = State()
        self.assertEqual(state.name, "")


class TestStateStr(unittest.TestCase):
    def test_str_with_arguments(self):
        obj = State()
        with self.assertRaises(TypeError):
            obj.__str__("arg1", "arg2")

    def test_str_method(self):
        obj = State()
        id = obj.id
        str_rep = obj.__str__()
        expected_str = f"[{type(obj).__name__}] ({id}) {obj.__dict__}"
        self.assertEqual(expected_str, str_rep)


class TestStateSave(unittest.TestCase):
    def test_save_with_arguments(self):
        obj = State()
        with self.assertRaises(TypeError):
            obj.save("arg1", "arg2")

    def test_save_method_updates_updated_at(self):
        obj = State()
        initial_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_save_not_update(self):
        obj = State()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertEqual(initial_updated_at, obj.updated_at)


class TestStateToDict(unittest.TestCase):
    def test_to_dict_with_arguments(self):
        obj = State()
        with self.assertRaises(TypeError):
            obj.to_dict("arg1", "arg2")

    def test_to_dict_type(self):
        obj = State()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_to_dict_keys(self):
        obj = State()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_initiation_with_args(self):
        obj = State(name="California", id="1234")
        self.assertIn("id", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_to_dict_values(self):
        obj = State(nick_name="California", id="1234")
        state_dict = obj.to_dict()
        self.assertEqual(state_dict["nick_name"], "California")
        self.assertEqual(state_dict["id"], "1234")

    def test_to_dict_output(self):
        obj = State()
        created_time = obj.created_at
        update_time = obj.updated_at
        obj.id = "1234"
        obj.name = "California"
        state_dictionary = {
            'id': '1234',
            '__class__': 'State',
            'created_at': created_time.isoformat(),
            'updated_at': update_time.isoformat(),
            'name': 'California'
        }
        self.assertDictEqual(obj.to_dict(), state_dictionary)


if __name__ == "__main__":
    unittest.main()
