#!/usr/bin/env python3
"""
A module that serializes instances to a JSON file
and deserializes JSON file to instances
"""


class FileStorage:
    """ A class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ """
        # print("newww")
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ """
        with open(self.__file.json, "w") as file:
            my_dict = {}
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, file)

    def reload(self):
        """ """
        if self.__file_path:
            with open(self.__file_path) as json_file:
                my_obj = json.load(json_file)
                print(my_obj)
        else:
            pass