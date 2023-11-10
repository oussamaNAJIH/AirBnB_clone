#!/usr/bin/python3
"""
    Unittest for models/engine/file_storage.py
"""
import models
import unittest
import uuid
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageConstructor(unittest.TestCase):
    def test_object_type(self):
        obj = FileStorage()
        self.assertEqual(FileStorage, type(obj))

    def test_file_path_attribute(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_attribute(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class Test_all_method(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all_method_empty_storage(self):
        result = self.storage.all()
        self.assertEqual(dict, type(result))

    def test_all_with_arguments(self):
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.all("arg1", "arg2")


class Test_new_method(unittest.TestCase):
    def test_new_method(self):
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        objects = storage.all()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, objects)
        self.assertEqual(objects[key], base_model)

    def test_new_with_invalid_object(self):
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            storage.new("invalid_object")


class Test_save_method(unittest.TestCase):
    def test_save_method(self):
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        storage.save()

    def test_save_with_arguments(self):
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.save("arg1", "arg2")


class Test_reload_method(unittest.TestCase):
    def test_reload_method(self):
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        storage.save()

    def test_reload_with_arguments(self):
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.reload("arg1", "arg2")


if __name__ == "__main__":
    unittest.main()
