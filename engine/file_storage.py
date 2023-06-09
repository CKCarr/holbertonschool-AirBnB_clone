#!/usr/bin/pyhton3
""" Module for FileStorage class """

import json
import os
import models


class FileStorage:
    """ class FileStorage serializes instances to a JSON file and deserializes JSON file to instances:
    Private class attributes: 
        __file_path: (string) - path to the JSON file (ex: file.json)
        __objects: (dictionary) - empty but will store all objects by <class name>.id """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists """
     if os.path.exists(self.__file_path):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    # Assuming you have a static method from_dict() in each model class
                    obj = eval(class_name).from_dict(obj_dict)
                    self.__objects[key] = obj
        except Exception:
            pass
