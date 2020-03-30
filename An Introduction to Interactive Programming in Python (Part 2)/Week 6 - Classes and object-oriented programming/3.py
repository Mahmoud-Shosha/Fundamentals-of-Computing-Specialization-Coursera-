"""
As we noted in the last problem, our current definition of the Tile class produces objects that contain no data.
This design is not going to be much help in re-implementing Memory. At this point, we should start considering
what kind of data a Tile object should contain. One piece of data that Tile objects should certainly contain is
the number associated with the tile. To create a Tile object that contains the number associated with the tile,
we need to define a special function known as an initializer in the body of the class definition.
(Functions defined in the body of the class definition are referred to as methods.)

In Python, the class initializer always has the special name __init__. The parameters to this function __init__
provide the information necessary to create the data stored in the object. By convention, the first parameter to
__init__ has the name self and serves as a reference to the object generated by the initializer.
The remaining parameters, if any, contain the information used in creating the object. The body of the initializer
consists of sequence of Python statements that use this information to compute and add data to the object.
Each piece of data stored in the object is named by a field. If name of a field is field_name, we can reference
this piece of data via the expression self.field_name.

Your next task is to implement an initializer for the Tile class and create two tiles; one called my_tile whose
number field has the value 3 and another called your_tile whose number field has value 4. The definition of
the initializer should include the required parameter self and a parameter num that is the number associated with
the tile. The body of the initializer should store num in the field number. To create a Tile object, you will need to
include the number associated with the tile as parameter when you call Tile(....) to create a Tile object.
(The reference corresponding to the parameter self is generated by Python during the creation of the Tile object
and is not included in the call to the initializer.)
"""


# Define an initializer for the Tile class, create a Tile object


#################################################
# Student adds code where appropriate

# definition of a Tile class
class Tile:

    def __init__(self, num):
        self.number = num


# create two tiles with numbers 3 and 4
my_tile = Tile(3)
your_tile = Tile(4)


###################################################
# Testing code

print my_tile
print my_tile.number
print your_tile
print your_tile.number

####################################################
# Output of testing code

# <__main__.Tile object>
# 3
# <__main__.Tile object>
# 4