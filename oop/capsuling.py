"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__status = "Active"
    
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
        
    def set_status(self, status):
        if status == "Active" or status == "Expelled" or status == "Finished" or status == "Inactive":
            self.__status = status
    
    def get_status(self):
        return self.__status
        
    pass
