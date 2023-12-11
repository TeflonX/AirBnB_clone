#!/usr/bin/python3
"""
A module for the class, FileStorage
"""


import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    a class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User
    }

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serialized_obj_dict = {}
        for key, value in FileStorage.__objects.items():
            serialized_obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
        """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name, instance_id = key.split('.')

                    cls = eval(class_name)

                    instance = cls(**value)
                    FileStorage.__objects[key] = instance

    def serialize(self):
        """
        Serialize object to JSON
        """
        serialize_obj = {}
        for key, obj in self.__objects.items():
            serialize_obj[key] = obj.to_dict()

        return serialized_obj

    def deserialize(self, json_dict):
        """
        Deserializes JSON to object
        """
        for key, value in json_dict.items():
            class_name, obj_id = key.split('.')
            cls = self.CLASSES.get(class_name)
            if cls:
                instance = cls(**value)
                self.__objects[key] = instance
