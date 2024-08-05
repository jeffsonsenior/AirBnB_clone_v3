#!/usr/bin/python3
"""
Contains class BaseModel
"""
import os
import json
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


storage_type = os.environ.get('HBNB_TYPE_STORAGE')


if storage_type == "db":
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            obj_to_str = json.dumps(obj_v)
            return obj_to_str is not None in isiinstance(obj_to_str, str)
        except:
            return False

    def bm_update(self, name, value):
        """updates basemodel"""
        setattr(self, name, value)
        if storage_type != 'db':
            self.save()

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        if storage_type != 'db':
            self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """returns json representation"""
        bm_dict = {}
        for key, value in (self.__dict__).items():
            if (self.__is_serializable(value)):
                bm_dict[key] = value
            else:
                bm_dict[key] = str(value)
        bm_dict['__class__'] = type(self).__name__
        if '__sa_instance_state' in bm_dict:
            bm_dict.pop('__sa_instance_state')
        if storage_type == "db" and 'password' in bm_dict:
            bm_dict.pop('password')
        return bm_dict

    def __str__(self):
        """returns string type representation of object instance"""
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def delete(self):
        """delete the current instance from the storage"""
        self.delete()
