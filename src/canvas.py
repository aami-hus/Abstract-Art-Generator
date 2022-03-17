##
# @file canvas.py
#
# @brief Defines the canvas class.
#
# @section author_sensors Author(s)
# - Created by Jessica Dawson on 03/16/2022.

# Imports
import pygame as pg

from widget_storage import widgets

class canvas:
    """! The canvas class.

    Provides the canvas the program draws on along with functions for drawing layers to the canvas and drawing the canvas to the ui.
    """

    def __init__(self, x, y, width, height, display_width, display_height, window):
        """! Initializes the canvas.

        @param x                Horizontal position to draw the canvas at on the ui.
        @param y                Vertical position to draw the canvas at on the ui.
        @param width            Width of the canvas surface.
        @param height           Height of the canvas surface.
        @param display_width    Width of the ui's canvas display port.
        @param display_height   Height of the ui's canvas display port.
        @param window           Ui window to draw the canvas to.
        """
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__display_width = display_width
        self.__display_height = display_height
        self.__window = window

        self.__canvas = pg.Surface((self.__width, self.__height))
        self.__canvas.fill((255, 255, 255))
        self.__display_canvas = pg.Surface((self.__display_width, self.__display_height))

        self.__bg_layer = pg.Surface((self.__width, self.__height))
        self.__bg_layer.fill((255, 255, 255))


    def generate_bg(self, color):
        """! Fill the canvas background with a color.
        
        @param color    Color to fill the background with.
        """
        self.__bg_layer.fill(pg.Color(color))


    def draw_to_canvas(self):
        """! Draws layers to the canvas.

        Calls any drawing widgets to draw to the canvas.
        """
        self.generate_bg(widgets.color_palette.get_background_color())
        self.__canvas.blit(self.__bg_layer, (0, 0))

        self.__canvas.convert()
        self.__display_canvas = pg.transform.smoothscale(self.__canvas, (self.__display_width, self.__display_height))


    def draw(self):
        """! Draws the canvas to the ui.
        """
        self.__window.blit(self.__display_canvas, (self.__x, self.__y))


    def get_canvas(self):
        """! Gets the pygame surface the canvas draws on.

        @return The pygame surface the canvas draws on.
        """
        return self.__canvas