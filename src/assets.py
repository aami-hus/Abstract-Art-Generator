import pygame as pg
import pygame.freetype

pg.freetype.init()

logo = pg.image.load("assets/logo.png")

background_color = pg.Color("#322f3d")

ui_h1_color = (250, 250, 250)
hi_color = pg.Color("#DFD6FF")

active_color = (90, 90, 90)
inactive_color = (20, 20, 20)

lock_enabled = pg.transform.scale(pg.image.load("assets/lock_enabled.png"), (20, 20))
lock_disabled = pg.transform.scale(pg.image.load("assets/lock_disabled.png"), (20, 20))

xs_font = pg.freetype.Font("Basic-Regular.ttf", 12)
small_font = pg.freetype.Font("Basic-Regular.ttf", 14)
medium_font = pg.freetype.Font("Basic-Regular.ttf", 18)
large_font = pg.freetype.Font("Basic-Regular.ttf", 24)
xl_font = pg.freetype.Font("Basic-Regular.ttf", 30)
xxl_font = pg.freetype.Font("Basic-Regular.ttf", 40)

fonts = [xs_font, small_font, medium_font, large_font, xl_font, xxl_font]
font_sizes = [12, 14, 18, 24, 30, 40]
#-------------------------------------------

def text_to_screen(window, text, color, pos, font_size):
    font_used = fonts[font_sizes.index(font_size)]
    font_used.render_to(window, pos, text, color)