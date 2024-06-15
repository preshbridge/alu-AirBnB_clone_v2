#!/usr/bin/python3
""" Class FileStorage """
from json import dump, load
from os.path import exists
from models.base_model import BaseModel
from models import User
from models import Place
from models import City
from models import Review
from models import State
from models import Amenity

name_class = ["BaseModel", "User", "Place",
              "State", "City", "Amenity", "Review"]


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dectionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets  the obj with key in __objects
        """
        class_name = obj.__class__.__name__
        id = obj.id
        class_id = class_name + "." + id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """ file storage
        """
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            dump(dict_to_json, file)

    def reload(self):
        """ if (__file_path) exists, deserializes JSON file to __objects
            else, do nothing.
        """
        dict_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                dict_obj = load(file)
                for key, value in dict_obj.items():
                    class_name = key.split(".")[0]
                    if class_name in name_class:
                        FileStorage.__objects[key] = eval(class_name)(**value)
                    else:
                        pass