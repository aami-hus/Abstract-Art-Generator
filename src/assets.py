##
# @file assets.py
#
# @brief Stores various assets useful to other modules.
#
# @section author_assets Author(s)
# - Created by Jessica Dawson on 03/16/2022.

# Imports
import pygame as pg

pg.freetype.init()

## Program logo.
logo = pg.image.load("assets/logo.png")

## Background_color of ui.
background_color = pg.Color("#322f3d")

## Color used for larger text elements.
ui_h1_color = (250, 250, 250)
## Color used for smaller text elements
ui_color = pg.Color("#DFD6FF")

## Color used to indicate active settings.
active_color = (90, 90, 90)
## Color used to indicate inactive settings.
inactive_color = (20, 20, 20)

## Lock enabled graphic
lock_enabled = pg.transform.scale(pg.image.load("assets/lock_enabled.png"), (20, 20))
## Lock disabled graphic
lock_disabled = pg.transform.scale(pg.image.load("assets/lock_disabled.png"), (20, 20))

## Extra small font.
xs_font = pg.freetype.Font("fonts/Basic.ttf", 12)
## Small font.
small_font = pg.freetype.Font("fonts/Basic.ttf", 14)
## Medium font.
medium_font = pg.freetype.Font("fonts/Basic.ttf", 18)
## Large font.
large_font = pg.freetype.Font("fonts/Basic.ttf", 24)
## Extra large font.
xl_font = pg.freetype.Font("fonts/Basic.ttf", 30)
## Extra extra large font.
xxl_font = pg.freetype.Font("fonts/Basic.ttf", 40)

## List of font sizes.
fonts = [xs_font, small_font, medium_font, large_font, xl_font, xxl_font]
## Font size numbers that correspond with defined font sizes.
font_sizes = [12, 14, 18, 24, 30, 40]
#-------------------------------------------

def text_to_screen(window, text, color, pos, font_size):
    """! Draws text to ui.
    
    @param window       Ui window to draw to.
    @param text         Text to draw.
    @param color        Color of text.
    @param pos          Position of text.
    @param font_size    Size of text.
    """
    font_used = fonts[font_sizes.index(font_size)]
    font_used.render_to(window, pos, text, color)