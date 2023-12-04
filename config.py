import pygame as pg

pg.init()
#Константы
WINDOW_SIZE = (900,900)
clickable_menu = 1
play = False
MENU_FONT = pg.font.Font(pg.font.get_default_font(),50)
FONT = pg.font.Font(pg.font.get_default_font(),18)
FONT2 = pg.font.Font(pg.font.get_default_font(),36)
background = pg.image.load('table.jpg')
background = pg.transform.scale(background, WINDOW_SIZE)
visible_setting_menu = 0
visible_rules = 0
visible_exit = 0
timer = 0
temp_time = timer
stop_time = 0
FPS = 60
CELL_QTY = 8
CELL_SIZE = 80
BLACK = (0,0,0)
WHITE = (255,255,255)
EMPTY = (255,255,255,0)
white = 'w'
black = 'b'
GREY = (180,180,180)
YELLOW = (255,255,0,150)
CELL_BLACK = (216, 140, 68)
CELL_WHITE = (252, 204, 156)
COLORS = [CELL_BLACK,CELL_WHITE]
ACTIVE_CELL_COLOR = (174,111,237,64)
MOVES_CELL_COLOR = (0, 255, 0, 64)
STR = 'abcdefghijklmnopqrstuvwxyz'
flag = -1
visible = 1
shah_flag_w = 0
shah_flag_b = 0
chose_after_win = -1
board_data = [
    ['r','h','a','b','q','k','b','c','h','r'],
    ['p','p','p','p','p','p','p','p','p','p'],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ['P','P','P','P','P','P','P','P','P','P'],
    ['R','H','A','B','Q','K','B','C','H','R']
]
board_data1 = [
    ['r','h','b','q','k','b','h','r'],
    ['p','p','p','p','p','p','p','p'],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ['P','P','P','P','P','P','P','P'],
    ['R','H','B','Q','K','B','H','R']
]
Pieces_Types = {
    'k':('King','b'),'K':('King','w'),
    'q':('Queen','b'),'Q':('Queen','w'),
    'r':('Rook','b'),'R':('Rook','w'),
    'h':('Horse','b'),'H':('Horse','w'),
    'a':('Archbishop','b'),'A':('Archbishop','w'),
    'b':('Bishop','b'),'B':('Bishop','w'),
    'c':('Chancellor','b'),'C':('Chancellor','w'),
    'p':('Pawn','b'), 'P':('Pawn','w')
}
