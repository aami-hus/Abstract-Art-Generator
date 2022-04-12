##
# @file canvas.py
#
# @brief Defines the canvas class.
#
# @section author_canvas Author(s)
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

        ## The surface the art is drawn to
        self.canvas = pg.Surface((self.__width, self.__height))
        self.canvas.fill((255, 255, 255))

        ## The surface that is drawn to the ui as a display port
        self.display_canvas = pg.Surface((self.__display_width, self.__display_height))

        ## The single color, background layer of the canvas
        self.bg_layer = pg.Surface((self.__width, self.__height))
        self.bg_layer.fill((255, 255, 255))


    def generate_bg(self, color):
        """! Fill the canvas background with a color.
        
        @param color    Color to fill the background with.
        """
        self.bg_layer.fill(pg.Color(color))


    def draw_layers(self):
        """! Calls various widgets to draw to their layers.

        Calls draw_canvas in all the drawing widgets.
        """
        self.generate_bg(widgets.color_palette.get_background_color())

        widgets.layer_one.draw_canvas()
        widgets.layer_two.draw_canvas()
        widgets.layer_three.draw_canvas()

        widgets.text_overlay.draw_canvas()


    def draw_to_canvas(self):
        """! Blits layers to the canvas.

        Combines the currently drawn layers into the canvas.
        """
        self.canvas.blit(self.bg_layer, (0, 0))

        self.canvas.blit(widgets.layer_one.layer, (0, 0))
        self.canvas.blit(widgets.layer_two.layer, (0, 0))
        self.canvas.blit(widgets.layer_three.layer, (0, 0))

        self.canvas.blit(widgets.text_overlay.layer, (0, 0))

        self.canvas.blit(widgets.overlay.overlay_layer, (0, 0))

        self.canvas.convert()
        self.display_canvas = pg.transform.smoothscale(self.canvas, (self.__display_width, self.__display_height))


    def draw(self):
        """! Draws the canvas to the ui.
        """
        self.__window.blit(self.display_canvas, (self.__x, self.__y))


    def get_canvas(self):
        """! Gets the pygame surface the canvas draws on.

        @return The pygame surface the canvas draws on.
        """
        return self.canvas

    def get_width(self):
        """! Gets the width of the canvas"""
        return self.__width
    def get_height(self):
        """! Gets the height of the canvas"""
        return self.__height