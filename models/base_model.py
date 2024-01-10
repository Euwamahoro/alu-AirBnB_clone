#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
Create class BaseModel that  defines all common
attributes/methods for other classes
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize"""
        if len(kwargs)> 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    
                if (key == "created_at" or key == "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            
    def __str__(self):
        """returns string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute 
        updated_at with the current datetime """
        self.updated_at= datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})
        return (dictionary)
