#!/usr/bin/python3
"""
review

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review

    Attributes:, text,user_id,place_id
    """

    text = ""
    user_id = ""
    place_id = ""
