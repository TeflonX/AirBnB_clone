#!/usr/bin/python3
"""
A module for the class, FileStorage
"""


import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """
    a class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

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
