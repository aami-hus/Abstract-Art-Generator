##
# @file layer.py
#
# @brief Defines the layer class.
#
# @section author_layer Author(s)
# - Created by Aamina Hussain on 03/17/2022.

# Imports
import pygame_gui as pgui
import pygame as pg
from random import randint, choice

from modules.widget import widget
from widget_storage import widgets
import assets

from generators.circle_generator import circle_generator
from generators.square_generator import square_generator
from generators.line_generator import line_generator
from generators.ring_generator import ring_generator
from generators.dots_generator import dots_generator
from generators.curves_generator import curves_generator
from generators.hpolygons_generator import hpolygons_generator
from generators.fpolygons_generator import fpolygons_generator

_art_styles_list = [
    "Chaotic",
    "Striped Horizontal",
    "Striped Vertical",
    "Mosaic",
    "Cornered",
    "Centered",
    "Empty"
]

_art_shapes_list = [
    "Lines",
    "Circles",
    "Squares",
    "Hollow Polygons",
    "Filled Polygons",
    "Dots",
    "Curves",
    "Rings"
]


class layer(widget):
    """! The layer widget class.

    Provides a ui and functionality to specify a drawing algorithm and draw to a pygame surface.
    """
    
    def __init__(self, x, y, window, ui_manager, layer_num):
        """! Initializes the layer widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        ## The pygame surface the layer draws to.
        self.layer = pg.Surface((3840, 2160), pg.SRCALPHA)
        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager
        self.__layer_num = layer_num

        #starting options for dropdown menus
        self.__style = choice(_art_styles_list)
        self.__shape = choice(_art_shapes_list)
        self.__complexity = randint(10,30)#15
        self.__size = randint(51, 400) #400

        #locks
        self.__style_lock = 0
        self.__shape_lock = 0
        self.__complexity_lock = 0
        self.__size_lock = 0


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the layer widget.
        
        Draws the text and lock icons.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 17

        pg.draw.rect(self.__window, pg.Color("#2B2834"), (self.__x, self.__y, 252, 190))

        if self.__style_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+30))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+30))

        if self.__shape_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+60))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+60))

        if self.__complexity_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+110))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+110))

        if self.__size_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+160))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+160))

        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " STYLE", color=assets.ui_h1_color, pos=(interactables_margin, self.__y+10), font_size=18)
        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " COMPLEXITY", color=assets.ui_color, pos=(interactables_margin, self.__y+95), font_size=14)
        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " SHAPE SIZE", color=assets.ui_color, pos=(interactables_margin, self.__y+145), font_size=14)


    def draw_ui_static(self):
        """! Draws the static ui elements for the layer widget.
        
        Draws the shape and style dropdowns, the complexity and size sliders, and lock button.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 6
        num_of_layer = self.__layer_num.lower()

        style_dropdown = pgui.elements.UIDropDownMenu(options_list=_art_styles_list,
                                                                starting_option=self.__style,
                                                                relative_rect=pg.Rect(interactables_margin, self.__y+30, 200, 22), manager=self.__ui_manager,
                                                                object_id="layer_"+num_of_layer+"_style_dropdown")

        shape_dropdown = pgui.elements.UIDropDownMenu(options_list=_art_shapes_list,
                                                                starting_option=self.__shape,
                                                                relative_rect=pg.Rect(interactables_margin, self.__y+60, 200, 22), manager=self.__ui_manager,
                                                                object_id="layer_"+num_of_layer+"_shape_dropdown")

        complexity_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+110, 200, 22),
                                                                    start_value=self.__complexity,
                                                                    value_range=(10, 30), manager=self.__ui_manager,
                                                                    object_id="layer_"+num_of_layer+"_complexity_slider")

        size_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+160, 200, 22),
                                                                start_value=self.__size, value_range=(50, 400),
                                                                manager=self.__ui_manager, object_id="layer_"+num_of_layer+"_size_slider")

        # "lock_button_three" changed to "layer_one_lock_butter"
        # etc, 4 = layer 1 shape, 5 = layer 1 complex, 6 = layer 1 size
        # repeat for layer 2 and 3
        style_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+37, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_style_lock_button")
        shape_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+67, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_shape_lock_button")
        complexity_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+117, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_complexity_lock_button")
        size_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+167, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_size_lock_button")


    def randomize(self):
        """! Randomize the shape, style, complexity, and size of the layer drawing algorithm. """

        if self.__style_lock == 0:
            self.__style = choice(_art_styles_list)
        if self.__shape_lock == 0:
            self.__shape = choice(_art_shapes_list)
        if self.__complexity_lock == 0:
            self.__complexity = randint(10,30)
        if self.__size_lock == 0:
            self.__size = randint(51, 400)


    def events(self, event):
        """! Processes pygame events for the layer widget.
        
        Handles the shape and style dropdowns, the complexity and size sliders, and lock button.

        @param event    The pygame event being processed.
        """

        num_of_layer = self.__layer_num.lower()

        if event.user_type == pgui.UI_BUTTON_PRESSED:
            if event.ui_object_id == "layer_"+num_of_layer+"_style_lock_button":
                self.__style_lock = 1 if self.__style_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_shape_lock_button":
                self.__shape_lock = 1 if self.__shape_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_complexity_lock_button":
                self.__complexity_lock = 1 if self.__complexity_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_size_lock_button":
                self.__size_lock = 1 if self.__size_lock == 0 else 0

        if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_object_id == "layer_"+num_of_layer+"_style_dropdown":
                self.__style = event.text
            if event.ui_object_id == "layer_"+num_of_layer+"_shape_dropdown":
                self.__shape = event.text

        if event.user_type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_object_id == "layer_"+num_of_layer+"_complexity_slider":
                self.__complexity = event.value
            if event.ui_object_id == "layer_"+num_of_layer+"_size_slider":
                self.__size = event.value


    def draw_canvas(self):
        """! Draw the layer to self.layer based on the current widget settings. """

        self.clean_layer()
        self.layer.set_colorkey((0, 0, 0))

        color_palette = widgets.color_palette.get_foreground_colors()

        if _art_shapes_list[0] == self.__shape:
            line_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)

        if _art_shapes_list[1] == self.__shape:
            circle_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)

        if _art_shapes_list[2] == self.__shape:
            square_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)

        if _art_shapes_list[3] == self.__shape:
            hpolygons_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)

        if _art_shapes_list[4] == self.__shape:
            fpolygons_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)

        if _art_shapes_list[5] == self.__shape:
            dots_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)

        if _art_shapes_list[6] == self.__shape:
            curves_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)

        if _art_shapes_list[7] == self.__shape:
            ring_generator.draw(self.layer, self.__complexity, color_palette, self.__style, self.__size)


    def clean_layer(self):
        """! Clean the layer by setting it to be blank and see-through. """
        self.layer.fill((0, 0, 0, 0))

    def get_layer_style(self):
        """! @return The layer style. """
        return self.__style
    def get_layer_shape(self):
        """! @return The layer shape. """
        return self.__shape
    def get_layer_complexity(self):
        """! @return The layer complexity. """
        return self.__complexity
    def get_layer_size(self):
        """! @return The layer size. """
        return self.__size