#!/usr/bin/python3
"""Module 3. BaseModel defines all common
attributes/methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """class BaseModel that defines all common
    attributes/methods for other classes:"""

    def __init__(self, *args, **kwargs):
        """Public attribuites initializing base Models """
        if kwargs:
            for key in kwargs:
                if "created_at" in kwargs:
                    self.created_at = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if "updated_at" in kwargs:
                    self.updated_at = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """return string with class name,
        id, dictionary class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        # get a copy of dict
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
