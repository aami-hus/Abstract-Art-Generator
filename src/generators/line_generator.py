##
# @file line_generator.py
#
# @brief Defines the line_generator class.
#
# @section author_line Author(s)
# - Created by Jessica Dawson on 03/17/2022.

# Imports
from random import randint

import pygame as pg

from generator import generator

art_styles_list = [
    "Chaotic",
    "Striped Horizontal",
    "Striped Vertical",
    "Mosaic",
    "Cornered",
    "Centered",
    "Empty"
]

class line_generator(generator):
    """! Class to draw lines. """

    def draw(self, layer, complexity, cp, style, magnitude):
        """! Draws lines to a layer. 
        
        @param layer        The layer to draw to.
        @param complexity   The complexity of the layer.
        @param cp           The color palette to draw with.
        @param style        The style of the layer.
        @param magnitude    The magnitude of the layer.
        """
        if style == art_styles_list[0]:     # Chaotic
            for i in range(complexity):
                posX = (randint(-200, self.width+200), randint(0, self.width))
                posY = (randint(-200, self.height+200), randint(0, self.height))
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1])
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size//4)
        elif style == art_styles_list[1]:   # Striped Horizontal
            interval = self.height // complexity
            for i in range(complexity):
                posX = 0, self.width
                posY = i * interval + randint(0, self.height//10), i * interval + randint(0, self.height//10)
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1])
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size // 4)
        elif style == art_styles_list[2]:   # Striped Vertical
            interval = self.width // complexity
            for i in range(complexity):
                posY = 0, self.height
                posX = i * interval + randint(0, self.width//10), i * interval + randint(0, self.width//10)
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1])
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size // 4)
        elif style == art_styles_list[3]:   # Mosaic
            row_line_count = complexity // 3 + 1
            row_count = complexity // 4 + 1
            x_interval = self.width // (row_line_count - 1)
            y_interval = self.height // (row_count - 1)
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            for i in range(row_count):
                for j in range(row_line_count):
                    current_color = color_one if (i+j) % 2 == 0 else color_two
                    size = randint(magnitude[0], magnitude[1]) // 4
                    posX = ((x_interval*j), (x_interval*(j+1)))
                    posY_u = ((y_interval*i), (y_interval*(i+1)))
                    posY_d = ((y_interval*(i+1)), (y_interval*i))
                    if randint(0,1) == 0:
                        pg.draw.line(layer, pg.Color(current_color), (posX[0], posY_u[0]), (posX[1], posY_u[1]), size)
                    else:
                        pg.draw.line(layer, pg.Color(current_color), (posX[0], posY_d[0]), (posX[1], posY_d[1]), size)

        elif style == art_styles_list[4]:   # Cornered
            for i in range(complexity*2):
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1]) // 4
                corner = randint(0, 3)
                first_x_area, second_x_area = 0, 0
                first_y_area, second_y_area = 0, 0
                if corner == 0:
                    first_x_area, second_x_area = (-50, 100), (0, self.width//2)
                    first_y_area, second_y_area = (-50, 100), (0, self.height//2)
                elif corner == 1:
                    first_x_area, second_x_area = (self.width-100, self.width+50), (self.width//2, self.width)
                    first_y_area, second_y_area = (-50, 100), (0, self.height // 2)
                elif corner == 2:
                    first_x_area, second_x_area = (self.width-100, self.width+50), (self.width//2, self.width)
                    first_y_area, second_y_area = (self.height-100, self.height+50), (self.height//2, self.height)
                elif corner == 3:
                    first_x_area, second_x_area = (-50, 100), (0, self.width // 2)
                    first_y_area, second_y_area = (self.height-100, self.height+50), (self.height//2, self.height)

                posX = (randint(first_x_area[0], first_x_area[1]), randint(second_x_area[0], second_x_area[1]))
                posY = (randint(first_y_area[0], first_y_area[1]), randint(second_y_area[0], second_y_area[1]))

                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size)
        elif style == art_styles_list[5]:   # Centered
            for i in range(complexity//2):
                current_color = cp[randint(0, len(cp)-1)]
                posX = (randint(2*self.width//5, 3*self.width//5), randint(0, self.width))
                posY = (randint(2*self.height//5, 3*self.height//5), randint(0, self.height))
                size = randint(magnitude[0], magnitude[1]) // 4
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size)
        elif style == art_styles_list[6]:   # Empty, do not draw anything.
            pass