#!/usr/bin/python3
"""
BaseModel class
"""


from datetime import datetime
import models
import uuid


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Method that initializes the attributes of the base class using args
        and kwargs
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def __str__(self):
        """
        function that prints a string literal
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of some instances
        """
        inst_dict = self.__dict__.copy()

        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()

        return inst_dict
