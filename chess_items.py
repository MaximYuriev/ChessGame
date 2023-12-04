from config import *
from random import randint
from time import sleep
class Menu:
    def __init__(self,parent_surface):
        self.screen = parent_surface
        self.draw_menu()
    def draw_menu(self):
        self.menu = pg.Surface((WINDOW_SIZE[0],WINDOW_SIZE[1]),pg.SRCALPHA)
        text_game = MENU_FONT.render('Шахматы Капабланки',1,WHITE)
        text_button_play_1 = FONT2.render('Совместная',1,WHITE)
        text_button_play_2 = FONT2.render('игра',1,WHITE)
        text_button_play_with_bots = FONT2.render('Игра с ботом',1,WHITE)
        text_button_settings = FONT2.render('Настройки',1,WHITE)
        text_button_rules = FONT2.render('Правила',1,WHITE)
        text_button_quit = FONT2.render('Выход',1,WHITE)
        pg.draw.rect(self.menu,CELL_BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2-250,300,100))
        pg.draw.rect(self.menu,BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2-250,300,100),3)
        pg.draw.rect(self.menu,CELL_BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2-100,300,100))
        pg.draw.rect(self.menu,BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2-100,300,100),3)
        pg.draw.rect(self.menu,CELL_BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+50,300,100))
        pg.draw.rect(self.menu,BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+50,300,100),3)
        pg.draw.rect(self.menu,CELL_BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+200,300,100))
        pg.draw.rect(self.menu,BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+200,300,100),3)
        pg.draw.rect(self.menu,CELL_BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+350,300,100))
        pg.draw.rect(self.menu,BLACK,((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+350,300,100),3)
        self.menu.blit(text_game,(self.menu.get_width()//2-270,10))
        self.menu.blit(text_button_play_with_bots,((self.menu.get_width()-300)//2+35,(self.menu.get_height()-100)//2-250+30))
        self.menu.blit(text_button_play_1,((self.menu.get_width()-300)//2+40,(self.menu.get_height()-100)//2-100+15))
        self.menu.blit(text_button_play_2,((self.menu.get_width()-300)//2+110,(self.menu.get_height()-100)//2-100+45))
        self.menu.blit(text_button_settings,((self.menu.get_width()-300)//2+55,(self.menu.get_height()-100)//2+50+30))
        self.menu.blit(text_button_rules,((self.menu.get_width()-300)//2+75,(self.menu.get_height()-100)//2+200+30))
        self.menu.blit(text_button_quit,((self.menu.get_width()-300)//2+90,(self.menu.get_height()-100)//2+350+30))
        self.button_play_rect = pg.Rect((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2-100,300,100)
        self.button_play_with_bots_rect = pg.Rect((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2-250,300,100)
        self.button_settings_rect = pg.Rect((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+50,300,100)
        self.button_rules_rect = pg.Rect((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+200,300,100)
        self.button_quit_rect = pg.Rect((self.menu.get_width()-300)//2,(self.menu.get_height()-100)//2+350,300,100)
        self.screen.blit(self.menu,(0,0))
        pg.display.update()
    def btn_down(self,button,position):
        if self.button_play_rect.collidepoint(position):
            if button == 1:
                return 0
        if self.button_play_with_bots_rect.collidepoint(position):
            if button == 1:
                return 1
        if self.button_settings_rect.collidepoint(position):
            if button == 1:
                return 2
        if self.button_rules_rect.collidepoint(position):
            if button == 1:
                return 3
        if self.button_quit_rect.collidepoint(position):
            if button == 1:
                return 4
    def draw_menu_chose_color(self):
        self.button_black_text = FONT2.render('Черный',1,WHITE)
        self.button_white_text = FONT2.render('Белый',1,WHITE)
        self.button_close_text = FONT2.render('Закрыть',1,WHITE)
        chose_color_surface = pg.Surface((WINDOW_SIZE[0]//2,WINDOW_SIZE[1]//4),pg.SRCALPHA)
        pg.draw.rect(chose_color_surface,CELL_BLACK,chose_color_surface.get_rect())
        pg.draw.rect(chose_color_surface,BLACK,chose_color_surface.get_rect(),3)
        pg.draw.rect(chose_color_surface,CELL_WHITE,(5,chose_color_surface.get_height()-140,200,50))
        pg.draw.rect(chose_color_surface,BLACK,(5,chose_color_surface.get_height()-140,200,50),3)
        pg.draw.rect(chose_color_surface,CELL_WHITE,(chose_color_surface.get_width()-205,chose_color_surface.get_height()-140,200,50))
        pg.draw.rect(chose_color_surface,BLACK,(chose_color_surface.get_width()-205,chose_color_surface.get_height()-140,200,50),3)
        pg.draw.rect(chose_color_surface,CELL_WHITE,(chose_color_surface.get_width()-320,chose_color_surface.get_height()-80,200,50))
        pg.draw.rect(chose_color_surface,BLACK,(chose_color_surface.get_width()-320,chose_color_surface.get_height()-80,200,50),3)
        text = FONT2.render('Выберите цвет',1,WHITE)
        chose_color_surface.blit(text,(90,3))
        chose_color_surface.blit(self.button_black_text,(30,chose_color_surface.get_height()-135))
        chose_color_surface.blit(self.button_white_text,(chose_color_surface.get_width()-165,chose_color_surface.get_height()-135))
        chose_color_surface.blit(self.button_close_text,(chose_color_surface.get_width()-295,chose_color_surface.get_height()-75))
        self.button_black_rect=pg.Rect((WINDOW_SIZE[0] - chose_color_surface.get_width())//2 + 5,((WINDOW_SIZE[1] - chose_color_surface.get_height())//2+chose_color_surface.get_height()-140),200,50)
        self.button_white_rect=pg.Rect((WINDOW_SIZE[0] - chose_color_surface.get_width())//2 + chose_color_surface.get_width()-205,((WINDOW_SIZE[1] - chose_color_surface.get_height())//2+chose_color_surface.get_height()-140),200,50)
        self.button_close_rect=pg.Rect((WINDOW_SIZE[0] - chose_color_surface.get_width())//2 + chose_color_surface.get_width()-320,((WINDOW_SIZE[1] - chose_color_surface.get_height())//2+chose_color_surface.get_height()-80),200,50)
        self.screen.blit(chose_color_surface,((WINDOW_SIZE[0] - chose_color_surface.get_width())//2,(WINDOW_SIZE[1] - chose_color_surface.get_height())//2))
        pg.display.update()
    def chose_color_btn_down(self,button, position):
        if button == 1:
            if self.button_black_rect.collidepoint(position):
                return 'b'
            if self.button_white_rect.collidepoint(position):
                return 'w'
            if self.button_close_rect.collidepoint(position):
                return 0
    def draw_exit(self):
        button_yes_text = FONT2.render('Да',1,WHITE)
        button_no_text = FONT2.render('Нет',1,WHITE)
        text = MENU_FONT.render('Покинуть игру?',1,WHITE)
        exit_surface = pg.Surface((WINDOW_SIZE[0]//2,WINDOW_SIZE[1]//4),pg.SRCALPHA)
        pg.draw.rect(exit_surface,CELL_BLACK,exit_surface.get_rect())
        pg.draw.rect(exit_surface,BLACK,exit_surface.get_rect(),3)
        pg.draw.rect(exit_surface,CELL_WHITE,(5,exit_surface.get_height()-70,200,50))
        pg.draw.rect(exit_surface,BLACK,(5,exit_surface.get_height()-70,200,50),3)
        pg.draw.rect(exit_surface,CELL_WHITE,(exit_surface.get_width()-205,exit_surface.get_height()-70,200,50))
        pg.draw.rect(exit_surface,BLACK,(exit_surface.get_width()-205,exit_surface.get_height()-70,200,50),3)
        exit_surface.blit(text,(35,3))
        exit_surface.blit(button_yes_text,(75,exit_surface.get_height()-65))
        exit_surface.blit(button_no_text,(exit_surface.get_width()-135,exit_surface.get_height()-65))
        self.button_yes_rect = pg.Rect((WINDOW_SIZE[0] - exit_surface.get_width())//2 + 5,((WINDOW_SIZE[1] - exit_surface.get_height())//2+exit_surface.get_height()-70),200,50)
        self.button_no_rect = pg.Rect((WINDOW_SIZE[0] - exit_surface.get_width())//2 + exit_surface.get_width()-205,((WINDOW_SIZE[1] - exit_surface.get_height())//2+exit_surface.get_height()-70),200,50)
        self.screen.blit(exit_surface,((WINDOW_SIZE[0] - exit_surface.get_width())//2,(WINDOW_SIZE[1] - exit_surface.get_height())//2))
        pg.display.update()
    def exit_btn_down(self,button,position):
        if button == 1:
            if self.button_yes_rect.collidepoint(position):
                return 1
            if self.button_no_rect.collidepoint(position):
                return 0
    def draw_rules(self):
        button_close_text = FONT2.render('Закрыть',1,WHITE)
        rule_text_1 = FONT.render('Архиепископ совмещает ходы коня и слона.',1,WHITE)
        rule_text_2 = FONT.render('Расположен на вертикале С.',1,WHITE)
        rule_text_3 = FONT.render('Канцлер совмещает ходы коня и ладьи.',1,WHITE)
        rule_text_4 = FONT.render('Расположен на вертикале H.',1,WHITE)
        rule_text_5 = FONT.render('При достижении конца поля пешка обращается',1,WHITE)
        rule_text_6 = FONT.render('в ферзя.',1,WHITE)
        rule_text_7 = FONT.render('Игра заканчивается после мата одной из сторон.',1,WHITE)
        rule_text_8 = FONT.render('Ничья объявляется в случае пата и если на поле',1,WHITE)
        rule_text_9 = FONT.render('осталось только два короля.',1,WHITE)
        rule_text_10 = FONT.render('Перемещение фигур осуществляется ЛКМ.',1,WHITE)
        rule_text_11 = FONT.render('С помощью ПКМ можно маркировать поле для',1,WHITE)
        rule_text_12 = FONT.render('визуализации планируемой стратегии.',1,WHITE)
        rule_text_13 = FONT.render('С помощью ESC можно вернуться в главное',1,WHITE)
        rule_text_14 = FONT.render('меню в процессе игры.',1,WHITE)
        text = MENU_FONT.render('Правила игры',1,WHITE)
        rules_surface = pg.Surface((WINDOW_SIZE[0]//2,WINDOW_SIZE[1]//2),pg.SRCALPHA)
        pg.draw.rect(rules_surface,CELL_BLACK,rules_surface.get_rect())
        pg.draw.rect(rules_surface,BLACK,rules_surface.get_rect(),3)
        pg.draw.rect(rules_surface,CELL_WHITE,(rules_surface.get_width()-320,rules_surface.get_height()-60,200,50))
        pg.draw.rect(rules_surface,BLACK,(rules_surface.get_width()-320,rules_surface.get_height()-60,200,50),3)
        rules_surface.blit(text,(50,3))
        rules_surface.blit(rule_text_1,(4,55))
        rules_surface.blit(rule_text_2,(4,75))
        rules_surface.blit(rule_text_3,(4,105))
        rules_surface.blit(rule_text_4,(4,125))
        rules_surface.blit(rule_text_5,(4,155))
        rules_surface.blit(rule_text_6,(4,175))
        rules_surface.blit(rule_text_7,(4,205))
        rules_surface.blit(rule_text_8,(4,235))
        rules_surface.blit(rule_text_9,(4,255))
        rules_surface.blit(rule_text_10,(4,285))
        rules_surface.blit(rule_text_11,(4,305))
        rules_surface.blit(rule_text_12,(4,325))
        rules_surface.blit(rule_text_13,(4,355))
        rules_surface.blit(rule_text_14,(4,370))
        rules_surface.blit(button_close_text,(rules_surface.get_width()-295,rules_surface.get_height()-55))
        self.button_close_rect = pg.Rect((WINDOW_SIZE[0] - rules_surface.get_width())//2 + rules_surface.get_width()-320,((WINDOW_SIZE[1] - rules_surface.get_height())//2+rules_surface.get_height()-60),200,50)
        self.screen.blit(rules_surface,((WINDOW_SIZE[0] - rules_surface.get_width())//2,(WINDOW_SIZE[1] - rules_surface.get_height())//2))
        pg.display.update()
    def rules_btn_down(self,button,position):
        if button == 1:
            if self.button_close_rect.collidepoint(position):
                return 0
    def draw_setting(self):
        text = MENU_FONT.render('Настройки',1,WHITE)
        time_text = FONT.render('Ограничение времени на ходы',1,WHITE)
        text_5 = FONT2.render('5 минут',1,WHITE)
        text_without = FONT2.render('Отсутсвует',1,WHITE)
        button_close_text = FONT2.render('Закрыть',1,WHITE)
        setting_surface = pg.Surface((WINDOW_SIZE[0]//2,WINDOW_SIZE[1]//4),pg.SRCALPHA)
        pg.draw.rect(setting_surface,CELL_BLACK,setting_surface.get_rect())
        pg.draw.rect(setting_surface,BLACK,setting_surface.get_rect(),3)
        pg.draw.rect(setting_surface,CELL_WHITE,(5,setting_surface.get_height()-140,200,50)) #5 min
        pg.draw.rect(setting_surface,BLACK,(5,setting_surface.get_height()-140,200,50),3)
        pg.draw.rect(setting_surface,CELL_WHITE,(setting_surface.get_width()-205,setting_surface.get_height()-140,200,50))#without
        pg.draw.rect(setting_surface,BLACK,(setting_surface.get_width()-205,setting_surface.get_height()-140,200,50),3)
        pg.draw.rect(setting_surface,CELL_WHITE,(setting_surface.get_width()-320,setting_surface.get_height()-80,200,50))
        pg.draw.rect(setting_surface,BLACK,(setting_surface.get_width()-320,setting_surface.get_height()-80,200,50),3)
        setting_surface.blit(text,(90,3))
        setting_surface.blit(time_text,(90,55))
        setting_surface.blit(text_5,(40,setting_surface.get_height()-135))
        setting_surface.blit(text_without,(setting_surface.get_width()-204,setting_surface.get_height()-135))
        setting_surface.blit(button_close_text,(setting_surface.get_width()-295,setting_surface.get_height()-75))
        self.button_close_rect = pg.Rect((WINDOW_SIZE[0] - setting_surface.get_width())//2 + setting_surface.get_width()-320,((WINDOW_SIZE[1] - setting_surface.get_height())//2+setting_surface.get_height()-80),200,50)
        self.button_text_without_rect = pg.Rect((WINDOW_SIZE[0] - setting_surface.get_width())//2 + setting_surface.get_width()-205,((WINDOW_SIZE[1] - setting_surface.get_height())//2+setting_surface.get_height()-140),200,50)
        self.button_text_5_rect = pg.Rect((WINDOW_SIZE[0] - setting_surface.get_width())//2 + 5,((WINDOW_SIZE[1] - setting_surface.get_height())//2+setting_surface.get_height()-140),200,50)
        self.screen.blit(setting_surface,((WINDOW_SIZE[0] - setting_surface.get_width())//2,(WINDOW_SIZE[1] - setting_surface.get_height())//2))
        pg.display.update()
    def setting_btn_down(self,button,position):
        text = MENU_FONT.render('Настройки изменены!',1,WHITE)
        if button == 1:
            if self.button_close_rect.collidepoint(position):
                return 0
            if self.button_text_without_rect.collidepoint(position):
                self.screen.blit(text,(0,WINDOW_SIZE[1]-50))
                pg.display.update()
                return 2
            if self.button_text_5_rect.collidepoint(position):
                self.screen.blit(text,(0,WINDOW_SIZE[1]-50))
                pg.display.update()
                return 3
            pg.display.update()
            
class Chessboard:
    def __init__(self, parent_surface,timer, play = 0,color = 'w'):
        self.screen = parent_surface
        self.table = board_data
        self.pieces_types = Pieces_Types
        self.number_of_moves = 0
        self.white_moves = 0
        self.black_moves = 0
        self.all_cells = pg.sprite.Group()
        self.all_pieces = pg.sprite.Group()
        self.all_areas = pg.sprite.Group()
        self.all_possible_moves = pg.sprite.Group()
        self.black_times = 300
        self.white_times = 300
        self.turn = 0
        self.antishah = []
        self.picked_piece = None
        self.pressed_cell = None
        self.draw_playboard()
        self.draw_cells()
        self.draw_pieces()
        self.get_turn()
        self.print_shah(0)
        self.print_moves()
        pg.display.update()
        self.play = play
        self.color = color
        if self.color == 'w':
            self.bot_color = 'b'
        if self.color == 'b':
            self.bot_color = 'w'
            sleep(2)
            self.bots_play()
            self.turn = 1
            self.grand_update()
    def draw_exit(self):
        button_yes_text = FONT2.render('Да',1,WHITE)
        button_no_text = FONT2.render('Нет',1,WHITE)
        text = MENU_FONT.render('Покинуть игру?',1,WHITE)
        exit_surface = pg.Surface((WINDOW_SIZE[0]//2,WINDOW_SIZE[1]//4),pg.SRCALPHA)
        pg.draw.rect(exit_surface,CELL_BLACK,exit_surface.get_rect())
        pg.draw.rect(exit_surface,BLACK,exit_surface.get_rect(),3)
        pg.draw.rect(exit_surface,CELL_WHITE,(5,exit_surface.get_height()-70,200,50))
        pg.draw.rect(exit_surface,BLACK,(5,exit_surface.get_height()-70,200,50),3)
        pg.draw.rect(exit_surface,CELL_WHITE,(exit_surface.get_width()-205,exit_surface.get_height()-70,200,50))
        pg.draw.rect(exit_surface,BLACK,(exit_surface.get_width()-205,exit_surface.get_height()-70,200,50),3)
        exit_surface.blit(text,(35,3))
        exit_surface.blit(button_yes_text,(75,exit_surface.get_height()-65))
        exit_surface.blit(button_no_text,(exit_surface.get_width()-135,exit_surface.get_height()-65))
        self.button_yes_rect = pg.Rect((WINDOW_SIZE[0] - exit_surface.get_width())//2 + 5,((WINDOW_SIZE[1] - exit_surface.get_height())//2+exit_surface.get_height()-70),200,50)
        self.button_no_rect = pg.Rect((WINDOW_SIZE[0] - exit_surface.get_width())//2 + exit_surface.get_width()-205,((WINDOW_SIZE[1] - exit_surface.get_height())//2+exit_surface.get_height()-70),200,50)
        self.screen.blit(exit_surface,((WINDOW_SIZE[0] - exit_surface.get_width())//2,(WINDOW_SIZE[1] - exit_surface.get_height())//2))
        pg.display.update()
    def exit_btn_down(self,button,position):
        if button == 1:
            if self.button_yes_rect.collidepoint(position):
                return 1
            if self.button_no_rect.collidepoint(position):
                return 0
    def print_time(self):
        white_time_text = FONT.render('Оставшееся время для белых',1,WHITE)
        black_time_text = FONT.render('Оставшееся время для черных',1,WHITE)
        if self.white_times%60 >= 10:
            white_time_minute = str(self.white_times%60)
        else:
            white_time_minute = '0' + str(self.white_times%60)
        if self.black_times%60 >= 10:
            black_time_minute = str(self.black_times%60)
        else:
            black_time_minute = '0' + str(self.black_times%60) 
        white_time = FONT2.render('0'+str(self.white_times//60)+':'+white_time_minute,1,WHITE)
        black_time = FONT2.render('0'+str(self.black_times//60)+':'+black_time_minute,1,WHITE)
        print_time_surface = pg.Surface((WINDOW_SIZE[0],(WINDOW_SIZE[1] - self.board.get_height())//2 + self.board.get_height()),pg.SRCALPHA)
        print_time_surface.blit(background,(0,0))
        print_time_surface.blit(black_time_text,(WINDOW_SIZE[0]-300,0))
        print_time_surface.blit(white_time_text,(0,0))
        print_time_surface.blit(white_time,(100,20))
        print_time_surface.blit(black_time,(WINDOW_SIZE[0]-180,20))
        self.screen.blit(print_time_surface,(0,(WINDOW_SIZE[1] - self.board.get_height())//2 + self.board.get_height()))
    def draw_playboard(self):
        #Создание поверхностей
        n_lines = pg.Surface(((CELL_QTY+2)*CELL_SIZE, CELL_SIZE // 2),pg.SRCALPHA)
        n_rows = pg.Surface((CELL_SIZE // 2, CELL_QTY*CELL_SIZE),pg.SRCALPHA)
        self.fields = pg.Surface(((CELL_QTY+2)*CELL_SIZE,CELL_QTY*CELL_SIZE),pg.SRCALPHA)
        self.board = pg.Surface((2*n_rows.get_width() + self.fields.get_width(),2*n_lines.get_height()+self.fields.get_height()),pg.SRCALPHA)
        
        #Отрисовка букв и цифр
        for i in range (0, CELL_QTY+2):
            letter = FONT.render(STR[i],1,WHITE)
            n_lines.blit(letter,(i*CELL_SIZE + (CELL_SIZE - letter.get_rect().width) // 2, (n_lines.get_height() - letter.get_rect().height)//2))
            number = FONT.render(str(CELL_QTY - i),1,WHITE)
            n_rows.blit(number,((n_rows.get_width() - letter.get_rect().width)//2,i*CELL_SIZE + (CELL_SIZE - number.get_rect().height)//2))
        #Заливка фона
        boardbackground = pg.image.load('chessboard.jpg')
        boardbackground = pg.transform.scale(background, (self.board.get_width(),self.board.get_height()))
        #Прикрепление слоев на доску, затем на экран
        self.board.blit(boardbackground,boardbackground.get_rect())
        self.board.blit(n_rows, (0, n_lines.get_height()))
        self.board.blit(n_rows,(n_rows.get_width() + self.fields.get_width(), n_lines.get_height()))
        self.board.blit(n_lines,(n_rows.get_width(),0))
        self.board.blit(n_lines, (n_rows.get_width(), self.fields.get_height()+n_rows.get_width()))
        self.board.blit(self.fields,(n_rows.get_width(), n_lines.get_height()))
        self.rows = n_rows.get_width()
        self.lines = n_lines.get_height()
        self.board.blit(self.fields,(self.rows, self.lines))
        self.screen.blit(self.board,((WINDOW_SIZE[0] - self.board.get_width())//2,(WINDOW_SIZE[1] - self.board.get_height())//2))
    
    def draw_cells(self):
        #Отрисовка игрового поля
        is_even_qty = (CELL_QTY % 2 == 0)
        cell_color_index = 1 if (is_even_qty) else 0
        for y in range(CELL_QTY):
            for x in range(CELL_QTY+2):
                field_name = STR[x] + str(CELL_QTY - y)
                if COLORS[cell_color_index] == CELL_BLACK:
                    color = 'b'
                if COLORS[cell_color_index] == CELL_WHITE:
                    color = 'w'
                cell = Cell(color,field_name)
                self.all_cells.add(cell)
                cell.rect = pg.Rect((WINDOW_SIZE[0] - self.fields.get_width())//2+x*CELL_SIZE,(WINDOW_SIZE[1] - self.fields.get_height())//2+y*CELL_SIZE,CELL_SIZE,CELL_SIZE)
                self.screen.blit(cell.image,cell.rect)
                cell_color_index ^= True
            cell_color_index = cell_color_index^True if (is_even_qty) else cell_color_index

    def draw_pieces(self):
       for y in range(CELL_QTY):
            for x in range(CELL_QTY+2):
               if self.table[y][x] != 0:
                   piece_tuple = self.pieces_types[self.table[y][x]]
                   field_name = STR[x] + str(CELL_QTY - y)
                   classname = globals()[piece_tuple[0]]
                   piece = classname(piece_tuple[1],field_name)
                   self.all_pieces.add(piece)
                   for cell in self.all_cells:
                       if piece.field_name == cell.field_name:
                           piece.rect = cell.rect
                           cell.occupied = 1
                           cell.occupied_color = piece.color
                   self.screen.blit(piece.image,piece.rect)
    def get_cell(self,position):
        for cell in self.all_cells:
            if cell.rect.collidepoint(position):
                return cell
        return None
    
    def btn_down(self,button,position):
        self.pressed_cell = self.get_cell(position)
        
    
    def btn_up(self,button,position):
        released_cell = self.get_cell(position)
        if (released_cell is not None) and (released_cell == self.pressed_cell):
            if button == 1:
                if self.play == 0:
                    self.pick_cell(released_cell)
                if self.play == 1:
                    self.pick_cell_with_play_bots(released_cell)
            if button == 3:
                self.draw_plan_moves(released_cell)
        self.grand_update()
    def draw_plan_moves(self,cell):
        if not cell.mark:
            pick = RightClickArea(cell)
            self.all_areas.add(pick)
            cell.mark = True
        else:
            for area in self.all_areas:
                if cell.field_name == area.field_name:
                    area.kill()
                    break
            cell.mark = False
    def grand_update(self):
        self.all_cells.draw(self.screen)
        self.all_areas.draw(self.screen)
        self.all_possible_moves.draw(self.screen)
        self.all_pieces.draw(self.screen)
        pg.display.update()
    
    def declare_win(self,color):
        self.button_exit_text = FONT.render('Выйти в меню',1,WHITE)
        self.button_close_declare_text = FONT.render('Просмотреть поле',1,WHITE)
        declare_surface = pg.Surface((WINDOW_SIZE[0]//2,WINDOW_SIZE[1]//4),pg.SRCALPHA)
        pg.draw.rect(declare_surface,CELL_BLACK,declare_surface.get_rect())
        pg.draw.rect(declare_surface,BLACK,declare_surface.get_rect(),3)
        pg.draw.rect(declare_surface,CELL_WHITE,(5,declare_surface.get_height()-70,200,50))
        pg.draw.rect(declare_surface,BLACK,(5,declare_surface.get_height()-70,200,50),3)
        pg.draw.rect(declare_surface,CELL_WHITE,(declare_surface.get_width()-205,declare_surface.get_height()-70,200,50))
        pg.draw.rect(declare_surface,BLACK,(declare_surface.get_width()-205,declare_surface.get_height()-70,200,50),3)
        if color == 'b':
            text = MENU_FONT.render('Победа черных!',1,WHITE)
            declare_surface.blit(text,(20,3))
        elif color == 'w':
            text = MENU_FONT.render('Победа белых!',1,WHITE)
            declare_surface.blit(text,(35,3))
        else:
            text = MENU_FONT.render('Ничья!',1,WHITE)
            declare_surface.blit(text,(150,3))
        declare_surface.blit(self.button_exit_text,(40,declare_surface.get_height()-55))
        declare_surface.blit(self.button_close_declare_text,(declare_surface.get_width()-185,declare_surface.get_height()-55))
        self.button_close_declare_rect = pg.Rect((WINDOW_SIZE[0] - declare_surface.get_width())//2 + declare_surface.get_width()-205,((WINDOW_SIZE[1] - declare_surface.get_height())//2+declare_surface.get_height()-70),200,50)
        self.button_exit_rect = pg.Rect((WINDOW_SIZE[0] - declare_surface.get_width())//2 + 5,(WINDOW_SIZE[1] - declare_surface.get_height())//2+declare_surface.get_height()-70,200,50)
        self.screen.blit(declare_surface,((WINDOW_SIZE[0] - declare_surface.get_width())//2,(WINDOW_SIZE[1] - declare_surface.get_height())//2))
    
    def declare_win_btn_dwn(self,button,position):
        if self.button_close_declare_rect.collidepoint(position):
            if button == 1:
                self.grand_update()
                return 1
        if self.button_exit_rect.collidepoint(position):
            if button == 1:
                self.grand_update()
                return 0
       

    def print_shah(self,color):
        surf = pg.Surface((420,40),pg.SRCALPHA)
        surf.blit(background,(0,0))
        if color == 'b':
            text = FONT2.render('Шах черному королю!',1,WHITE)
        elif color == 'w':
            text = FONT2.render('Шах белому королю!',1,WHITE)
        else:
            text = FONT2.render('',1,WHITE)
        surf.blit(text,(0,0))
        self.screen.blit(surf,(WINDOW_SIZE[0]//2-200,40))
        pg.display.update()

    def print_mat(self,color):
        surf = pg.Surface((420,40),pg.SRCALPHA)
        surf.blit(background,(0,0))
        if color == 'b':
            text = FONT2.render('Мат черному королю!',1,WHITE)
        elif color == 'w':
            text = FONT2.render('Мат белому королю!',1,WHITE)
        else:
            text = FONT2.render('',1,WHITE)
        surf.blit(text,(0,0))
        self.screen.blit(surf,(WINDOW_SIZE[0]//2-200,40))
        pg.display.update()

    def print_moves(self):
        surf = pg.Surface((220,40),pg.SRCALPHA)
        surf.blit(background,(0,0))
        number_of_moves = str(self.number_of_moves+1)
        text = FONT2.render('Ход: '+number_of_moves,1,WHITE)
        surf.blit(text,(0,0))
        self.screen.blit(surf,(WINDOW_SIZE[0]-200,40))
        pg.display.update()

    def get_turn(self):
        surf = pg.Surface((220,40),pg.SRCALPHA)
        surf.blit(background,(0,0))
        if self.turn == 0:
            text = FONT2.render('Ход белых',1,WHITE)
        else:
            text = FONT2.render('Ход черных',1,WHITE)
        surf.blit(text,(0,0))
        self.screen.blit(surf,(WINDOW_SIZE[0]//2-100,0))
        pg.display.update()

    def pick_cell_with_play_bots(self,cell):
        if self.turn == 0 and self.color == 'w':
            self.pick_cell(cell)
            if self.turn == 1:
                self.grand_update()
                self.bots_play()
        elif self.turn == 1 and self.color == 'b':
            self.pick_cell(cell)
            if self.turn == 0:
                self.grand_update()
                self.bots_play()
            
    def bots_play(self):
        pg.time.delay(1000)
        if self.bot_color == 'w':
            self.white_times -= 1
        if self.bot_color == 'b':
            self.black_times -=1
        if self.get_shah(self.bot_color) == False:
            bot_pieces = []
            for piece in self.all_pieces:
                if piece.color != self.color:
                    bot_pieces.append(piece)
            run = True
            while run:
                bot_index_pick_piece = randint(0,len(bot_pieces)-1)
                bot_pick_piece = bot_pieces[bot_index_pick_piece]
                for cell in self.all_cells:
                    if cell.field_name == bot_pick_piece.field_name:
                        bot_moves = bot_pick_piece.get_moves(self.all_cells,cell,self.number_of_moves,self.all_pieces)
                        if len(bot_moves) != 0:
                            cell.occupied = 0
                            cell.occupied_color = 0
                            run = False
                        break
            bot_pick_move = bot_moves[randint(0,len(bot_moves)-1)]
            for cell in self.all_cells:
                if cell.field_name == bot_pick_move:
                    if cell.occupied == 0:
                        bot_pick_piece.rect = cell.rect
                        bot_pick_piece.field_name = cell.field_name
                        cell.occupied = 1
                        cell.occupied_color = self.bot_color
                        if bot_pick_piece.__class__.__name__ == 'Pawn':
                            self.check_pawn(bot_pick_piece)
                        break
                    if cell.occupied == 1 and cell.occupied_color != self.bot_color:
                        self.delete_piece(cell)
                        bot_pick_piece.rect = cell.rect
                        bot_pick_piece.field_name = cell.field_name
                        cell.occupied = 1
                        cell.occupied_color = self.bot_color
                        if bot_pick_piece.__class__.__name__ == 'Pawn':
                            self.check_pawn(bot_pick_piece)
                        break
        elif self.get_shah(self.bot_color) == True and self.get_mat(self.bot_color) == False:
            self.set_antishah(self.bot_color)
            bot_pieces = []
            for piece in self.all_pieces:
                if piece.color != self.color:
                    bot_pieces.append(piece)
            run = True
            finally_bot_moves = []
            while run:
                bot_index_pick_piece = randint(0,len(bot_pieces)-1)
                bot_pick_piece = bot_pieces[bot_index_pick_piece]
                if bot_pick_piece.__class__.__name__ != 'King':
                    for cell in self.all_cells:
                        if cell.field_name == bot_pick_piece.field_name:
                            bot_moves = bot_pick_piece.get_moves(self.all_cells,cell,self.number_of_moves,self.all_pieces)
                            if len(bot_moves) != 0:
                                for i in bot_moves:
                                    if i in self.antishah:
                                        finally_bot_moves.append(i)
                                        cell.occupied = 0
                                        cell.occupied_color = 0
                                        run = False
                            break
                elif bot_pick_piece.__class__.__name__ == 'King':
                    for cell in self.all_cells:
                        if cell.field_name == bot_pick_piece.field_name:
                            bot_moves = bot_pick_piece.get_moves(self.all_cells,cell,self.number_of_moves,self.all_pieces)
                            if len(bot_moves) != 0:
                                for i in bot_moves:
                                    finally_bot_moves.append(i)
                                    cell.occupied = 0
                                    cell.occupied_color = 0
                                    run = False
                            break
            bot_pick_move = finally_bot_moves[randint(0,len(finally_bot_moves)-1)]
            for cell in self.all_cells:
                if cell.field_name == bot_pick_move:
                    if cell.occupied == 0:
                        bot_pick_piece.rect = cell.rect
                        bot_pick_piece.field_name = cell.field_name
                        cell.occupied = 1
                        cell.occupied_color = self.bot_color
                        if bot_pick_piece.__class__.__name__ == 'Pawn':
                            self.check_pawn(bot_pick_piece)
                        break
                    if cell.occupied == 1 and cell.occupied_color != self.bot_color:
                        self.delete_piece(cell)
                        bot_pick_piece.rect = cell.rect
                        bot_pick_piece.field_name = cell.field_name
                        cell.occupied = 1
                        cell.occupied_color = self.bot_color
                        if bot_pick_piece.__class__.__name__ == 'Pawn':
                            self.check_pawn(bot_pick_piece)
                        break
        if self.turn == 0:
            self.turn = 1
        elif self.turn == 1:
            self.turn = 0
            self.number_of_moves += 1
    def check_pawn(self,pawn):
        if pawn.color == 'w':
            if pawn.field_name[1] == '8':
                self.change_pawn(pawn)
        if pawn.color == 'b':
            if pawn.field_name[1] == '1':
                self.change_pawn(pawn)
    def change_pawn(self,pawn):
        for cell in self.all_cells:
            if cell.field_name == pawn.field_name:
                ncell = cell
                break
        color = pawn.color
        pawn.kill()
        field_name = ncell.field_name
        piece = Queen(color,field_name)
        piece.rect = cell.rect
        self.all_pieces.add(piece)
        self.grand_update
    def check_pat(self):
        if len(self.all_pieces) == 2:
            return True
        if self.get_shah('w') == False and self.get_shah('b') == False:
            count_move_black = 0
            count_move_white = 0
            for piece in self.all_pieces:
                for cell in self.all_cells:
                        if cell.field_name == piece.field_name:
                            if piece.color == 'b':
                                black_moves = piece.get_moves(self.all_cells,cell,self.number_of_moves,self.all_pieces)
                                count_move_black += len(black_moves)
                                break
                            if piece.color == 'w':
                                white_moves = piece.get_moves(self.all_cells,cell,self.number_of_moves,self.all_pieces)
                                count_move_white += len(white_moves)
                                break
                if count_move_black > 0 and count_move_white > 0:
                    return False
            if count_move_black == 0 or count_move_white == 0:
                return True
        return False
    def check_mat_after_move(self,cell):
        if self.picked_piece.__class__.__name__ != 'King':
            for piece in self.all_pieces:
                if piece.color == self.picked_piece.color:
                    if piece.__class__.__name__ == 'King':
                        king_cell = self.king_cell(piece)
                        break
            cell.occupied = 0
            temp_occupied_color = cell.occupied_color
            cell.occupied_color = 0
            delete_moves = []
            moves_cells = []
            for move in self.moves:
                for i in self.all_cells:
                    if move == i.field_name:
                        moves_cells.append(i)
            for piece in self.all_pieces:
                if piece.color != temp_occupied_color and piece.__class__.__name__ != 'King':
                    for i in self.all_cells:
                        if i.field_name == piece.field_name:
                            ncell = i
                            break
                    for move in moves_cells:
                        temp_move_oc = move.occupied
                        temp_move_oc_col = move.occupied_color
                        move.occupied = 1
                        move.occupied_color = temp_occupied_color
                        piece_moves = piece.get_moves(self.all_cells,ncell,self.number_of_moves,self.all_pieces)
                        if len(piece_moves)!= 0:
                            for pm in piece_moves:
                                if king_cell.field_name == pm:
                                    if move.field_name != ncell.field_name:
                                        delete_moves.append(move.field_name)
                                    break
                        move.occupied = temp_move_oc
                        move.occupied_color = temp_move_oc_col
            cell.occupied = 1
            cell.occupied_color = temp_occupied_color
            if len(delete_moves) != 0:
                for i in delete_moves:
                    if i in self.moves:
                        self.moves.remove(i)
    def pick_cell(self,cell):
        self.unmark()
        if (self.picked_piece is None):
            for piece in self.all_pieces:
                if piece.field_name == cell.field_name:
                    if(self.turn == 0) and (piece.color == 'w'):
                        pick = Area(cell)
                        self.all_areas.add(pick)
                        self.picked_piece = piece
                        self.white_moves += 1
                        self.previous_cell = cell
                        break
                    elif (self.turn == 1) and (piece.color == 'b'):
                        pick = Area(cell)
                        self.all_areas.add(pick)
                        self.picked_piece = piece
                        self.black_moves += 1
                        self.previous_cell = cell
                        break
            if (self.picked_piece is not None):
                self.moves = self.picked_piece.get_moves(self.all_cells,self.previous_cell,self.number_of_moves,self.all_pieces)
                self.check_mat_after_move(self.previous_cell)
                if self.get_shah(self.picked_piece.color) == False:
                    for move in self.moves:
                        for cells in self.all_cells:
                            if move == cells.field_name:
                                possible_moves = Possible_moves(cells)
                                self.all_possible_moves.add(possible_moves)
                elif self.get_shah(self.picked_piece.color) == True:
                    if self.picked_piece.__class__.__name__ != 'King':
                        for move in self.moves:
                            for i in self.antishah:
                                if i == move:
                                    for cells in self.all_cells:
                                        if move == cells.field_name:
                                            possible_moves = Possible_moves(cells)
                                            self.all_possible_moves.add(possible_moves)
                    else:
                        for move in self.moves:
                            for cells in self.all_cells:
                                if move == cells.field_name:
                                    possible_moves = Possible_moves(cells)
                                    self.all_possible_moves.add(possible_moves)

        else:
            if self.get_shah(self.picked_piece.color) == False:
                flag = 0
                for piece in self.all_pieces:
                    if piece.field_name == cell.field_name:
                        newpickedpice = piece
                        color = piece.color
                        flag = 1
                        break
                if flag == 0:
                    f = 0
                    for i in self.moves:
                        if cell.field_name == i:
                            self.picked_piece.rect = cell.rect
                            self.picked_piece.field_name = cell.field_name
                            self.previous_cell.occupied = 0
                            self.previous_cell.occupied_color = 0
                            cell.occupied = 1
                            cell.occupied_color = self.picked_piece.color
                            if self.picked_piece.color == 'b':
                                self.number_of_moves += 1
                            if self.turn == 1:
                                self.turn = 0
                            elif self.turn == 0:
                                self.turn = 1
                            if self.picked_piece.__class__.__name__ == 'Pawn':
                                self.check_pawn(self.picked_piece)
                            self.picked_piece.number_of_moves += 1
                            self.picked_piece = None
                            f = 1
                            break
                    if f == 0:
                        pick = Area(self.previous_cell)
                        self.all_areas.add(pick)
                        for move in self.moves:
                            for cells in self.all_cells:
                                if move == cells.field_name:
                                    possible_moves = Possible_moves(cells)
                                    self.all_possible_moves.add(possible_moves)
                else:
                    if color == self.picked_piece.color:
                        self.picked_piece = newpickedpice
                        self.previous_cell = cell
                        pick = Area(cell)
                        self.all_areas.add(pick)
                        self.moves = self.picked_piece.get_moves(self.all_cells,self.previous_cell,self.number_of_moves,self.all_pieces)
                        self.check_mat_after_move(self.previous_cell)
                        for move in self.moves:
                            for cells in self.all_cells:
                                if move == cells.field_name:
                                    possible_moves = Possible_moves(cells)
                                    self.all_possible_moves.add(possible_moves)
                    else:
                        flag = 0
                        for i in self.moves:
                            if cell.field_name == i:
                                self.delete_piece(cell)
                                self.picked_piece.rect = cell.rect
                                self.picked_piece.field_name = cell.field_name
                                self.previous_cell.occupied = 0
                                self.previous_cell.occupied_color = 0
                                cell.occupied = 1
                                cell.occupied_color = self.picked_piece.color
                                if self.picked_piece.color == 'b':
                                    self.number_of_moves += 1
                                if self.turn == 1:
                                    self.turn = 0
                                elif self.turn == 0:
                                    self.turn = 1
                                if self.picked_piece.__class__.__name__ == 'Pawn':
                                    self.check_pawn(self.picked_piece)
                                self.picked_piece.number_of_moves += 1
                                self.picked_piece = None
                                flag = 1
                                break
                        if flag == 0:
                            pick = Area(self.previous_cell)
                            self.all_areas.add(pick)
                            for move in self.moves:
                                for cells in self.all_cells:
                                    if move == cells.field_name:
                                        possible_moves = Possible_moves(cells)
                                        self.all_possible_moves.add(possible_moves)
            elif self.get_shah(self.picked_piece.color) == True:
                flag = 0
                for piece in self.all_pieces:
                    if piece.field_name == cell.field_name:
                        newpickedpice = piece
                        color = piece.color
                        flag = 1
                        break
                if flag == 0:
                    f = 0
                    if self.picked_piece.__class__.__name__ != 'King':
                        for i in self.moves:
                            for j in self.antishah:
                                if i == j:
                                    if cell.field_name == i:
                                        self.picked_piece.rect = cell.rect
                                        self.picked_piece.field_name = cell.field_name
                                        self.previous_cell.occupied = 0
                                        self.previous_cell.occupied_color = 0
                                        cell.occupied = 1
                                        cell.occupied_color = self.picked_piece.color
                                        if self.picked_piece.color == 'b':
                                            self.number_of_moves += 1
                                        if self.turn == 1:
                                            self.turn = 0
                                        elif self.turn == 0:
                                            self.turn = 1
                                        if self.picked_piece.__class__.__name__ == 'Pawn':
                                            self.check_pawn(self.picked_piece)
                                        self.picked_piece.number_of_moves += 1
                                        self.picked_piece = None
                                        f = 1
                                        break
                    if self.picked_piece.__class__.__name__ == 'King':
                        for i in self.moves:
                            if cell.field_name == i:
                                self.picked_piece.rect = cell.rect
                                self.picked_piece.field_name = cell.field_name
                                self.previous_cell.occupied = 0
                                self.previous_cell.occupied_color = 0
                                cell.occupied = 1
                                cell.occupied_color = self.picked_piece.color
                                if self.picked_piece.color == 'b':
                                    self.number_of_moves += 1
                                if self.turn == 1:
                                    self.turn = 0
                                elif self.turn == 0:
                                    self.turn = 1
                                self.picked_piece.number_of_moves += 1
                                self.picked_piece = None
                                f = 1
                                break
                    if f == 0:
                        pick = Area(self.previous_cell)
                        self.all_areas.add(pick)
                        if self.picked_piece.__class__.__name__ != 'King':
                            for move in self.moves:
                                for i in self.antishah:
                                    if i == move:
                                        for cells in self.all_cells:
                                            if move == cells.field_name:
                                                possible_moves = Possible_moves(cells)
                                                self.all_possible_moves.add(possible_moves)
                        else:
                            for move in self.moves:
                                for cells in self.all_cells:
                                    if move == cells.field_name:
                                        possible_moves = Possible_moves(cells)
                                        self.all_possible_moves.add(possible_moves)
                else:
                    if color == self.picked_piece.color:
                        self.picked_piece = newpickedpice
                        self.previous_cell = cell
                        pick = Area(cell)
                        self.all_areas.add(pick)
                        self.moves = self.picked_piece.get_moves(self.all_cells,self.previous_cell,self.number_of_moves,self.all_pieces)
                        self.check_mat_after_move(self.previous_cell)
                        if self.picked_piece.__class__.__name__ != 'King':
                            for move in self.moves:
                                for i in self.antishah:
                                    if i == move:
                                        for cells in self.all_cells:
                                            if move == cells.field_name:
                                                possible_moves = Possible_moves(cells)
                                                self.all_possible_moves.add(possible_moves)
                        else:
                            for move in self.moves:
                                for cells in self.all_cells:
                                    if move == cells.field_name:
                                        possible_moves = Possible_moves(cells)
                                        self.all_possible_moves.add(possible_moves)
                    else:
                        flag = 0
                        if self.picked_piece.__class__.__name__ != 'King':
                            for i in self.moves:
                                for j in self.antishah:
                                    if i == j:
                                        if cell.field_name == i:
                                            self.delete_piece(cell)
                                            self.picked_piece.rect = cell.rect
                                            self.picked_piece.field_name = cell.field_name
                                            self.previous_cell.occupied = 0
                                            self.previous_cell.occupied_color = 0
                                            cell.occupied = 1
                                            cell.occupied_color = self.picked_piece.color
                                            if self.picked_piece.color == 'b':
                                                self.number_of_moves += 1
                                            if self.turn == 1:
                                                self.turn = 0
                                            elif self.turn == 0:
                                                self.turn = 1
                                            if self.picked_piece.__class__.__name__ == 'Pawn':
                                                self.check_pawn(self.picked_piece)
                                            self.picked_piece.number_of_moves += 1
                                            self.picked_piece = None
                                            flag = 1
                                            break
                        if self.picked_piece.__class__.__name__ == 'King':
                            for i in self.moves:
                                if cell.field_name == i:
                                    self.delete_piece(cell)
                                    self.picked_piece.rect = cell.rect
                                    self.picked_piece.field_name = cell.field_name
                                    self.previous_cell.occupied = 0
                                    self.previous_cell.occupied_color = 0
                                    cell.occupied = 1
                                    cell.occupied_color = self.picked_piece.color
                                    if self.picked_piece.color == 'b':
                                        self.number_of_moves += 1
                                    if self.turn == 1:
                                        self.turn = 0
                                    elif self.turn == 0:
                                        self.turn = 1
                                    self.picked_piece.number_of_moves += 1
                                    self.picked_piece = None
                                    flag = 1
                                    break
                        if flag == 0:
                            pick = Area(self.previous_cell)
                            self.all_areas.add(pick)
                            if self.picked_piece.__class__.__name__ != 'King':
                                for move in self.moves:
                                    for i in self.antishah:
                                        if i == move:
                                            for cells in self.all_cells:
                                                if move == cells.field_name:
                                                    possible_moves = Possible_moves(cells)
                                                    self.all_possible_moves.add(possible_moves)
                            else:
                                for move in self.moves:
                                    for cells in self.all_cells:
                                        if move == cells.field_name:
                                            possible_moves = Possible_moves(cells)
                                            self.all_possible_moves.add(possible_moves)

    
    def delete_piece(self,cell):
        for piece in self.all_pieces:
            if piece.field_name == cell.field_name:
                piece.kill()
                break
    
    def unmark(self):
        for cell in self.all_cells:
            cell.mark = False
        self.all_areas.empty()
        self.all_possible_moves.empty()

    def set_antishah(self,color):
        self.antishah = []
        self.antishah.append(self.piece_shah_cell.field_name)
        shah_cells = self.get_shah_moves(color)
        for piece in self.all_pieces:
            if piece.color == color:
                for cell in self.all_cells:
                    if piece.field_name == cell.field_name:
                        piece_cell = cell
                        break
                piece_moves = piece.get_moves(self.all_cells,piece_cell,self.number_of_moves, self.all_pieces)
                for i in piece_moves:
                    for j in shah_cells:
                        if i == j:
                            self.antishah.append(i)
    
    def get_mat(self,color):
        if self.turn == 0 and color == 'b':
            return True
        elif self.turn == 1 and color == 'w':
            return True
        king = self.pick_king(color)
        if king == 0:
            return True
        king_cell = self.king_cell(king)
        king_moves = king.get_moves(self.all_cells,king_cell,self.number_of_moves,self.all_pieces)
        self.set_antishah(color)
        flag = 0
        if len(king_moves) == 0:
            for piece in self.all_pieces:
                if piece.color == king.color:
                    for cell in self.all_cells:
                        if piece.field_name == cell.field_name:
                            piece_cell = cell
                            break
                    piece_moves = piece.get_moves(self.all_cells,piece_cell,self.number_of_moves, self.all_pieces)
                    for i in piece_moves:
                        if i == self.piece_shah.field_name:
                            flag = 1
            if flag == 1:
                return False
            if len(self.antishah) > 1:
                return False
            return True
        return False
    def get_shah_moves(self,color):
        if color == 'w':
            occolor = 'b'
        elif color == 'b':
            occolor = 'w'
        shah_moves = self.piece_shah.get_moves(self.all_cells,self.piece_shah_cell,self.number_of_moves,self.all_pieces)
        piece_shah = self.piece_shah
        piece_shah_cell = self.piece_shah_cell
        shah_cells = []
        for cell in self.all_cells:
            for i in shah_moves:
                if cell.field_name == i:
                    temp_occupied = cell.occupied
                    temp_occupied_color = cell.occupied_color
                    cell.occupied = 1
                    cell.occupied_color = occolor
                    if self.get_shah(color) == False:
                        shah_cells.append(i)
                    cell.occupied = temp_occupied
                    cell.occupied_color = temp_occupied_color
        self.piece_shah = piece_shah
        self.piece_shah_cell = piece_shah_cell
        return shah_cells
    def get_shah(self,color):
        king = self.pick_king(color)
        if king == 0:
            return True
        king_cell = self.king_cell(king)
        for piece in self.all_pieces: 
            if piece.color != king.color:
                for cell in self.all_cells:
                    if piece.field_name == cell.field_name: 
                        piece_cell = cell
                        break
                piece_moves = piece.get_moves(self.all_cells,piece_cell,self.number_of_moves,self.all_pieces)
                for i in piece_moves:
                    if i == king_cell.field_name:
                        self.piece_shah = piece
                        self.piece_shah_cell = piece_cell
                        return True
        return False

    def pick_king(self, color):
        for piece in self.all_pieces:
            if piece.__class__.__name__ == 'King':
                if piece.color == color:
                    return piece
        return 0
    def king_cell(self,king):
        for cell in self.all_cells:
            if cell.field_name == king.field_name:
                return cell
    
class Possible_moves(pg.sprite.Sprite):
    def __init__(self,cell):
        super().__init__()
        coords = (cell.rect.x,cell.rect.y)
        area_size = (cell.rect.width,cell.rect.height)
        self.image = pg.Surface(area_size).convert_alpha()
        self.image.fill(MOVES_CELL_COLOR)  
        self.rect = pg.Rect(coords,area_size)
        self.field_name = cell.field_name
                    
class Area(pg.sprite.Sprite):
    def __init__(self,cell):
        super().__init__() 
        coords = (cell.rect.x,cell.rect.y)
        area_size = (cell.rect.width,cell.rect.height)
        self.image = pg.Surface(area_size).convert_alpha()
        self.image.fill(ACTIVE_CELL_COLOR)   
        self.rect = pg.Rect(coords,area_size)
        self.field_name = cell.field_name
class RightClickArea(pg.sprite.Sprite):
    def __init__(self,cell):
        super().__init__()
        coords = (cell.rect.x,cell.rect.y)
        area_size = (cell.rect.width,cell.rect.height)
        self.image = pg.Surface(area_size).convert_alpha()
        self.image.fill(YELLOW)
        self.rect = pg.Rect(coords,area_size)
        self.field_name = cell.field_name  
                
class Cell(pg.sprite.Sprite):
    def __init__(self, color, field_name):
        super().__init__()
        picture = pg.image.load('chessfigure/' + color + '_board.png').convert_alpha()
        self.image = pg.transform.scale(picture,(CELL_SIZE,CELL_SIZE))
        self.rect = self.image.get_rect()
        self.color = color
        self.field_name = field_name
        self.occupied = 0
        self.occupied_color = 0
        self.mark = False 
class Piece(pg.sprite.Sprite):
    def __init__(self, color, field_name,file):
        super().__init__()
        picture = pg.image.load('chessfigure/' + color + file).convert_alpha()
        self.image = pg.transform.scale(picture,(CELL_SIZE,CELL_SIZE))
        self.rect = self.image.get_rect()
        self.color = color
        self.field_name = field_name
        self.number_of_moves = 0
    

class Archbishop(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_Archbishop.png')
    def get_moves(self,cells,cell, number_of_moves,pieces):
        bishop = Bishop(self.color,cell)
        horse = Horse(self.color, cell)
        moves_horse = horse.get_moves(cells,cell,number_of_moves,pieces)
        moves_bishop = bishop.get_moves(cells,cell,number_of_moves,pieces)
        moves = []
        for i in moves_horse:
            moves.append(i)
        for i in moves_bishop:
            moves.append(i)
        return moves


class Bishop(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_Bishop.png')
    def get_moves(self,cells,cell, number_of_moves,pieces):
        moves = []
        for x in range (10):
            if STR[x] == cell.field_name[0]:
                posl = x
                break
        posn = int(cell.field_name[1])
        temp = posl
        while posl != 10:
            posl += 1
            posn += 1
            nextcell = STR[posl] + str(posn)
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else:
                        flag = 1
                    break
            if flag == 1 :
                break
        posl = temp
        posn = int(cell.field_name[1])
        while posl != 10:
            posl += 1
            posn -= 1
            nextcell = STR[posl] + str(posn)
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else:
                        flag = 1
                    break
            if flag == 1 :
                break
        posl = temp 
        posn = int(cell.field_name[1])
        while posl != 0:
            posl -=1
            posn += 1
            nextcell = STR[posl] + str(posn)
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else:
                        flag = 1
                    break
            if flag == 1 :
                break
        posl = temp
        posn = int(cell.field_name[1])
        while posl != 0:
            posl -= 1
            posn -= 1
            nextcell = STR[posl] + str(posn)
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else:
                        flag = 1
                    break
            if flag == 1 :
                break
        return moves

class Chancellor(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_Chancellor.png')
    def get_moves(self,cells,cell,number_of_moves,pieces):
        horse = Horse(self.color,cell)
        rook =Rook(self.color,cell)
        moves_horse = horse.get_moves(cells,cell,number_of_moves,pieces)
        moves_rook = rook.get_moves(cells,cell,number_of_moves,pieces)
        moves = []
        for i in moves_horse:
            moves.append(i)
        for i in moves_rook:
            moves.append(i)
        return moves

class Horse(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_Horse.png')
    def get_moves(self,cells,cell, number_of_moves,pieces):
        moves = []
        nextcell = []
        posn = int(cell.field_name[1])
        for x in range (10):
            if STR[x] == cell.field_name[0]:
                posl = x
        if posl == 0:
            ncell = STR[posl+1] + str(posn+2)
            nextcell.append(ncell)
            ncell = STR[posl+2] + str(posn+1) 
            nextcell.append(ncell)
            ncell = STR[posl+2] + str(posn-1)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn-2)
            nextcell.append(ncell)
        if posl != 0:
            ncell = STR[posl+1] + str(posn+2)
            nextcell.append(ncell)
            ncell = STR[posl+2] + str(posn+1) 
            nextcell.append(ncell)
            ncell = STR[posl+2] + str(posn-1)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn-2)
            nextcell.append(ncell)
            ncell = STR[posl-1] + str(posn+2)
            nextcell.append(ncell)
            ncell = STR[posl-1] + str(posn-2)
            nextcell.append(ncell)
            if posl-1 != 0:
                ncell = STR[posl-2] + str(posn+1)
                nextcell.append(ncell)
                ncell = STR[posl-2] + str(posn-1)
                nextcell.append(ncell)
        for a in cells:
            for i in nextcell: 
                if a.field_name == i:
                    if a.occupied == 0:
                        moves.append(i)
                    elif a.occupied == 1 and a.occupied_color != self.color:
                        moves.append(i)

        return moves


class King(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_King.png')
    def get_moves(self,cells,cell,number_of_moves,pieces):
        moves = []
        nextcell = []
        posn = int(cell.field_name[1])
        for x in range (10):
            if STR[x] == cell.field_name[0]:
                posl = x
        if posl == 0:
            ncell = STR[posl] + str(posn + 1)
            nextcell.append(ncell)
            ncell = STR[posl] + str(posn - 1)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn + 1)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn - 1)
            nextcell.append(ncell)
        if posl != 0:
            ncell = STR[posl] + str(posn + 1)
            nextcell.append(ncell)
            ncell = STR[posl] + str(posn - 1)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn + 1)
            nextcell.append(ncell)
            ncell = STR[posl+1] + str(posn - 1)
            nextcell.append(ncell)
            ncell = STR[posl-1] + str(posn)
            nextcell.append(ncell)
            ncell = STR[posl-1] + str(posn+1)
            nextcell.append(ncell)
            ncell = STR[posl-1] + str(posn-1)
            nextcell.append(ncell)
        for a in cells:
            for i in nextcell: 
                if a.field_name == i:
                    if a.occupied == 0:
                        moves.append(i)
                    elif a.occupied == 1 and a.occupied_color != self.color:
                        moves.append(i)
        delete_moves = []
        for piece in pieces: 
            if piece.color != self.color:
                if piece.__class__.__name__ != 'King' and piece.__class__.__name__ != 'Pawn':
                    for i in cells:
                        if i.field_name == piece.field_name:
                            ncell = i
                            break
                    piece_moves = piece.get_moves(cells,ncell,number_of_moves,pieces)
                    if len (piece_moves) != 0:
                        for i in piece_moves:
                            for j in moves:
                                if i == j:
                                    delete_moves.append(i)
                if piece.__class__.__name__ == 'Pawn':
                    for i in cells: 
                        if i.field_name == piece.field_name:
                            ncell = i
                            break
                    for x in range (10):
                        if STR[x] == ncell.field_name[0]:
                            nlitra = x
                            break
                    if piece.color == 'w':
                        if nlitra == 0:
                            pawn_moves = STR[nlitra+1] + str(int(ncell.field_name[1]) + 1)
                            delete_moves.append(pawn_moves)
                        if nlitra != 0:
                            pawn_moves = STR[nlitra+1] + str(int(ncell.field_name[1]) + 1)
                            delete_moves.append(pawn_moves)
                            pawn_moves = STR[nlitra-1] + str(int(ncell.field_name[1]) + 1)
                            delete_moves.append(pawn_moves)
                    if piece.color == 'b':
                        if nlitra == 0:
                            pawn_moves = STR[nlitra+1] + str(int(ncell.field_name[1]) - 1)
                            delete_moves.append(pawn_moves)
                        if nlitra != 0:
                            pawn_moves = STR[nlitra+1] + str(int(ncell.field_name[1]) - 1)
                            delete_moves.append(pawn_moves)
                            pawn_moves = STR[nlitra-1] + str(int(ncell.field_name[1]) - 1)
                            delete_moves.append(pawn_moves)
                if piece.__class__.__name__ == 'King':
                    for i in cells: 
                        if i.field_name == piece.field_name:
                            ncell = i
                            break
                    for x in range (10):
                        if STR[x] == ncell.field_name[0]:
                            nlitra = x
                            break
                    posn = int(ncell.field_name[1])
                    if nlitra == 0:
                        kingmove = STR[nlitra] + str(posn + 1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra] + str(posn - 1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra+1] + str(posn)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra+1] + str(posn +1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra+1] + str(posn - 1)
                        delete_moves.append(kingmove)
                    if nlitra != 0:
                        kingmove = STR[nlitra] + str(posn + 1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra] + str(posn - 1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra+1] + str(posn)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra+1] + str(posn +1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra+1] + str(posn - 1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra-1] + str(posn - 1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra-1] + str(posn + 1)
                        delete_moves.append(kingmove)
                        kingmove = STR[nlitra+1] + str(posn)
                        delete_moves.append(kingmove)
        if len (delete_moves) != 0:
            for i in delete_moves:
                if i in moves:
                    moves.remove(i)
        delete_moves = []
        moves_cells = []
        for move in moves:
            for i in cells:
                if i.field_name == move:
                    moves_cells.append(i)
                    break
        tempoc = []
        tempoccol = []
        for move in moves_cells:
            tempoc.append(move.occupied)
            tempoccol.append(move.occupied_color)
            cell.occupied = 0
            cell.occupied_color = 0
            move.occupied = 1
            move.occupied_color = self.color
        for piece in pieces:
            if piece.color != self.color:
                if piece.__class__.__name__ != 'King':
                    for i in cells:
                        if i.field_name == piece.field_name:
                            ncell = i
                            break
                    piece_moves = piece.get_moves(cells,ncell,number_of_moves,pieces)
                    if len (piece_moves) != 0:
                        for i in piece_moves:
                            for j in moves:
                                if i == j:
                                    delete_moves.append(i)
        for i in range(len(moves_cells)):
            for j in range(len(tempoc)):
                if i == j:
                    moves_cells[i].occupied = tempoc[j]
                    moves_cells[i].occupied_color = tempoccol[j]
        cell.occupied = 1
        cell.occupied_color = self.color
        if len(delete_moves) != 0:
            for i in delete_moves:
                if i in moves:
                    moves.remove(i)
        return moves
            

class Pawn(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_Pawn.png')
    def get_moves(self,cells,cell, number_of_moves,pieces):
        moves = []
        flag = 0
        if self.color == 'w':
            number_of_litra = 0
            for x in range (10):
                if STR[x] == cell.field_name[0]:
                    number_of_litra = x
            nextcell = cell.field_name[0] + str(int(cell.field_name[1]) + 1)
            if number_of_litra == 0:
                nextcell1 = 0
            else:
                nextcell1 = STR[number_of_litra-1] + str(int(cell.field_name[1]) + 1)
            nextcell2 = STR[number_of_litra+1] + str(int(cell.field_name[1]) + 1)
            for i in cells:
                if nextcell == i.field_name:
                    if i.occupied == 0:
                        moves.append(nextcell)
                if nextcell1 == i.field_name:
                    if i.occupied == 1 and i.occupied_color != cell.occupied_color:
                        moves.append(nextcell1)
                if nextcell2 == i.field_name:
                    if i.occupied == 1 and i.occupied_color != cell.occupied_color:
                        moves.append(nextcell2)
            if self.number_of_moves == 0:
                nextcell2 = nextcell[0] + str(int(nextcell[1])+1)
                for i in cells:
                    if i.field_name == nextcell:
                        if i.occupied == 0:
                            moves.append(nextcell)
                            flag = 1
                for i in cells:
                    if i.field_name == nextcell2:
                        if i.occupied == 0 and flag == 1:
                            moves.append(nextcell2)     
            return moves
        
        if self.color == 'b':
            number_of_litra = 0
            for x in range (10):
                if STR[x] == cell.field_name[0]:
                    number_of_litra = x
            nextcell = cell.field_name[0] + str(int(cell.field_name[1]) - 1)
            if number_of_litra == 0:
                nextcell1 = 0
            else:
                nextcell1 = STR[number_of_litra-1] + str(int(cell.field_name[1]) - 1)
            nextcell2 = STR[number_of_litra+1] + str(int(cell.field_name[1]) - 1)
            for i in cells:
                if nextcell == i.field_name:
                    if i.occupied == 0:
                        moves.append(nextcell)
                if nextcell1 == i.field_name:
                    if i.occupied == 1 and i.occupied_color != cell.occupied_color:
                        moves.append(nextcell1)
                if nextcell2 == i.field_name:
                    if i.occupied == 1 and i.occupied_color != cell.occupied_color:
                        moves.append(nextcell2)
            if self.number_of_moves == 0:
                nextcell2 = nextcell[0] + str(int(nextcell[1])-1)
                for i in cells:
                    if i.field_name == nextcell:
                        if i.occupied == 0:
                            moves.append(nextcell)
                            flag = 1
                for i in cells:
                    if i.field_name == nextcell2:
                        if i.occupied == 0 and flag == 1:
                            moves.append(nextcell2)

            return moves

            
class Queen(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_Queen.png')
    def get_moves(self,cells,cell, number_of_moves,pieces):
        moves = []
        rook = Rook(self.color,cell)
        bishop = Bishop(self.color, cell)
        rook_moves = rook.get_moves(cells,cell, number_of_moves,pieces)
        bishop_moves = bishop.get_moves(cells,cell, number_of_moves,pieces)
        for i in rook_moves:
            moves.append(i)
        for i in bishop_moves:
            moves.append(i)

        return moves

class Rook(Piece):
    def __init__(self, color, field):
        super().__init__(color,field,'_Rook.png')
    def get_moves(self,cells,cell, number_of_moves,pieces):
        moves = []
        for x in range (10):
            if STR[x] == cell.field_name[0]:
                posl = x
                break
        posn = int(cell.field_name[1])
        while posn != 8:
            posn +=1
            nextcell = cell.field_name[0] + str(posn)
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else:
                        flag = 1
                    break
            if flag == 1 :
                break
        posn = int(cell.field_name[1])
        while posn != 1:
            posn -= 1
            nextcell = cell.field_name[0] + str (posn)
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else: 
                        flag = 1
                    break
            if flag == 1:
                break
        temp = posl
        while posl != 9:
            posl += 1
            nextcell = STR[posl] + cell.field_name[1]
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else: 
                        flag = 1
                    break
            if flag == 1:
                break
        posl = temp
        while posl != 0:
            posl -= 1
            nextcell = STR[posl] + cell.field_name[1]
            flag = 0
            for i in cells:
                if i.field_name == nextcell:
                    if i.occupied == 0:
                        moves.append(nextcell)
                    elif i.occupied == 1 and i.occupied_color != self.color:
                        moves.append(nextcell)
                        flag = 1
                    else: 
                        flag = 1
                    break
            if flag == 1:
                break

        return moves