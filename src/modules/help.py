##
# @file help.py
#
# @brief Defines the help class.
#
# @section author_help Author(s)
# - Created by Jessica Dawson on 03/16/2022.

# Imports
import pygame_gui as pgui
import pygame as pg

from modules.widget import widget
import assets

class help(widget):
    """! The help widget class.

    Displays a ui help button that displays the program instructions when clicked.
    """

    def __init__(self, x, y, window, ui_manager):
        """! Initializes the help widget.

        @param x                Horizontal position to draw the widget at on the ui.
        @param y                Vertical position to draw the widget at on the ui.
        @param window           Ui window to draw the widget to.
        @param ui_manager       Pygame_gui element manager to tie pygame_gui elements to.
        """

        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager

        self.__help_opt = 0
        self.__help_left = False


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui elements for the help widget.
        
        Draws a dialog with the instructions for using the program.
        """
        if self.__help_opt == 0:
            return
        
        if self.__help_left:
            pg.draw.rect(self.__window, pg.Color("#2B2834"), (self.__x - 510, self.__y, 510, 380))
            p = [self.__x - 500, self.__y+10]
        else:
            pg.draw.rect(self.__window, pg.Color("#2B2834"), (self.__x+100, 90, 510, 380))
            p = [self.__x + 110, self.__y+10]
        c, s = [255, 255, 255], 12     # Color, Position, Font-size
        ri = 12     # Row interval
        assets.text_to_screen(self.__window, "Thanks for trying out my program! Let me help you with how the program works.", c, p, s)
        p = [p[0], p[1]+ri+10]
        assets.text_to_screen(self.__window, "Left side contains the art generation options, we have two layers that can be in different", c, p, s)
        p = [p[0], p[1]+ri]
        assets.text_to_screen(self.__window, "styles, different shapes, different complexities and different sizes. For example a layer", c, p, s)
        p = [p[0], p[1]+ri]
        assets.text_to_screen(self.__window, "with 'Cornered' 'Circles' options, will generate circles that are roughly cornered.", c, p, s)
        p = [p[0], p[1]+ri+10]
        assets.text_to_screen(self.__window, "Random values have a big part in my program to make the possibilities endless", c, p, s)
        p = [p[0], p[1]+ri]
        assets.text_to_screen(self.__window, "If you like a setting and want to keep it but randomize other settings, you can just click", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "on the small buttons right next to the options to 'Lock' them for generating randomly.", c, p, s)
        p = [p[0], p[1] + ri+10]
        c = pg.Color("#DFD6FF")
        assets.text_to_screen(self.__window, "Generate Button: Generates art with the options specified in the options panel.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Generate Randomly Button: Generates art by randomizing the options on the left.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Export Button: Opens a file dialog and let's you export a png of your art in 4k quality.", c, p, s)
        p = [p[0], p[1] + ri+10]
        c = [255, 255, 255]
        assets.text_to_screen(self.__window, "Overlay options don't change by randomizing or generating new art with adjusting the options.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "And you can try new overlays with existing art. ", c, p, s)
        p = [p[0], p[1] + ri+10]
        assets.text_to_screen(self.__window, "There are 20 unique color palettes, and there are seven style options with eight shape options.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Shapes are self explanatory but let's take a look at the styles:", c, p, s)
        p = [p[0], p[1] + ri+5]
        c = pg.Color("#DFD6FF")
        assets.text_to_screen(self.__window, "Chaotic - The most randomized option.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Striped Horizontal - Whatever the shape is, the shapes roughly line up in horizontal lines", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Striped Vertical - Same with striped horizontal but it's vertical.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Mosaic - The selected shape will cover the canvas with equal amount of spacing between them.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Cornered - Forces the randomizer to make the shapes appear roughly on the corners.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Centered - Forces the randomizer to make the shapes appear roughlt on the center.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Empty - Doesn't draw any shapes to the layer. Sometimes one shape is enough for the art.", c, p, s)
        p = [p[0], p[1] + ri+10]
        c = [255, 255, 255]
        assets.text_to_screen(self.__window, "Complexity adjusts how many shapes will be drawn, it's more absolute than the size option.", c, p, s)
        p = [p[0], p[1] + ri]
        assets.text_to_screen(self.__window, "Size option adjusts how large the shapes 'can' be. Size is still more randomized for variety.", c, p, s)
        p = [p[0], p[1] + ri+10]
        c = pg.Color("#DFD6FF")
        assets.text_to_screen(self.__window, "ENJOY!", c, p, s)


    def draw_ui_static(self):
        """! Draws the static ui elements for the help widget.
        
        Draws a button with "help" written on it.
        """
        __help_opt_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.__x, self.__y, 100, 30), text="HELP", manager=self.__ui_manager,
                                            object_id="help_opt_button")


    def events(self, event):
        """! Processes pygame events for the help widget.
        
        If event in the help button being pressed display the instructions dialog.

        @param event    The pygame event being processed.
        """
        if event.user_type == pgui.UI_BUTTON_PRESSED and event.ui_object_id == "help_opt_button":
            self.__help_opt = 1 if self.__help_opt == 0 else 0