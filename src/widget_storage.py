##
# @file widget_storage.py
#
# @brief Defines and initializes the widget_storage class.
#
# @section author_sensors Author(s)
# - Created by Jessica Dawson on 03/16/2022.

## Instance of widget_storage to access widgets through.
#
# Import this instance and access widgets with widgets.widget_name()
widgets = None

class widget_storage:
    """! Storage for program widgets.

    Allows all other modules to access program widgets.
    """
    def __init__(self):
        ## The color palette widget.
        self.color_palette = None
        ## The help button widget.
        self.help = None
        ## The layers widget
        self.layer_one = None
        self.layer_two = None
        self.layer_three = None

widgets = widget_storage()