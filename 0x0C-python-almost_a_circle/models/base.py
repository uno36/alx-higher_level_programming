#!/usr/bin/python3
"""Base module"""

import json
"""import json"""


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method: initialize the passing variables
        Args:
            id: id of the base
        Attributes:
            __nb_objects: number of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string static method: Serialize obj to a JSON
        formatted str.
        Args:
           list_dictionaries: a list of dictionaries
        Return:
           returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file classmethod: writes the JSON string
        representation of list_objs to a file
        Args:
            cls: the class itself
            list_objs: a list of instances who inherits of Base
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string static method: Deserialize JSON string
        to object
        Args:
            json_string: a string representing a list of dictionaries
        Return:
            returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create classmethod: Dictionary to Instance
        Args:
           cls: the class itself
           dictionary: double pointer to a dictionary
        Return:
           returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file classmethod: File to instances
        Args:
           cls: the class itself
        Return:
           returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        list_instance = []
        try:
            with open(filename, mode="r", encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
            for d in list_dict:
                list_instance.append(cls.create(**d))
            return list_instance
        except FileNotFoundError:
            return []
