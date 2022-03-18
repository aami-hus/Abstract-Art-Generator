##
# @file overlay.py
#
# @brief Defines the overlay class.
#
# @section author_sensors Author(s)
# - Created by Fady Morcos on 03/17/2022.

# Imports
from random import randint, choice

import pygame_gui as pgui
import pygame as pg

from modules.widget import widget
import assets


class overlay(widget):

    """! The overlay widget class.

    Provides ui settings to change the current overlay style.
    """

    def __init__(self, x, y, window, ui_manager):
        """! Initializes the color palette widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager
