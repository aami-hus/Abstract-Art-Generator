##
# @file switch_theme.py
#
# @brief Defines the switch theme class.
#
# @section author_theme Author(s)
# - Created by Fady Morcos on 04/04/2022.

# Imports
import pygame_gui as pgui
import pygame as pg

from modules.widget import widget
import assets

class switch_theme(widget):
    """! The theme switch widget class.

    Displays a ui switch theme button that changes the interface theme when clicked.
    """

    def __init__(self, x, y, window, ui_manager):
        """! Initializes the theme widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager

        ## True if in dark mode, False if in light
        self.switch_theme_dark = True


        

    def getDarkMode(self):
        """! @return True if in dark mode, False if in light mode. """
        return self.switch_theme_dark

    def draw_ui_static(self):
        """! Draws the static ui elements for the theme widget.
        
        Draws a button with "theme" written on it.
        """
        __switch_theme_opt_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x, self.__y, 100, 30), text="THEME", manager=self.__ui_manager,
                                            object_id="switch_theme_opt_button")


    def events(self, event):
        """! Processes pygame events for the theme widget.
        
        If event is the switch theme button being pressed change the interface theme.

        @param event    The pygame event being processed.
        """
        if event.user_type == pgui.UI_BUTTON_PRESSED and event.ui_object_id == "switch_theme_opt_button":
            self.switch_theme_dark = (self.switch_theme_dark != True)
            return True
            