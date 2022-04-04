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


class overlay(widget):
    """! The overlay widget class.

    Provides a ui and functionality to specify an overlay and draw to a pygame surface.
    """
    
    def __init__(self, x, y, window, ui_manager, overlays):
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
        self.__overlays = overlays
        
        self.color = "#2B2834"
        self.ui_h1_color = "#FFFFFF"

        self.__active_overlay = 0
        self.__active_color = assets.active_color
        self.__inactive_color = assets.inactive_color


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the overlay widget.
        
        Draws the text and overlay thumbnails.
        """

        pg.draw.rect(self.__window, pg.Color(self.color), (self.__x, self.__y, 210, 350))

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
        self.color = "#eeeeee" if self.color=="#2B2834" else "#2B2834"
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
        #if event.user_type == pgui.UI_BUTTON_PRESSED:
        if event.ui_object_id == "overlay1_button":
            self.__active_overlay = 1
            #c1.generate_fg(assets.overlays[0])
        if event.ui_object_id == "overlay2_button":
            self.__active_overlay = 2
            #c1.generate_fg(assets.overlays[1])
        if event.ui_object_id == "overlay3_button":
            self.__active_overlay = 3
            #c1.generate_fg(assets.overlays[2])
        if event.ui_object_id == "overlay4_button":
            self.__active_overlay = 4
            #c1.generate_fg(assets.overlays[3])
        if event.ui_object_id == "overlay5_button":
            self.__active_overlay = 5
            #c1.generate_fg(assets.overlays[4])
        if event.ui_object_id == "overlay6_button":
            self.__active_overlay = 6
            #c1.generate_fg(assets.overlays[5])
        if event.ui_object_id == "overlay7_button":
            self.__active_overlay = 0
        # c1.clean_layer(c1.fg_layer)
            #c1.blit_to_canvas([l1, l2, l3])


    def draw_canvas(self):
        """! Draw the currently selected overlay image to self.overlay_layer. """
        pass


    def clean_layer(self):
        """! Clean the overlay by setting it to be blank and see-through. """
        self.layer.fill((0, 0, 0, 0))
    
    def get_active_overlay(self):
        return self.__active_overlay

    # def generate_overlay_fg(self, overlay):
    #     self.clean_layer(self.overlay_layer)
    #     self.overlay_layer.blit(overlay, (0, 0))
    #     self.blit_to_canvas([l1,l2,l3])