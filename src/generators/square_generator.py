##
# @file square_generator.py
#
# @brief Defines the square_generator class.
#
# @section author_square Author(s)
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

class square_generator(generator):
    """! Class to draw squares. """

    def draw(self, layer, complexity, cp, style, magnitude):
        """! Draws squares to a layer. 
        
        @param layer        The layer to draw to.
        @param complexity   The complexity of the layer.
        @param cp           The color palette to draw with.
        @param style        The style of the layer.
        @param magnitude    The magnitude of the layer.
        """
        if style == art_styles_list[0]:     # Chaotic
            for i in range(complexity*2):
                size = randint(magnitude[0], magnitude[1])
                posX = randint(-size, self.width)
                posY = randint(-size, self.height)
                current_color = cp[randint(0, len(cp)-1)]
                pg.draw.rect(layer, pg.Color(current_color), (posX, posY, size, size))

        if style == art_styles_list[1]:     # Striped Horizontal
            row_square_count = complexity // 2 + 2
            point = self.width // (row_square_count - 2)
            row_count = self.height // point + 2
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                if i % 2 == 0:
                    current_color = color_one if current_color == color_two else color_two
                for j in range(row_square_count):
                    posX = j * point
                    posY = i * point
                    size = randint(magnitude[0], magnitude[1])
                    if i % 2 == 0:
                        pg.draw.rect(layer, pg.Color(current_color),(posX, posY, size, size))

        if style == art_styles_list[2]:     # Striped Vertical
            row_square_count = complexity // 2 + 2
            point = self.width // (row_square_count - 2)
            row_count = self.height // point + 2
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                for j in range(row_square_count):
                    if j % 1 == 0:
                        current_color = color_one if current_color == color_two else color_two
                    posX = j * point
                    posY = i * point
                    size = randint(magnitude[0], magnitude[1])
                    if j % 2 == 0:
                        pg.draw.rect(layer, pg.Color(current_color), (posX-size//2, posY-size//2, size, size))

        if style == art_styles_list[3]:     # Mosaic
            row_square_count = complexity//2 + 2
            size = self.width // (row_square_count-2)
            row_count = self.height // size + 2
            color_one = cp[randint(0, len(cp)-1)]
            color_two = cp[randint(0, len(cp)-1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                for j in range(row_square_count):
                    current_color = color_one if (i + j) % 2 == 0 else color_two
                    posX = j * size
                    posY = i * size
                    pg.draw.rect(layer, pg.Color(current_color), (posX+size//20, posY+size//20, size-size//10, size-size//10))

        if style == art_styles_list[4]:     # Cornered
            for corner in range(4):
                corner_color = cp[randint(0, len(cp)-1)]
                if corner == 0:
                    pg.draw.rect(layer, pg.Color(corner_color), (0, 0, magnitude[1], magnitude[1]))
                if corner == 1:
                    pg.draw.rect(layer, pg.Color(corner_color), (self.width-magnitude[1], 0, magnitude[1], magnitude[1]))
                if corner == 2:
                    pg.draw.rect(layer, pg.Color(corner_color), (self.width-magnitude[1], self.height-magnitude[1], magnitude[1], magnitude[1]))
                if corner == 3:
                    pg.draw.rect(layer, pg.Color(corner_color), (0, self.height-magnitude[1], magnitude[1], magnitude[1]))

            for i in range(complexity*3):
                current_color = cp[randint(0, len(cp)-1)]
                corner = randint(0, 3)
                x_area, y_area = (0, 0), (0, 0)
                if corner == 0:
                    x_area, y_area = (-magnitude[1]//2, self.width//3), (-magnitude[1]//2, self.height//2-magnitude[1])
                if corner == 1:
                    x_area, y_area = (2*self.width//3-magnitude[1], self.width), (-magnitude[1]//2, self.height//2-magnitude[1])
                if corner == 2:
                    x_area, y_area = (2*self.width//3-magnitude[1], self.width), (self.height//2, self.height)
                if corner == 3:
                    x_area, y_area = (-magnitude[1], self.width//3), (self.height//2, self.height)

                posX = randint(x_area[0], x_area[1])
                posY = randint(y_area[0], y_area[1])
                size = randint(magnitude[0], magnitude[1])

                pg.draw.rect(layer, pg.Color(current_color), (posX, posY, size, size))

        if style == art_styles_list[5]:     # Centered
            in_x_area, in_y_area = (self.width // 4, 3 * self.width // 4), (self.height // 4, 3 * self.height // 4)
            out_x_area, out_y_area = (self.width // 6, 5 * self.width // 6), (self.height // 6, 5 * self.height // 6)

            for i in range(complexity):
                random_number = randint(0, 5)
                if random_number < 4:
                    center_x = randint(in_x_area[0], in_x_area[1])
                    center_y = randint(in_y_area[0], in_y_area[1])
                else:
                    center_x = randint(out_x_area[0], out_x_area[1])
                    center_y = randint(out_y_area[0], out_y_area[1])

                size = randint(magnitude[0], magnitude[1])
                current_color = cp[randint(0, len(cp) - 1)]

                pg.draw.rect(layer, pg.Color(current_color), (center_x-size//2, center_y-size//2, size, size))
        if style == art_styles_list[6]:     # Empty
            pass