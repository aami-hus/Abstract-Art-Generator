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

        ## Theme color for background
        self.color = "#2B2834"
        ## Theme color for text
        self.u1_h1_color = "#FFFFFF"

        #starting options for dropdown menus
        ## The style or pattern the layer draws in
        self.style = choice(_art_styles_list)
        ## The shape the layer draws
        self.shape = choice(_art_shapes_list)
        ## The complexity of the layer's drawing
        self.complexity = randint(10,30)#15
        ## The size of the drawn shapes
        self.size = [51, randint(51,400)] #400
        ## The transparency of the layer
        self.transparency = randint(0, 255)

        #locks
        ## 1 if radomization of the style is locked, 0 otherwise
        self.style_lock = 0
        ## 1 if radomization of the shape is locked, 0 otherwise
        self.shape_lock = 0
        ## 1 if radomization of the complexity is locked, 0 otherwise
        self.complexity_lock = 0
        ## 1 if radomization of the size is locked, 0 otherwise
        self.size_lock = 0
        ## 1 if radomization of the transparency is locked, 0 otherwise
        self.transparency_lock = 0


    def change_colors(self):
        """! Change the theme colors. """
        self.color = "#AAB1B6" if self.color=="#2B2834" else "#2B2834"
        self.u1_h1_color = "#000000" if self.u1_h1_color=="#FFFFFF" else "#FFFFFF"


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the layer widget.
        
        Draws the text and lock icons.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 17

        # pg.draw.rect(self.__window, pg.Color("#2B2834"), (self.__x, self.__y, 252, 220))
        pg.draw.rect(self.__window, pg.Color(self.color), (self.__x, self.__y, 252, 220))
        
        if self.style_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+30))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+30))

        if self.shape_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+55))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+55))

        if self.complexity_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+100))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+100))

        if self.size_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+145))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+145))
        
        if self.transparency_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+190))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+190))

        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " STYLE", color=self.u1_h1_color, pos=(interactables_margin, self.__y+10), font_size=18)
        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " COMPLEXITY", color=self.u1_h1_color, pos=(interactables_margin, self.__y+85), font_size=14)
        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " SHAPE SIZE", color=self.u1_h1_color, pos=(interactables_margin, self.__y+130), font_size=14)
        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " TRANSPARENCY", color=self.u1_h1_color, pos=(interactables_margin, self.__y+175), font_size=14)


    def draw_ui_static(self):
        """! Draws the static ui elements for the layer widget.
        
        Draws the shape and style dropdowns, the complexity and size sliders, and lock button.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 6
        num_of_layer = self.__layer_num.lower()

        style_dropdown = pgui.elements.UIDropDownMenu(options_list=_art_styles_list,
                                                                starting_option=self.style,
                                                                relative_rect=pg.Rect(interactables_margin, self.__y+30, 200, 22), manager=self.__ui_manager,
                                                                object_id="layer_"+num_of_layer+"_style_dropdown")

        shape_dropdown = pgui.elements.UIDropDownMenu(options_list=_art_shapes_list,
                                                                starting_option=self.shape,
                                                                relative_rect=pg.Rect(interactables_margin, self.__y+55, 200, 22), manager=self.__ui_manager,
                                                                object_id="layer_"+num_of_layer+"_shape_dropdown")

        complexity_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+100, 200, 22),
                                                                    start_value=self.complexity,
                                                                    value_range=(10, 30), manager=self.__ui_manager,
                                                                    object_id="layer_"+num_of_layer+"_complexity_slider")

        size_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+145, 200, 22),
                                                                start_value=self.size[1], value_range=(50, 400),
                                                                manager=self.__ui_manager, object_id="layer_"+num_of_layer+"_size_slider")
        
        transparency_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+190, 200, 22),
                                                                start_value=self.transparency, value_range=(0, 255),
                                                                manager=self.__ui_manager, object_id="layer_"+num_of_layer+"_transparency_slider")

        # "lock_button_three" changed to "layer_one_lock_butter"
        # etc, 4 = layer 1 shape, 5 = layer 1 complex, 6 = layer 1 size
        # repeat for layer 2 and 3
        style_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+37, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_style_lock_button")
        shape_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+62, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_shape_lock_button")
        complexity_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+107, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_complexity_lock_button")
        size_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+152, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_size_lock_button")
        transparency_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+197, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_transparency_lock_button")


    def randomize(self):
        """! Randomize the shape, style, complexity, and size of the layer drawing algorithm. """

        if self.style_lock == 0:
            self.style = choice(_art_styles_list)
        if self.shape_lock == 0:
            self.shape = choice(_art_shapes_list)
        if self.complexity_lock == 0:
            self.complexity = randint(10,30)
        if self.size_lock == 0:
            self.size[1] = randint(51, 400)
        if self.transparency_lock == 0:
            self.transparency = randint(0, 255)


    def events(self, event):
        """! Processes pygame events for the layer widget.
        
        Handles the shape and style dropdowns, the complexity and size sliders, and lock button.

        @param event    The pygame event being processed.
        """

        num_of_layer = self.__layer_num.lower()

        if event.user_type == pgui.UI_BUTTON_PRESSED:
            if event.ui_object_id == "layer_"+num_of_layer+"_style_lock_button":
                self.style_lock = 1 if self.style_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_shape_lock_button":
                self.shape_lock = 1 if self.shape_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_complexity_lock_button":
                self.complexity_lock = 1 if self.complexity_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_size_lock_button":
                self.size_lock = 1 if self.size_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_transparency_lock_button":
                self.transparency_lock = 1 if self.transparency_lock == 0 else 0

        if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_object_id == "layer_"+num_of_layer+"_style_dropdown":
                self.style = event.text
            if event.ui_object_id == "layer_"+num_of_layer+"_shape_dropdown":
                self.shape = event.text

        if event.user_type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_object_id == "layer_"+num_of_layer+"_complexity_slider":
                self.complexity = event.value
            if event.ui_object_id == "layer_"+num_of_layer+"_size_slider":
                self.size[1] = event.value
            if event.ui_object_id == "layer_"+num_of_layer+"_transparency_slider":
                self.transparency = event.value

        return 0


    def draw_canvas(self):
        """! Draw the layer to self.layer based on the current widget settings. """

        self.clean_layer()
        self.layer.set_colorkey((0, 0, 0))

        color_palette = widgets.color_palette.get_foreground_colors()

        if _art_shapes_list[0] == self.shape:
            widgets.generators.draw_lines(self.layer, self.complexity, color_palette, self.style, self.size)

        if _art_shapes_list[1] == self.shape:
            widgets.generators.draw_circles(self.layer, self.complexity, color_palette, self.style, self.size)

        if _art_shapes_list[2] == self.shape:
            widgets.generators.draw_squares(self.layer, self.complexity, color_palette, self.style, self.size)

        if _art_shapes_list[3] == self.shape:
            widgets.generators.draw_hpolygons(self.layer, self.complexity, color_palette, self.style, self.size)

        if _art_shapes_list[4] == self.shape:
            widgets.generators.draw_fpolygons(self.layer, self.complexity, color_palette, self.style, self.size)

        if _art_shapes_list[5] == self.shape:
            widgets.generators.draw_dots(self.layer, self.complexity, color_palette, self.style, self.size)

        if _art_shapes_list[6] == self.shape:
            widgets.generators.draw_curves(self.layer, self.complexity, color_palette, self.style, self.size)

        if _art_shapes_list[7] == self.shape:
            widgets.generators.draw_rings(self.layer, self.complexity, color_palette, self.style, self.size)

        self.layer.set_alpha(self.transparency)


    def clean_layer(self):
        """! Clean the layer by setting it to be blank and see-through. """
        self.layer.fill((0, 0, 0, 0))

    def get_layer_style(self):
        """! @return The layer style. """
        return self.style
    def get_layer_shape(self):
        """! @return The layer shape. """
        return self.shape
    def get_layer_complexity(self):
        """! @return The layer complexity. """
        return self.complexity
    def get_layer_size(self):
        """! @return The layer size. """
        return self.size
    def get_layer_transparency(self):
        """! @return The layer transparency"""
        return self.transparency
