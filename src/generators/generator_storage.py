##
# @file generator_storage.py
#
# @brief Defines and initializes the generator_storage class.
#
# @section author_generator_storage Author(s)
# - Created by Jessica Dawson on 03/16/2022.

from generators.circle_generator import circle_generator
from generators.square_generator import square_generator
from generators.line_generator import line_generator
from generators.ring_generator import ring_generator
from generators.dots_generator import dots_generator
from generators.curves_generator import curves_generator
from generators.hpolygons_generator import hpolygons_generator
from generators.fpolygons_generator import fpolygons_generator

## Instance of generator_storage to access generators through.
#
# Import this instance and access widgets with widgets.widget_name()
generator_storage = None

class generator_storage:
    """! Storage for program generators .

    Allows all other modules to access program generators.
    """
    def __init__(self):
        ## The color palette widget.
        self.circle_generator = circle_generator()
        self.squa

generator_storage = generator_storage()