#!/usr/bin/python3
"""
Parent class that other classes will inherit
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """ Defines all th common methods/attributes
    """

    def __init__(self, *args, **kwargs):
        """Initializes all attributes of the class
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(kwargs[key], fmt)
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """ Returns a dictionary (dctn) of class name, id and attribute
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dctn = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dctn)

    def save(self):
        """ Updates the last update time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        new_dictionary = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dictionary[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dictionary[key] = values
        new_dictionary['__class__'] = self.__class__.__name__

        return new_dictionary
