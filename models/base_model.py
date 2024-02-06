""" Module with the Parent class: BaseModel for the AirBnB clone project"""


import uuid
from datetime import datetime
from models.__init__ import storage
from models.engine.file_storage import new


class BaseModel:
    """Parent class
    Attributes:
        id: universal unique identifier for object
        created_at: current date time for instance creation
        updated_at: current time for instance update
    """
    def __init__(self, *args, **kwargs):
        """instantiation of object attributes"""
        if kwargs:
            # Avoid adding __class__ as an attribute
            kwargs.pop('__class__', None)
            # Convert the created_at and updated_at to datetime objects
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], 
                        '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], 
                        '%Y-%m-%dT%H:%M:%S.%f')
            #set attributes using kwargs
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        # if it’s a new instance (not from a dictionary representation)
        new(storage)

    def __str__(self):
        """string representation of class attributes"""
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """dictionary containing all key/values of instances"""
        object_dict = self.__dict__
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()

        return object_dict
