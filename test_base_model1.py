#!/usr/bin/env python3
from models.base_model import BaseModel
import uuid

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(type(my_model))
print("----")
print(my_model)
print("----")
print(my_model.my_number)
print(uuid.uuid4())
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))