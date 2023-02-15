#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Args:
           attrs: a list of strings, only attributes name contain in
           this list must be retrieved
        Return:
           return new new dictionary
        """
        attr_list = {}
        try:
            for key in attrs:
                if self.__dict__.get(key) is not None:
                    attr_list.update({key: self.__dict__.get(key)})
            return attr_list
        except:
            return self.__dict__
