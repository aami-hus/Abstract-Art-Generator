##
# @file hpolygons_generator.py
#
# @brief Defines the hpolygons_generator class.
#
# @section author_hpolygons Author(s)
# - Created by Jessica Dawson on 03/17/2022.

# Imports
from random import randint

import pygame as pg

from generators.generator import generator

art_styles_list = [
    "Chaotic",
    "Striped Horizontal",
    "Striped Vertical",
    "Mosaic",
    "Cornered",
    "Centered",
    "Empty"
]

class hpolygons_generator(generator):
    """! Class to draw hollow polygons. """

    def draw(layer, complexity, cp, style, magnitude):
        """! Draws hollow polygons to a layer. 
        
        @param layer        The layer to draw to.
        @param complexity   The complexity of the layer.
        @param cp           The color palette to draw with.
        @param style        The style of the layer.
        @param magnitude    The magnitude of the layer.
        """

        fill = 1

        if style == art_styles_list[0]:     # Chaotic
            for i in range(complexity//2):
                current_color = cp[randint(0, len(cp)-1)]
                if fill == 0:
                    fill_type = 0
                else:
                    fill_type = randint(magnitude[0]//5, magnitude[1]//5)
                points_count = randint(3, 5)
                points = []
                first_point = [randint(0, self.width), randint(0, self.height)]
                for _ in range(points_count):
                    points.append([randint(first_point[0]-magnitude[1]*2, first_point[0]+magnitude[1]*2),
                                   randint(first_point[1]-magnitude[1]*2, first_point[1]+magnitude[1]*2)])

                pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        if style == art_styles_list[1]:     # Striped Horizontal
            row_polygon_count = int(complexity // 2)
            row_count = complexity // 3
            x_interval = self.width // row_polygon_count
            y_interval = self.height // row_count

            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            for i in range(row_count):
                if (i + 1) % 2 == 0:
                    current_color = color_one if current_color == color_two else color_two
                for j in range(row_polygon_count):
                    if fill == 0:
                        fill_type = 0
                    else:
                        fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                    x_area = (x_interval * j, x_interval * (j + 1))
                    y_area = (y_interval * i, y_interval * (i + 1))
                    point_count = randint(3, 5)
                    points = []
                    if (i + 1) % 2 == 0:
                        for k in range(point_count):
                            points.append((randint(x_area[0], x_area[1]), randint(y_area[0], y_area[1])))
                        pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        if style == art_styles_list[2]:     # Striped Vertical
            row_polygon_count = int(complexity // 2)
            row_count = complexity // 3
            x_interval = self.width // row_polygon_count
            y_interval = self.height // row_count

            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            for i in range(row_count):
                for j in range(row_polygon_count):
                    if fill == 0:
                        fill_type = 0
                    else:
                        fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                    x_area = (x_interval * j, x_interval * (j + 1))
                    y_area = (y_interval * i, y_interval * (i + 1))
                    point_count = randint(3, 5)
                    points = []
                    if j % 2 == 0:
                        current_color = color_one if current_color == color_two else color_two
                        for k in range(point_count):
                            points.append((randint(x_area[0], x_area[1]), randint(y_area[0], y_area[1])))
                        pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        if style == art_styles_list[3]:     # Mosaic
            row_polygon_count = int(complexity // 2)
            row_count = complexity // 3
            x_interval = self.width // row_polygon_count
            y_interval = self.height // row_count

            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            for i in range(row_count):
                for j in range(row_polygon_count):
                    if fill == 0:
                        fill_type = 0
                    else:
                        fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                    current_color = color_one if (i + j) % 2 == 0 else color_two
                    x_area = (x_interval*j, x_interval*(j+1))
                    y_area = (y_interval*i, y_interval*(i+1))
                    point_count = randint(3, 5)
                    points = []
                    for k in range(point_count):
                        points.append((randint(x_area[0], x_area[1]), randint(y_area[0], y_area[1])))
                    pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        if style == art_styles_list[4]:     # Cornered
            x_areas = [(-100, self.width//3), (2*self.width//3, self.width+100),
                       (2*self.width//3, self.width+100), (-100, self.width//3)]

            y_areas = [(-100, self.height//2-50), (-100, self.height//2-100),
                       (self.height//2+100, self.height+100), (self.height//2+100, self.height+100)]

            point_count = randint(3, 5)
            for i in range(complexity//2):
                corner = randint(0, 3)
                if fill == 0:
                    fill_type = 0
                else:
                    fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)
                current_color = cp[randint(0, len(cp)-1)]
                points = []
                for j in range(point_count):
                    pos = (randint(x_areas[corner][0], x_areas[corner][1]),
                           randint(y_areas[corner][0], y_areas[corner][1]))
                    points.append(pos)

                pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        if style == art_styles_list[5]:     # Centered
            x_inner_area = [self.width // 4, 3 * self.width // 4]
            x_outer_area = [self.width // 6, 5 * self.width // 6]
            y_area = [self.height // 4, 3 * self.height // 4]
            for i in range(complexity // 4):
                if fill == 0:
                    fill_type = 0
                else:
                    fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                current_color = cp[randint(0, len(cp)-1)]

                point_count = randint(3, 4)
                points = []
                for j in range(point_count):
                    if randint(0, 6) <= 4:
                        pos = (randint(x_inner_area[0], x_inner_area[1]), randint(y_area[0], y_area[1]))
                    else:
                        pos = (randint(x_outer_area[0], x_outer_area[1]), randint(y_area[0], y_area[1]))

                    points.append(pos)
                pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        if style == art_styles_list[6]:     # Empty
            pass