#!/usr/bin/python3
"""
    Unittest for models/base_model.py
"""
import unittest
import uuid
from datetime import datetime
import time
from models.base_model import BaseModel

class TestBaseModelConstructor(unittest.TestCase):
    """
    Unittests for testing the constructor
    """
    def test_type_object(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_initiation_with_args(self):
        obj = BaseModel(id="1234", created_at="2023-07-06T13:15:32.4534")
        self.assertIn("1234", obj.__str__())
    
    def test_type_id(self):
        self.assertEqual(type(BaseModel().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_unicity_id(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_two_models_different_created_at(self):
        obj1 = BaseModel()
        time.sleep(1)
        obj2 = BaseModel()
        self.assertLess(obj1.created_at, obj2.created_at)

class TestBaseModelstr(unittest.TestCase):
    """
    Unittests for testing __str__
    """
    def test_str_method(self):
        obj = BaseModel()
        id = obj.id
        str_rep = obj.__str__()
        expected_str = f"[{type(obj).__name__}] ({id}) {obj.__dict__}"
        self.assertEqual(expected_str, str_rep)
    

class TestBaseModelsave(unittest.TestCase):
    """
    Unittests for testing save method
    """
    pass

class TestBaseModelto_dict(unittest.TestCase):
    """
    Unittests for testing to_dict
    """

    def test_to_dict_type(self):
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()), dict)
    
    def test_to_dict_keys(self):
        obj = BaseModel()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_initiation_with_args(self):
        obj = BaseModel(name = "mike", id="1234", created_at="2023-07-06T13:15:32.45")
        self.assertIn("id", obj.to_dict())
        self.assertIn("name", obj.to_dict())

    def test_to_dict_values(self):
        obj = BaseModel(name = "mike", id="1234")
        dict = obj.to_dict()
        self.assertEqual(dict["name"], "mike")
        self.assertEqual(dict["id"], "1234")

    def test_to_dict_output(self):
        obj = BaseModel()
        created_time = obj.created_at
        update_time = obj.updated_at
        obj.id = "1234"
        my_dictionnary = {
            'id': '1234',
            '__class__': 'BaseModel',
            'created_at': created_time.isoformat(),
            'updated_at': update_time.isoformat()
        }
        self.assertDictEqual(obj.to_dict(), my_dictionnary)



if __name__ == "__main__":
    unittest.main()
