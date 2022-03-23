##
# @file overlay.py
#
# @brief Defines the overlay class.
#
# @section author_overlay Author(s)
# - Created by Jessica Dawson on 03/17/2022.

# Imports
import pygame_gui as pgui
import pygame as pg
from random import randint, choice

from modules.widget import widget
from widget_storage import widgets


class overlay(widget):
    """! The overlay widget class.

    Provides a ui and functionality to specify an overlay and draw to a pygame surface.
    """
    
    def __init__(self, x, y, window, ui_manager, layer_num):
        """! Initializes the overlay widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        ## The pygame surface the overlay draws to.
        self.overlay_layer = pg.Surface((3840, 2160), pg.SRCALPHA)


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the overlay widget.
        
        Draws the text and overlay thumbnails.
        """

        pass


    def draw_ui_static(self):
        """! Draws the static ui elements for the overlay widget.
        
        Draws the overlay selection buttons.
        """

        pass


    def events(self, event):
        """! Processes pygame events for the overlay widget.
        
        Handles the overlay selection buttons.

        @param event    The pygame event being processed.
        """

        pass


    def draw_canvas(self):
        """! Draw the currently selected overlay image to self.overlay_layer. """
        pass


    def clean_layer(self):
        """! Clean the overlay by setting it to be blank and see-through. """
        self.layer.fill((0, 0, 0, 0))
