from abc import ABC, abstractmethod

class widget(ABC):
    
    # draw dynamic ui elements (basically anything that isn't a pgui widget) (OVERRIDE)
    @abstractmethod
    def draw_ui_dynamic(self, window, x, y):
        pass

    # draw static ui elements (basically the pgui widgets) (OVERRIDE)
    @abstractmethod
    def draw_ui_static(self, ui_manager, x, y):
        pass

    # randomize settings (OVERRIDE)
    @abstractmethod
    def randomize(self):
        pass

    # process pgui interaction events (OVERRIDE)
    @abstractmethod
    def events(self, event):
        pass

    # draw to canvas (MAYBE OVERRIDE)
    def draw_canvas(self, window, x, y):
        pass

    # refresh the static ui elements, useful when you need to change the widgets pgui widgets (MAYBE OVERRIDE)
    def refresh_ui_static(self):
        pass