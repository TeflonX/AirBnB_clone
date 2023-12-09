#!/usr/bin/python3


import json
from os.path import exists


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
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serialized_obj_dict = {}
        for key, value in self.__objects.items():
            serialized_obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json.loads(file)

                for key, value in data.items():
                    class_name, instance_id = key.split('.')
                    module = __import__("models." + class_name,
                            from_list[class_name])
                    cls = getattr(module, class_name)
                    instance = cls(**value)
                    self.__objects[key] = instance
