#!/usr/bin/python3
"""Student Module"""


class Student:
    """Student class"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """
        initializes student
        Args:
        first_name: student first name
        last_name: student last name
        age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns a dict representation of variables of student
        """
        if type(attrs) is list:
            bool = all(type(i) is str for i in attrs)
            if bool:
                ret = {}
                for key in attrs:
                    if key in vars(self).keys():
                        ret[key] = vars(self)[key]
                return ret
        return vars(self)
