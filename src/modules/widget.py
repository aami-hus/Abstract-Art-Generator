##
# @file widget.py
#
# @brief Defines the widget abstract class.
#
# @section author_widget Author(s)
# - Created by Jessica Dawson on 03/16/2022.

# Imports
from abc import ABC, abstractmethod

class widget(ABC):
    """! An abstract class for widgets to extend.

    Provides an interface widgets typically use.
    """

    @abstractmethod
    def __init__(self, x, y, window, ui_manager):
        """! Initializes the widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """
        pass

    def draw_ui_dynamic(self):
        """! Draw ui elements that need to be refreshed each frame.

        For our purposes draws everything that isn't a pygame_gui element.
        """
        pass


    def draw_ui_static(self):
        """! Draw ui elements that only need to be drawn once.

        For our purposes draws pygame_gui elements.
        """
        pass


    def events(self, event):
        """! Handle pygame events for the widget.
        
        @param event    The event to be processed.
        """
        pass


    def randomize(self):
        """! Randomize the widget settings. """
        pass


    def draw_canvas(self):
        """! Draw to the canvas. """
        pass


    def refresh_ui_static(self):
        """! Refresh the static ui elements. """
        pass