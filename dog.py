# Add comments before you do anything else.
#--------------------------------
#!/usr/bin/env python3
# Author: Daniel Tian
# Date: November 6th, 2024
# Purpose: class Dog
#--------------------------------

class Dog:
    # init is the constructor, it is called an object of this class is created.
    # this constructor function creates two variables; _name and _breed.
    # these variables are called attributes or instance variables.
    # instance variables are created for each class object.
    # each class object received its own instance variables.
    
    def __init__(self, dog_name, dog_breed): 
        # self has the reference/address of a specific object
        # self.variable_name makes sure that variable is created for the specific object.
        self._name = dog_name  # _name is being assigned the value name passed as parameter
        self._breed = dog_breed  # _breed is being assigned the value breed passed as parameter

    def bark(self):
        # each class method can access instance variables.
        return f"{self._name} says woof!"
