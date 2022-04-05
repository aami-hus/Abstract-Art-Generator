##
# @file overlay.py
#
# @brief Defines the overlay class.
#
# @section author_overlay Author(s)
# - Created by Jessica Dawson on 03/17/2022.

# Imports
import pygame_gui as pgui
import pygame as pg
from random import randint, choice

from modules.widget import widget
from widget_storage import widgets
import assets

_overlays = [
    "assets/overlay1.png",
    "assets/overlay2.png",
    "assets/overlay3.png",
    "assets/overlay4.png",
    "assets/overlay5.png",
    "assets/overlay6.png"
]

class overlay(widget):
    """! The overlay widget class.

    Provides a ui and functionality to specify an overlay and draw to a pygame surface.
    """
    
    def __init__(self, x, y, window, ui_manager):
        """! Initializes the overlay widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        ## The pygame surface the overlay draws to.
        self.overlay_layer = pg.Surface((3840, 2160), pg.SRCALPHA)
        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager
        
        self.color = "#2B2834"
        self.ui_h1_color = "#FFFFFF"

        self.__active_overlay = 0
        self.__active_color = assets.active_color
        self.__inactive_color = assets.inactive_color

        self.__overlays = [pg.image.load(o).convert_alpha() for o in _overlays]


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the overlay widget.
        
        Draws the text and overlay thumbnails.
        """
        
        pg.draw.rect(self.__window, pg.Color(self.color), (self.__x, self.__y, 210, 350))

        assets.text_to_screen(window=self.__window, text="OVERLAY/BORDER", color=self.ui_h1_color, pos=(self.__x+15, self.__y+12), font_size=18)

        pg.draw.rect(self.__window, self.__active_color if self.__active_overlay == 1 else self.__inactive_color, (self.__x+13, self.__y+38, 84, 49), 1)
        pg.draw.rect(self.__window, self.__active_color if self.__active_overlay == 2 else self.__inactive_color, (self.__x+113, self.__y+38, 84, 49), 1)
        pg.draw.rect(self.__window, self.__active_color if self.__active_overlay == 3 else self.__inactive_color, (self.__x+13, self.__y+118, 84, 49), 1)
        pg.draw.rect(self.__window, self.__active_color if self.__active_overlay == 4 else self.__inactive_color, (self.__x+113, self.__y+118, 84, 49), 1)
        pg.draw.rect(self.__window, self.__active_color if self.__active_overlay == 5 else self.__inactive_color, (self.__x+13, self.__y+198, 84, 49), 1)
        pg.draw.rect(self.__window, self.__active_color if self.__active_overlay == 6 else self.__inactive_color, (self.__x+113, self.__y+198, 84, 49), 1)
        pg.draw.rect(self.__window, self.__active_color if self.__active_overlay == 0 else self.__inactive_color, (self.__x+63, self.__y+278, 84, 49), 1)

        self.__window.blit(pg.transform.scale(self.__overlays[0], (80, 45)), (self.__x+15, self.__y+40))
        self.__window.blit(pg.transform.scale(self.__overlays[1], (80, 45)), (self.__x+115, self.__y+40))
        self.__window.blit(pg.transform.scale(self.__overlays[2], (80, 45)), (self.__x+15, self.__y+120))
        self.__window.blit(pg.transform.scale(self.__overlays[3], (80, 45)), (self.__x+115, self.__y+120))
        self.__window.blit(pg.transform.scale(self.__overlays[4], (80, 45)), (self.__x+15, self.__y+200))
        self.__window.blit(pg.transform.scale(self.__overlays[5], (80, 45)), (self.__x+115, self.__y+200))



    def change_colors(self):
        self.color = "#AAB1B6" if self.color=="#2B2834" else "#2B2834"
        self.ui_h1_color = "#000000" if self.ui_h1_color=="#FFFFFF" else "#FFFFFF"

    def draw_ui_static(self):
        """! Draws the static ui elements for the overlay widget.
        
        Draws the overlay selection buttons.
        """

        overlay1_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x+48, self.__y+90, 14, 14), text="", manager=self.__ui_manager,
                                             object_id="overlay1_button")
        overlay2_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x+148, self.__y+90, 14, 14), text="", manager=self.__ui_manager,
                                                object_id="overlay2_button")
        overlay3_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x+48, self.__y+170, 14, 14), text="", manager=self.__ui_manager,
                                                object_id="overlay3_button")
        overlay4_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x+148, self.__y+170, 14, 14), text="", manager=self.__ui_manager,
                                                object_id="overlay4_button")
        overlay5_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x+48, self.__y+250, 14, 14), text="", manager=self.__ui_manager,
                                                object_id="overlay5_button")
        overlay6_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x+148, self.__y+250, 14, 14), text="", manager=self.__ui_manager,
                                                object_id="overlay6_button")
        overlay7_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x+98, self.__y+330, 14, 14), text="", manager=self.__ui_manager,
                                                object_id="overlay7_button")


    def events(self, event):
        """! Processes pygame events for the overlay widget.
        
        Handles the overlay selection buttons.

        @param event    The pygame event being processed.
        """
        if event.user_type == pgui.UI_BUTTON_PRESSED:
            if event.ui_object_id == "overlay1_button":
                self.__active_overlay = 1
                self.draw_canvas()
            if event.ui_object_id == "overlay2_button":
                self.__active_overlay = 2
                self.draw_canvas()
            if event.ui_object_id == "overlay3_button":
                self.__active_overlay = 3
                self.draw_canvas()
            if event.ui_object_id == "overlay4_button":
                self.__active_overlay = 4
                self.draw_canvas()
            if event.ui_object_id == "overlay5_button":
                self.__active_overlay = 5
                self.draw_canvas()
            if event.ui_object_id == "overlay6_button":
                self.__active_overlay = 6
                self.draw_canvas()
            if event.ui_object_id == "overlay7_button":
                self.__active_overlay = 0
                self.clean_layer()

            return 1

        return 0


    def draw_canvas(self):
        """! Draw the currently selected overlay image to self.overlay_layer. """
        self.clean_layer()
        self.overlay_layer.blit(self.__overlays[self.__active_overlay-1], (0, 0))


    def clean_layer(self):
        """! Clean the overlay by setting it to be blank and see-through. """
        self.overlay_layer.fill((0, 0, 0, 0))
    
    def get_active_overlay(self):
        return self.__active_overlay

    # def generate_overlay_fg(self, overlay):
    #     self.clean_layer(self.overlay_layer)
    #     self.overlay_layer.blit(overlay, (0, 0))
    #     self.blit_to_canvas([l1,l2,l3])