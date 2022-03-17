##
# @file ui_controller.py
#
# @brief Defines and initializes the ui_controller class.
#
# @section author_sensors Author(s)
# - Created by Jessica Dawson on 03/16/2022.

# Imports
import pygame as pg
import pygame_gui as pgui
from tkinter import *
from tkinter.filedialog import asksaveasfilename

from canvas import canvas
from widget_storage import widgets
from modules.color_palette import color_palette
from modules.help import help
import assets

class ui_controller:
    """! The ui_controller class.

    A high level class that calls all other modules.
    Orchestrates pygame event handling, ui drawing, art generation, setting randomization, and art exporting.
    """

    ## Possible canvas export resolutions.
    resolutions_list = [
        "4K: 3840x2160",
        "Full HD: 1920x1080",
        "HD: 1280x720"
    ]
    ## Current canvas export resolution.
    export_resolution = resolutions_list[0]

    ## Application window width.
    SW = 1280
    ## Application window height
    SH = 720

    # general menu locations
    ui_menus_left = 18
    ui_menus_right = SW-270

    # positions of widgets
    palette_pos = (ui_menus_right, 60)
    layer_one_pos = (ui_menus_left, 60)
    layer_two_pos = (ui_menus_left, layer_one_pos[1]+200)
    layer_three_pos = (ui_menus_left, layer_two_pos[1]+200)
    overlay_pos = (0, palette_pos[1]+155)
    help_pos = (284, 60)

    # canvas settings
    canvas_size = (3840, 2160)
    canvas_display_size = (int(SW//1.8), int(SH//1.8))
    canvas_pos = ((SW - canvas_display_size[0])//2, (SH - canvas_display_size[1])//2)


    def __init__(self):
        """! Initializes ui_controller.
        
        Initializes pygame, the application window, the canvas, and all widgets.
        """
        pg.init()
        
        self.__create_window()

        self.canvas = canvas(self.canvas_pos[0], self.canvas_pos[1], self.canvas_size[0], self.canvas_size[1],
                            self.canvas_display_size[0], self.canvas_display_size[1], self.window)

        self.__initialize_widgets()

        self.isrunning = True


    def __create_window(self):
        self.window = pg.display.set_mode((self.SW, self.SH))
        pg.display.set_caption("Abstract Art Generator")
        pg.display.set_icon(assets.logo)
        self.ui_manager = pgui.UIManager((self.SW, self.SH))


    def __initialize_widgets(self):
        widgets.color_palette = color_palette(self.palette_pos[0], self.palette_pos[1], self.window, self.ui_manager)
        widgets.help = help(self.help_pos[0], self.help_pos[1], self.window, self.ui_manager)


    def process_events(self):
        """! Processes pygame events.
        
        Handles generation and export controls itself and calls events() in widgets for all other event processing.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.isrunning = False
                break

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.isrunning = False
                    break

            if event.type == pg.USEREVENT:
                if event.user_type == pgui.UI_BUTTON_PRESSED:
                    if event.ui_object_id == "generate_button":

                        self.canvas.draw_to_canvas()

                    if event.ui_object_id == "random_generate_button":
                        widgets.color_palette.randomize()

                        self.draw_ui_static()
                        
                        self.canvas.draw_to_canvas()
                        pass
                        
                    if event.ui_object_id == "export_art_button":
                        self.export_art()

                widgets.color_palette.events(event)
                widgets.help.events(event)

            self.ui_manager.process_events(event)


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui.
        
        Draws background color and some text itself and calls canvas and widgets for all other drawing.
        """
        self.window.fill(assets.background_color)

        self.canvas.draw()

        assets.text_to_screen(window=self.window, text="ABSTRACT ART GENERATOR", color=assets.ui_h1_color, pos=(430, 35), font_size=40)
        assets.text_to_screen(window=self.window, text="LAYERS", color=assets.ui_h1_color, pos=(self.layer_one_pos[0] + 42,
                            self.layer_one_pos[1]-25), font_size=24)
        assets.text_to_screen(window=self.window, text="RESOLUTION", color=assets.ui_color, pos=(self.SW-240, 560+20), font_size=14)

        widgets.color_palette.draw_ui_dynamic()
        widgets.help.draw_ui_dynamic()


    def draw_ui_static(self):
        """! Draws the static ui.
        
        Draws generation and export controls itself and calls widgets for all other drawing.
        """
        self.ui_manager.clear_and_reset()

        widgets.color_palette.draw_ui_static()
        widgets.help.draw_ui_static()

        resolution_dropdown = pgui.elements.UIDropDownMenu(options_list=self.resolutions_list,
                                                starting_option=self.export_resolution,
                                                relative_rect=pg.Rect(self.SW-240, 575+20, 200, 22), manager=self.ui_manager,
                                                object_id = "resolution_dropdown")

        export_art_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.SW - 240, self.SH - 100, 200, 50),
                                                text="Export", manager=self.ui_manager, object_id="export_art_button")

        generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.SW // 2 - 200, self.SH - 100, 200, 50),
                                                text="Generate", manager=self.ui_manager, object_id="generate_button")

        random_generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.SW // 2, self.SH - 100, 200, 50),
                                                text="Generate Randomly", manager=self.ui_manager,
                                                object_id="random_generate_button")


    def export_art(self):
        """! Exports the canvas to a png image. """
        tkinter_window = Tk()
        tkinter_window.withdraw()

        available_formats = [("Portable Network Graphics", "*.png")]
        filename = asksaveasfilename(title="Export File", filetypes=available_formats)

        if filename:
            path = filename[:]
            if self.__export_resolution == self.resolutions_list[0]:
                pg.image.save(self.canvas.get_canvas(), path + ".png")
            elif self.__export_resolution == self.resolutions_list[1]:
                pg.image.save(pg.transform.smoothscale(self.canvas.get_canvas(), (1920, 1080)), path + ".png")
            elif self.__export_resolution == self.resolutions_list[2]:
                pg.image.save(pg.transform.smoothscale(self.canvas.get_canvas(), (1280, 720)), path + ".png")
        else:
            pass


    def run(self):
        """! Main loop.

        Draws static ui then enters loop where it processes events and draws the dynamic ui.
        """
        self.draw_ui_static()

        while self.isrunning:
            delta_time = pg.time.Clock().tick(60)/1000.0

            self.process_events()

            self.ui_manager.update(delta_time)

            self.draw_ui_dynamic()

            self.ui_manager.draw_ui(self.window)

            pg.display.update()

        pg.quit()

controller = ui_controller()
controller.run()