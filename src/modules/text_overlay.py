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

_fonts = [
    "Basic-Regular"
]


class text_overlay(widget):
    """! The layer widget class.

    Provides a ui and functionality to specify a drawing algorithm and draw to a pygame surface.
    """
    
    def __init__(self, x, y, window, ui_manager):
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

        #starting options for dropdown menus
        self.__font = choice(_fonts)
        self.__size = randint(75, 600)
        self.__pos = [randint(0,3840), randint(0, 2160)]
        self.__color = choice(widgets.color_palette.get_foreground_colors())
        self.__text = ""


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the layer widget.
        
        Draws the text and lock icons.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 30

        pg.draw.rect(self.__window, pg.Color("#2B2834"), (self.__x, self.__y, 252, 190))

        assets.text_to_screen(window=self.__window, text="TEXT OVERLAY", color=assets.ui_h1_color, pos=(interactables_margin, self.__y+15), font_size=18)
        assets.text_to_screen(window=self.__window, text="TEXT SIZE", color=assets.ui_color, pos=(interactables_margin, self.__y+60), font_size=14)
        assets.text_to_screen(window=self.__window, text="X", color=assets.ui_color, pos=(lock_margin, self.__y+105), font_size=14)
        assets.text_to_screen(window=self.__window, text="Y", color=assets.ui_color, pos=(lock_margin, self.__y+130), font_size=14)


    def draw_ui_static(self):
        """! Draws the static ui elements for the layer widget.
        
        Draws the shape and style dropdowns, the complexity and size sliders, and lock button.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 6

        font_dropdown = pgui.elements.UIDropDownMenu(options_list=_fonts,
                                                    starting_option=self.__font,
                                                    relative_rect=pg.Rect(interactables_margin, self.__y+30, 200, 22), manager=self.__ui_manager,
                                                    object_id="font_dropdown")

        size_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+75, 200, 22),
                                                                start_value=self.__size, value_range=(75, 600),
                                                                manager=self.__ui_manager, object_id="size_slider")

        x_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+100, 200, 22),
                                                                    start_value=self.__pos[0],
                                                                    value_range=(0,3840), manager=self.__ui_manager,
                                                                    object_id="x_slider")

        y_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+125, 200, 22),
                                                                start_value=self.__pos[1], value_range=(0, 2160),
                                                                manager=self.__ui_manager, object_id="y_slider")

        text_entry = pgui.elements.UITextEntryLine(relative_rect=pg.Rect(interactables_margin, self.__y+150, 200, 30), manager=self.__ui_manager,
                                                    object_id="text_entry")


    def events(self, event):
        """! Processes pygame events for the layer widget.
        
        Handles the shape and style dropdowns, the complexity and size sliders, and lock button.

        @param event    The pygame event being processed.
        """

        if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_object_id == "font_dropdown":
                self.__font = event.text
                self.text_to_canvas()

        if event.user_type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_object_id == "size_slider":
                self.__size = event.value
                self.text_to_canvas()
            if event.ui_object_id == "x_slider":
                self.__pos[0] = event.value
                self.text_to_canvas()
            if event.ui_object_id == "y_slider":
                self.__pos[1] = event.value
                self.text_to_canvas()

        if event.user_type == pgui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_object_id == "text_entry":
                self.__text = event.text

        if event.user_type == pgui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_object_id == "text_entry":
                self.text_to_canvas()


    def draw_canvas(self):
        """! Draw the layer to self.layer based on the current widget settings. """

        self.__color = choice(widgets.color_palette.get_foreground_colors())
        self.text_to_canvas()


    def text_to_canvas(self):
        self.clean_layer()
        
        font_used = pg.freetype.Font(self.__font + ".ttf", self.__size)
        font_used.render_to(self.layer, self.__pos, self.__text, self.__color)


    def clean_layer(self):
        """! Clean the layer by setting it to be blank and see-through. """
        self.layer.fill((0, 0, 0, 0))
