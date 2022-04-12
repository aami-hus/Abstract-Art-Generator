##
# @file text_overlay.py
#
# @brief Defines the text_overlay class.
#
# @section author_text_overlay Author(s)
# - Created by Jessica Dawson on 03/22/2022.

# Imports
import pygame_gui as pgui
import pygame as pg
from random import randint, choice

from modules.widget import widget
from widget_storage import widgets
import assets

_fonts = [
    "Basic",
    "Bauhaus",
    "Dearlove",
    "LemonMilk",
    "Blanka",
    "Balloon"
]


class text_overlay(widget):
    """! The text overlay widget class.

    Provides a ui and functionality to specify text to be drawn to a pygame surface.
    """
    
    def __init__(self, x, y, window, ui_manager):
        """! Initializes the text overlay widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        ## The pygame surface the text overlay draws to.
        self.layer = pg.Surface((3840, 2160), pg.SRCALPHA)
        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager

        ## Theme color for background
        self.bg_color = "#2B2834"
        ## Theme color for text
        self.ui_h1_color = "#FFFFFF"
        ## Theme color for smaller text
        self.ui_color = "#DFD6FF"

        #starting options for dropdown menus
        ## The font used to draw text
        self.font = choice(_fonts)
        ## The size of the text
        self.size = randint(75, 600)
        ## The x and y position of the text on the canvas
        self.pos = [randint(0,3840), randint(0, 2160)]
        ## The color to draw the text with
        self.color = choice(widgets.color_palette.get_foreground_colors())
        ## The text to draw
        self.text = ""


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the text overlay widget.
        
        Draws the text.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 30

        pg.draw.rect(self.__window, pg.Color(self.bg_color), (self.__x, self.__y, 252, 190))

        assets.text_to_screen(window=self.__window, text="TEXT OVERLAY", color=self.ui_h1_color, pos=(interactables_margin, self.__y+15), font_size=18)
        assets.text_to_screen(window=self.__window, text="TEXT SIZE", color=self.ui_color, pos=(interactables_margin, self.__y+60), font_size=14)
        assets.text_to_screen(window=self.__window, text="X", color=self.ui_color, pos=(lock_margin, self.__y+105), font_size=14)
        assets.text_to_screen(window=self.__window, text="Y", color=self.ui_color, pos=(lock_margin, self.__y+130), font_size=14)

    def change_colors(self):
        """! Change the theme colors. """
        self.bg_color = "#AAB1B6" if self.bg_color=="#2B2834" else "#2B2834"
        self.ui_h1_color = "#000000" if self.ui_h1_color=="#FFFFFF" else "#FFFFFF"
        self.ui_color = "#2B2B2B" if self.ui_color == "#DFD6FF" else "#DFD6FF"

    def draw_ui_static(self):
        """! Draws the static ui elements for the text overlay widget.
        
        Draws the font dropdown, size and position sliders, and the text entry box.
        """

        interactables_margin = self.__x + 42
        lock_margin = self.__x + 6

        font_dropdown = pgui.elements.UIDropDownMenu(options_list=_fonts,
                                                    starting_option=self.font,
                                                    relative_rect=pg.Rect(interactables_margin, self.__y+30, 200, 22), manager=self.__ui_manager,
                                                    object_id="font_dropdown")

        size_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+75, 200, 22),
                                                                start_value=self.size, value_range=(75, 600),
                                                                manager=self.__ui_manager, object_id="size_slider")

        x_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+100, 200, 22),
                                                                    start_value=self.pos[0],
                                                                    value_range=(0,3840), manager=self.__ui_manager,
                                                                    object_id="x_slider")

        y_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+125, 200, 22),
                                                                start_value=self.pos[1], value_range=(0, 2160),
                                                                manager=self.__ui_manager, object_id="y_slider")

        text_entry = pgui.elements.UITextEntryLine(relative_rect=pg.Rect(interactables_margin, self.__y+150, 200, 30), manager=self.__ui_manager,
                                                    object_id="text_entry")


    def events(self, event):
        """! Processes pygame events for the text overlay widget.
        
        Handles the font dropdown, size and position sliders, and the text entry box.

        @param event    The pygame event being processed.
        """

        r = 0

        if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_object_id == "font_dropdown":
                self.font = event.text
                self.text_to_canvas()
                r = 1

        if event.user_type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_object_id == "size_slider":
                self.size = event.value
                self.text_to_canvas()
                r = 1
            if event.ui_object_id == "x_slider":
                self.pos[0] = event.value
                self.text_to_canvas()
                r = 1
            if event.ui_object_id == "y_slider":
                self.pos[1] = event.value
                self.text_to_canvas()
                r = 1

        if event.user_type == pgui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_object_id == "text_entry":
                self.text = event.text

        if event.user_type == pgui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_object_id == "text_entry":
                self.draw_canvas()
                r = 1

        return r


    def draw_canvas(self):
        """! Randomizes the text color and draws text to self.layer based on the current widget settings. """

        self.color = choice(widgets.color_palette.get_foreground_colors())
        self.text_to_canvas()


    def text_to_canvas(self):
        """! Draws text to self.layer based on the current widget settings. """
        self.clean_layer()
        
        font_used = pg.freetype.Font("fonts/" + self.font + ".ttf", self.size)
        font_used.render_to(self.layer, self.pos, self.text, self.color)


    def clean_layer(self):
        """! Clean the layer by setting it to be blank and see-through. """
        self.layer.fill((0, 0, 0, 0))
