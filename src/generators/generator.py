##
# @file generator.py
#
# @brief Defines the abstract class generator.
#
# @section author_generator Author(s)
# - Created by Jessica Dawson on 03/17/2022.

# Import
from abc import ABC, abstractmethod

from ui_controller import controller

class generator(ABC):
    """! Abstract class for generators to extend. """

    @abstractmethod
    def draw(layer, complexity, cp, style, magnitude):
        """! Draws to a layer. 
        
        @param layer        The layer to draw to.
        @param complexity   The complexity of the layer.
        @param cp           The color palette to draw with.
        @param style        The style of the layer.
        @param magnitude    The magnitude of the layer.
        """
        pass