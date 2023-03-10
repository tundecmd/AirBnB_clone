#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """ A BaseModel class that defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initializes the class """
        # print("init function")
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)        

    def __str__(self):
        """ A string representation that is readablinfe to humans """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        
    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__

        dates_to_be_converted = ("created_at", "updated_at")
        for k, v in self.__dict__.items():
            if k in dates_to_be_converted:
                my_dict[k] = my_dict[k].isoformat()
        # Basically, this is what we did above
        # my_dict["created_at"] = my_dict["created_at"].isoformat() 
        # my_dict["updated_at"] = my_dict["updated_at"].isoformat()
       
        return my_dict
