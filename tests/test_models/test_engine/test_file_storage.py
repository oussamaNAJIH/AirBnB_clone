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

class Test_new_method(unittest.TestCase):
    pass


class Test_save_method(unittest.TestCase):
    pass


class Test_reload_method(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()