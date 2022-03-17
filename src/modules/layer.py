import pygame_gui as pgui
import pygame as pg
from random import randint, choice

from modules.widget import widget
import assets

art_styles_list = [
    "Chaotic",
    "Striped Horizontal",
    "Striped Vertical",
    "Mosaic",
    "Cornered",
    "Centered",
    "Empty"
]

art_shapes_list = [
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
    
    #layer_num = string --> ex: "ONE"
    def __init__(self, x, y, window, ui_manager, layer_num):
        self.layer = pg.Surface((3840, 2160), pg.SRCALPHA)
        self.__x = x
        self.__y = y
        self.__window = window
        self.__ui_manager = ui_manager
        self.__layer_num = layer_num

        #starting options for dropdown menus
        self.__style = choice(art_styles_list)
        self.__shape = choice(art_shapes_list)
        self.__complexity = randint(10,30)#15
        self.__size = randint(51, 400) #400

        #locks
        self.__style_lock = 0
        self.__shape_lock = 0
        self.__complexity_lock = 0
        self.__size_lock = 0


    # draw dynamic ui elements (basically anything that isn't a pgui widget) (OVERRIDE)
    #@abstractmethod
    def draw_ui_dynamic(self):
        interactables_margin = self.__x + 42
        lock_margin = self.__x + 17

        pg.draw.rect(self.__window, pg.Color("#2B2834"), (self.__x, self.__y, 252, 190))

        if self.__style_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+30))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+30))

        if self.__shape_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+60))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+60))

        if self.__complexity_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+110))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+110))

        if self.__size_lock == 0:
            self.__window.blit(assets.lock_disabled, (lock_margin, self.__y+160))
        else:
            self.__window.blit(assets.lock_enabled, (lock_margin, self.__y+160))

        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " STYLE", color=assets.ui_h1_color, pos=(interactables_margin, self.__y+10), font_size=18)
        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " COMPLEXITY", color=assets.ui_color, pos=(interactables_margin, self.__y+95), font_size=14)
        assets.text_to_screen(window=self.__window, text="LAYER " + self.__layer_num + " SHAPE SIZE", color=assets.ui_color, pos=(interactables_margin, self.__y+145), font_size=14)



    # draw static ui elements (basically the pgui widgets) (OVERRIDE)
    #@abstractmethod
    def draw_ui_static(self):
        interactables_margin = self.__x + 42
        lock_margin = self.__x + 6
        num_of_layer = self.__layer_num.lower()

        style_dropdown = pgui.elements.UIDropDownMenu(options_list=art_styles_list,
                                                                starting_option=self.__style,
                                                                relative_rect=pg.Rect(interactables_margin, self.__y+30, 200, 22), manager=self.__ui_manager,
                                                                object_id="layer_"+num_of_layer+"_style_dropdown")

        shape_dropdown = pgui.elements.UIDropDownMenu(options_list=art_shapes_list,
                                                                starting_option=self.__shape,
                                                                relative_rect=pg.Rect(interactables_margin, self.__y+60, 200, 22), manager=self.__ui_manager,
                                                                object_id="layer_"+num_of_layer+"_shape_dropdown")

        complexity_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+110, 200, 22),
                                                                    start_value=self.__complexity,
                                                                    value_range=(10, 30), manager=self.__ui_manager,
                                                                    object_id="layer_"+num_of_layer+"_complexity_slider")

        size_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(interactables_margin, self.__y+160, 200, 22),
                                                                start_value=self.__size, value_range=(50, 400),
                                                                manager=self.__ui_manager, object_id="layer_"+num_of_layer+"_size_slider")

        # "lock_button_three" changed to "layer_one_lock_butter"
        # etc, 4 = layer 1 shape, 5 = layer 1 complex, 6 = layer 1 size
        # repeat for layer 2 and 3
        style_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+37, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_style_lock_button")
        shape_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+67, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_shape_lock_button")
        complexity_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+117, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_complexity_lock_button")
        size_lock_button = pgui.elements.UIButton(relative_rect=pg.Rect(lock_margin, self.__y+167, 12, 12), text="", manager=self.__ui_manager,
                                                object_id="layer_"+num_of_layer+"_size_lock_button")



    # randomize settings (OVERRIDE)
    #@abstractmethod
    def randomize(self):
        if self.__style_lock == 0:
            self.__style = choice(art_styles_list)
        if self.__shape_lock == 0:
            self.__shape = choice(art_shapes_list)
        if self.__complexity_lock == 0:
            self.__complexity = randint(10,30)
        if self.__size_lock == 0:
            self.__size = randint(51, 400)

    # process pgui interaction events (OVERRIDE)
    #@abstractmethod
    def events(self, event):
        num_of_layer = self.__layer_num.lower()

        if event.user_type == pgui.UI_BUTTON_PRESSED:
            if event.ui_object_id == "layer_"+num_of_layer+"_style_lock_button":
                self.__style_lock = 1 if self.__style_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_shape_lock_button":
                self.__shape_lock = 1 if self.__shape_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_complexity_lock_button":
                self.__complexity_lock = 1 if self.__complexity_lock == 0 else 0
            if event.ui_object_id == "layer_"+num_of_layer+"_size_lock_button":
                self.__size_lock = 1 if self.__size_lock == 0 else 0

        if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_object_id == "layer_"+num_of_layer+"_style_dropdown":
                self.__style = event.text
            if event.ui_object_id == "layer_"+num_of_layer+"_shape_dropdown":
                self.__shape = event.text

        if event.user_type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_object_id == "layer_"+num_of_layer+"_complexity_slider":
                self.__complexity = event.value
            if event.ui_object_id == "layer_"+num_of_layer+"_size_slider":
                self.__size = event.value



    # draw to canvas (MAYBE OVERRIDE)
    def draw_canvas(self, color_palette):
        pass

    # refresh the static ui elements, useful when you need to change the widgets pgui widgets (MAYBE OVERRIDE)
    def refresh_ui_static(self):
        pass


    def clean_layer(self):
        self.layer.fill((0, 0, 0, 0))

    def get_layer_style(self):
        return self.__style
    def get_layer_shape(self):
        return self.__shape
    def get_layer_complexity(self):
        return self.__complexity
    def get_layer_size(self):
        return self.__size