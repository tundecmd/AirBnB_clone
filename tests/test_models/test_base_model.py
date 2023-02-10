#!/usr/bin/env python3
""" A module that contains the test suite for the BaseModel class """

from models.base_model import BaseModel
import uuid
import json
import unittest
import time
import re
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ The test suite for models.base_model.BaseModel """

    def test_3_init(self):
        """Tests instantiation of BaseModel class."""
        b = BaseModel()
        # type of b = BaseModel
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        # b is instance of BaseModel
        self.assertIsInstance(b, BaseModel)
        # b is a sub of BaseModel
        self.assertTrue(issubclass(type(b), BaseModel))
        
    def test_3_init_with_no_args(self):
        """ Tests __init__ with no argument """
        # with self.assertRaises(TypeError) as e:
        #     BaseModel.__init__()
        # msg = "__init__() is missing 1 required positional argument: 'self'"
        # self.assertEqual(str(e.exception), msg)
        
    def test_3_init_many_args(self):
        """ Test __init__() with many arguments """
        args = [i for i in range(1000)]
        b = BaseModel(0, 1, 2, 3, 4, 5)
        b = BaseModel(*args)

    def test_3_attributes(self):
        """ Checks that instance of BaseModel has attribute(s) initialization """
        b = BaseModel()
        # self.assertTrue(hasattr(b))

    def test_3_if_BaseModel_has_id_attribute(self):
        """ Checks that instance has an id attribute on initialization """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_3_if_BaseModel_has_id_attribute_is_unique(self):
        """ Checks if id is generated randomly and uniquely """
        b1 = BaseModel()
        b2 = BaseModel()
        # check for 2 instances
        self.assertNotEqual(b1.id, b2.id)
        b = [BaseModel().id for i in range(1000)]
        # check for a thousand (1000) instances
        self.assertEqual(len(set(b)), len(b))

    def test_3_str_representation(self):
        """ Checks if the string representation is appropriate """
        b = BaseModel()
        self.assertEqual(str(b), "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_3_save(self):
        """ """
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(
                base_model.created_at.microsecond,
                base_model.updated_at.microsecond
                )
                
    def test_3_to_dict(self):
        """ Checks if BaseModel.to_dict() returns a dict object """
        base_model = BaseModel()
        my_model = base_model.to_dict()
        self.assertEqual(my_model["id"], base_model.id)
        self.assertEqual(
                my_model["created_at"],
                base_model.created_at.isoformat()
                )
        self.assertEqual(
                my_model["updated_at"],
                base_model.updated_at.isoformat()
                )

    def test_3_to_dict_with_no_args(self):
        pass
    
    def test_3_to_dict_with_excess_args(self):
        pass

    def test_3_to_dict_check_if_it_returns_dict(self):
        pass

    def test_if_to_dict_returns_class_dunder_method(self):
        pass

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        pass

    
if __name__ == "__main__":
    unittest.main()