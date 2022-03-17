from random import randint, choice

import pygame_gui as pgui
import pygame as pg

from modules.widget import widget
import assets

color_palettes = {
    "Forest" : ["#323232", "#295f4e", "#6db193", "#f4e5c2"],
    "Futuristic" : ["#222831", "#393e46", "#00adb5", "#eeeeee"],
    "Sunset" : ["#f9ed69", "#f08a5d", "#b83b5e", "#6a2c70"],
    "Vintage" : ["#f85f73", "#fbe8d3", "#928a97", "#283c63"],
    "Crimson" : ["#0f1021", "#d01257", "#fb90b7", "#ffcee4"],
    "Vampire" : ["#34374c", "#2c2e3e", "#ee2b47", "#f6f6f6"],
    "Lightning" : ["#f3f3f3", "#ffdd67", "#ffcd38", "#4a4a4a"],
    "Pastel" : ["#8fcfd1", "#df5e88", "#f6ab6c", "#f6efa6"],
    "Lava" : ["#2f2519", "#4a3f35", "#fa7d09", "#ff4301"],
    "Neon" : ["#0c093c", "#df42d1", "#eea5f6", "#fad6d6"],
    "Lilac" : ["#f0e3ff", "#d89cf6", "#916dd5", "#3e206d"],
    "Soft Gray" : ["#3c4245", "#5f6769", "#719192", "#dfcdc3"],
    "Low Saturation" : ["#333644", "#84577c", "#c65f63", "#f6e1b8"],
    "Poison" : ["#151716", "#3e432e", "#616f39", "#a7d129"],
    "Spring" : ["#f9f9f9", "#ffe0ac", "#ffacb7", "#6886c5"],
    "Black & White" : ["#262626", "#595959", "#b0b0b0", "#e3e3e3"],
    "Corruption" : ["#6f4a8e", "#221f3b", "#050505", "#ebebeb"],
    "Ivy" : ["#1fab89", "#62d2a2", "#9df3c4", "#d7fbe8"],
    "Ocean" : ["#73f7dd", "#2cc4cb", "#1972a4", "#2e3a87"],
    "Royalty" : ["#fcf0c8", "#f7d098", "#911f27", "#630a10"],
    "Transit" : ["#5BCEFA", "#F5A9B8", "#FFFFFF"],
    "Girls" : ["#d52d00", "#ef7627", "#ff9a56", "#ffffff",
    "#D162A4", "#B55690", "#A30262"],
    "Test" : ["#73f7dd", "#2cc4cb", "#1972a4", "#2e3a87",
    "#fcf0c8", "#f7d098", "#911f27", "#630a10"],
}

#margins for where to place text/interactables in the dialogs
#cpm = palette_pos[0] + 42
#dynamic:
#cp_lock = palette_pos[0] + 17
#static:
#cp_lock = palette_pos[0] + 6

