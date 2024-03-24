#!/usr/bin/python3
"""
base
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
        attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())

        self.updated_at = datetime.now()

        self.created_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        string
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        cur time
        """
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """
        dict
        """
        dict = {**self.__dict__}
        dict["__class__"] = type(self).__name__
        dict["updated_at"] = dict["updated_at"].isoformat()
        dict["created_at"] = dict["created_at"].isoformat()

        return dict
