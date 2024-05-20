#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        """Test save method"""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))

if __name__ == '__main__':
    unittest.main()

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(
        key,
        type(my_model_json[key]),
        my_model_json[key]
    ))
