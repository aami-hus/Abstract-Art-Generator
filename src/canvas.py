import pygame as pg

from widget_storage import widgets

class canvas:

    def __init__(self, x, y, width, height, display_width, display_height, window):
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
        self.__bg_layer.fill(pg.Color(color))


    def draw_to_canvas(self):
        self.generate_bg(widgets.color_palette.get_background_color())
        self.__canvas.blit(self.__bg_layer, (0, 0))

        self.__canvas.convert()
        self.__display_canvas = pg.transform.smoothscale(self.__canvas, (self.__display_width, self.__display_height))


    def draw(self):
        self.__window.blit(self.__display_canvas, (self.__x, self.__y))


    def get_canvas(self):
        return self.__canvas