class color_palette(widget):

    def __init__(self, x, y, window, ui_manager):
        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager

        self.__palette_name = choice(list(color_palettes.keys()))
        self.__palette_colors = color_palettes[self.__palette_name]
        self.__background_index = 0

        self.__palette_lock = 0
        self.__background_lock = 0


    def draw_ui_dynamic(self):
        interactables_margin = self.__x + 42
        lock_margin = self.__x + 17

        pg.draw.rect(self.__window, pg.Color("#2B2834"), (self.__x, self.__y, 252, 135))

        if self.__palette_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+35))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+35))

        if self.__background_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+68))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+68))

        assets.text_to_screen(window=self.__window, text="COLOR PALETTE", color=assets.ui_h1_color, pos=(interactables_margin, self.__y+15), font_size=18)
        for i, color in enumerate(self.__palette_colors):
            pg.draw.rect(self.__window, assets.active_color if self.__background_index == i else assets.inactive_color,
                        (interactables_margin+((i%4)*50), self.__y+65+(36*(i//4)), 26, 26))
            pg.draw.rect(self.__window, pg.Color(color), (interactables_margin+3+((i%4)*50), self.__y+68+(36*(i//4)), 20, 20))


    def draw_ui_static(self):
        interactables_margin = self.__x + 42
        lock_margin = self.__x + 6

        cp_len = len(self.__palette_colors)

        current_palette_dropdown = pgui.elements.UIDropDownMenu(options_list=color_palettes.keys(),
                                                            starting_option=self.__palette_name,
                                                            relative_rect=pg.Rect(interactables_margin, self.__y+35, 200, 22), manager=self.__ui_manager,
                                                            object_id="current_palette_dropdown")

        palette_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+42, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="palette_lock_button")
        background_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+72, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="background_lock_button")
        
        background_index_button_one = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_one", visible=cp_len>0)
        background_index_button_two = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+50+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_two", visible=cp_len>1)
        background_index_button_three = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+100+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_three", visible=cp_len>2)
        background_index_button_four = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+150+12, self.__y+65+12, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_four", visible=cp_len>3)
        background_index_button_five = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_five", visible=cp_len>4)
        background_index_button_six = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+50+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_six", visible=cp_len>5)
        background_index_button_seven = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+100+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_seven", visible=cp_len>6)
        background_index_button_eight = pgui.elements.UIButton(relative_rect=pg.Rect(interactables_margin+150+12, self.__y+65+12+36, 14, 14), text="",
                                                manager=self.__ui_manager, object_id="background_index_button_eight", visible=cp_len>7)

        self.background_index_buttons = [background_index_button_one, background_index_button_two, background_index_button_three, background_index_button_four, background_index_button_five,
                        background_index_button_six, background_index_button_seven, background_index_button_eight]


    def refresh_ui_static(self):
        cp_len = len(self.__palette_colors)

        for i in range(8):
            if i < cp_len:
                self.background_index_buttons[i].show()
            else:
                self.background_index_buttons[i].hide()


    def randomize(self):
        if self.__palette_lock == 0:
            self.__palette_name = choice(list(color_palettes.keys()))
            self.__palette_colors = color_palettes[self.__palette_name]
            if self.__background_index >= len(self.__palette_colors):
                    self.__background_index = randint(0, len(self.__palette_colors)-1)
            self.refresh_ui_static()
        
        if self.__background_lock == 0:
            self.__background_index = randint(0, len(self.__palette_colors)-1)


    def events(self, event):
        if event.user_type == pgui.UI_BUTTON_PRESSED:
            if event.ui_object_id == "palette_lock_button":
                self.__palette_lock = 1 if self.__palette_lock == 0 else 0
            if event.ui_object_id == "background_lock_button":
                self.__background_lock = 1 if self.__background_lock == 0 else 0

            if event.ui_object_id == "background_index_button_one":
                self.__background_index = 0
            if event.ui_object_id == "background_index_button_two":
                self.__background_index = 1
            if event.ui_object_id == "background_index_button_three":
                self.__background_index = 2
            if event.ui_object_id == "background_index_button_four":
                self.__background_index = 3
            if event.ui_object_id == "background_index_button_five":
                self.__background_index = 4
            if event.ui_object_id == "background_index_button_six":
                self.__background_index = 5
            if event.ui_object_id == "background_index_button_seven":
                self.__background_index = 6
            if event.ui_object_id == "background_index_button_eight":
                self.__background_index = 7

        if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_object_id == "current_palette_dropdown":
                self.__palette_name = event.text
                self.__palette_colors = color_palettes[self.__palette_name]
                if self.__background_index >= len(self.__palette_colors):
                    self.__background_index = randint(0, len(self.__palette_colors)-1)
                self.refresh_ui_static()


    def get_name_of_palette(self):
        return self.__palette_name


    def get_colors_from_palette(self):
        return self.__palette_colors


    def get_background_color(self):
        return self.__palette_colors[self.__background_index]


    def get_foreground_colors(self):
        return [c for c in self.__palette_colors if c != self.__palette_colors[self.__background_index]]