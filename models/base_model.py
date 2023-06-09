#!/usr/bin/python3

"""Module 3. BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """class BaseModel that defines all common
    attributes/methods for other classes:"""

    def __init__(self, *args, **kwargs):
        """Public attribuites initializing base Models """
        if kwargs:
            if key == "created_at" or key == "updated_at":
                value = datetime.strptime(value,
                                                "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """return string with class name,
        id, dictionary class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        dictionary = self.__dict__.copy()  # get a copy of dict
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = getattr(
                                self, "created_at", None).isoformat()
        dictionary["updated_at"] = getattr(
                                self, "updated_at", None).isoformat()
        return dictionary
