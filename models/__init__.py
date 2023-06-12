#!/usr/bin/python3
"""Module create a unique FileStorage
instance for your application"""

from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

storage = FileStorage()
storage.reload()
