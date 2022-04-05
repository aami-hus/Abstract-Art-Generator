##
# @file ui_controller.py
#
# @brief Defines and initializes the ui_controller class.
#
# @section author_controller Author(s)
# - Created by Jessica Dawson on 03/16/2022.
# - Modified by Aamina Hussain on 03/17/2022.

# Imports
import pygame as pg
import pygame_gui as pgui
from tkinter import *
from tkinter.filedialog import asksaveasfilename

from canvas import canvas
from widget_storage import widgets
from modules.color_palette import color_palette
from modules.help import help
from modules.layer import layer
from modules.overlay import overlay
from modules.text_overlay import text_overlay
from modules.switch_theme import switch_theme
from modules.generators import generators
import assets

class ui_controller:
    """! The ui_controller class.

    A high level class that calls all other modules.
    Orchestrates pygame event handling, ui drawing, art generation, randomization, and art exporting.
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
    ## Application window height.
    SH = 720

    # general menu locations
    _ui_menus_left = 18
    _ui_menus_right = SW-270

    ## Position of the color palette widget.
    palette_pos = (_ui_menus_right, 15)
    ## Position of the layer one widget.
    layer_one_pos = (_ui_menus_left, 30)
    ## Position of the layer two widget.
    layer_two_pos = (_ui_menus_left, layer_one_pos[1]+230)
    ## Position of the layer three widget.
    layer_three_pos = (_ui_menus_left, layer_two_pos[1]+230)
    ## Position of the overlay widget.
    overlay_pos = (SW-245, palette_pos[1]+155)
    ## Position of the text overlay widget
    text_overlay_pos = (_ui_menus_right, overlay_pos[1]+360)
    ## Position of the help widget.
    help_pos = (284, 60)
    ## Position of the switch theme widget
    switch_theme_pos = (284, 90)

    ## Canvas internal size.
    canvas_size = (3840, 2160)
    ## Canvas ui display port size.
    canvas_display_size = (int(SW//1.8), int(SH//1.8))
    ## Position of the canvas on the ui.
    canvas_pos = ((SW - canvas_display_size[0])//2, (SH - canvas_display_size[1])//2)


    def __init__(self):
        """! Initializes ui_controller.
        
        Initializes pygame, the application window, the canvas, and all widgets.
        """
        pg.init()
        
        self.__create_window()

        ## The canvas to draw the generated art on.
        self.canvas = canvas(self.canvas_pos[0], self.canvas_pos[1], self.canvas_size[0], self.canvas_size[1],
                            self.canvas_display_size[0], self.canvas_display_size[1], self.window)

        self.__initialize_widgets()
        
        ## A boolean that specifies if the program is running, program terminates if False.
        self.isrunning = True


    def __create_window(self):
        ## Program window.
        self.window = pg.display.set_mode((self.SW, self.SH))
        pg.display.set_caption("Abstract Art Generator")
        pg.display.set_icon(assets.logo)
        ## Manages pygame_gui elements and events.
        self.ui_manager = pgui.UIManager((self.SW, self.SH))


    def __initialize_widgets(self):
        self.overlays = [
            pg.image.load("assets/overlay1.png").convert_alpha(),
            pg.image.load("assets/overlay2.png").convert_alpha(),
            pg.image.load("assets/overlay3.png").convert_alpha(),
            pg.image.load("assets/overlay4.png").convert_alpha(),
            pg.image.load("assets/overlay5.png").convert_alpha(),
            pg.image.load("assets/overlay6.png").convert_alpha()
        ]
        widgets.color_palette = color_palette(self.palette_pos[0], self.palette_pos[1], self.window, self.ui_manager)
        widgets.help = help(self.help_pos[0], self.help_pos[1], self.window, self.ui_manager)
        widgets.switch_theme = switch_theme(self.switch_theme_pos[0], self.switch_theme_pos[1], self.window, self.ui_manager)
        widgets.layer_one = layer(self.layer_one_pos[0], self.layer_one_pos[1], self.window, self.ui_manager, "ONE")
        widgets.layer_two = layer(self.layer_two_pos[0], self.layer_two_pos[1], self.window, self.ui_manager, "TWO")
        widgets.layer_three = layer(self.layer_three_pos[0], self.layer_three_pos[1], self.window, self.ui_manager, "THREE")
        widgets.text_overlay = text_overlay(self.text_overlay_pos[0], self.text_overlay_pos[1], self.window, self.ui_manager)
        widgets.overlay = overlay(self.overlay_pos[0], self.overlay_pos[1], self.window, self.ui_manager)
        
        widgets.generators = generators(self.canvas_size[0], self.canvas_size[1])


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

                        self.canvas.draw_layers()
                        self.canvas.draw_to_canvas()

                    if event.ui_object_id == "random_generate_button":
                        widgets.color_palette.randomize()
                        widgets.layer_one.randomize()
                        widgets.layer_two.randomize()
                        widgets.layer_three.randomize()

                        self.draw_ui_static()
                        
                        self.canvas.draw_layers()
                        self.canvas.draw_to_canvas()
                        
                    if event.ui_object_id == "export_art_button":
                        self.export_art()

                    widgets.overlay.events(event)
                    # if ob.get_active_overlay() != 0:
                    #     c1.generate_fg(overlays[ob.get_active_overlay()-1])
                    # else:
                    #     c1.clean_layer(c1.fg_layer)
                    #     c1.blit_to_canvas([l1, l2, l3])

                redraw = 0

                redraw += widgets.color_palette.events(event)
                redraw += widgets.help.events(event)
                redraw += widgets.layer_one.events(event)
                redraw += widgets.layer_two.events(event)
                redraw += widgets.layer_three.events(event)
                redraw += widgets.overlay.events(event)
                redraw += widgets.text_overlay.events(event)

                if redraw > 0:
                    self.canvas.draw_to_canvas()

                if widgets.switch_theme.events(event):
                    widgets.layer_one.change_colors()
                    widgets.layer_two.change_colors()
                    widgets.layer_three.change_colors()
                    widgets.color_palette.change_colors()
                    widgets.text_overlay.change_colors()
                    widgets.overlay.change_colors()

            self.ui_manager.process_events(event)


    def draw_ui_dynamic(self):
        """! Draws the dynamic ui.
        
        Draws the background color and some text itself and calls canvas and widgets for all other drawing.
        """
        self.window.fill(assets.background_color if widgets.switch_theme.getDarkMode() else pg.Color("#ffffff"))
        #self.window.fill(assets.background_color)

        self.canvas.draw()

        assets.text_to_screen(window=self.window, text="ABSTRACT ART GENERATOR", color=assets.ui_h1_color, pos=(430, 35), font_size=40)
        assets.text_to_screen(window=self.window, text="LAYERS", color=assets.ui_h1_color, pos=(self.layer_one_pos[0] + 42,
                            self.layer_one_pos[1]-22.5), font_size=24)
        assets.text_to_screen(window=self.window, text="RESOLUTION", color=assets.ui_color, pos=(self.SW-240, 560+20), font_size=14)

        widgets.color_palette.draw_ui_dynamic()
        widgets.help.draw_ui_dynamic()
        widgets.layer_one.draw_ui_dynamic()
        widgets.layer_two.draw_ui_dynamic()
        widgets.layer_three.draw_ui_dynamic()
        widgets.overlay.draw_ui_dynamic()
        widgets.text_overlay.draw_ui_dynamic()


    def draw_ui_static(self):
        """! Draws the static ui.
        
        Draws generation and export controls itself and calls widgets for all other drawing.
        """
        self.ui_manager.clear_and_reset()

        widgets.color_palette.draw_ui_static()
        widgets.help.draw_ui_static()
        widgets.switch_theme.draw_ui_static()
        widgets.layer_one.draw_ui_static()
        widgets.layer_two.draw_ui_static()
        widgets.layer_three.draw_ui_static()
        widgets.overlay.draw_ui_static()
        widgets.text_overlay.draw_ui_static()

        resolution_dropdown = pgui.elements.UIDropDownMenu(options_list=self.resolutions_list,
                                                starting_option=self.export_resolution,
                                                relative_rect=pg.Rect(self.SW // 2 + 100, 575+20, 200, 22), manager=self.ui_manager,
                                                object_id = "resolution_dropdown")

        export_art_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.SW // 2 + 100, self.SH - 100, 200, 50),
                                                text="Export", manager=self.ui_manager, object_id="export_art_button")

        generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.SW // 2 - 200 - 100, self.SH - 100, 200, 50),
                                                text="Generate", manager=self.ui_manager, object_id="generate_button")

        random_generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(self.SW // 2 - 200 + 100, self.SH - 100, 200, 50),
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